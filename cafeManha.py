import os

#lista opções cafe da manha1
menu_cafe = [{'nome': 'Ovos'},
                {'nome': 'Panquecas'},
                {'nome': 'Wafles'},
                {'nome': 'Frutas'}]


#dicionário de acompanhamentos
acompanhamentos = {1: "Mel",
                   2: "Manteiga",
                   3: "Ketchup",
                   4: "Mostarda",
                   5: "Maionese"}

def exibir_opcoes():
    print("Qual a escolha para o café da manha: \n")
    #Ela percorre sua lista menu_cafe e ao mesmo tempo cria uma numeração automática.
    #com o (numero) enumerando e (item) sendo a lista, e o start é para começar com 1 ao invez de 0
    for numero, item in enumerate(menu_cafe, start=1):
        print("{} - {}".format(numero, item['nome']))


def acomp():
    escolha_acomp = input("Deseja acompanhamento?, (Sim) ou (Não)?: ").lower()

    if escolha_acomp == "sim":
        print("Qual acompanhamento deseja?: ")
        for chave, valor in acompanhamentos.items():
            print("{} - {}".format(chave, valor))
        opcao = int(input("Digite o número da opção: "))
        if opcao in acompanhamentos:
                print("Você escolheu Ovos com {}!".format(acompanhamentos[opcao]))
        else:
            opcao_invalida()
    else:
        print("Sem Acompanhamento!")
        
def ovos():
    print("Você escolheu Ovos!")


def panquecas():
     print("Você escolheu Panquecas!")


def wafles():
     print("Você escolheu Wafles!")


def frutas():
     print("Você escolheu Frutas!")


def voltar_menu_inicial():
    input("\nDigíte uma tecla para voltar ao menu inicial: ")
    main()


def opcao_invalida():
    print("Opção Inválida!")
    voltar_menu_inicial()


def escolher_opcoes():
    try:
        escolha = int(input("Escolha uma das opções: "))

        if escolha == 1:
            ovos()
            acomp()
            voltar_menu_inicial()
        elif escolha == 2:
            panquecas()
            acomp()
            voltar_menu_inicial()
        elif escolha == 3:
             wafles()
             acomp()
             voltar_menu_inicial()
        elif escolha == 4:
             frutas()
        else:
             opcao_invalida
             voltar_menu_inicial()
    except:
         opcao_invalida()


def main():
    os.system("cls")
    exibir_opcoes()
    escolher_opcoes()



if __name__ == "__main__":
    main()