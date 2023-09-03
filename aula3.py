
'''
for i in range(1, 11):
    for j in range(1, 11):
        print(f' {i} x {j} = {i*j}')
    print("-------------------")


x = 1
y = 1

while x <= 10:
    while y <= 10:
        multi = x * y
    
        print(f' {x} x {y} = {multi}')

        y += 1
    print('---------------') 
    x += 1
    y = 1
    '''

notas_ac = 0
voltas = 0

while True:
    nota = input('digite a nota: ')
    
    if nota not in "012345678910":
        print('numero não encontrado')
    else:
        nota = float(nota)

        if nota >= 0 and nota <=10:
            notas_ac += nota
            voltas += 1

            escolha = input("Quer adicionar mais notas ? (s/n)")

            if escolha.lower() == 'n' or escolha.lower == "não" :
                break
        else:
            print('notas apenas entre 0 e 10')

media = notas_ac / voltas

print(f'A media é :{media}')
