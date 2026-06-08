class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None

    def set_hijos(self, hijos):
        self.hijos = hijos
        for hijo in self.hijos:
            hijo.padre = self

    def get_hijos(self): return self.hijos
    def set_padre(self, padre): self.padre = padre
    def get_padre(self): return self.padre
    def get_datos(self): return self.datos