from ast import NotIn


nome = "SKYline o melhor"

#O IN SERVE PARA VERIFICAR SE A STRING ESTA DENTRO DA VARIAVEL(TRUE OU FALSE)
res = "SKYline" in nome;
print(res)

#O IN SERVE PARA VERIFICAR SE A STRING NÃO ESTA DENTRO DA VARIAVEL(TRUE OU FALSE)
res = "SKYline" not in nome;
print(res)


texto = "Skyline o melhor"
palavra = "Skyline"

res = palavra.lower() in texto.lower();
print(res)

res = palavra.upper() not in texto.upper();
print(res)