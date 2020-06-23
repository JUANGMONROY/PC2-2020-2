def contarletra(txt,letra):
    suma=0
    for i in txt:
        if (letra==i):
            suma = suma+1
    return suma

def main():
    tx = (input("INGRESE UNA FRASE: ")).lower()
    let = "a"

    print(contarletra(tx,let))

if __name__ == "__main__":
    main()