"""
Ejercicio 2.3.3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.

"""

from src.ej2_32b import comprobarNum

def cuentaAtras (num: int):
    serie = ""
    for i in range (num,0,-1):
        serie += str(i)
        if i !=1:
            serie += ","
        else:
            serie += "."
    return serie


def main ():
    
    error = True
    while error:
        num = input("Introduzca un número entero positivo: ")
        try: 
            comprobarNum (num)
            error = False
        except ValueError:   
            print("Error. No está introduciendo un NÚMERO ENTERO POSITIVO.")
            
        except Exception:
            print("Error. No está introduciendo un NÚMERO ENTERO POSITIVO.")
        
    num = int(num)
    print (f"Esta es la cadena de todos los números hacia atrás: \n{cuentaAtras(num)}")


if __name__ == "__main__":
    main()


