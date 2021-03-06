# pip install infi.systray

import shutil

teclado1 = 'tecladochico.ini'
teclado2 = 'tecladogrande.ini'
teclado = r'..\RemapKeys.ini'

from infi.systray import SysTrayIcon
hover_text = "Remapkey.ini changer"

def tecladochico(sysTrayIcon):
    shutil.copyfile(teclado1, teclado)
def bye(sysTrayIcon):
    print ('Chau.')
def tecladogrande(sysTrayIcon):
    shutil.copyfile(teclado2, teclado)
menu_options = (('Skyloong SK64', None, tecladochico),
                ('Ozone Strike Battle', None, tecladogrande),
               )
sysTrayIcon = SysTrayIcon("teclado.ico", hover_text, menu_options, on_quit=bye, default_menu_index=1)
sysTrayIcon.start()
