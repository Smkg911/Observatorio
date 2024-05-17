from Planeta import Planeta

class Observatorio:
    # Constantes
    CANTIDAD_PLANETAS = 8
    NOMBRE_MERCURIO = "Mercurio"
    NOMBRE_VENUS = "Venus"
    NOMBRE_TIERRA = "Tierra"
    NOMBRE_MARTE = "Marte"
    NOMBRE_JUPITER = "Júpiter"
    NOMBRE_SATURNO = "Saturno"
    NOMBRE_URANO = "Urano"
    NOMBRE_NEPTUNO = "Neptuno"

    def __init__(self):
        self.planetas = []*self.CANTIDAD_PLANETAS
        self.planetas[0] = Planeta(self.NOMBRE_MERCURIO, 0.466, 0.205, 115.88, 478.725, 7.004)
        self.planetas[1] = Planeta(self.NOMBRE_VENUS, 0.728, 0.006, 583.92, 35.021, 339.471)
        self.planetas[2] = Planeta(self.NOMBRE_TIERRA, 1.016, 0.0167, 365.25, 30.28, 23.45)
        self.planetas[3] = Planeta(self.NOMBRE_MARTE, 1.665, 0.09341233, 779.95, 24.13, 1.850)
        self.planetas[4] = Planeta(self.NOMBRE_JUPITER, 5.458, 0.09341233, 398.9, 13.069, 1.305)
        self.planetas[5] = Planeta(self.NOMBRE_SATURNO, 10.115, 0.0541506, 378.1, 9.67, 2.484)
        self.planetas[6] = Planeta(self.NOMBRE_URANO, 20.096, 0.04716771, 369.7, 6.835, 0.769)
        self.planetas[7] = Planeta(self.NOMBRE_NEPTUNO, 30.327, 0.00858587, 367.5, 5.47, 1.769)

    def darNombresPlanetas(self):
        nombres = []*self.CANTIDAD_PLANETAS
        for i in range(len(self.planetas)):
            nombres[i] = self.planetas[i].obtenerNombre()
        return nombres

    def darSateliteNatural(self, pNombrePlaneta, pNombreSatelite):
        satelite = None
        for planeta in self.planetas:
            if planeta.obtenerNombre() == pNombrePlaneta:
                satelite = planeta.obtenerSateliteNatural(pNombreSatelite)
        return satelite

    def darSatelitesNaturales(self, pNombrePlaneta):
        satelites = []
        encontrado = False
        for i in range(len(self.planetas)):
            if not encontrado and self.planetas[i].obtenerNombre() == pNombrePlaneta:
                satelites = self.planetas[i].obtenerSatelitesNaturales()
                encontrado = True
        return satelites

    def darPlanetasPorDistancia(self, pDistancia):
        listaPlanetas = []
        for planeta in self.planetas:
            if planeta.obtenerDistancia() <= pDistancia:
                listaPlanetas.append(planeta.obtenerNombre())
        return listaPlanetas

    def darPlanetasPorInclinacion(self, pNombre):
        listaPlanetas = []
        for i in range(len(self.planetas)):
            planeta = self.planetas[i]
            if planeta.obtenerNombre() == pNombre:
                inclinacion = planeta.obtenerInclinacion()
                for j in range(len(self.planetas)):
                    if self.planetas[j].obtenerInclinacion() < inclinacion:
                        listaPlanetas.append(self.planetas[j].obtenerNombre())
        return listaPlanetas

    def agregarSateliteNatural(self, pNombrePlaneta, pNombreSatelite, pExcentricidad, pInclinacion):
        agregado = False
        for i in range(len(self.planetas)):
            if not agregado and pNombrePlaneta == self.planetas[i].obtenerNombre():
                agregado = self.planetas[i].agregarSateliteNatural(pNombreSatelite, pExcentricidad, pInclinacion)
        return agregado

    def eliminarSatelite(self, pNombrePlaneta, pNombreSatelite):
        encontrado = False
        for i in range(len(self.planetas)):
            if not encontrado:
                planeta = self.planetas[i]
                if planeta.obtenerNombre() == pNombrePlaneta:
                    planeta.eliminarSateliteNatural(pNombreSatelite)
                    encontrado = True

    def editarSateliteNatural(self, pNombrePlaneta, pNombre, pExcentricidad, pInclinacion):
        for i in range(len(self.planetas)):
            if self.planetas[i].obtenerNombre() == pNombrePlaneta:
                self.planetas[i].editarSateliteNatural(pNombre, pExcentricidad, pInclinacion)

    # Puntos de Extensión
    def metodo1(self):
        return "Respuesta 1"

    def metodo2(self):
        return "Respuesta 2"
