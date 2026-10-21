from dragonpy import DragonPy


def test_has_http_client():
    dpy = DragonPy()
    assert hasattr(dpy, "_client")
    assert callable(dpy._client.get)
    assert callable(dpy._client.post)
