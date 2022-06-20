carros = ["HVR", "Golf", "Argo", "Focus"]
print(carros)

#IMPRESSÃO POR INDECE
print(carros[0])#DO COMEÇO PARA O FIM
print(carros[-1])#DO FIM PARA O COMEÇO

#MUDANÇÃ DE CARRO
carros[0] = "BMW"
print(carros[0])

#INCLUSÃO DE VALORES NA LIST
carros.append("Volvo")
carros.append("Camaro")
carros.append("Audi TT")
print(carros)

#VENDO O TAMANHO DA LIST
print(str(len(carros)) + "Carros na list")

#REMOVENDO VALOR
carros.remove("Volvo")
print(carros)

#REMOVENDO O ULTIMO ELEMENTO DA LIST(POP, DEL, CLEAR)
#POP
carros.pop()
print(carros)
#DEL
del carros[2]
print(carros)
#clear(APAGA TUDO)
carros.clear()
print(carros)

#COPIANDO UMA LIST PARA OUTRA
carros2 = list(carros)
print(str(len(carros2)) + " Tamannho de carro2")

#FUNDINDO LIST
carros2 = ["Opala", "Maverick", "Honda Civc"]
carros3 = carros + carros2
print(carros3)




