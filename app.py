from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'chave_rafael_2024_final'

USUARIOS_PROFESSOR = {"admin": "admin123", "rafael": "12345"}
USUARIOS_ALUNO = {"estudante": "aluno123", "joao": "tabuada"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('usuario')
    senha = request.form.get('senha')
    if user in USUARIOS_PROFESSOR and USUARIOS_PROFESSOR[user] == senha:
        session['perfil'] = 'professor'
        session['nome'] = user
        return redirect(url_for('professor'))
    if user in USUARIOS_ALUNO and USUARIOS_ALUNO[user] == senha:
        session['perfil'] = 'aluno'
        session['nome'] = user
        session['contador'] = 0
        session['acertos'] = 0
        return redirect(url_for('aluno'))
    return "Erro: Dados incorretos! <a href='/'>Voltar</a>"

@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    if session.get('perfil') != 'aluno': return redirect(url_for('index'))
    
    feedback = None
    if request.method == 'POST':
        n1 = int(request.form.get('n1'))
        n2 = int(request.form.get('n2'))
        resp = int(request.form.get('resposta'))
        
        session['contador'] += 1
        if resp == (n1 * n2):
            session['acertos'] += 1
            feedback = {"texto": "✅ Acertou!", "cor": "bg-green-500"}
        else:
            feedback = {"texto": f"❌ Errou! {n1}x{n2}={n1*n2}", "cor": "bg-red-500"}

        if session['contador'] >= 10:
            res = {"acertos": session['acertos'], "total": 10}
            # Resetamos para a próxima vez
            session['contador'] = 0
            session['acertos'] = 0
            return render_template('resultado.html', resultado=res)

    # Gera números para a próxima
    n1, n2 = random.randint(2, 9), random.randint(2, 9)
    return render_template('aluno.html', n1=n1, n2=n2, feedback=feedback, progresso=session['contador'] + 1)

@app.route('/professor')
def professor():
    if session.get('perfil') != 'professor': return redirect(url_for('index'))
    return render_template('professor.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)