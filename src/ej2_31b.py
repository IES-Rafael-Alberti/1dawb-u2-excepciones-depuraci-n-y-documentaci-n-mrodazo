"""
Ejercicio 2.3.1¶
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

"""

def comprobarNumero(numero: str) -> bool:
    """
    Comprobar que se trata de un número entero .
    
    Args:
        numero (str): string que toma el valor del número introducido.
    Retorna:    
        True o False dependiendo si el argumento 'número' es un entero.
    """
    try:
        int(numero)
        return True
    except ValueError:
        return False 


def mostrarYears (edad: int) -> str:
    """
    Crea un string con los años cumplidos separados por un guión.
    
    Args:
        edad (int): entero que represnta la edad solicitada.
    Retorna:    
        years: cadena de caracteres con todos los años cumplidos desde 1 hasta edad separados por un guión.
    """

    if edad < 0:
        raise ValueError("Edad no puede ser negativa")

    years = ""
    for i in range (1,edad+1):
        years += str(i)
        if i != edad:
            years += "-"
        else:
            years += "."
    return years


def main():
    edad = input("Introduzca su edad: ")
    while comprobarNumero(edad) != True:
       edad = input("Error. Introduzca su edad en años: ")
    edad = int(edad)

    try:
       print (f"Esta es la cadena de todos los años que ha cumplido: \n{mostrarYears(edad)}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()