import re

def arithmetic_arranger(problems, solve = False):

    header = ''
    body = ''
    sep = ''
    result = ''

    #Too many problems
    if len(problems) > 5:
        print('Error: Too many problems.')
        quit()
    for problem in problems:
        problem = re.split('(\W)', problem.replace(' ', ''))
        # '+' or '-'
        if problem[1].find('/') == 0:
            print("Error: Operator must be '+' or '-'.")
            quit()
        elif problem[1].find('*') == 0:
            print("Error: Operator must be '+' or '-'.")
            quit()
        #Only digits
        if problem[0].isdigit() == 0:
            print("Error: Numbers must only contain digits.")
            quit()
        elif problem[2].isdigit() == 0:
            print("Error: Numbers must only contain digits.")
            quit()
        # < 4 digits
        if len(problem[0]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        elif len(problem[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()

        block_size = len(problem[0]) + 2 if len(problem[0]) > len(problem[2]) else len(problem[2]) + 2

        temp_header = problem[0]
        temp_body = f'{problem[1]} {problem[2]}'
        temp_result = str(eval(f'{problem[0]} {problem[1]} {problem[2]}'))

        temp_header = ' ' * (2) + temp_header
        temp_body = ' ' * (block_size - len(temp_body)) + temp_body
        temp_result = ' ' * (block_size - len(temp_result)) + temp_result
        temp_sep = '-' * (block_size)
        
        header += f'{temp_header}  '
        body += f'{temp_body}  '
        sep += f'{temp_sep}  '
        result += f'{temp_result}  '


    if solve == False:
        print(header)
        print(body)
        print(sep)
    else:
        print(header)
        print(body)
        print(sep)
        print(result)


arithmetic_arranger(["32 + 698", "3802 - 2", "45 + 43", "123 + 49"], True)