import Lab2


def test_find_min_max():
    result = Lab2.find_min_max([5.0, 67.0, 32.0])
    assert (result == [5.0, 67.0])


def test_calc_average():
    result = Lab2.calc_average([5.0, 67.0, 32.0])
    assert (abs(result - 34.666666) < 0.001)


def test_calc_median_odd():
    result = Lab2.calc_median_temperature([5.0, 67.0, 32.0])
    assert (result == 32.0)


def test_calc_median_even():
    result = Lab2.calc_median_temperature([10.0, 40.0, 20.0, 30.0])
    assert (result == 25.0)