Palavra = "AMOR"
ListaPalavra = []
for i in range (len(Palavra)):
    Palavra[i].append(ListaPalavra)
while (n < len(Palavra)) or (erro <= 6):
    Letra = raw_input("Digite uma letra : ")
    if Letra in ListaPalavra:
            n+=1
    elif Letra not in ListaPalavra:
            erro+=1
    
