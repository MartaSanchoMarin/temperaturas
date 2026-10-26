from analisis import (calcularMedia)

temperaturas=[18.5, 21.2, 19.8, 23.1, 25.4]

media=calcularMedia(temperaturas)
maxima=max(temperaturas)
minima=min(temperaturas)

print(temperaturas)

print("La media de las temperaturas es de: ", media)
print("La máxima de las temperaturas es de: ", maxima)
print("La minima de las temperaturas es de: ", minima)

umbral_calor=30

if(maxima > umbral_calor):
    print("Aviso! Se ha superado el umbral de calor: ", umbral_calor)
else:
    print("Todo en orden")
    
contador=0
for t in temperaturas:
    if t > 20:
        contador+=1
print("Dias por encima de los 20º: ", contador)

for i in range(1, len(temperaturas)):
    diferencia = temperaturas[i]-temperaturas[i-1]
    if diferencia > 0:
        tendencia = "sube"
    elif diferencia < 0 :
        tendencia = "baja"
    else:
        tendencia = "igual"
        
    print(f"Dia {i}  ->  dia {i+1}: {tendencia} {round(diferencia,2)} grados")