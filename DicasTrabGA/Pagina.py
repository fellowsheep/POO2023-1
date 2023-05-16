from Figurinha import *

NRO_FIGS_POR_PAGINA = 5
TITULOS = [ 'TRIASSICO', 'JURASSICO', 'CRETACEO' ] #solucao temporaria

class Pagina:
    def __init__(self,nro):
        self.nro = nro
        self.titulo = TITULOS[nro]
        self.minNro = nro 
        self.maxNro = nro + NRO_FIGS_POR_PAGINA

    def getTitulo(self):
        return self.titulo