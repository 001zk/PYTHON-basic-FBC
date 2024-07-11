#print("hello world!")

#codigo = 105
#salario = 1650.00
#nome = 'josé Santana'
#ativo = True

#print('codigo',codigo, "nome: ", nome, "O salario atual é de", salario)
#codigo = int(input("Digite o codigo do funcionario"))
#nome = input("digite o nome do funcionario")
#salario = float(input("Digite o salario do funcionario "))
#ativo = True
#print("codigo: %d " % codigo)
#print("nome: %s" % nome)
#print("Salario: %.2f" % salario)
#print("ativo: %r " % ativo)

#fruta = input('Digite o nome de uma fruta')
#print(fruta)

#modulo 04

#A = 5
#B = 15
#C = 20

#print ("A == B AND B > C : ", A == B and B > C)
#print ("A < B OR B > C : ", A < B or B > C)
#print ("not A == B : ", not A == B)

#idade = int (input ("'Digite a idade da pessoa"))
#if idade > 18:
 #   print("maior de idade")
#if idade < 18: 
    #print("menor de idade")

#A = input("Informe um valor para a variavel A: ")
#B = input("Informe um valor para a variavel B: ")

#if (A>B):
#    aux=A;
 #   A=B;
#    B=aux;
#print("O valor da variavel A agora é : ", A);
#print("O valor da variavel B agora é :", B);

#idade = int (input ("Digite a idade da pessoa: "))
#if idade > 18:
  #  print("Maior de idade")
#else:
#    print("menor de idade")

#notaA=float(input("informe a primeira nota: "))
#notaB=float(input("informe a segunda nota: "))

#calcular media

#mediafinal = (notaA + notaB) / 2

#verificação
#if mediafinal >=7.0:
   # print("A media: %.1f - aprovado"% mediafinal)
#else:
  #print("A media: %.1f - Reprovado " % mediafinal

#idade = int(input ("Digite a idade da pessoa: "))
#if idade > 18:
# print("maior de idade")
#elif idade >16:
    #    print("infanto juvenil")
#else:
   #     print("menor de idade")

#for n in range(10):
#  print(n)

#for n in range(5, 16):
  #print(n)


#for n in range(10,0, -1):
 # print(n)

#x = 1;
#while x<=15:
 # print(x);
  #x=x+1

  #Media valores

#qtd =0
#soma=0
#media=0
#valor = float(input("Digite um valor: "))

#while (valor > 0.0):
  #soma = soma + valor
  #qtd = qtd + 1
  #Entrada de valores
  #valor = float(input("Digite um valor: "))

#caso digite um valor negativo o laço encerra
#media = soma / qtd
#print("\n Total da soma: ", soma)
#print("\n Quantidade de valores digitados: ", qtd)
#print("\n Media dos valores: ", media)

#MODULO 05

## def
#def mensagem1():
#  print("hello world")

#def mensagem2():
#  return 'hello world'

#mensagem1()

#texto = mensagem2()
#print(texto)

#def lernotas():
 # n=float(input('digite uma nota para o aluno (a):' ))
 # return n


#def resultado(n1,n2):
 # media=(n1+n2)/2
 # print("nota:1 ", n1)
 # print("nota 2: ", n2)
 # print("media: ", media, "resultado: ", end="")
 # if media >= 7:
 #   print("aprovado")
 # else:
 #   print("reprovado")

#a = lernotas()
#b = lernotas()
#resultado(a,b)

##modulo 6

##gravar

##write/open
 
#arquivo = open('arqText.txt', 'w')

#arquivo.write('curso python \n')
#arquivo.write('Aula Pratica')
#arquivo.close()

#arquivo = open('arqText.txt', 'w')

#arquivo.write('curso Python \n')
#arquivo.write('Aula Pratica')
#arquivo.close()

##Leiturado arquivo texto

#leitura=open('arqText.txt', 'r')
#print(leitura.read())
#leitura.close()
