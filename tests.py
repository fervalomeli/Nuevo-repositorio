

import main as andef
    assert an.hello_world() is True


def test_get_minium_1():
    resultado = an. get_minium([3, 1, 3])
    assert resultado is 1


def assert_almost_equal(resultado2, param, param1):
    pass


def test_get_minium_2():
   resultado2 =mn.get_min([3,0,-9,8,6])
   assert_almost_equal(resultado2, -9, 1)

def test_get_max1():
    resultado1 =mn.get_max([3,0,-1,8,6])
    assert resultado1 == 8

def test_get_max2():
    resultado2 =mn.get_max([6,0,12,8,1])
    assert resultado2 == 12

def test_fibonacci():
    fibonacci =mn.get_fibonacci(5)
    assert fibonacci == [0, 1, 1, 2, 3]

def test_comun_list():
    comun =mn.comun_lists([6,0,12,8,1], [1,3,6,24,12,8])
    assert comun == [1,6,8,12]

def test_goldbach():
    gold =mn.goldbach(28)
    assert gold == "5 + 23"

def test_tanque():
    area =  mn.maxarea([10, 8, 6, 5, 4, 3, 2, 1])
    assert area == 16