from calc import *

def exec_program(program):
    if is_program(program): # Checks if the input is a valid program
        p = program_statements(program)
        return exec_statements(p)
    else:
        print("this isnt a calc program")
        return False


def exec_statements(p):

    if not empty_statements(p):
        
        pathfind(first_statement(p))
        if not empty_statements(rest_statements(p)):
            pathfind(rest_statements(p))


def pathfind(p):
    
    if is_statement(p):
        return exec_statement(p)
    
    else:
        return exec_expression(p)


def exec_statement(p):

    if is_assignment(p):
        exec_assignement(p)

    elif is_repetition(p):
        exec_repetition(p)

    elif is_selection(p):
        exec_selection(p)

    elif is_input(p):
        exec_input(p)

    elif is_output(p):
        exec_output(p)


def exec_expression(p):
    
    if is_variable(p):
        return p

    elif is_constant(p):
        return p
    
    elif is_binaryexpr(p):
        return exec_binaryexpr(p)

    elif is_condition(p):
        return exec_condition(p)


def exec_assignement(p):
    1


def exec_repetition(p):
    if repetition_condition(p):
        pathfind(repetition_statements(p))
        exec_repetition(p)
    else:
        pathfind(p)


def exec_selection(p):

    if pathfind(selection_condition(p)):
        return pathfind(selection_true_branch(p))

    elif selection_has_false_branch(p):
        return pathfind(selection_false_branch(p))


def exec_input(p):
    return input_variable(p)


def exec_output(p):
    print(pathfind(output_expression(p)))


def exec_binaryexpr(p):

    if binaryexpr_operator(p) == '+':
        return binaryexpr_left(p) + binaryexpr_right(p)

    if binaryexpr_operator(p) == '-':
        return binaryexpr_left(p) - binaryexpr_right(p)

    if binaryexpr_operator(p) == '*':
        return binaryexpr_left(p) * binaryexpr_right(p)

    if binaryexpr_operator(p) == '/':
        return binaryexpr_left(p) / binaryexpr_right(p)


def exec_condition(p):

    if condition_operator(p) == '>':
        return (condition_left(p) > condition_right(p))

    elif condition_operator(p) == '<':
        return (condition_left(p) < condition_right(p))

    elif condition_operator(p) == '=':
        return (condition_left(p) == condition_right(p))





    
calc1 = ['calc', ['if', [3, '<', 5], ['print', 2], ['print', 4]]]
calc2 = ['calc', ['while', [3, '<', 5], ['print', 2]], ['print', 'end']]
calc3 = ['calc', ['print', [3, '+', 5]]]
exec_program(calc2)