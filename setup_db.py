from pymongo import MongoClient

def inicializar_banco():
    # Conecta ao MongoDB local
    client = MongoClient("mongodb://localhost:27017/")
    db = client["escola_saber_mais"]
    usuarios_col = db["usuarios"]

    # Limpa a coleção para não duplicar se rodar duas vezes
    usuarios_col.delete_many({})

    # Lista de utilizadores para inserir
    lista_usuarios = [
        {"usuario": "admin", "senha": "admin123", "perfil": "professor"},
        {"usuario": "rafael", "senha": "12345", "perfil": "professor"},
        {"usuario": "estudante", "senha": "aluno123", "perfil": "aluno"},
        {"usuario": "joao", "senha": "tabuada", "perfil": "aluno"}
    ]

    # Insere no banco
    usuarios_col.insert_many(lista_usuarios)
    print("✅ Banco de dados inicializado com sucesso!")
    print("Utilizadores criados: admin, rafael, estudante, joao.")

if __name__ == "__main__":
    inicializar_banco()