import main as an

def test_hello_world():
    assert an.hello_world() is True

def test_get_minimum_1():
    resultado = an.get_minium([3, 1, 3])
    assert resultado == 1

def assert_almost_equal(resultado2, param, tolerance=1e-7):
    assert abs(resultado2 - param) < tolerance

def test_get_minimum_2():
    resultado2 = an.get_minium([3, 0, -9, 8, 6])
    assert_almost_equal(resultado2, -9)

def test_get_max1():
    resultado1 = an.get_max([3, 0, -1, 8, 6])
    assert resultado1 == 8

def test_get_max2():
    resultado2 = an.get_max([6, 0, 12, 8, 1])
    assert resultado2 == 12

def test_fibonacci():
    fibonacci = an.get_fibonacci(5)
    assert fibonacci == [0, 1, 1, 2, 3]

def test_common_lists():
    comun = an.comun_lists([6, 0, 12, 8, 1], [1, 3, 6, 24, 12, 8])
    assert comun == [6, 8, 12]

def test_goldbach():
    gold = an.goldbach(28)
    assert gold == "5 + 23"

def test_maxarea():
    area = an.maxarea([10, 8, 6, 5, 4, 3, 2, 1])
    assert area == 16
