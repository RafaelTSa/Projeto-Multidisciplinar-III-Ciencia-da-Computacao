# 🧮 Quiz de Tabuada Adaptativo — Escola Saber Mais

Este projeto foi desenvolvido como parte do **Projeto Multidisciplinar III** do curso de **Ciência da Computação**. A aplicação tem como objetivo **automatizar o reforço escolar de matemática**, reduzindo o trabalho manual de correção e oferecendo uma experiência de aprendizagem **personalizada e adaptativa** para os alunos.

Por meio de uma lógica inteligente, o sistema identifica as dificuldades individuais de cada estudante e ajusta automaticamente os exercícios, tornando o processo de estudo mais eficiente e motivador.

---

## 🚀 Funcionalidades Principais

### 🎮 Perfil do Aluno

* Interface **gamificada** e intuitiva
* Feedback visual imediato para respostas corretas e incorretas
* Foco no aprendizado progressivo e motivador

### 🧠 Lógica Adaptativa

* Análise automática do desempenho do aluno
* Priorização das **tabuadas com menor taxa de acerto**
* Reforço direcionado às principais dificuldades

### 📊 Painel do Professor

* Dashboard em **tempo real** com estatísticas da turma
* Identificação automática de alunos que precisam de reforço
* Apoio à tomada de decisão pedagógica

### 💾 Persistência de Dados

* Armazenamento do histórico de progresso dos alunos
* Gerenciamento de credenciais de acesso
* Integração com banco de dados **MongoDB**

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Flask (Back-end)
* **Banco de Dados:** MongoDB (NoSQL)
* **Frontend:** HTML5, Tailwind CSS (UI/UX)
* **Arquitetura:** Cliente-Servidor (Arquitetura em 3 Camadas)

---

## 🔑 Credenciais de Acesso (Ambiente de Teste)

Para testar as diferentes visões do sistema, utilize os usuários previamente configurados no banco de dados.

### 👨‍🏫 Painel do Professor (Visão de Gestão)

| Usuário | Senha    | Perfil        |
| ------- | -------- | ------------- |
| admin   | admin123 | Administrador |
| rafael  | 12345    | Professor     |

### ✍️ Interface do Aluno (Quiz de Reforço)

| Usuário   | Senha    | Perfil |
| --------- | -------- | ------ |
| estudante | aluno123 | Aluno  |
| joao      | tabuada  | Aluno  |

---

## 📦 Como Executar o Projeto

### 1️⃣ Instalar as Dependências

```bash
pip install flask pymongo
```

### 2️⃣ Configurar o Banco de Dados

* Certifique-se de que o **MongoDB** está em execução localmente ou via **MongoDB Atlas**.
* Execute o script de configuração inicial para criar os usuários e dados padrão:

```bash
python setup_db.py
```

### 3️⃣ Iniciar o Servidor

```bash
python app.py
```

### 4️⃣ Acessar a Aplicação

Abra o navegador e acesse:

```
http://127.0.0.1:5000
```

---

## 📊 Estrutura do Projeto

```text
📁 Projeto-Multidisciplinar-III-Ciencia-da-Computacao/
/
├── app.py                # Servidor Flask e lógica de rotas
├── setup_db.py           # Script de configuração inicial do MongoDB
├── templates/            # Telas da aplicação
│   ├── index.html        # Tela de Login
│   ├── aluno.html        # Interface do Quiz
│   ├── professor.html    # Dashboard de gestão
│   └── resultado.html    # Resumo do desempenho
└── README.md             # Documentação
```

---

## 👨‍💻 Autoria

**Desenvolvido por:** Rafael Teixeira

**Curso:** Ciência da Computação
**Disciplina:** Projeto Multidisciplinar III
