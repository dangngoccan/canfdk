from generator import r_gen
from r_gui import r_gui

import os.path

megen = r_gen()
megen.path_current = os.path.dirname(__file__)
print(megen.path_current)
megen.gen()

myApp = r_gui()
myApp.r_MainApp()

