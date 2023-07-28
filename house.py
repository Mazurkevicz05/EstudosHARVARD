nome = input("Qual seu nome? ")

#Aqui coloquei um variavel junto com um nome e com uma codição caso o nome tenha a mesma condição colacamos or 
if nome == "Matheus":
    print("Coxa branca")
elif nome == "Nelson" or nome == "Isabella":
    print("Palmeirense")
elif nome == "Josineide":
    print("Atleticana")

else:
    print("Quem?")

#Existe outro metodo aonde colocamos um MATCH com a variavel e invés de colocar if ou elif colocamos case, no lugar de else case_ e no lugar de or colocamos barras verticais sem variaveis.