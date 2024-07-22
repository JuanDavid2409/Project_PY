def main():
    palabra = input("Ingrese la palabra: ")
    res = acortar(palabra)
    print("Abreviacion: " +" ".join(res))
    #acortar(palabra)
    
    
def acortar(pbl):
    pbl = pbl.lower()
    lista=[]
    for i in range(len(pbl)):
        if pbl[i] not in ["a", "e", "i", "o", "u", " "]:
                lista.append(pbl[i]) #Append agrega los elementos a una lista
    return lista

if __name__ == "__main__":
    main()