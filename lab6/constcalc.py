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
        
        pathfind(first_statement(p),var_dict)

        if not empty_statements(rest_statements(p)):
            pathfind(rest_statements(p),var_dict)

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
        exec_assignement(p,var_dict)

    elif is_repetition(p):
        exec_repetition(p,var_dict)

    elif is_selection(p):
        exec_selection(p,var_dict)

    elif is_input(p):
        exec_input(p,var_dict)

    elif is_output(p):
        exec_output(p,var_dict)

    else:
        kill_program()


def exec_expression(p,var_dict):
    
    if is_variable(p):
        return var_dict[p]

    elif is_constant(p):
        return p
    
    elif is_binaryexpr(p):
        return exec_binaryexpr(p,var_dict)

    elif is_condition(p):
        return exec_condition(p,var_dict)

    else:
        kill_program()


def exec_assignement(p,var_dict):
    new_dict = var_dict.copy()
    new_dict[assignment_variable(p)] = assignment_expression(p)
    pathfind(p,new_dict)


def exec_repetition(p,var_dict):

    if repetition_condition(p,var_dict):
        pathfind(repetition_statements(p,var_dict),var_dict)
        exec_repetition(p,var_dict)
    else:
        pathfind(p,var_dict)


def exec_selection(p,var_dict):

    if pathfind(selection_condition(p),var_dict):
        return pathfind(selection_true_branch(p),var_dict)

    elif selection_has_false_branch(p):
        return pathfind(selection_false_branch(p),var_dict)



def exec_input(p,var_dict):
    return input_variable(p,var_dict)


def exec_output(p,var_dict):
    print(pathfind(output_expression(p),var_dict))


def exec_binaryexpr(p,var_dict):

    if binaryexpr_operator(p) == '+':
        return binaryexpr_left(p) + binaryexpr_right(p)

    if binaryexpr_operator(p) == '-':
        return binaryexpr_left(p) - binaryexpr_right(p)

    if binaryexpr_operator(p) == '*':
        return binaryexpr_left(p) * binaryexpr_right(p)

    if binaryexpr_operator(p) == '/':
        return binaryexpr_left(p) / binaryexpr_right(p)


def exec_condition(p,var_dict):

    if condition_operator(p) == '>':
        return (condition_left(p) > condition_right(p))

    elif condition_operator(p) == '<':
        return (condition_left(p) < condition_right(p))

    elif condition_operator(p) == '=':
        return (condition_left(p) == condition_right(p))



def test_code():
        
    calc1 = ['calc', ['if', [4, '=', 5], ['print', 2], ['print', 4]]]
    #TODO fix while
    calc2 = ['calc', ['while', [3, '<', 5], ['print', 2]], ['print', 'end']]
    calc3 = ['calc', ['print', [3, '/', 5]]]
    calc4 = ['calc', ['print', 5]]
    calc5 = ['calc', ['set', 'a', 5], ['print', 'a']]
    exec_program(calc5)


test_code()





