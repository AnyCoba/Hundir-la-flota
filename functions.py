import numpy as np
import random
from variables import *
import time

# Funciones para colocar los barcos

def colocar_barco(barco, tablero):                              
    '''
    Función para colocar los barcos, que tiene como argumentos barco y tablero.
    Devuelve el tablero actualizado
    '''
    for casilla in barco:        
        fila,columna = casilla               
        tablero[fila][columna] = "O"                  
    return tablero

def verificar_superposicion(barco, tablero):
    '''
    Función para verificar que no hay un barco en la casilla.
    Devuelve un True si hay un barco en esa casilla y un False si no lo hay
    '''
    for casilla in barco:
        fila, columna = casilla
        if tablero[fila][columna] == "O":     
            return True
    return False       

def casilla_valida(fila, columna):
    '''
    Función que sirve para comprobar que las coordenadas no se salen del tablero
    Devuelve las coordenadas si cumplen la condición
    '''
    return 0 <= fila < 10 and 0 <= columna < 10

def crear_barco_random(eslora, tablero):
    '''
    Función que genera los barcos aleatoriamente con su respectiva dirección (N, S, E, O).

    Tiene como argumentos la eslora y el tablero. 

    También llamamos a la función casilla_valida y verificar_superposicion para comprobar si las coordenadas son correctas.

    Devuelve una lista con las coordenadas del barco a colocar en el tablero
    
    '''
    while True:
        fila_random = random.randint(0,9)
        columna_random = random.randint (0,9)

        direccion = random.choice(["N", "S", "E", "O"])
        barco_random = [(fila_random, columna_random)]
        # Aquí le resto uno a la eslora porque ya tengo la primera tupla generada en la variable barco_random
        # Con este bucle, genero la dirección a partir de la random.choice
        for _ in range(eslora - 1):         
            if direccion == "N":
                fila_random -= 1
            elif direccion == "S":
                fila_random += 1       
            elif direccion == "E":
                columna_random +=1
            elif direccion == "O":
                columna_random -= 1

            casilla = (fila_random, columna_random)         
            if not casilla_valida(fila_random, columna_random) or casilla in barco_random or verificar_superposicion(barco_random, tablero):
                break              #rompo el bucle for y empieza de nuevo el while
            barco_random.append(casilla)
        else:                                        
            return barco_random       #me devuelve el barco y para el while

def colocar_barcos_en_tablero(tablero, barcos):
    '''
    Función para colocar los barcos en el tablero que utiliza las funciones:
        crear_barco_random y colocar_barco

    Recorre el diccionario barcos con sus valores,
    para generarme la cantidad de barcos que tiene cada uno
    con su correspondiente eslora.

    Devuelve el tablero actualizado con todos los barcos.
    '''
    for _, (eslora, cantidad) in barcos.items():
        # Recorro el diccionario y como es una tupla pongo el () para acceder a los valores de la tupla, y no la tupla en si
        for _ in range(cantidad):
            # Aquí itero la cantidad de barcos, para  que me cree los barcos dados en la variable
            barco = crear_barco_random(eslora, tablero)
            tablero = colocar_barco(barco, tablero)
    return tablero                                                 

# Funciones para disparar

def disparar(tablero, casilla):
    '''
    Función para disparar:
        Pide una fila y una columna para disparar en el tablero enemigo, 
        si aciertas devolvera "Tocado" con una "X" si no, devolvera "Agua" con una "A"
    
    Devuelve el tablero actualizado
    '''

    fila, columna = casilla

    if tablero[fila, columna] == "O":
        print("Tocado")
        tablero[fila, columna] == "X"
        return "Tocado"
    else:
        print("Agua")
        tablero[fila, columna] = "A"
        return "Agua"
    

def comprobar_disparo_cpu(disparos_realizados):
    '''
    Comprobar que el disparo de la CPU es valido y no se repite, es decir que no esta en la variable disparos_realizados.

    Devuelve el disparo aleatorio de la CPU y guarda ese disparo en la variable disparos_realizados
    '''
    while True:
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
        casilla = (fila_random, columna_random)

        if casilla not in disparos_realizados:
            disparos_realizados.add(casilla)        
            return casilla
        
def mostrar_menu():
    '''
    Función para imprimir por pantalla el menú e iniciar el juego.
    '''

    print("Bienvenido a Hundir la flota")
    print("1. Iniciar juego")
    print("2. Salir")

def jugar(tablero_player, tablero_cpu, barcos,                 
          disparos_player_realizados, disparos_cpu_realizados,
          tablero_player_disparos, tablero_cpu_disparos,
          cantidad_total_de_barcos):
    '''
    Función jugar en la que se desarrollan los turnos del juego, se colocan los barcos y
    se dispara.
                                                                                              
    El juego acaba cuando un jugador pierde todos los barcos, es decir, la cantidad de "X" en su tablero es 20.

    Tiene como argumentos:

        tablero_player: Tablero de jugador_1
        tablero_cpu: Tablero de la CPU
        barcos: Diccionario con los barcos, sus esloras y la cantidad de cada tipo de barco
        disparos_player_realizados y disparos_cpu_realizados: 
            un set en el que se guardan las tuplas con las coordenadas de los disparos realizados
        tablero_player_disparos y tablero_cpu_disparos: Tableros en los que se visualizan los disparos de los jugadores
        cantidad_total_de_barcos: Son las 20 casillas que suman todos los barcos para finalizar el juego cuando sean todas "X"

    '''
    
    # Colocar los barcos en los tablero del jugador y de la CPU con las variables ya declaradas         
    
    # tablero_player = colocar_barcos_en_tablero(tablero_player, barcos)
    
    while np.count_nonzero(tablero_player == "O") != 20:
        tablero_player = colocar_barcos_en_tablero(tablero_player, barcos)
    
    while np.count_nonzero(tablero_cpu == "O") != 20:
        tablero_cpu = colocar_barcos_en_tablero(tablero_cpu, barcos)

    # Genero una variable para saber si el jugador o la cpu tienen un turno extra          
    turno_extra_jugador = False
    turno_extra_cpu = False

    # Implementar los turnos del juego
    while True:
        time.sleep(3)
        # Comienza siempre el jugador
        if turno_extra_cpu == False:
            # Reinicio la variable turno_extra_jugador para poder cambiar turno
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

                if casilla not in disparos_player_realizados:         #comprueba que no estén en disparos realizados
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

        # Muestra los tableros después del disparo del jugador (actualizados)
        time.sleep(1)
        print("Tablero del jugador:")
        print(tablero_player)
        print("\n")
        time.sleep(1)
        print("Tablero de disparos del jugador:")
        print(tablero_player_disparos)
        print("\n")
        time.sleep(1)
        print("Disparos del jugador realizados")
        print(disparos_player_realizados)
        print("\n")
        time.sleep(1)

        # Verificar si el jugador ha ganado o perdido y terminar el juego si fuera el caso
        if np.count_nonzero(tablero_cpu == "X") == cantidad_total_de_barcos:
            print("El jugador ha ganado")
            break

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
            time.sleep(1)
            print("Tablero de CPU:")
            print(tablero_cpu)
            print("\n")
            time.sleep(1)
            print("Tablero de disparos de CPU:")
            print(tablero_cpu_disparos)
            print("\n")
            time.sleep(1)
            print("Disparos de CPU realizados")
            print(disparos_cpu_realizados)
            print("\n")
            time.sleep(1)

            if np.count_nonzero(tablero_cpu == "X") == cantidad_total_de_barcos:
                print("La CPU ha ganado")
                break

            # Verificar si la CPU acertó y debe tener otro turno
            if resultado_disparo_cpu == "Tocado":
                turno_extra_cpu = True