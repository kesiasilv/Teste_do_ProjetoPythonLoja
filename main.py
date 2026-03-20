from Funcionalidades.produtos import blusas, calcas, sapatos
from Funcionalidades.carrinho import Carrinho
from Funcionalidades.loja import Loja


loja = Loja(blusas, calcas, sapatos)
carrinho = Carrinho()

def menu_principal():
    while True:
        print("--------------------------------------------------------------")
        print("---------- BEM-VINDO À LOJA VIRTUAL DE ROUPAS PYSTORE --------")
        print("--------------------------------------------------------------")
        print("Insira a opção que deseja para prosseguir sua compra na loja:")
        print("\n")
        print("1 - Exibir produtos da loja")
        print("2 - Adicionar produto ao carrinho")
        print("3 - Remover produto do carrinho")
        print("4 - Sair")
        print("\n")

        opcao = input("Selecione a opção desejada: ")

        if opcao == "1":
            loja.exibir_produtos()

        elif opcao == "2":
            while True:
                nome_produto = input("\nDigite o nome do produto que deseja adicionar ao carrinho: ")
                try:
                    quantidade = int(input("\nInsira a quantidade desejada: "))
                    for produto in loja.blusas + loja.calcas + loja.sapatos:
                        if produto.nome_produto.lower().strip() == nome_produto.lower().strip():
                            carrinho.adicionar_roupas(produto, quantidade)
                            break
                    else:
                        print("Produto não encontrado. Tente novamente.\n")
                except ValueError:
                    print("Quantidade inválida. Use apenas números.\n")

                print("\n1 - Adicionar mais produtos")
                print("2 - Finalizar compra")
                print("3 - Voltar ao menu principal")
                sub_opcao = input("Escolha uma opção: ")

                if sub_opcao == "1":
                    continue
                elif sub_opcao == "2":
                    if not carrinho.itens:
                        print("Carrinho vazio. Nenhum produto para finalizar.")
                    else:
                        loja.simular_pagamento(carrinho)
                    break
                elif sub_opcao == "3":
                    break
                else:
                    print("Opção inválida. Voltando ao menu principal.\n")
                    break

        elif opcao == "3":
            if not carrinho.itens:
                print("O carrinho está vazio.\n")
                continue

            carrinho.exibir_itens()
            remove_produto = input("\nDigite o nome do produto que deseja remover do carrinho: ").strip()
            for produto, quantidade in carrinho.itens:
                if produto.nome_produto.lower().strip() == remove_produto.lower():
                    carrinho.itens.remove((produto, quantidade))
                    produto.quantidade += quantidade
                    print(f"{quantidade} '{produto.nome_produto}' removido(s) do carrinho.\n")
                    break
            else:
                print("Produto não encontrado no carrinho.\n")

        elif opcao == "4":
            print("Obrigado por visitar a Loja Virtual PyStore! Volte sempre!\n")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu_principal()
