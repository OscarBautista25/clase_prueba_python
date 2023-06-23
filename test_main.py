from main import sum, es_mayor_que, login

def test_sum():
    assert sum(2,5) == 7
    print("La función suma1 trabaja correctamente")

def test_sum2():
    assert sum(4,6) == 10
    print("La función suma2 trabaja correctamente")

def test_es_mayor_que():
    assert es_mayor_que(10,2)
    print("La función es mayor que trabaja correctamente")
    
@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (3, 4, 7),
        (5, sum(5,6), 16),
        (sum(2,1), 5, 8),
    ]
)
def test_sum_params(input_x, input_y, esperado):
    assert sum(input_x, input_y) == esperado
    print("Las funciones parametrizadas trabajan correctamente")
    
def test_login_pass():
    login_passes = login("Metodologia", "710011C")
    assert login_passes
    
def test_login_fail():
    login_fails = login("Metodologias", "710012C")
    assert not login_fails
    
 

if __name__ == '__main__':
    test_sum()
    test_sum2()
    test_es_mayor_que()
 