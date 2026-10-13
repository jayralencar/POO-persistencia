# CLI
from src.repositories import CadastroPessoasJson
from src.repositories import CadastroPessoasSQLite
from src.domain import Pessoa

CAMINHO = "./data/pessoas.json"
repositorioPessoa = CadastroPessoasJson(CAMINHO)

CAMINHO_SQLITE = "./data/pessoas.db"
repositorioPessoa = CadastroPessoasSQLite(CAMINHO_SQLITE)

while True:
    print("Menu")
    print("1 - Listar pessoas")
    print("2 - Cadastrar pessoa")
    print("0 - sair")
    opcao = input()
    if opcao == "0":
        break
    
    elif opcao == "1":
        
        lista = repositorioPessoa.carregar()
        if len(lista) == 0:
            print("Nenhuma pessoa cadastrada")
        for pessoa in lista:
            print(pessoa)
        id_pessoa = int(input("selecione uma pessoa pelo ID (ex: 1): "))
        pessoa_da_vez = repositorioPessoa.get_by_id(id_pessoa)
        print(pessoa_da_vez)
    elif opcao == "2":
        nome = input("Nome da pessoa")
        email = input("E-mail da pessoa")
        idade = int(input("Idade da pessoa"))

        nova_pessoa = Pessoa(nome, email, idade)
        
        repositorioPessoa.adicionar(nova_pessoa)



        