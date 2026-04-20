
ancho = 36

max_frec_cardiaca = 123
frec_cardiaca_max_edad = 34
frec_cardiaca_max_nombre = "Fabrizo"
frec_cardiaca_max_genero = "Zepesky"
frec_cardiaca_max_ingreso = "123"

print(f"┌{'─' * ancho}┐")
print(f"│  {'✙ MEDICPY':<{ancho - 2}}│ ")
print(f"│  {'Mayor Frecuencia cardiaca':<34}│")
print(f"├{'─' * ancho}┤")
print(f"│  {'Ingreso':<9} →  {frec_cardiaca_max_ingreso:<21}│")
print(f"│  {'Nombre':<9} →  {frec_cardiaca_max_nombre:<21}│")
print(f"│  {'Edad':<9} →  {str(frec_cardiaca_max_edad) + ' años':<21}│")
print(f"├{'─' * ancho}┤")
print(f"│  {'Temp':<9} →  {str(max_frec_cardiaca) + ' °C  ⚠':<21}│")
print(f"└{'─' * ancho}┘")