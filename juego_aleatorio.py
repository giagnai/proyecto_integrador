import random
import csv


def input_datos(nombre, num_usuario):
    
    nombre = str(input('Por favor, ingrese su nombre: ')).upper()
    print(f'¡Bienvenido {nombre}!')
    try:
        num_usuario = int(input('Ingrese un numero aleatorio en el rango de 1-100 para comenzar -----> '))
        verificar_numero_ingresado(num_usuario)

    except:
        num_usuario == ' '

    return nombre, num_usuario


def number_pc(num_pc):
    
    num_pc = random.randrange(start = 1, stop = 100)
    return num_pc


def verificar_numero_ingresado(num_usuario):
    
    while num_usuario < 1 or num_usuario > 100:
        print('Numero ingresado fuera del rango...Ingrese nuevamente un numero')
        num_usuario = int(input('Ingrese un numero aleatorio entre 1 y 100...'))
    return num_usuario


def comparar_number(num_usuario, numero_generado, contador, adivino):
    
    while contador < 6:
        try:
            if num_usuario == numero_generado:
                
                adivino = 'si'
                print('¡Adivino!')
                contador += 1
                break
            
            elif num_usuario < numero_generado:
                
                adivino = 'no'
                print('El numero que ingreso es menor al numero de la PC')
                num_usuario = input('Ingrese un numero aleatorio entre 1 y 100: ')

                if num_usuario == 'FIN' or num_usuario == 'fin':
                    break
                
                num_usuario = int(num_usuario)

                if num_usuario == numero_generado:
                    adivino = 'si'
                    contador += 1
                    break

                verificar_numero_ingresado(num_usuario)
                contador += 1
            
            else:
               
                adivino = 'no'
                print('El numero que ingreso es mayor al numero de la PC')
                num_usuario = input('Ingrese un numero aleatorio entre 1 y 100: ')
                
                if num_usuario == 'FIN' or num_usuario == 'fin':
                    break
                
                num_usuario = int(num_usuario)
                
                if num_usuario == numero_generado:
                    adivino = 'si'
                    contador += 1
                    break  

                verificar_numero_ingresado(num_usuario)
                contador += 1
        
        except:
            num_usuario == ' '
            
    return num_usuario, numero_generado, contador, adivino


def registro(nombre, adivino, contador):
    with open('jugadas.csv', 'a', newline='') as csvfile:
        header = ['jugador', 'adivino', 'intentos']
        writer = csv.DictWriter(csvfile, fieldnames=header)

        fila = {}
        fila['jugador'] = nombre
        fila['adivino'] = adivino
        fila['intentos'] = contador
        
        writer.writerow(fila)



if __name__ == "__main__":
    print('''***Bienvenidos al juego de adivinar un numero aleatorio en un rango de 1-100***
                        ---Usted tendra un maximo de 6 intentos---''')
    nombre = None
    num_usuario = 0
    num_pc = 0
    contador = 0
    adivino = None

    nombre, num_usuario = input_datos(nombre, num_usuario)
    print('Nombre: {} --- Numero elegido: {}'.format(nombre, num_usuario))

    numero_generado = number_pc(num_pc)

    
    comparacion = comparar_number(num_usuario, numero_generado, contador, adivino)
    print(f'Numero de PC: {comparacion[1]} --- Numero de intentos: {comparacion[2]} --- Adivino: {comparacion[3]}')

    registro_jugadas = registro(nombre, comparacion[3], comparacion[2])
