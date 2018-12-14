from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista] #Se encarga de seperar los elementos de la lista

# print(lista)

lista = lista[1:]  #Se encarga de tomar los valores en adelante del que se pone
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
lista_personas =[]
for d in lista:
    # print(d)
    p = Persona(d[1], d[2], d[3],d[0],d[4], d[5])
    print(p)
    lista_personas.append(p)

operacion = OperacionesPersona(lista_personas)


print(operacion.obtener_promedio("nota1"))
print(operacion.obtener_promedio("nota2"))