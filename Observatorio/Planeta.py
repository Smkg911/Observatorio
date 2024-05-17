from Satelite import Satelite
class Planeta:
    def __init__(self, pNombre, pDistanciaMediaSol, pExcentricidad, pPeriodoOrbitalSinodico, pVelocidadOrbitalMedia, pInclinacion):
        self.nombre = pNombre
        self.distanciaMediaSol = pDistanciaMediaSol
        self.excentricidad = pExcentricidad
        self.periodoOrbitalSinodico = pPeriodoOrbitalSinodico
        self.velocidadOrbitalMedia = pVelocidadOrbitalMedia
        self.inclinacion = pInclinacion
        self.satelites = []

    def obtenerNombre(self):
        return self.nombre

    def obtenerDistancia(self):
        return self.distanciaMediaSol

    def obtenerInclinacion(self):
        return self.inclinacion

    def agregarSatelite(self, pNombreSatelite, pExcentricidad, pInclinacion):
        for satelite in self.satelites:
            if satelite.darNombre() == pNombreSatelite:
                return False
        satelite = Satelite(pNombreSatelite, pExcentricidad, pInclinacion)
        self.satelites.append(satelite)
        return True

    def obtenerSatelites(self):
        return self.satelites

    def eliminarSatelite(self, pNombreSatelite):
        for i in range(len(self.satelites)):
            if self.satelites[i].darNombre() == pNombreSatelite:
                del self.satelites[i]
                return

    def obtenerSatelite(self, pNombreSatelite):
        for satelite in self.satelites:
            if satelite.darNombre() == pNombreSatelite:
                return satelite
        return None

    def editarSatelite(self, pNombreSatelite, pExcentricidad, pInclinacion):
        for satelite in self.satelites:
            if satelite.darNombre() == pNombreSatelite:
                satelite.cambiarExcentricidad(pExcentricidad)
                satelite.cambiarInclinacionOrbital(pInclinacion)
