# Determine Sex by Name

This function allows you to determine a person's sex using a combined technique:

1) Searching for names in a list of 6288 male and 5901 female names, for a total of 12209 names, and calculating the percentage of certainty that the name belongs to one sex or the other according to rules. Each list of names was compiled from multiple real-world databases where the sex was known in advance and then supplemented with dictionaries of male and female names obtained from the web (PDFs) and then text-mined. This is the most accurate method (not based on probability).

2) Determining the probability of sex for unrecognized names whose final syllables have specific endings. You can use this method optionally.

The result:

	{'sex': 'female', 'probability': 75.0}


If you find it useful, leave me a star ⭐


# Determinar el sexo mediante el nombre

Esta función permite determinar el sexo de una persona mediante una técnica combinada:

1) Buscando los nombres en una lista de 6288 nombres masculinos y 5901 femeninos para un total de 12209 nombres y calculando el porcentaje de seguridad de que pertenezca a uno u otro sexo según reglas. Cada lista de nombres se conformó a partir de múltiples bases de datos reales en las que se conocía el sexo de antemano y posteriormente se complementaron con diccionarios de nombres de hombres y mujeres obtenidos de la web (PDFs) a los que se aplicó minería de texto. Este es el método más preciso (no basado en probabilidad).
 
2) Determinando la probabilidad del sexo para los nombres no reconocidos y cuyas sílabas finales tienen terminaciones específicas. Este método puedes utilizarlo de manera opcional.


El resultado:
		
	{'sexo': 'femenino', 'probabilidad': 75.0}

Si te resulta de utilidad déjame una estrella ⭐
