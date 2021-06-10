import math_func
import pytest
import sys
import decorations
from math_func import Admin

@pytest.fixture(scope='module')
def AdminFixture():
    print("----------------------Setup----------------------")
    admin = Admin()
    admin.connect('admins.json')
    yield admin
    print("----------------------Teardown----------------------")
    admin.close()


# def teardown_module(module): # close connections
   # print("----------------------Teardown----------------------")
   # admin.close()

def test_maths():
    assert math_func.percentage(10, 20) == 50
    assert math_func.percentage(15, 20) == 75

def test_powerment():
    assert math_func.powerment(2, 4) == 16
    assert math_func.powerment(3, 3) == 27

def customDecor(func):
    print("Custom Decor")
    func()

@customDecor
def test_decor():
    assert math_func.add(1,1) == 2

def test_gen():
    assert math_func.gen(1,1,1) == 0


a = decorations.Square(2)
b = decorations.Square(4)
c = a + b

@pytest.mark.skipif(sys.version_info < (3, 8) ,reason=(str(sys.version_info) + " Version Error"))
@pytest.mark.parametrize("A, B, R",
                         [
                                ('A', 'B', 'AB'),
                                (423,245, (423+245)),
                                (a.getSide(), b.getSide(), c.getSide())
                         ]
                         )
def test_parameterize_attempt(A, B, R):
    assert math_func.add(A, B) == R

def test_add_strings():
    assert math_func.add("A", "B") == "AB"
    result = math_func.add("C", "D")
    assert type(result) is str
    assert result == "CD"
    assert "C" in result and "D" in result
    print("Logger: YAY!")


@pytest.mark.json
def test_nexorel_data(AdminFixture):
    necorel_data = AdminFixture.get_data('Nexorel')
    assert necorel_data['id'] == 1
    assert necorel_data['name'] == "Nexorel"
    assert necorel_data['type'] == "Organic"


@pytest.mark.json
def test_aegis_data(AdminFixture):
    aegis_data = AdminFixture.get_data('Aperture Employee Guardian and Intrusion System (AEGIS)')
    assert aegis_data['id'] == 2
    assert aegis_data['name'] == "Aperture Employee Guardian and Intrusion System (AEGIS)"
    assert aegis_data['type'] == "Mechanical"
