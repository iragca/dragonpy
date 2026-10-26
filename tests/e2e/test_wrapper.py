from dragonpy import DragonPy


def test_wrapper():
    dpy = DragonPy()
    data = dpy.securities.get_stock_profile("ABS")

    assert isinstance(data, dict)
