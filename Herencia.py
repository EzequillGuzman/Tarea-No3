class Humano:
    def _init_(self,edad):
        self.edad = edad
    
    def hablar(self,mensaje):
        
        print (mensaje)
        
class IngSistemas(Humano):
    def _init_(self):
        print("Hola")
        
    def programar(self,lenguaje):
        print("Voy a programar", lenguaje)
        
class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print("Debo estudiar el caso de:", de)

pedro = IngSistemas(26)
raul = LicDerecho(27)

pedro.programar("Python")
raul.estudiarCaso("Pedro")



pedro.hablar("Hola")
raul.hablar("Hola, Pedro!")