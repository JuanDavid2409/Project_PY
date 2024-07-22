def main():
    
    menu = {
        "baja taco": 4.00,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 9.50,
        "buper quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salada": 8.00
    }
    
    order_total = 0.0
    
    while True:
        try:
            item = input("Ingrese su pedido: ")
        except EOFError:
            break
        
        item = item.lower()
        
        if item in menu:
            order_total += menu[item]
            print(menu[item])
        elif item == "control-d":
            print(f"El total es ${order_total:.2f}")
            break
        else:
            print("Articulo no se encuentra en el menu")
            
if __name__ == "__main__":
    main()
    
