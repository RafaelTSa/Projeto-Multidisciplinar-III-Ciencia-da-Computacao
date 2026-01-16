from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Rota para a página inicial (que você já tem: index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a Área do Aluno - Aqui acontece a mágica do Quiz
@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    mensagem = ""
    # Se o aluno enviou uma resposta (clicou no botão)
    if request.method == 'POST':
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        resposta_usuario = int(request.form['resposta'])
        
        if resposta_usuario == (n1 * n2):
            mensagem = "✅ Parabéns! Você acertou!"
        else:
            mensagem = f"❌ Quase! {n1} x {n2} é igual a {n1*n2}."

    # Lógica Adaptativa Inicial: Sorteia números para a próxima pergunta
    # No futuro, faremos o sistema escolher números que o aluno tem dificuldade
    numero1 = random.randint(2, 9)
    numero2 = random.randint(2, 9)
    
    return render_template('aluno.html', n1=numero1, n2=numero2, msg=mensagem)

if __name__ == '__main__':
    app.run(debug=True)