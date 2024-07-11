arquivo = open('arqText.txt', 'w')

arquivo.write('curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close()

#Leiturado arquivo texto

leitura=open('arqText.txt', 'r')
print(leitura.read())
leitura.close()