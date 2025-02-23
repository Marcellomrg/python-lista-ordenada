lista = []
i = 0
while True:
    number = int(input('Digite um valor: '))
    lista.append(number)

    j = i
    while j > 0 and lista[j] < lista[j - 1]:

        temp = lista[j]
        lista[j] = lista[j - 1]
        lista[j - 1] = temp
        j -= 1

    i += 1
    print(f'O {number} foi adicionado na posição {lista.index(number)} da lista')

    pergunta = input('Quer continuar? (s/n): ')
    if pergunta.lower() != 's':
        break

print('Lista final ordenada:', lista)