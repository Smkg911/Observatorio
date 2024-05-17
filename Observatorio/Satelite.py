class Satelite:
    def __init__(self, pNombreSatelite, pExcentricidad, pInclinacion):
        self.nombre = pNombreSatelite
        self.excentricidad = pExcentricidad
        self.inclinacionOrbital = pInclinacion

    def darNombre(self):
        return self.nombre

    def darExcentricidad(self):
        return self.excentricidad

    def darInclinacion(self):
        return self.inclinacionOrbital

    def cambiarExcentricidad(self, pExcentricidad):
        self.excentricidad = pExcentricidad

    def cambiarInclinacionOrbital(self, pInclinacionOrbital):
        self.inclinacionOrbital = pInclinacionOrbital