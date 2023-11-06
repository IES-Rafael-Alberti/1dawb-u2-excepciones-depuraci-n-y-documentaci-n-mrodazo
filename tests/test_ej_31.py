import pytest
from src.ej2_31b import mostrarYears

def test_mostrarYears_ValueError():
    with pytest.raises(ValueError):
        mostrarYears(-6)