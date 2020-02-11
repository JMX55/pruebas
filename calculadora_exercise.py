#Calculadora para usuario

operacion_matematica = input("¿Que operacion quieres realizar? (suma, resta, multiplicacion, division)")

operacion_suma = "suma"
operacion_resta = "resta"
operacion_multiplicacion = "multiplicacion"
operacion_division = "division"

primer_numero = int(input("Ingrese un numero"))
segundo_numero =int(input("Ingrese otro numero"))

if operacion_matematica == "suma":
    print(primer_numero+segundo_numero)

elif operacion_matematica == "resta":
    print(primer_numero-segundo_numero)

elif operacion_matematica == "multiplicacion":
    print(primer_numero*segundo_numero)

elif operacion_matematica == "division":
    print(float(primer_numero/segundo_numero))








