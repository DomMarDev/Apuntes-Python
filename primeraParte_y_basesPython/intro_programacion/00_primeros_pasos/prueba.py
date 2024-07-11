# Funciones


#Son numeros?

def son_numeros(num1, num2):
    if num1.isdigit() and num2.isdigit():
        control = True
    else:
        control = False
    
    return control

     

# Introducir datos

def introducir_datos():
    num1 = input('Dame el número A')
    num2 = input('Dame el número B')
    
    return num1, num2
    


#Suma

def suma_valores(num1, num2):

    return print(num1 + num2)
  







#Resta



#Multiplicación

#División


        



#Función principal

while True:
    prompt = ''' ¿Qué quieres hacer?
            
 1) Suma 

2) Resta

3) Multiplicación

4) División

5) Salir
    

        '''
    print(prompt)

    
    opcion = input('Entra la opción')

    match opcion:
        case '1':
           introducir_datos()
           if son_numeros(num1, num2):
               num1 = int(num1)
               num2 = int(num2)
               suma_valores(num1,num2)
           else:
               print('ha salido fuera')
               break


           


        case '2':
            print('2')
        
        case '3':
            print('3')
        case '4':
            print('4')        
        case '5':
            print('Adiós Lucas')
            break
        case _:
            print('Opción no contemplada')
