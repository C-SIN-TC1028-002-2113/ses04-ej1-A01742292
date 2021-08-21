def main():
    #escribe tu código abajo de esta línea
    e1= int(input("Ingresa el primer numero"))
    e2= int(input("Ingresa el segundo numero"))
    e3= int(input("Ingresa el tercer numero"))

    if e1 < e2 and e1<e3:
        print(e1)
    elif e2 < e1 and e2<e3:
        print(e2)
    else e3 < e1 and e3<e1:
        print(e3)
    pass

if __name__=='__main__':
    main()
