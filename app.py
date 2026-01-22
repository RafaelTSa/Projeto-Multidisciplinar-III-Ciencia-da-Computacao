from flask import Flask, render_template, request, redirect, url_for, session
import random
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

app = Flask(__name__)
# Chave secreta para gerir as sessões (segurança)
app.secret_key = 'chave_rafael_2024_final'

# --- CONFIGURAÇÃO E CONEXÃO AO MONGODB ---
try:
    # Liga ao serviço MongoDB no seu PC (localhost)
    # serverSelectionTimeoutMS=2000 evita que o site fique travado se o banco estiver desligado
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
    db = client["escola_saber_mais"]
    
    # Coleções (Pastas de documentos)
    usuarios_col = db["usuarios"]
    progresso_col = db["progresso"]
    
    # Testa se o banco de dados está a responder
    client.server_info()
    print("✅ SUCESSO: Conectado ao MongoDB!")
except Exception as e:
    print(f"❌ ERRO: Não foi possível conectar ao MongoDB: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user_input = request.form.get('usuario')
    senha_input = request.form.get('senha')
    
    # BUSCA NO BANCO DE DADOS (Substitui as listas manuais)
    usuario_db = usuarios_col.find_one({"usuario": user_input, "senha": senha_input})
    
    if usuario_db:
        session['perfil'] = usuario_db['perfil']
        session['nome'] = usuario_db['usuario']
        
        if session['perfil'] == 'professor':
            return redirect(url_for('professor'))
        else:
            session['contador'] = 0
            session['acertos'] = 0
            return redirect(url_for('aluno'))
            
    return "Erro: Usuário ou senha incorretos! <a href='/'>Voltar</a>"

@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    if session.get('perfil') != 'aluno': 
        return redirect(url_for('index'))
    
    feedback = None
    if request.method == 'POST':
        n1 = int(request.form.get('n1'))
        n2 = int(request.form.get('n2'))
        resp_input = request.form.get('resposta')
        
        if resp_input:
            resp = int(resp_input)
            session['contador'] += 1
            
            # Verificação da Resposta
            if resp == (n1 * n2):
                session['acertos'] += 1
                feedback = {"texto": "✅ MUITO BEM! VOCÊ ACERTOU!", "cor": "bg-emerald-500"}
            else:
                # LÓGICA ADAPTATIVA: Salva o erro no MongoDB para análise posterior
                progresso_col.update_one(
                    {"aluno": session['nome']},
                    {"$inc": {f"erros_tabuada_{n1}": 1}}, # Soma +1 erro nesta tabuada
                    upsert=True
                )
                feedback = {"texto": f"❌ QUASE! A RESPOSTA CORRETA ERA {n1 * n2}", "cor": "bg-rose-600"}

            # Finaliza após 10 perguntas
            if session['contador'] >= 10:
                percentagem = (session['acertos'] / 10) * 100
                status = "Dominou" if percentagem >= 70 else "Reforço"
                
                # Salva o resultado final do ciclo no banco
                progresso_col.update_one(
                    {"aluno": session['nome']},
                    {"$set": {
                        "score": f"{int(percentagem)}%", 
                        "status": status
                    }},
                    upsert=True
                )
                
                res = {"acertos": session['acertos'], "total": 10}
                session['contador'] = 0
                session['acertos'] = 0
                return render_template('resultado.html', resultado=res)

    # Gera números para a próxima pergunta
    n1, n2 = random.randint(2, 9), random.randint(2, 9)
    return render_template('aluno.html', 
                           n1=n1, 
                           n2=n2, 
                           feedback=feedback, 
                           progresso=session.get('contador', 0) + 1)

@app.route('/professor')
def professor():
    if session.get('perfil') != 'professor': 
        return redirect(url_for('index'))
    
    # BUSCA NO BANCO: Pega todos os registros de desempenho dos alunos
    dados_alunos = list(progresso_col.find())
    
    return render_template('professor.html', nome=session.get('nome'), alunos=dados_alunos)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)