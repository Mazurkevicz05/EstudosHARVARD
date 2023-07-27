#criou a variavel e colocou um codigo para numero inteiro e codigo para o usuario conseguir inserir um numero
pontuação = int(input("Sua pontuação: "))

#temos que colocar nome da variavel
if  pontuação >= 9 : 
    print("Parabens sua nota foi 10")

elif pontuação >= 3 and pontuação <=8:
    print("A gente pensa !")

#não precia colocar nenhuma condição dentro somente colocar else e o print
else:
    print("Você reprovou ")