from persona import Persona
from deportista import Deportista


class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, años_practicando, goles_marcados, tarjetas_rojas, pierna_habil):
        self._goles_marcados = goles_marcados
        self._tarjetas_rojas = tarjetas_rojas
        self._pierna_habil = pierna_habil
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", años_practicando)
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._goles_marcados

    def getTarjetasRojas(self):
        return self._tarjetas_rojas

    def getPiernaHabil(self):
        return self._pierna_habil

    def __str__(self):
        return f'Mi nombre es {Persona.getNombre(self)} soy profesional en el deporte {Deportista.getDeporte(self)} Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte'
