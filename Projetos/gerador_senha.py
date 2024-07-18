#Gerador de Senha
import random


def caracteres():
    Maiusculos = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    minusculos = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    numeros = ("0","1", "2", "3", "4", "5", "6", "7", "8", "9")
    caracteres_especiais = ("!", "@", "#", "$", "%", "&", "*", "-", "_", "=", "+", "/", "|", "<", ">", ";", ":", "/", "?")

    return Maiusculos, minusculos, numeros, caracteres_especiais
def inputs():
    while True:
        try:
            
            tamanho = int(input("Digite o tamanho da senha: "))
            letraMaiuscula = input("Adicionar letra Maiusculas (S/N): ").upper()
            letraminuscula = input("Adicionar letra minuscula (S/N): ").upper()
            addnumeros = input("Adicionar Números: (S/N): ").upper()
            caracteresespeciais = input("Adicionar Caracteres Especiais: (S/N): ").upper()

            return tamanho, letraMaiuscula, letraminuscula, addnumeros, caracteresespeciais
        except (ValueError, TypeError):
            print("ERROR, Digite apenas valores válidos")


def gerar_senha(tam, lM, lm, num, ce, Maiusculos, minusculos, numeros, caracteres_esp):
    conjuntos = []

    if lM == "S":
        for l in Maiusculos:
            conjuntos.append(l)
    
    if lm == "S":
        for l in minusculos:
            conjuntos.append(l)
    if num == "S":
        for l in numeros:
            conjuntos.append(l)
    
    if ce == "S":
        for l in caracteres_esp:
            conjuntos.append(l)

    if not conjuntos:
        print("Escolha pelo menos uma opção para gerar senha")

    senha = []

    while len(senha) <= tam:
        caracteres_aleatorios = random.choice(conjuntos)
        senha.append(caracteres_aleatorios)

    senha_gerada = ''.join(senha)

    return senha_gerada

def design():
    print(f"""
{'=' * 30}
{'GERADOR DE SENHA'.center(30)}
{'=' * 30}
          """)

def main():
    while True:
        design()
        mm, m, n, cce = caracteres()
        tam, lM, lm, num, ce = inputs()
        senha = gerar_senha(tam, lM, lm, num, ce, mm, m, n, cce)

        if senha:
            print(f"\nSua senha foi gerada com sucesso: {senha}")

        cont = ' '
        while cont not in "SN":
            cont = input("\nDesejar continuar usando Gerador de Senhas: (S/N): ").upper()

        if cont == "N":
            break


main()

