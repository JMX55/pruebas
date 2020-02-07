
number_to_guess = 2
contador = 0

#user_number = int(input("Adivina un numero"))

while contador <= 5:
    user_number = int(input("Adivina un numero"))
    if number_to_guess == user_number:
        print("has ganado")
        break
    else:
        print("Intentalo de nuevo")
    contador += 1



