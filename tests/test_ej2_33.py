import pytest

from src.ej2_33 import comprobarNum, cuentaAtras

def test_comprobarNum_ValueError():
    with pytest.raises(ValueError):
        comprobarNum('u')


@pytest.mark.parametrize(
    "num, expected",
    [
        (5, '5,4,3,2,1.'),
        (3, '3,2,1.'),
        (10, '10,9,8,7,6,5,4,3,2,1.')
        
    ]
)
def test_cuentaAtras_params(num, expected):
    assert cuentaAtras(num) == expected