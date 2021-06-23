#!/usr/bin/env python3

def main():
    print(" _                      ___          _                   ")
    print("|_) o __ _|_    __ _     |  _  __ _ |_) _    _|_ o  _  _ ")
    print("|   | | | |_|_| | (_|    | (/_ | (_||  (/_|_| |_ | (_ (_|")
    print("~~~~~~~~~~~~~~~~~~~~~   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    # First Step - Image loading and reading parameters
    try:
        image_path = input("Caminho da imagem a ser convertida: ").rstrip()
        ink_quant  = int(input("Quantidade de tintas desejadas: "))
    except:
        print("Erro: verifique se o caminho da imagem ou a quantidade de tintas foram inseridas corretamente!")
        exit(0)

    # Second Step - 
    

if __name__ == "__main__":
    main()