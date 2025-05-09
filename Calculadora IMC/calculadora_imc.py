#1.receber a variável peso [float]
#2.receber a variável altura [altura]
#3. realizar o calculo de imc = (peso / altura²)
#4. imprimir o resultado do imc

#Operações usadas : soma (+), divisão (/) e potência (**)

peso = float(input('Insira o peso:'))
print(peso)

altura = float(input('Insira a altura:'))
print(altura)

imc = peso / (altura**2)
print(imc)