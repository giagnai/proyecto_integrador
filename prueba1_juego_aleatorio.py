import random
import csv


def input_datos(nombre, num_usuario):
    nombre = str(input('Por favor, ingrese su nombre: ')).upper() #Guarda el nombre en mayuscula
    print(f'¡Bienvenido {nombre}!')
    
    try:
        num_usuario = int(input('Ingrese un numero aleatorio en el rango de 1-100 para comenzar -----> '))
        verificar_numero_ingresado(num_usuario)
    except:
        num_usuario == ' '
    #while num_usuario < 1 or num_usuario > 100:
    #    print('Numero ingresado fuera del rango...Ingrese nuevamente un numero')
    #    num_usuario = int(input('Ingrese un numero aleatorio entre 1 y 100...'))
    return nombre, num_usuario


def verificar_numero_ingresado(num_usuario):
    while num_usuario < 1 or num_usuario > 100:
        print('Numero ingresado fuera del rango...Ingrese nuevamente un numero')
        num_usuario = int(input('Ingrese un numero aleatorio entre 1 y 100...'))
    
    return num_usuario


def number_pc(num_pc):
    num_pc = random.randrange(start = 1, stop = 100)
    return num_pc


def comparar_number(num_usuario, numero_generado, contador, adivino):
    
    while contador < 6:
       
        try: #try-except para que pueda seguir el programa al ingresar un espacio '' o un caracter.
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
                #verificar_dato(num_usuario, numero_generado, contador, adivino)
                #while num_usuario < 1 or num_usuario > 100:
                #    print('Numero ingresado fuera del rango...Ingrese nuevamente un numero')
                #    num_usuario = int(input('Ingrese un numero aleatorio entre 1 y 100...'))
                
            
            #elif num_usuario == 'FIN' or num_usuario == 'fin':
            #    exit()
            
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
                #verificar_dato(num_usuario, numero_generado, contador, adivino)
                #while num_usuario < 1 or num_usuario > 100:
                    #print('Numero ingresado fuera del rango...Ingrese nuevamente un numero')
                    #num_usuario = int(input('Ingrese un numero aleatorio entre 1 y 100...'))
                
            
        except:
            num_usuario == ''
            
    return num_usuario, numero_generado, contador, adivino


#def verificar_dato(num_usuario, numero_generado, contador, adivino):
#    if num_usuario == 'FIN' or num_usuario == 'fin':
#        exit()

#   num_usuario = int(num_usuario)

#    if num_usuario == numero_generado:
#        adivino = 'si'
#        contador += 1
#        exit()
    
#    return num_usuario, numero_generado, contador, adivino


def registro(nombre, adivino, contador):
    with open('jugadas.csv', 'a', newline='') as csvfile:
        header = ['jugador', 'adivino', 'intentos']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        #writer.writeheader() --- > esta linea se elimina porque no quiero que me escriba el titulo cada vez que corro el codigo

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
    #jugar_de_nuevo = None

    nombre, num_usuario = input_datos(nombre, num_usuario)
    print('Nombre: {} --- Numero elegido: {}'.format(nombre, num_usuario))

    numero_generado = number_pc(num_pc)
    #print(f'Numero de PC: {numero_generado}') ---> escondemos el numero que emite la PC

    
    comparacion = comparar_number(num_usuario, numero_generado, contador, adivino)
    print(f'Numero de PC: {comparacion[1]} --- Numero de intentos: {comparacion[2]} --- Adivino: {comparacion[3]}')

    #verificar_datos = verificar_dato(num_usuario, numero_generado, contador, adivino)

    registro_jugadas = registro(nombre, comparacion[3], comparacion[2])