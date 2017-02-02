# -*- coding: cp1252 -*-
#Definir que tipo de variavel eh

def DefinirTipoInteiro(variavel):
    Numeros = [0,1,2,3,4,5,6,7,8,9]
    try:
        variavel = int(variavel)
        if int(variavel)+1 == variavel+1:
            print "eh um numero"
        return True 
    except:
        print "nao eh um numero"
        return False
def DefinirTipoString(variavel):
    Alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','=']
    try:
        if variavel[0] in Alfabeto:
            print "eh um texto"
            return True
        elif variavel[0] not in Alfabeto:
            if int(variavel+1) == variavel+1:
                print "nao eh um texto"
                return False
            elif variavel[0] == "[":
                print "nao eh um texto"
                return False
            else:
                print "ehh um texto"
                return False
    except:
        print "nao eh uma string"
        return False
while True:
    variavel = raw_input("Digite o valor da variavel")
    DefinirTipoInteiro(variavel)
    DefinirTipoString(variavel)
    if variavel == 'aaaaaaaaaa':
        break
