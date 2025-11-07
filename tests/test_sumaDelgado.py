from funciones.sumaDelgado import sumaDelgado

def test_sumaDelgado():
    assert sumaDelgado(2, 3) == 5
    assert sumaDelgado(-1, 1) == 0
