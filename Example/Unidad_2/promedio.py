grades = []

while True:
    grade = input("Ingresa una nota (o 'salir' para terminar): ")
    if grade.lower() == "salir":
        break
    else:
        grades.append(float(grade))
        
prom = sum(grades)/len(grades)

print(prom)