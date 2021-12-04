numbers = [x for x in range(10)]#Gera 10 numeros do tipo int e os inclui na lista
cont_impar = 0
cont_par = 0

for num in numbers: # iteração sobre a lista numbers
	if num % 2 == 0:  # verifica se o num de numbers è par
		print(num," è par")
		cont_par+=1
	else:# caso nao seja par,
		print(num," è ímpar")
		cont_impar+=1
		
print("na lista [numbers] temos:" ,cont_impar,"numeros impares \ne temos ",cont_par,"numeros pares")