from solver_module.solver_problems import solve_problems


def switcher_function(option: int):
    switch_dic = {
        1: solve_problems.problem_1,
        2: solve_problems.problem_2,
        3: solve_problems.problem_3,
        4: solve_problems.problem_4,
        5: solve_problems.problem_5,
        6: solve_problems.problem_6,
        7: solve_problems.problem_7,
        8: solve_problems.problem_8,
        9: solve_problems.problem_9,
    }
    return switch_dic.get(option, lambda: ' no hay esa opción')()


if __name__ == '__main__':
    try:
        case = int(input('Ingrese el número correspondiente al problema que desea resolver:'))
    except ValueError:
        print(f'\nEl valor ingresado debe ser un número entero\n')
    except Exception as e:
        print(f'\nOcurrió el siguiente error ==> {e}\n')
    else:
        switcher_function(case)
