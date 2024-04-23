print("Bem vindo, escreva números a vontade e para finalizar gigite o número 30000")
contador = 0
soma = 0
maior = 0
menor = 9999999999999
contadorPar = 0
contadorImpar = 0
porcentagemImpar = 0
par = 0
n = 0
while n != 30000:
  contador = contador + 1
  n = float(input("Digite um número "))
    soma = soma + n
    media = soma / contador

  if n > maior:
    maior = n
  
  if n < menor:
    menor = n
   
  if n % 2 == 0:
    contadorPar = contadorPar + 1     
    par = par + n
    mediaPar = par / contadorPar
  else:
    contadorImpar = contadorImpar + 1

porcentagemImpar = ((contadorImpar/contadorPar)* 100)
print("A soma de todos os números é = ", soma)
print("A quantidade de numeros digitados é = ", contador)  
print("A média dos números digitados é = ", media)  
print("O maior número digitado é = ", maior)    
print("O menor número digitado é = ", menor)
print("A média dos números pares é = ",mediaPar)
print("A porcentagem de número impar entre dosos os números digitados é = ", porcentagemImpar, "%")    