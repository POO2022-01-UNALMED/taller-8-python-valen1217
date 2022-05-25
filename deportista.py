class Deportista:

    def __init__(self, deporte, años_practicando):
        self._deporte = deporte
        self._años_practicando = años_practicando

    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._años_practicando
