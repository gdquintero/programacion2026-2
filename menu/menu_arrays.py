import numpy as np
import os
import subprocess

def limpiar_pantalla():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])


