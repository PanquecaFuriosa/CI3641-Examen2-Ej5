
from ManejadorDeTipos import ManejadorDeTipos

def test():
    """Test para probar el manejador de tipos y almacenamiento.
    """
    manejador = ManejadorDeTipos()
    assert manejador.def_atom(["int", "4", "4"])
    assert manejador.describir("int") == [[4, 4, 0], [4, 4, 0], [4, 4, 0]]

    assert manejador.def_atom(["char", "1", "2"])
    assert manejador.describir("char") == [[1, 2, 0], [1, 2, 0], [1, 2, 0]]

    assert manejador.def_atom(["bool", "1", "2"])
    assert manejador.describir("bool") == [[1, 2, 0], [1, 2, 0], [1, 2, 0]]

    assert manejador.def_atom(["double", "8", "8"])
    assert manejador.describir("double") == [[8, 8, 0], [8, 8, 0], [8, 8, 0]]

    assert manejador.def_atom(["str", "4", "4"])
    assert manejador.describir("str") == [[4, 4, 0], [4, 4, 0], [4, 4, 0]]

    assert manejador.def_atom(["pair", "8", "8"])
    assert manejador.describir("pair") == [[8, 8, 0], [8, 8, 0], [8, 8, 0]]

    assert not(manejador.def_atom(["str", "4", "4"])) #Debe dar false ya que ya hay un tipo int

    assert manejador.def_stc(["meta", "int", "char", "double", "str", "pair", "double", "int", "bool"])
    assert manejador.describir("meta") == [[45, 4, 7], [38, 4, 0], [39, 8, 1]]

    assert manejador.def_stc(["holi", "pair", "str", "int", "str", "char", "double", "int"])
    assert manejador.describir("holi") == [[36, 8, 3],[33, 8, 0],[33, 8, 0]]

    assert manejador.def_stc(["wtf", "meta", "double", "double", "int", "bool"])
    assert manejador.describir("wtf") == [[69, 4, 3],[59, 4, 0],[61, 8, 1]]

    assert manejador.def_stc(["ola", "meta", "int", "bool", "holi", "bool", "wtf", "char", "int", "wtf", "meta", "holi"])
    assert manejador.describir("ola") == [[332, 4, 21],[271, 4, 0],[297, 8, 20]]

    assert not(manejador.def_stc(["ola", "meta", "int", "bool", "holi", "bool", "wtf", "char", "int", "wtf", "meta", "holi"])) #Ya hay un tipo ola
   
    assert manejador.def_uni(["lala", "ola", "meta", "holi", "wtf", "int", "bool"])
    assert manejador.describir("lala") == [[332, 8, 0],[271, 8, 0],[297, 8, 0]]

    assert manejador.def_uni(["f", "meta", "pair", "bool", "holi", "lala", "ola", "wtf"])
    assert manejador.describir("f") == [[332, 8, 0],[271, 8, 0],[297, 8, 0]]

