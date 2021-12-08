# ========= Calculadora Python ===========
import time
adic = lambda a,b: a+b # Adiçao
mult= lambda a, b: a*b # Multiplicação
sub= lambda a,b: a-b # Subtração
div = lambda a, b: a / b # Divisão

def painel( ):
	print("""
	     ====Calculadora Python====
	     
	     Escolha a operação:
	            
	     [1] Adição
	     [2] Multiplicação
	     [3] Dividir
	     [4] Subtrair
	     
	     S - sair
	           
	""")


while True:
	painel()
	ent = input("Escolha uma das opçoes: ")
	
		
	if ent.upper() == 'S':
		print("fechando calculadora python")
		time.sleep(2)
		break
	
	if  int(ent) == 1:
		n1 = int(input("Digite um numero para soma: "))
		n2 = int(input("Digite outro numero: "))
		print(n1, "+",n2,"=",adic(n1,n2))
		time.sleep(3)
	
	elif int(ent) == 2:
		n1 = int(input("Digite um numero para multiplicar: "))
		n2 = int(input("Digite outro numero: "))
		print(n1, "x",n2,"=",mult(n1,n2))
		time.sleep(3)
	
	if int(ent) == 3:
		n1 = int(input("Digite um numero para dividir: "))
		n2 = int(input("Digite outro numero: "))
		print(n1, "÷",n2,"=",div(n1,n2))
		time.sleep(3)
		
	elif int(ent) == 4:
		n1 = int(input("Digite um numero para subtrair: "))
		n2 = int(input("Digite outro numero: "))
		print(n1, "-",n2,"=",sub(n1,n2))
		time.sleep(3)
	
