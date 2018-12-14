"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod,n1,n2):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo

    def agregar_apellido(self,n):
        ""
        ""
        self.apellido = n

    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_nota1(self,n):
        ""
        ""
        self.nota1 = int(n)

    def obtener_nota1(self):
        """
        """
        return self.nota1

    def agregar_nota2(self,n):
        ""
        ""
        self.nota2 = int(n)

    def obtener_nota2(self):
        """
        """
        return self.nota2

    #Sirver como un Override de java para sobreescribir la clase e imprimir los valores que estan expuestos
    def __str__(self):
        """
        """
        return "%s - %s - %d - %d- %d- %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo,self.nota1,self.nota2)


class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado

    def agregar_listado_personas(self, lista):

        self.listado_personas = lista

    def obtener_listado_personas(self):
       return self.listado_personas

    def obtener_promedio(self,tipo):
        suma = 0


        if tipo=="nota1":
            for d in self.obtener_listado_personas():
                suma = suma + d.obtener_nota1()
        if tipo=="nota2":
            for d in self.obtener_listado_personas():
                suma = suma + d.obtener_nota2()

        promedio = suma / len(self.listado_personas)
        return promedio

    def obtener_notas_menores(self, tipo):
        if tipo == "nota1":
            for d in self.obtener_listado_personas():
                if d.obtener_nota1() < 15:
                    menor = (d.obtener_nombre())

        if tipo == "nota2":
            for d in self.obtener_listado_personas():
                if d.obtener_nota2() < 15:
                    menor = (d.obtener_nombre())

        return menor

    def obtener_nombres(self, a1, a2):
        for d in self.obtener_listado_personas():
            if (d.obtener_nombre()[0]==a1 or a2) and d.obtener_nota1()<15:
                cadena = d.obtener_nombre();
                print(cadena)

            if (d.obtener_nombre()[0]==a1 or a2) and d.obtener_nota2()<15:
                cadena = d.obtener_nombre();
                print(cadena)


    def __str__(self):
        cadena=" "
        for n in self.listado_personas:
            cadena ="%s %s %s\n"%(cadena, n.obtener_nombre(),n.obtener_apellido())
        return cadena
