#imc = peso (kg) / (altura (m)*2)
# 18.5 y 24.9 saludable - debajo de 18.5 bajo peso - encia de 24.9 sobre peso

def main():
    peso = float(input("Ingrese su peso actual (KG): "))
    altura = float(input("Ingrese su altura actual (M)"))
    
    resultado = imc(peso, altura)
    
    if resultado < 18.5:
        print(f"Bajo peso con un IMC {resultado: .2f}")
    elif resultado > 24.9:
        print(f"Sobre peso con un IMC {resultado: .2f}")
    else:
        print(f"Saludable con un IMC {resultado:.2f}")
    

def imc(p, a):
    return p / (a**2)


if __name__ == "__main__":
    main()