# Ejercicios de entrevistas
En este repo encontraras un listado de ejercicios comunes que se toman en entrevistas con sus implementaciones.

## Enunciados

1. Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, 
pero hacerla por nosotros mismos es un muy buen ejercicio)

```python
def max(a:float,b:float):
    return a if a>b else b
```

2. Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.

```python
#haciendo uso de la function max creada previamente
def max_de_tres(a:float,b:float,c:float):
   return max(max(a,b),c)
```

3. Escribir una función que tome un carácter alfabético y devuelva True si es una vocal, de lo contrario devuelve False.

```python
def vowel_detector(letter: str):
    try:
        float(letter)
    except:
        if len(letter)>1:
            raise Exception('Debe ingresar solo una letra')
        else:
            vowels = ['a','e','i','o','u']
            result = True if letter.casefold() in vowels else False
            return result
    else:
        raise Exception('Solo se permite carácter alfabético')
```

4. Escribir una función sum() y una función multi() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multi([1,2,3,4]) debería devolver 24.

````python
def sum(*args:float):
    result = 0
    for arg in args:
        result += arg
    return result

def multi(*args:float):
    result = 1
    for arg in args:
        result *= arg
    return result

```

5. Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".

````python
def inverse(string: str):
    return string[::-1]

```

6. Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

````python
def is_palindrome(string: str):
    return True if string == string[::-1] else False

```

7. Definir una función superposición() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

````python
def superposition(string1: str,string2: str):
    for letter in string1:
        if letter in string2:
            return True
    return False

```

8. Definir una función generar_n_caracteres() que tome un entero n y devuelva el carácter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

````python
def gen_n_caracteres(num:int, string:str) -> str:
    return string * num

```

9. Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

````python
def problem_9():
   from .function.func import gen_n_caracteres
   try:
      input_list = [int(x) for x in get_multiple_inputs()]
   except Exception as e:
      print(f'\nOcurrió el siguiente error ==> {e}\n')
   else:
      for element in input_list:
            print(gen_n_caracteres(element,'*'))
```

## Ejecución

1. You must have installed Python 3.10.x on your PC.
2. Make sure to have Python installed and run main.py:
   - python main.py
