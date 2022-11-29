from calc import *

def exec_program(program, var_dict={}):
    if is_program(program): # Checks if the input is a valid program
        p = program_statements(program)
        return exec_statements(p,var_dict)
    else:
        raise SyntaxError('program isnt a calc program')


def exec_statements(p,var_dict):

    if not empty_statements(p):
        
        var_dict = exec_statement(first_statement(p),var_dict)
        var_dict = exec_statements(rest_statements(p),var_dict)

    return var_dict

def exec_statement(p,var_dict):

    if is_repetition(p):   
        return exec_repetition(p,var_dict)

    elif is_selection(p):
        return exec_selection(p,var_dict)

    elif is_input(p):
        return exec_input(p,var_dict)

    elif is_output(p):
        return exec_output(p,var_dict)

    elif is_condition(p):
        return eval_condition(p,var_dict)

    elif is_assignment:
        return exec_assignement(p,var_dict)

    else:
        raise TypeError


def eval_expression(p,var_dict):
    
    if is_variable(p):
        return var_dict[p]

    elif is_constant(p):
        return p

    elif is_binaryexpr(p):
        return exec_binaryexpr(p,var_dict)

    else:
        raise TypeError


def exec_assignement(p,var_dict):
    new_dict = var_dict.copy()
    new_dict[assignment_variable(p)] = eval_expression(assignment_expression(p),var_dict)
    return new_dict


def exec_repetition(p,var_dict):

    while eval_condition(repetition_condition(p),var_dict):
        var_dict = exec_statements(repetition_statements(p),var_dict)
        
    return var_dict


def exec_selection(p,var_dict):

    if eval_condition(selection_condition(p),var_dict):
        return exec_statement(selection_true_branch(p),var_dict)

    elif selection_has_false_branch(p):
        return exec_statement(selection_false_branch(p),var_dict)

    else:
        return var_dict



def exec_input(p,var_dict):

    new_dict = var_dict.copy()
    new_dict[input_variable(p)] = int(input(f"Enter value for {input_variable(p)}: "))
    return new_dict



def exec_output(p,var_dict):

    if is_variable(output_expression(p)):
        print(output_expression(p), '=', eval_expression(output_expression(p),var_dict))
    else:
        print(eval_expression(output_expression(p),var_dict))

    return var_dict


def exec_binaryexpr(p,var_dict):

    if binaryexpr_operator(p) == '+':
        return eval_expression(binaryexpr_left(p),var_dict) + eval_expression(binaryexpr_right(p),var_dict)

    if binaryexpr_operator(p) == '-':
        return eval_expression(binaryexpr_left(p),var_dict) - eval_expression(binaryexpr_right(p),var_dict)

    if binaryexpr_operator(p) == '*':
        return eval_expression(binaryexpr_left(p),var_dict) * eval_expression(binaryexpr_right(p),var_dict)

    if binaryexpr_operator(p) == '/':
        return eval_expression(binaryexpr_left(p),var_dict) / eval_expression(binaryexpr_right(p),var_dict)

    else:
        raise SyntaxError


def eval_condition(p,var_dict):

    if condition_operator(p) == '>':
        return (eval_expression(condition_left(p),var_dict) > eval_expression(condition_right(p),var_dict))

    elif condition_operator(p) == '<':
        return (eval_expression(condition_left(p),var_dict) < eval_expression(condition_right(p),var_dict))

    elif condition_operator(p) == '=':
        return (eval_expression(condition_left(p),var_dict) == eval_expression(condition_right(p),var_dict))

    else:
        raise SyntaxError


def test_code():
    # Calc 1,2,3,4 are tests who are supposed to send out errors 
    calc1 = ['calc', ['set', 'n', 'wow'], ['print', 'n']] # tries to set a string as a value to a variable. 
    calc2 = ['calc', ['read', 'x'], ['read', 'y'], ['while', ['x', '<', 5], ['set', 'x', ['y', '+', 'x']], ['print', 'x']], ['print', 'x']] # test reading decimals or strings
    calc3 = ['calc', ['print', [3, '%', 5]]] # Tries to print a binary expression 
    calc4 = ['print', 'hi'] # Not a calc
        
    # Calc 5-10 are normal tests to show the functionality of the 'calc' language
    calc5 = ['calc', ['print', 5]]
    calc6 = ['calc', ['set', 'a', 5], ['print', 'a']]
    calc7 = ['calc', ['read', 'n'], ['print', 'n'], ['if', ['n', '>', 5], ['print', 2], ['print', 4]]]
    calc8 = ['calc', ['set', 'x', 7], ['set', 'y', 12], ['set', 'z', ['x', '+', 'y']], ['print', 'z']]
    calc9 = ['calc', ['read', 'p1'], ['set', 'p2', 47], ['set', 'p3', 179], ['set', 'result', [['p1', '*', 'p2'], '-', 'p3']], ['print', 'result']]
    calc10 = ['calc', ['read', 'n'],['set', 'sum', 0],['while', ['n', '>', 0], ['set', 'sum', ['sum', '+', 'n']], ['set', 'n', ['n', '-', 1]]], ['print', 'sum']]
    exec_program(calc10)


test_code()