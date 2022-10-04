#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

# Entrada
Valor = int(input())

contador = 2
resultado = 1
while contador <= Valor:    
	  resultado = resultado * contador
	  contador = contador + 1
	    
print("%i! = %i" %(Valor, resultado))