class Paciemte:
    def _init_(self, rut:str, nombre:str, edad:int,prevencion:str ):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.prevencion = prevencion

    @property
    def rut(self) -> str:
        return self._rut

    @rut.setter
    def rut(self,rut:str):
        self._rut = rut 