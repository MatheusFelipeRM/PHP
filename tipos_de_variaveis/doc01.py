#variavel global
nome = "john"

def exibirNome():
    #variavel local
    #nome = "Fred"

    #declarando a variavel em global
    global nome
    nome2 = "Fredy"
    print(nome)

exibirNome()

print(nome2)