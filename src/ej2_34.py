"""
Ejercicio 2.3.4
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

"""

def comprobarEntero (num):
    if not int(num):
        raise ValueError


def main ():
    num = input("Introduzca un número entero: ")
    try: 
        comprobarEntero (num)
    except ValueError:   
        print("La entrada no es correcta.")
        
    except Exception:
        print("La entrada no es correcta.")
    
    print ("Correcto, has introducido un número entero.")


if __name__ == "__main__":
    main()
