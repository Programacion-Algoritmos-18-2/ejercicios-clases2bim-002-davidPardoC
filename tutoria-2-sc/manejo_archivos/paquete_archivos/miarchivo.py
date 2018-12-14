import codecs
import sys


class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo_notas.csv", "r")#MAnda a abrir el archivp

    def obtener_informacion(self):
        return self.archivo.readlines()#Retorna los datos contenidos en el csv En el demo

    def cerrar_archivo(self):
        self.archivo.close()#Cierra el archivo


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo))

    def cerrar_archivo(self):
        self.archivo.close()
