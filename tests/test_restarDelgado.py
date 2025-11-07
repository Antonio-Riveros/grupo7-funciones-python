from funciones.restarDelgado import restarDelgado

def test_restarDelgado():
    assert restarDelgado(4, 3) == 1
    assert restarDelgado(3, 1) == 2
