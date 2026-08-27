nombre = input("Nombre del empleado: ")
horas = int(input("Numero de horas trabajadas: "))
valor_hora = int(input("Valor de cada hora: "))

salario = horas * valor_hora

print("Empleado:", nombre)
print("Horas trabajadas:", horas)
print("Valor hora: $", valor_hora)
print("Salario: $", salario)