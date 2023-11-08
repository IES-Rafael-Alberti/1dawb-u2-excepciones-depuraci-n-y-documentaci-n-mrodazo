import pytest
from src.ej2_31b import mostrarYears, comprobarNumero

def test_mostrarYears_ValueError():
    with pytest.raises(ValueError):
        mostrarYears(-6)


@pytest.mark.parametrize(
    "numero, expected",
    [
        ('100', True),
        ('hola', False),
        ('-5', True),
        ('0', True),
        ('298.56', False)
    ]
)
def test_comprobarNumero_params(numero, expected):
    assert comprobarNumero(numero) == expected