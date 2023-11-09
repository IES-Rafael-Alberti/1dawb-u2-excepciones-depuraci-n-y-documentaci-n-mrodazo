"""
Ejercicio 2.3.2
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

En este caso no capturamos el error en la función

"""
def comprobarNum (num):
    if int(num) < 1:
        raise ValueError


def mostrarImpares (num: int) -> str:
    """
    Crea un string con los números impares desde 1 hasta el número introducido, separado por comas. En el caso de introducir un número positivo, se mostrará es impar anterior a positivo introducido.
    
    Args:
        num (int): entero que representa el final de la cadena.
    Retorna:    
        impares: cadena de caracteres con todos los números impares desde 1 hasta num separadps por comas.
    """
    impares = ""
    if (num%2 == 0):
        num = num - 1
    for i in range (1,num+1,2):
            impares += str(i)
            if i !=num:
               impares += ","
            else:
                impares += "."
    return impares
   


def main():
    num = input("Introduzca un número entero positivo: ")
    try: 
       comprobarNum (num)
    except ValueError:   
        num = input("Error. Introduzca un ENTERO POSITIVO: ")
    num = int(num)
    print (f"Esta es la cadena de todos los números impares: \n{mostrarImpares(num)}")




if __name__ == "__main__":
    main()