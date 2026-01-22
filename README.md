🧮 Quiz de Tabuada Adaptativo - Escola Saber Mais

Este projeto foi desenvolvido como parte do Projeto Multidisciplinar III (Ciência da Computação). A solução visa automatizar o processo de reforço escolar de matemática, eliminando o trabalho manual de correção e oferecendo um aprendizado personalizado através de uma lógica adaptativa.

🚀 Funcionalidades Principais

Perfil Aluno: Interface gamificada com feedback visual imediato (cores vibrantes para acertos e erros).

Lógica Adaptativa: O sistema identifica as dificuldades do aluno e prioriza as tabuadas com menor desempenho.

Painel do Professor: Dashboard em tempo real com estatísticas da turma e identificação automática de alunos que precisam de reforço.

Persistência de Dados: Integração com MongoDB para salvar o histórico de progresso e credenciais.

🛠️ Tecnologias Utilizadas

Linguagem: Python 3.x

Framework Web: Flask

Banco de Dados: MongoDB (NoSQL)

Frontend: HTML5, Tailwind CSS e Jinja2

Arquitetura: Cliente-Servidor (3 Camadas)

🔑 Credenciais de Acesso (Teste)

Para testar as diferentes visões do sistema, utilize os utilizadores configurados no banco de dados:

👨‍🏫 Painel do Professor (Visão de Gestão)

Usuário

Senha

Perfil

admin

admin123

Administrador

rafael

12345

Professor

✍️ Interface do Aluno (Quiz de Reforço)

Usuário

Senha

Perfil

estudante

aluno123

Aluno

joao

tabuada

Aluno

📦 Como Executar o Projeto

Instale as dependências:

pip install flask pymongo


Configure o Banco de Dados:

Certifique-se de que o MongoDB está a correr localmente (ou via Atlas).

Execute o script de configuração inicial para criar os utilizadores:

python setup_db.py


Inicie o Servidor:

python app.py


Acesse no Navegador:
Aceda a http://127.0.0.1:5000

📊 Estrutura do Projeto

app.py: Servidor principal e rotas da aplicação.

setup_db.py: Script para criar os utilizadores e dados iniciais no MongoDB.

templates/: Ficheiros HTML (index, aluno, professor).

README.md: Documentação do repositório.

Desenvolvido por: [Seu Nome / Nome do Grupo]

Instituição: Ciência da Computação - Projeto Multidisciplinar III