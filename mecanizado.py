import math

def calcular_velocidad_de_corte(diametro, velocidad_de_rotacion):
    return(math.pi*diametro*velocidad_de_rotacion)/1000

def calcular_avance_por_diente(avance_total,cantidad_de_dientes):
    return avance_total/cantidad_de_dientes


#definir propiedades de corte para diferentes materiales
propiedades_de_corte={"acero":{"coeficiente_potencia":0.1,"factor_material":5},
                      "aluminio":{"coeficiente_potencia":0.08,"factor_material":2}}

#funcion lambda
calcular_potencia_de_corte= lambda coeficiente,velocidad,avance,factor:( coeficiente*velocidad*avance)+factor
                      
#entrada dinamica de datos 
try:
    diametro= float (input("ingrese el diametro de la fresa(mm):"))
    velocidad_rotacion=float(input("ingrese la velocidad de rotacion de la fresa (rpm):"))
    avance_total=float(input("ingresamos el avance total(mm):"))
    cantidad_de_dientes=(input("ingresa la cantidad de dientes de la fresa"))
    tipo_material=input("ingrese el tipo de material")

    velocidad_de_corte=calcular_velocidad_de_corte(diametro,velocidad_rotacion)
    avance_por_diente=calcular_avance_por_diente(avance_total,cantidad_de_dientes)

    #verificar material
    if tipo_material in propiedades_de_corte:
       propiedades=propiedades_de_corte[tipo_material]
       coeficiente_potencia=propiedades["coeficiente_potencia"]
       factor_material=propiedades["factor_material"]

       #funcion lambda
       potencia_de_corte=calcular_potencia_de_corte(coeficiente_potencia,velocidad_de_corte)

       print("\nresultados: ")
       print ()
       print()
       print()
    else:
       print(f"no se encontarron propiedades para ese material`{tipo_material}")
except