import os.path
import cx_Freeze
executables=[cx_Freeze.Executable('snake.py')]

os.environ['TCL_LIBRARY'] = r'C:\Users\RedCode\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\RedCode\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

cx_Freeze.setup(
    name='Snake',
    version = "1.1",
    options={'build.exe':{'packages':['pygame'],'include_files':['apple_1.png','apple_icon.png','snakehead.png']}},
    description='Snake',
    executables=executables
    )
