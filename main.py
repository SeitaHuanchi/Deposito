from data_user import Data

def main():

    client_x = 0
    name = ""
    run = 0 
    amount = 0

    name = input("Ingrese el nombre: ")
    run = int(input("Ingrese el run (sin DV): "))
        
    client_x = Data(name,run,amount)
    
    client_x.display()
    print("\nDesea ingresar un monto?")
    print("1.-Si    y    2.-No")
    opcion = int(input())
    if(opcion == 1):
        client_x.deposit()
        #print("\n")
        client_x.display()
    else:
        print("Hasta luego")


if __name__ == "__main__":
    main()
