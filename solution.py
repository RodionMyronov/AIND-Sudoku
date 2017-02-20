from solution_init import *

assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    for unit in unitlist:
        # find unique two-digit values in unit
        pairs = set([values[box] for box in unit if len(values[box]) == 2])
        for p in pairs:
            cnt = len([values[box] for box in unit if values[box] == p])
            # if the value appears exactly twice in unit, exclude its digits from other boxes
            if cnt == 2:
                for box in unit:
                    if values[box] != p:
                        assign_value(values, box, values[box].replace(p[0],'').replace(p[1],''))
    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    assert len(grid)==81, 'Input string should contain exactly 81 character'
    return dict(zip(boxes,[('123456789' if c=='.' else c) for c in grid]))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print

def eliminate(values):
    result = values.copy()
    for box in values:
        # if the box has single value, exclude this digit from all pears of this box
        if len(values[box]) == 1:
            for p in peers[box]:
                assign_value(result, p, result[p].replace(values[box],''))
                
    return result

def only_choice(values):
    for u in unitlist:
        # for each digit find all the boxes it appears in
        digits = {str(i+1) : [] for i in range(9)}
        for box in u:
            for c in values[box]:
                digits[c].append(box)
        # if some digit appears exactly ones and this appearence is not in resolved box - put digit there
        for d in digits.keys():
            if (len(digits[d]) == 1) and (len(values[digits[d][0]]) > 1):
                assign_value(values, digits[d][0], d)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        # repeat elimination while it changes anything
        values = eliminate(values)

        # apply naked_tweens (not in requirements, but why not)
        values = naked_twins(values)

        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    reduced = reduce_puzzle(values)
    # reduction found a box with no available values
    if not reduced:
        return False
    #check if we solved it. If yes - return solution
    if len([box for box in reduced if len(reduced[box]) == 1]) == 81:
        return reduced
    
    # Choose one of the unfilled squares with the fewest possibilities
    min_options = min([len(reduced[box]) for box in reduced if len(reduced[box]) > 1])
    box_to_guess = [box for box in reduced if len(reduced[box]) == min_options][0]
    
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for c in reduced[box_to_guess]:
        new_guess = reduced.copy()
        new_guess[box_to_guess] = c
        res = search(new_guess)
        if res:
            return res

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))


    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

