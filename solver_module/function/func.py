def max(a:float,b:float):
    return a if a>b else b

def max_de_tres(a:float,b:float,c:float):
    return max(max(a,b),c)

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

def inverse(string: str):
    return string[::-1]

def is_palindrome(string: str):
    return True if string == string[::-1] else False

def superposition(string1: str,string2: str):
    for letter in string1:
        if letter in string2:
            return True
    return False

def gen_n_caracteres(num:int, string:str) -> str:
    return string * num

def beginner_decorator(message:str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            num_spaces = 4
            num_stars = int(len(message) + (num_spaces*2))
            print(num_stars*'*',num_spaces*' '+message,num_stars*'*',sep='\n')
            return func(*args, **kwargs)
        return wrapper
    return decorator

def get_multiple_inputs():
    inputs = list()
    while True:
        user_input = input("Enter input (or 'done' to finish): ")
        if user_input == 'done':
            break    
        try:
            num_input = float(user_input)
        except:
            raise Exception('Debe ingresar solo números')
        else:
            inputs.append(num_input)
    return inputs
