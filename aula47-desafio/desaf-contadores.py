'''Desafio dos contadores'''
'''Retornar os seguintes caracteres:
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
'''

c1 = 0
c2 = 10

while True:
    print(c1, c2)
    c1 += 1
    c2 -= 1

    if (c1 == 8 and c2 == 2):
        print(c1, c2)
        break

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'''"""
print()

for p, r in enumerate(range(10,1, -1)):
    print(p, r)
