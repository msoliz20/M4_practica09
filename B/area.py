areas = ["cuina", 7.88, "menjador2", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]
#imprimi el segon element
print (areas [1])
#Imprimir l'últim element
print (areas [-1])
#Imprimir l'àrea de la terrassa
print (areas [5])
#Imprimir del primer element al tercer element
print (areas [:3])
#Imprimir del tencer element a 1'Outin
print (areas [2:])
#Imprimir el total de l'área de les dues. habitacions
print (areas [9]+areas [11])
#Modificar l'àrea del lavabo 1 imprimir la nova list area
areas[7]=9
print (areas)
#Afegin Warea de "pati interior" 1 2.78 a les últimes posicions. Imprimir
areas.extend (["pati interior", 2.78])
print (areas)
