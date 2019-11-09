'''
    Certo aço é classificado de acordo com o resultado de três testes, que devem verificar se o
    mesmo satisfaz às seguintes especificações:
    a. Teste 1- conteúdo de carbono abaixo de 7%;
    b. Teste 2- dureza Rokwell maior que 50;
    c. Teste 3- resistência à tração maior do que 80.000 psi.
    Ao aço é atribuído o grau 10, se passa pelos três testes; 9 , se passa apenas nos testes 1 e 2;
    8 , se passa no teste 1; e 7, para as outras alternativas. Supondo que sejam lidos de uma
    unidade de entrada o número de amostra, conteúdo de carbono, a dureza Rokwell e a
    resistência à tração faça um programa que leia os dados de uma amostra de aço, escrevendo
    para ela o grau obtido.
'''
carbono = int(input("informe o conteúdo do carbono: "))
rokwell = int(input("Informe a dureza Rokwell: "))
resistencia = int(input("Informe a resistência a tração: "))

if carbono < 7 and rokwell > 50 and resistencia > 80000: 
    print("O grau do aço é 10, pois passou em todos os testes. ")
elif carbono < 7 and rokwell > 50 and resistencia < 80000: 
    print("O grau do aço é 9, pois passou apenas nos testes 1 e 2. ")
elif carbono < 7 and rokwell < 50 and resistencia < 80000: 
    print("O grau do aço é 8, pois passou apenas no teste 1. ")
elif carbono > 7 and rokwell < 50 and resistencia < 80000: 
    print("O grau do aço é 7")