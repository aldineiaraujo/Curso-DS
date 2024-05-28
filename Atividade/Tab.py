print("Tabuada")

input("Data: ")

numero_tabuada = int(input("Digite o número para a tabuada: "))

def tabuada(numero):
    print(f"Tabuada de {numero}:")

    for i in range(1, 11):
        
        print(f"{numero} + {i} = {numero + i}")

        
        print(f"{numero} - {i} = {numero - i}")

        
        print(f"{numero} x {i} = {numero * i}")

        
        if i != 0:
            print(f"{numero} ÷ {i} = {numero / i:.2f}".replace(".00", ""))
        else:
            print(f"Divisão por zero não é permitida.")

        print("-" * 20)

tabuada(numero_tabuada)






