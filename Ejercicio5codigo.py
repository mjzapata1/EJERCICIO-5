#Importamos el método date de la librería datetime, para usarlo a la hora de inscribir la hora del usuario.
from datetime import date

#Creamos una función para que se implemente la hora mediante el datetime
def validarFecha():
  while True:
    try:
      dia = int(input("\nIngrese el día (en números) en que se realizó la prueba: "))
      mes = int(input("\nIngrese el mes (en números) en que se realizó la prueba: "))
      año = int(input("\nIngrese el año (en números) en que se realizó la prueba: "))
      fechaDate = date(año,mes,dia)
      fechaVal = fechaDate.strftime("%Y/%m/%d")
      return fechaVal
    except ValueError:
      print("\nLos valores que ha ingresado en la fecha no son válidos.\n\nPor favor intente nuevamente...")

#Definiremos primero la clase índices, pues esta estará incluisa en un clase posterior que será la clase visita
class Indices:
    def __init__(self):
        self.__pdel = 0
        self.__ptetha = 0
        self.__palf1 = 0
        self.__palf2 = 0
        self.__pbeta = 0
        self.__pgamma = 0
    
    def verPdel(self):
       return self.__pdel
    
    def asignarPdel(self,p):
       self.__pdel = p

    def verPtetha(self):
       return self.__ptetha
    
    def asignarPtetha(self,p):
       self.__ptetha = p

    def verPa1(self):
       return self.__palf1
    
    def asignarPa1(self,p):
       self.__palf1 = p
      
    
#Definiremos luego la clase Visitas, que posteriormente hará parte de la clase Paciente
class Visita:
    def __init__(self):
      self.__fecha = ""
      self.__registro = ""
      self.__notas = ""

    def verFecha(self):
      return self.__fecha
    
    def asignarFecha(self,fecha):
        self.__fecha = fecha

    def verRegistro(self):
       return self.__registro
    
    def asignarRegistro(self,reg):
       self.__registro = reg

    def verNotas(self):
       return self.__notas
    
    def asignarNotas(self,nota):
       self.__notas = nota

#Definiremos la clase principal que es la clase Paciente
class Paciente:
   def __init__(self):
      self.__
   
