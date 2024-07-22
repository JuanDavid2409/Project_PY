camel_case = input("Ingrese variable en Camel Case: ")
snake_case = ""

for i in range (len(camel_case)):
    if camel_case[i].isupper():
        snake_case += "_" + camel_case[i].lower()
    else:
        snake_case += camel_case[i]
        
print("El nombre de la variable es ", snake_case)