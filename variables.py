import numpy as np

barcos = {"barco_eslora_1": (1,4),
          "barco_eslora_2": (2,3),
          "barco_eslora_3": (3,2),
          "barco_eslora_4": (4,1)}

#Tableros jugador
tablero_player = np.full((10, 10), "_")             #aquí se posicionan los barcos
tablero_player_disparos = np.full((10,10), "_")      #aquí se muestran los disparos

#Tableros cpu
tablero_cpu = np.full((10,10), "_")
tablero_cpu_disparos = np.full((10, 10), "_")

# variables para llevar el registro de los disparos realizados
disparos_player_realizados = set()
disparos_cpu_realizados = set()


cantidad_total_de_barcos = 20