from calculadora import Calculadora

def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

def test_multi():
    calc = Calculadora()
    assert calc.multi(2, 3) == 9