from .function.func import beginner_decorator
from .function.func import get_multiple_inputs

class solve_problems:
    @beginner_decorator('PROBLEMA 1')
    def problem_1():
        from .function.func import max
        try:
            a = float(input('Ingrese el primer valor:'))
            b = float(input('Ingrese el segundo valor:'))
        except ValueError:
            print(f'\nEl valor ingresado debería ser un número\n')
        else:
            print(f'Los valores ingresados son : {a} y {b}')
            result = max(a,b)
            print(f'\nEl mayor valor entre [{a},{b}] resulta: {result}\n')
            return result        

    @beginner_decorator('PROBLEMA 2')
    def problem_2():
        from .function.func import max_de_tres
        try:
            a = float(input('Ingrese el primer valor:'))
            b = float(input('Ingrese el segundo valor:'))
            c = float(input('Ingrese el tercer valor:'))
        #except ValueError:
        #    print(f'\nEl valor ingresado debe ser un número\n')
        except Exception as e:
            print(f'\nOcurrió el siguiente error ==> {e}\n')
        else:
            result = max_de_tres(a,b,c)
            print(f'\nEl mayor valor entre [{a},{b},{c}] resulta: {result}\n')
            return result

    @beginner_decorator('PROBLEMA 3') 
    def problem_3():
        from .function.func import vowel_detector
        letter = input('Ingrese la letra para analizar:')
        try:
            result = vowel_detector(letter)
        except ValueError:
            print(f'\nEl valor ingresado debe ser un carácter')
        except Exception as e:
            print(e)
        else:
            if result == True:
                print(f'{letter} es una vocal')
            else:
                print(f'{letter} no es una vocal')

    @beginner_decorator('PROBLEMA 4')
    def problem_4():
        from .function.func import sum
        from .function.func import multi
        inputs = get_multiple_inputs()
        if len(inputs) == 0:
            print('\nNo se ingresaron valores\n')
            return None
        print(f'\nLa suma de los valores {inputs} ingresados es: {sum(*inputs)}\n')
        print(f'La multiplicación de los valores {inputs} ingresados es: {multi(*inputs)}\n')

    @beginner_decorator('PROBLEMA 5')
    def problem_5():
        from .function.func import multi
        from .function.func import inverse
        word = input('Ingrese la palabra a invertir:')
        try:
            inverse_word = inverse(word)
        except Exception as e:
            print(f'\nOcurrió el siguiente error ==> {e}\n')
        else:
            print(f'\nLa palabra {word} invertida es {inverse_word}\n')

    @beginner_decorator('PROBLEMA 6')
    def problem_6():
        from .function.func import inverse
        from .function.func import is_palindrome
        word = input('Ingrese la palabra a analizar:')
        try:
            if is_palindrome(word):
                print(f'\nLa palabra {word} es palindrome. {is_palindrome(word)}\n')
            else:
                print(f'\nLa palabra {word} no es palindrome. {is_palindrome(word)}\n')
        except Exception as e:
            print(f'\nOcurrió el siguiente error ==> {e}\n')

    @beginner_decorator('PROBLEMA 7')
    def problem_7():
        from .function.func import superposition
        # first way
        print('Ingrese los elementos de la primera lista:')
        list1 = list(map(lambda x: int(x),get_multiple_inputs()))
        # second way
        print('Ingrese los elementos de la segunda lista:')
        list2 = get_multiple_inputs()   
        list2 = [int(x) for x in list2]
        # getting the result
        result = superposition(list1,list2)
        print(f'\nLas listas {list1} y {list2} tienen elementos en común? Respuesta: {result}\n')
        

    @beginner_decorator('PROBLEMA 8')
    def problem_8():
        from .function.func import gen_n_caracteres
        num = int(input('Ingrese el número de veces que se repetirá el carácter:'))
        char = input('Ingrese el carácter a repetir:')
        print(f'\nEl resultado de repetir {num} veces el carácter {char} es: {gen_n_caracteres(num,char)}\n')
        
    @beginner_decorator('PROBLEMA 9')
    def problem_9():
        from .function.func import gen_n_caracteres
        try:
            input_list = [int(x) for x in get_multiple_inputs()]
        except Exception as e:
            print(f'\nOcurrió el siguiente error ==> {e}\n')
        else:
            for element in input_list:
                print(gen_n_caracteres(element,'*'))
