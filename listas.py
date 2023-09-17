import random

clientes = list()

while True:
    escolha = int(input("digite uma das opçoes a seguir:\n" +
                        "1 - Adicionar novo cliente. \n" +
                        "0 - Finalizar o sistema\n"))
    
    match escolha:
        case 1:
            nome = input("digite o nome do cliente: ")
            numero= int(input("digite o numero do cliente: "))

            clientes.append([nome, numero])
        
        case 0:
              break

print(clientes)
print('-='*15)
for i, v in clientes:
    print(f"Cliente {i} de numero {v} ")
   
print('-='*15)

print(f' Foi um total de {len(clientes)} clientes')

print('-='*15)


posicao = random.randint(0, len(clientes))


print(clientes[posicao])