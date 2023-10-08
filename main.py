import numpy as np
import time
from variables import *
from functions import *

def jugar(tablero_player, barcos, tablero_cpu,
          disparos_player_realizados, disparos_cpu_realizados,
          tablero_player_disparos, tablero_cpu_disparos,
          cantidad_total_de_barcos):
    '''
    Función jugar en la que se desarrollan los turnos del juego, se colocan los barcos y
    se dispara.

    El juego acaba cuando un jugador pierde todos los barcos es decir la cantidad de "X" en su tablero es 20.

    Tiene como argumentos:

        tablero_player: Tablero de jugador_1
        tablero_cpu: Tablero de la CPU
        barcos: Diccionario con los barcos, sus esloras y la cantidad de cada tipo de barco
        disparos_player_realizados y disparos_cpu_realizados: 
            un set en el que se guardan las tuplas con las coordenadas de los disparos realizados
        tablero_player_disparos y tablero_cpu_disparos: Tableros en los que se visualizan los disparos de los jugadores
        cantidad_total_de_barcos: Son las 20 casillas que suman todos los barcos para finalizar el juego cuando sean todos "X"

    '''
    
    # Colocar los barcos en los tablero del jugador y de la CPU
    tablero_player = colocar_barcos_en_tablero(tablero_player, barcos)
    tablero_cpu = colocar_barcos_en_tablero(tablero_cpu, barcos)

    # Variable para saber si el jugador o la cpu tienen un turno extra
    turno_extra_jugador = False
    turno_extra_cpu = False

    # Implementar los turnos del juego
    while True:
        time.sleep(3)
        # Comienza siempre el jugador
        if turno_extra_cpu == False:
            turno_extra_jugador = False
            print("\n")
            print("-------------------------------")
            print("Tu turno:")
            print("\n")
            fila = int(input("Ingrese la fila a disparar (0-9): "))
            columna = int(input("Ingrese la columna a disparar (0-9): "))
            # Comprobar que la fila y la columna son validas
            if 0 <= fila < 10 and 0 <= columna <10:
                casilla = (fila, columna)

                if casilla not in disparos_player_realizados:
                    disparos_player_realizados.add(casilla)
                    resultado_disparo = disparar(tablero_cpu, casilla)

                    if resultado_disparo == "Tocado":
                        #Actualizar el tablero de disparos del jugador con el resultado
                        tablero_player_disparos[fila, columna] = "X"
                        turno_extra_jugador = True
                        print("¡Has acertado! Tienes otro turno.")
                    if resultado_disparo != "Tocado":
                        tablero_player_disparos[fila, columna] = "A"

        else:
            print("Las coordinadas no son válidas. Por favor, ingrese otras de nuevo.")

        # Mostras los tableros después del disparo del jugador
        print("Tablero del jugador:")
        print("\n")
        print(tablero_player)

        print("Tablero de disparos del jugador:")
        print("\n")
        print(tablero_player_disparos)

        print("Disparos del jugador realizados")
        print("\n")
        print(disparos_player_realizados)

        # Verificar si el jugador ha ganado o perdido y terminar el juego si fuera el caso
        if np.count_nonzero(tablero_cpu == "X") == cantidad_total_de_barcos:
            print("El jugador ha ganado")
            break
        time.sleep(3)

        # Turno de la CPU
        if turno_extra_jugador == False:
            turno_extra_cpu = False
            print("\n")
            print("-------------------------------")
            print("Turno de la CPU:")
            print("\n")
            casilla_cpu = comprobar_disparo_cpu(disparos_cpu_realizados)
            resultado_disparo_cpu = disparar(tablero_player, casilla_cpu)

            # Actualizar el tablero de disparos de la CPU con el resultado
            fila_cpu, columna_cpu = casilla_cpu
            tablero_cpu_disparos[fila_cpu, columna_cpu] = resultado_disparo_cpu
            if resultado_disparo_cpu != "Tocado":
                tablero_cpu_disparos[fila, columna] = "A"
            else:
                tablero_cpu_disparos[fila, columna] = "X"

            # Mostrar los tableros después del disparo de la CPU
            print("Tablero de la CPU:")
            print("\n")
            print(tablero_cpu)
            time.sleep(3)

            print("Tablero de disparos de la CPU:")
            print("\n")
            print(tablero_cpu_disparos)
            time.sleep(3)

            print("Disparos de la CPU realizados")
            print("\n")
            print(disparos_cpu_realizados)
            time.sleep(3)

            if np.count_nonzero(tablero_player == "X") == cantidad_total_de_barcos:
                print("La CPU ha ganado")
                break

            # Verificar si la CPU acertó y debe tener otro turno
            if resultado_disparo_cpu == "Tocado":
                turno_extra_cpu = True
            time.sleep(3)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar(tablero_player, barcos, tablero_cpu,
                  disparos_player_realizados, disparos_cpu_realizados,
                  tablero_player_disparos, tablero_cpu_disparos,
                  cantidad_total_de_barcos)
        elif opcion == "2":
            print("¡Gracias por jugar! Hasta otro día")
            break
        else:
            print("Opción no valida. Por favor, selecione una opcción válida.")


main()