
apetece_helado_input = input("Te apetece un helado? (Si / No)")

if apetece_helado_input == "Si":
    apetece_helado = True
elif apetece_helado_input == "No":
    apetece_helado = False
else:
    print("Te he dicho que me digas si o no, como no te entiendo cuento como que no")
    apetece_helado = False

tiene_dinero_input = input("Tienes dinero para un helado? (Si / No)")
esta_el_heladero_input = input("Esta el heladero? (Si / No)")
esta_tu_tia_input = input("Estás con tu tia? (Si/ No)")

apetece_helado = apetece_helado_input
tiene_dinero = tiene_dinero_input
esta_tu_tia = esta_tu_tia_input
esta_el_heladero = esta_el_heladero_input

if apetece_helado == "Si"and esta_el_heladero == "Si" and (tiene_dinero == "Si" or esta_tu_tia == "Si"):
    print ("Comete un helado")
else:
    print ("Pues nada")