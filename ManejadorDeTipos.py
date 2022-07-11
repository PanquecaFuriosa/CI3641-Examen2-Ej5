import math

class ManejadorDeTipos:

    def __init__(self) -> None:
        self.tiposG = {}
    
    class Atomico:
        """Clase que implementa los tipos atómicos o primitivos.
        """
        def __init__(self, a, b, c, ls) -> None:
            """Inicialización del atómico.

            Args:
                a (str): Nombre del atómico.
                b (int): Tamaño que ocupa el atómico.
                c (int): Alineación del atómico.
            """
            self.nombre = a
            self.representacion = b
            self.alineacion = c
            self.sinP = [int(b), int(c), 0] #Se calcula la info sin empaquetar
            self.emp = [int(b), int(c), 0] #Se calcula la info empaquetando
            self.ord = [int(b), int(c), 0] #Se calcula la info ordenando de manera óptima

    class Struct:
        """Clase que implememta los tipos struct.
        """
        def __init__(self, a, b, ls) -> None:
            """Inicialización del struct.

            Args:
                a (str): Nombre del struct.
                b (int): Lista de tipos de los campos del struct.
            """
            self.nombre = a
            self.tipos = b
            self.tiposG = ls
            self.sinP = self.sin_empaquetar(b) #Se calcula la info sin empaquetar
            self.emp = self.empaquetar() #Se calcula la info empaquetando
            self.ord = self.ordenado() #Se calcula la info ordenando de manera óptima
        
        def sin_empaquetar(self, lstipos) -> list:
            """Función que determina el tamaño que ocupa el struct sin empaquetar,
            así como la alineación y el espacio desperdiciado.

            Args:
                lstipos (list): Lista de tipos de los campos del struct.

            Returns:
                list: Contiene la información -> tamaño total, alineación, espacio desperdiciado.
            """
            al = self.tiposG.get(lstipos[0]).sinP[1]
            ocup = 0
            desp = 0
            for i in lstipos:
                tipo = self.tiposG.get(i)
                e = False
                while not(e):
                    if ocup%(tipo.sinP[1]) == 0: #Se verifica la alineación
                        ocup += tipo.sinP[0]
                        e = True
                    else: #Si no se consigue la alineación adecuada, se sigue buscando, pero se cuenta el espacio desperdiciado
                        ocup += 1
                        desp += 1
            return [ocup, al, desp]

        def empaquetar(self) -> list:
            """Función que determina el tamaño que ocupa el struct si se empaqueta,
            así como la alineación y el espacio desperdiciado.

            Returns:
                list: Contiene la información -> tamaño total, alineación, espacio desperdiciado.
            """
            al = self.tiposG.get(self.tipos[0]).emp[1]
            ocup = 0
            for i in self.tipos:
                tipo = self.tiposG.get(i)
                ocup += tipo.emp[0]
            return [ocup, al, 0]
        
        def sin_empaquetar2(self, lstipos) -> list:
            """Función que determina el tamaño que ocupa el struct sin empaquetar,
            pero tomando los tipos de manera ordenada
            así como la alineación y el espacio desperdiciado.

            Args:
                lstipos (list): Lista de tipos de los campos del struct.

            Returns:
                list: Contiene la información -> tamaño total, alineación, espacio desperdiciado.
            """
            al = self.tiposG.get(lstipos[0]).ord[1]
            ocup = 0
            desp = 0
            for i in lstipos:
                tipo = self.tiposG.get(i)
                e = False
                while not(e):
                    if ocup%(tipo.ord[1]) == 0: #Se verifica la alineación
                        ocup += tipo.ord[0]
                        e = True
                    else: #Si no se consigue la alineación adecuada, se sigue buscando, pero se cuenta el espacio desperdiciado
                        ocup += 1
                        desp += 1
            return [ocup, al, desp]

        def ordenado(self) -> list:
            """Función que determina el tamaño que ocupa el struct si reordenan los campos,
            así como la alineación y el espacio desperdiciado.

            Returns:
                list: Contiene la información -> tamaño total, alineación, espacio desperdiciado.
            """
            if len(self.tipos) < 8: #Solo hasta 10 tipos ya que puede volverse muy ineficiente
                minimo = [math.inf, 0, 0]
                for m in misterio(self.tipos): #Se usa el iterador para determinar los posibles órdenes
                    actual = self.sin_empaquetar2(m) #Se calcula el espacio sin empaquetar con el orden obtenido
                    if minimo[0] > actual[0]: #Se verifica si se ocupa menos espacio
                        minimo = actual
                return minimo

            t = sorted(self.tipos, key = lambda tipo : self.tiposG.get(tipo).ord[1], reverse = True) #Si se tienen más de 20 tipos, se toma el orden dependiente de la alineación
            return self.sin_empaquetar2(t)

    class Union: 
        """ Clase que implementa las uniones.
        """
        def __init__(self, a, b, ls) -> None:
            """Inicialización de las uniones.

            Args:
                a (str): Nombre de la unión.
                b (list): Lista de los tipos de los campos de la unión.
            """
            self.nombre = a
            self.tipos = b
            self.tiposG = ls
            self.sinP = self.sin_empaquetar() #Se calcula la info sin empaquetar
            self.emp = self.empaquetar() #Se calcula la info empaquetando
            self.ord = self.ordenado() #Se calcula la info ordenando de manera óptima
        
        def sin_empaquetar(self):
            """Función que determina el tamaño que ocupa la unión sin empaquetar,
            así como la alineación y el espacio desperdiciado.

            Returns:
                list: Contiene la información -> tamaño total, alineación, espacio desperdiciado.
            """
            al = 1
            ocup = 0
            desp = math.inf
            for i in self.tipos:
                tipo = self.tiposG.get(i)
                al = mcm(al, tipo.sinP[1]) #Se determina que la alineación coincida con todas las alineaciones de los tipos
                ocup = max(ocup, tipo.sinP[0]) #Se determina el espacion máximo
                desp = min(desp, tipo.sinP[2]) 
            return [ocup, al, desp]

        def empaquetar(self) -> list:
            """Función que determina el tamaño que ocupa la unión empaquetada,
            así como la alineación y el espacio desperdiciado.

            Returns:
                list: Contiene la información -> tamaño total, alineación, espacio desperdiciado.
            """
            al = 1
            ocup = 0
            desp = math.inf
            for i in self.tipos:
                tipo = self.tiposG.get(i)
                al = mcm(al, tipo.emp[1]) #Se determina que la alineación coincida con todas las alineaciones de los tipos
                ocup = max(ocup, tipo.emp[0]) #Se determina el espacion máximo
                desp = min(desp, tipo.emp[2])
            return [ocup, al, desp]

        def ordenado(self) -> list:
            """Función que determina el tamaño que ocupa la unión con ordenación óptima,
            así como la alineación y el espacio desperdiciado.

            Returns:
                list: Contiene la información -> tamaño total, alineación, espacio desperdiciado.
            """
            al = 1
            ocup = 0
            desp = math.inf
            for i in self.tipos:
                tipo = self.tiposG.get(i)
                al = mcm(al, tipo.ord[1]) #Se determina que la alineación coincida con todas las alineaciones de los tipos
                ocup = max(ocup, tipo.ord[0]) #Se determina el espacion máximo
                desp = min(desp, tipo.ord[2])
            return [ocup, al, desp]
    # Variable global, contiene a todos los tipos que se han definido
    def def_atom(self, atomico) -> bool:
        """Función que define un nuevo tipo atómico.

        Args:
            atomico (list): Lista con los datos del atómico a definir.
        """
        if self.tiposG.get(atomico[0]) != None: #Verificamos que no exista un tipo con el nombre especificado.
            print("Error, el nombre especificado ya tiene un tipo asociado.")
            return False
        self.tiposG.update({atomico[0] : self.Atomico(*atomico, self.tiposG)})
        print("Definicón exitosa.\n")
        return True

    def def_stc(self, struct) -> bool:
        """Función que define un nuevo tipo struct.

        Args:
            atomico (list): Lista con los datos del struct a definir.
        """
        if self.tiposG.get(struct[0]) != None: #Verificamos que no exista un tipo con el nombre especificado.
            print("Error, el nombre especificado ya tiene un tipo asociado.")
            return False

        for i in struct[1:]:
            if self.tiposG.get(i) == None:
                print("Error, el tipo "+i+" no está definido.")
                return False

        self.tiposG.update({struct[0]: self.Struct(struct[0], struct[1:], self.tiposG)})
        print("Definicón exitosa.\n")
        return True
                    
    def def_uni(self, union) -> bool:
        """Función que define un nuevo tipo unión.

        Args:
            atomico (list): Lista con los datos de la unión a definir.
        """
        if self.tiposG.get(union[0]) != None: #Verificamos que no exista un tipo con el nombre especificado.
            print("Error, el nombre especificado ya tiene un tipo asociado.")
            return False
        for i in union[1:]:
            if self.tiposG.get(i) == None:
                print("Error, el tipo "+i+" no está definido.")
                return False

        self.tiposG.update({union[0]: self.Union(union[0], union[1:], self.tiposG)})
        print("Definicón exitosa.")
        return True

    def describir(self, tipo) -> list:
        """Función que imprime la información de un tipo especificado.

        Args:
            tipo (str): Nombre del tipo a describir.
        """
        t = self.tiposG.get(tipo)
        if t == None: #Verificamos que el tipo ya esté definido
            print("Error, el nombre especificado no tiene un tipo asociado.")
            return [None, None, None]
        print("El tipo asociado al nombre especificado tiene la siguiente información:\n-----------------------------------------------------------------------")
        print("Sin empaquetar:\nTamaño total del tipo: ",t.sinP[0],"bytes.\nAlineación del tipo: ",t.sinP[1],"bytes.\nEspacio total desperdiciado: ",t.sinP[2],"bytes.")
        print("-----------------------------------------------------------------------")
        print("Empaquetado:\nTamaño total del tipo: ",t.emp[0],"bytes.\nAlineación del tipo: ",t.emp[1],"bytes.\nEspacio total desperdiciado: ",t.emp[2],"bytes.")
        print("-----------------------------------------------------------------------")
        print("Ordenado de manera óptima:\nTamaño total del tipo: ",t.ord[0],"bytes.\nAlineación del tipo: ",t.ord[1],"bytes.\nEspacio total desperdiciado: ",t.ord[2],"bytes.")
        return [t.sinP,t.emp,t.ord]

def ins(e, ls):
    """Función que determina todas las maneras de insertar un elemento en una lista

    Args:
        e (any): Elemento cualquiera a ser insertado.
        ls (list): Lista a la cual se le insertará e.

    Yields:
        lis: Lista con el elemento insertado en alguna posición.
    """
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def misterio(ls):
    """Función que determina las posibles permutaciones de los elementos
    de un arreglo.

    Args:
        ls (list): Lista a determinar las posibles permutaciones.

    Yields:
        list: Lista con una permutación.
    """
    if ls:
        for m in misterio(ls[1:]):
            for i in ins(ls[0], m):
                yield i
    else:
        yield []

def mcm(a, b) -> int:
    """Función que determina el mcm entre dos números.

    Args:
        a (int): Uno de los números.
        b (int): El otro de los números.

    Returns:
        int: mcm de a y b.
    """
    c = max(a, b)
    d = min(a, b)
    mcd = 0
    while d:
        mcd = d
        d = c%d
        c = mcd
    return (a*b)//mcd
        
# main xd
def main():
    print("Bienvenido al simulador de manejador de tipo de datos.")
    manejador = ManejadorDeTipos()
    while True:
        print("Por favor, elija una opción: 'ATOMICO' 'STRUCT' 'UNION' 'SALIR'.")
        opcion = input()
        opcion = opcion.split()
        if opcion[0] == "ATOMICO":
            manejador.def_atom(opcion[1:])
        elif opcion[0] == "STRUCT":
            manejador.def_stc(opcion[1:])
        elif opcion[0] == "UNION":
            manejador.def_uni(opcion[1:])
        elif opcion[0] == "DESCRIBIR":
            manejador.describir(opcion[1])
        elif opcion[0] == "SALIR":
            break
        else:
            print("Error, la opción especificada no es válida.")        

if __name__ == '__main__':
    main()