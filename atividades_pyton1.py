'''print("atividade\n" +
      "2-")

numero_imp = list()

while True:
    num = int(input("digite um numero: "))

    if num % 2 != 0:
        numero_imp.append([num])
            
        if len(numero_imp) == 10:
            break

print(numero_imp)
'''

print("atividade\n" +
      "4-")

lista = list()
lista_par = list()

while True:
    num = int(input('Digite um numero: '))

    lista.append([num])

    if num % 2 == 0:
        lista_par.append([num])
    if len(lista) == 20:
        break
print()
print(f"o numero total de numeros pares foi {len(lista_par)}")
print()
print(lista_par)


