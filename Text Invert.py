Sair = 0
while Sair == 0:
    string = raw_input ("Digite o Texto: ")
    Tamanho = len(string)-1
    Nome = ''
    while Tamanho >= 0 :
        Nome = Nome + string[Tamanho]
        Tamanho-=1
    print Nome
    print "Deseja Sair? 1. Para Sim  0. Para Não"
    Sair = input()
