from variables import *
from functions import *


def main():
    while True:         
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar(tablero_player, tablero_cpu, barcos,                 
                disparos_player_realizados, disparos_cpu_realizados,
                tablero_player_disparos, tablero_cpu_disparos,
                cantidad_total_de_barcos)
        elif opcion == "2":
            print("¡Gracias por jugar! Hasta otro día")
            break
        else:
            print("Opción no valida. Por favor, selecione una opcción válida.")

main()