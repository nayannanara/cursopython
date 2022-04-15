
secreto = 'perfume'
digitadas = []  #lista vazia
chances = 6

while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Isso não vale... Digite apenas uma letra')
        continue  #volta pro inicio do laço

    digitadas.append(letra)  #adiciona o valor inserido em 'letra' no final da lista 'digitadas'

    if letra in secreto:
        print(f'Boa! "{letra}" está na palavra secreta')
    else:
        print(f'Poxa! "{letra}" não está na palavra secreta')
        digitadas.pop()  #pop() remove o ultimo valor da lista

    temporario = ''
    for ltr_secreta in secreto:
        if ltr_secreta in digitadas:
            temporario += ltr_secreta
        else:
            temporario += '*'

    if temporario == secreto:
        print('CONGRATULATIONS, YOU WINSS  :)')
        print('A PALAVRA SECRETA É: perfume')
        break
    else:
        print(f' Palavra secreta: {temporario}')
    if letra not in secreto:
        chances -= 1
        print(f'Você tem {chances} chances')
    if chances == 0:
        print('Você perdeu  :(')
        break