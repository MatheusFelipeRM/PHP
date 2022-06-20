from posixpath import split


nome = "  SKYline o melhor ";

print("strip:" + nome.strip())
#STRING É UM ARRAY DE CARACTERES
print(nome[1])
#UMA FORMA DE DIZER QUE EU QUERO OS VALORES DA POSIÇÃO 0 ATE A POSIÇÃO 8
print(nome[0:8])
#len() SERVE PARA SABER O TAMANHO
print("tamanho: " + str(len(nome)))
#TRANFORMA TUDO EM MINUSCULO
print(nome.lower())
#TRANFORMA TUDO EM MAIUSCULO
print(nome.upper())
#TROCA O VALOR INDICADO DE UMA STRING POR OUTRA
print(nome.replace("SKYline", "Supra"))
#SPLIT NO EXEMPLO AI TODA VEZ QUE ELE ENCONTRAR UM ESPAÇO ELE VAI QUEBRAR A STRING EM ARRAY
a = nome.split(" ")
print("a: " + a[0])

