nombre = input("Nombre: ")
peso = float(input("Peso: "))
estatura = float(input("Estatura (METROS): "))

imc = peso / (estatura ** 2)

print("IMC:", round(imc, 2))