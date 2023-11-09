import pytest
from src.ej2_32b import mostrarImpares, comprobarNum

def test_comprobarNum_ValueError():
    with pytest.raises(ValueError):
        comprobarNum(-6)


@pytest.mark.parametrize(
    "num, expected",
    [
        (13, '1,3,5,7,9,11,13.'),
        (12, '1,3,5,7,9,11.'),
        (5, '1,3,5.')
        
    ]
)
def test_mostrarImpares_params(num, expected):
    assert mostrarImpares(num) == expected

