from Animal import animales
class Ave(animales):
    def __init__(self, nombre, peso, nacimiento, propietario):
        super().__init__(nombre, peso)
        self.nacimiento = nacimiento
        self.propietario = propietario
    
    def calcularedad(self):
        año_actual = 2024
        edad = año_actual-self.nacimiento
        if edad > 5:
            return("Es un adulto")
        else:
            return("Es un bebé")
        
ave1 = Ave("loro",1,2012,"Jesus")
print("el animal es un",ave1.Nombre, "pesa",ave1.Peso, "nacio el ",ave1.nacimiento,"y su dueño es " ,ave1.propietario, "y", ave1.calcularedad())
ave1.calcularedad()