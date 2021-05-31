# pip install infi.systray

import shutil

teclado1 = r'C:\Program Files (x86)\Steam\steamapps\common\Worms Armageddon\RemapsFiles\tecladochico.ini'
teclado2 = r'C:\Program Files (x86)\Steam\steamapps\common\Worms Armageddon\RemapsFiles\tecladogrande.ini'
teclado = r'C:\Program Files (x86)\Steam\steamapps\common\Worms Armageddon\RemapKeys.ini'

from infi.systray import SysTrayIcon
hover_text = "Remapkey.ini changer"

def tecladochico(sysTrayIcon):
    shutil.copyfile(teclado1, teclado)
def simon(sysTrayIcon):
    print ("Hello Simon.")
def bye(sysTrayIcon):
    print ('Bye, then.')
def tecladogrande(sysTrayIcon):
    shutil.copyfile(teclado2, teclado)
menu_options = (('Skyloong SK64', "hello.ico", tecladochico),
                ('Ozone Strike Battle', None, tecladogrande),
               )
sysTrayIcon = SysTrayIcon("main.ico", hover_text, menu_options, on_quit=bye, default_menu_index=1)
sysTrayIcon.start()