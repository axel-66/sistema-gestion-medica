class HistoriaClinica:

    def __init__(self, idHistoria, antecedentes, observaciones):
        self.__idHistoria = idHistoria
        self.__antecedentes = antecedentes
        self.__observaciones = observaciones

    def registrarAnotacion(self, anotacion):
        if not anotacion.strip():
            raise ValueError("La anotación no puede estar vacía.")

        if self.__observaciones:
            self.__observaciones += "\n" + anotacion
        else:
            self.__observaciones = anotacion

        return "Anotación registrada correctamente."

    def consultarHistorial(self):
        return {
            "antecedentes": self.__antecedentes,
            "observaciones": self.__observaciones
        }

    @property
    def idHistoria(self):
        return self.__idHistoria

    @property
    def antecedentes(self):
        return self.__antecedentes

    @property
    def observaciones(self):
        return self.__observaciones