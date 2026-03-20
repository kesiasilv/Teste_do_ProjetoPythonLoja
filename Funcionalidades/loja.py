
class Loja:
    def __init__(self, blusas, calcas, sapatos):
        self.blusas = blusas
        self.calcas = calcas
        self.sapatos = sapatos

    def exibir_produtos(self):
        print('Lista de produtos da Loja Virtual PyStore:\n')

        print('--- Blusas ---')
        for blusa in self.blusas:
            print(blusa)

        print('\n--- Calças ---')
        for calca in self.calcas:
            print(calca)

        print('\n--- Sapatos ---')
        for sapato in self.sapatos:
            print(sapato)

    def simular_pagamento(self, carrinho):
        if not carrinho.itens:
            print("Carrinho vazio. Nenhum produto para finalizar.\n")
            return

        total = carrinho.calcular_total()
        print(f"\nTotal da compra: R$ {total:.2f}\n")

        print("\n----------------------")
        print("Métodos de pagamento: ")
        print("----------------------")
        print("1 - Cartão")
        print("2 - Pix (10% de desconto)")

        opcao = input("\nEscolha a forma de pagamento: ")

        desconto = 0.0

        if opcao == "1":
            print("1 - Crédito (sem desconto)")
            print("2 - Débito (5% de desconto)")
            tipo_cartao = input("Escolha o tipo de cartão: ")

            if tipo_cartao == "2":
                desconto = total * 0.05
                total -= desconto
                print(f"Desconto de 5% aplicado. Total com desconto: R$ {total:.2f}\n")
            elif tipo_cartao == "1":
                print("Pagamento via Cartão de Crédito aprovado. Sem desconto.\n")
            else:
                print("Tipo de cartão inválido.\n")
                return

        elif opcao == "2":
            desconto = total * 0.10
            total -= desconto
            print(f"Desconto de 10% aplicado. Total com desconto: R$ {total:.2f}\n")
            print("Pagamento via Pix aprovado.")

    
        else:
            print("Forma de pagamento inválida.")
            return

        print("\n--------------------------------------------------")
        print("------------- RECIBO DA COMPRA -------------------")
        print("--------------------------------------------------")
        carrinho.exibir_itens(mostrar_titulo=False) 
        print(f"Total pago: R$ {total:.2f}")
        print("--------------------------------------------------\n")
        carrinho.esvaziar()
