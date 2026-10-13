from dragonpy import DragonPy

dpy = DragonPy()


data = dpy.dashboard.get_delayed_bars("AC")

print(data)
