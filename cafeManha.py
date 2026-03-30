import os

#lista opções cafe da manha1
menu_cafe = [{'nome': 'Ovos'},
                {'nome': 'Panquecas'},
                {'nome': 'Wafles'},
                {'nome': 'Frutas'},
                {'nome': 'Pão'},
                {'nome': 'Cereal'},
                {'nome': 'Torradas'},
                {'nome': 'Misto quente'}]


#dicionário de acompanhamentos
acompanhamentos = {1: "Mel",
                   2: "Manteiga",
                   3: "Ketchup",
                   4: "Mostarda",
                   5: "Maionese",
                   6: "Frutas",
                   7: "Nutella",
                   8: "Geleia de Morango"}


#Lista bebidas
bebidas_cafe = {1: "Coca-Cola",
           2: "Fanta",
           3: "Café",
           4: "Suco de Laranja",
           5: "Suco de Uva",
           6: "Limonada",
           7: "Água",
           8: "Leite com Achocolatado"}

def exibir_opcoes():
    print("Qual a escolha para o café da manha: \n")
    #Ela percorre sua lista menu_cafe e ao mesmo tempo cria uma numeração automática.
    #com o (numero) enumerando e (item) sendo a lista, e o start é para começar com 1 ao invez de 0
    for numero, item in enumerate(menu_cafe, start=1):
        print("{} - {}".format(numero, item['nome']))


def acomp(pedido):
    escolha_acomp = input("Deseja acompanhamento?, (Sim) ou (Não)?: ").lower()

    if escolha_acomp == "sim" or escolha_acomp == "s":
        print("Qual acompanhamento deseja?: ")
        for chave, valor in acompanhamentos.items():
            print("{} - {}".format(chave, valor))
        opcao_acomp = int(input("Digite o número da opção: "))
        if opcao_acomp in acompanhamentos:
                acompanhamento = acompanhamentos[opcao_acomp]
                print("Você escolheu {} com {}!".format(pedido, acompanhamento))
                bebidas(pedido, acompanhamento)
        else:
            opcao_invalida()
    else:
        print("Sem Acompanhamento!")
        bebidas(pedido, None)
        

def bebidas(pedido, acompanhamento):
    escolha_bebidas = input("Deseja alguma bebida?, (Sim) ou (Não): ").lower()
    
    if escolha_bebidas == "sim" or escolha_bebidas == "s":
        print("Qual bebida deseja: ")
        for chave, valor in bebidas_cafe.items():
            print("{} - {}".format(chave, valor))
        opcao_bebidas = int(input("Digite o número da bebida escolhida: "))
        if opcao_bebidas in bebidas_cafe:
            bebida = bebidas_cafe[opcao_bebidas]
            if acompanhamento:
                print("Pedido final: {} com {} e {}".format(pedido, acompanhamento, bebida))
            else:
                print("Pedido final: {} e {}".format(pedido, bebida))
        else:
            opcao_invalida()
    else:
        if acompanhamento:
            print("Pedido final: {} com {}".format(pedido, acompanhamento))
        else:
            print("Pedido final: {}".format(pedido))



def ovos():
    print("Você escolheu Ovos!")

def panquecas():
     print("Você escolheu Panquecas!")

def wafles():
     print("Você escolheu Wafles!")

def frutas():
     print("Você escolheu Frutas!")

def pao():
    print("Você escolheu Pão")

def cereal():
    print("Você escolheu Cereal!")

def torradas():
    print("Você escolheu Torradas!")

def mistoquente():
    print("Você escolheu Misto quente!")

def voltar_menu_inicial():
    input("\nDigíte uma tecla para voltar ao menu inicial: ")
    main()


def opcao_invalida():
    print("Opção Inválida!")


def escolher_opcoes():
    try:
        escolha = int(input("Escolha uma das opções: "))

        if escolha == 1:
            pedido = "Ovos"
            ovos()
            acomp(pedido)
            voltar_menu_inicial()

        elif escolha == 2:
            pedido = "Panquecas"
            panquecas()
            acomp(pedido)
            voltar_menu_inicial()

        elif escolha == 3:
            pedido = "Wafles"
            wafles()
            acomp(pedido)
            voltar_menu_inicial()

        elif escolha == 4:
            pedido = "Frutas"
            frutas()
            acomp(pedido)
            voltar_menu_inicial()

        elif escolha == 5:
            pedido = "Pão"
            pao()
            acomp(pedido)
            voltar_menu_inicial()

        elif escolha == 6:
            pedido = "Cereal"
            cereal()
            acomp(pedido)
            voltar_menu_inicial()

        elif escolha == 7:
            pedido = "Torradas"
            torradas()
            acomp(pedido)
            voltar_menu_inicial()

        elif escolha == 8:
            pedido = "Misto quente"
            mistoquente()
            acomp(pedido)
            voltar_menu_inicial()

        else:
             opcao_invalida()
             voltar_menu_inicial()

    except ValueError:
         opcao_invalida()


def main():
    os.system("cls")
    exibir_opcoes()
    escolher_opcoes()



if __name__ == "__main__":
    main()