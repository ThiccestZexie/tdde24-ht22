from calc import *

def exec_program(program, var_dict={}):
    if is_program(program): # Checks if the input is a valid program
        p = program_statements(program)
        return exec_statements(p,var_dict)
    else:
        print("this isnt a calc program")
        return False


def exec_statements(p,var_dict):

    if not empty_statements(p):
        
        var_dict = pathfind(first_statement(p),var_dict)
        exec_statements(rest_statements(p),var_dict)



def kill_program():
    print("something went wrong")
    exit()

def pathfind(p,var_dict):
    
    if is_statement(p):
        return exec_statement(p,var_dict)
    
    else:
        return exec_expression(p,var_dict)


def exec_statement(p,var_dict):

    if is_assignment(p):
        return exec_assignement(p,var_dict)

    elif is_repetition(p):
        return exec_repetition(p,var_dict)

    elif is_selection(p):
        return exec_selection(p,var_dict)

    elif is_input(p):
        return exec_input(p,var_dict)

    elif is_output(p):
        return exec_output(p,var_dict)


def exec_expression(p,var_dict):
    
    if is_variable(p):
        return var_dict[p]

    elif is_constant(p):
        return p
    
    elif is_binaryexpr(p):
        return exec_binaryexpr(p,var_dict)

    elif is_condition(p):
        return exec_condition(p,var_dict)


def exec_assignement(p,var_dict):
    new_dict = var_dict.copy()
    new_dict[assignment_variable(p)] = pathfind(assignment_expression(p),var_dict)
    return new_dict


def exec_repetition(p,var_dict):

    while repetition_condition(p):
        return pathfind(repetition_statements(p),var_dict)
    else:
        return pathfind(p,var_dict)


def exec_selection(p,var_dict):

    if pathfind(selection_condition(p),var_dict):
        return pathfind(selection_true_branch(p),var_dict)

    elif selection_has_false_branch(p):
        return pathfind(selection_false_branch(p),var_dict)



def exec_input(p,var_dict):

    new_dict = var_dict.copy()
    new_dict[input_variable(p)] = int(input("input variable value: "))
    return new_dict



def exec_output(p,var_dict):
    print(pathfind(output_expression(p),var_dict))
    return var_dict


def exec_binaryexpr(p,var_dict):

    if binaryexpr_operator(p) == '+':
        return pathfind(binaryexpr_left(p),var_dict) + pathfind(binaryexpr_right(p),var_dict)

    if binaryexpr_operator(p) == '-':
        return pathfind(binaryexpr_left(p),var_dict) - pathfind(binaryexpr_right(p),var_dict)

    if binaryexpr_operator(p) == '*':
        return pathfind(binaryexpr_left(p),var_dict) * pathfind(binaryexpr_right(p),var_dict)

    if binaryexpr_operator(p) == '/':
        return pathfind(binaryexpr_left(p),var_dict) / pathfind(binaryexpr_right(p),var_dict)

    else:
        kill_program()


def exec_condition(p,var_dict):

    if condition_operator(p) == '>':
        return (pathfind(condition_left(p),var_dict) > pathfind(condition_right(p),var_dict))

    elif condition_operator(p) == '<':
        return (pathfind(condition_left(p),var_dict) < pathfind(condition_right(p),var_dict))

    elif condition_operator(p) == '=':
        return (pathfind(condition_left(p),var_dict) == pathfind(condition_right(p),var_dict))

    else:
        kill_program()



def test_code():
        
    calc1 = ['calc', ['if', [4, '=', 5], ['print', 2], ['print', 4]]]
    #TODO fix while
    calc2 = ['calc', ['while', [3, '<', 5], ['print', 2]], ['print', 'end']]
    calc3 = ['calc', ['print', [3, '/', 5]]]
    calc4 = ['calc', ['print', 5]]
    calc5 = ['calc', ['set', 'a', 5], ['print', 'a']]
    calc6 = ['calc', ['read', 'n'], ['print', 'n'], ['if', ['n', '>', 5], ['print', 2], ['print', 4]]]
    calc7 = ['calc', ['set', 'x', 7], ['set', 'y', 12], ['set', 'z', ['x', '+', 'y']], ['print', 'z']]
    calc8 = ['calc', ['read', 'p1'],['set', 'p2', 47],['set', 'p3', 179],['set', 'result', [['p1', '*', 'p2'], '-', 'p3']],['print', 'result']]
    calc9 = ['calc', ['read', 'n'],['set', 'sum', 0],['while', ['n', '>', 0],['set', 'sum', ['sum', '+', 'n']],['set', 'n', ['n', '-', 1]]],['print', 'sum']]
    exec_program(calc2)


test_code()





