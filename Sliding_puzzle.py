"""Sliding Puzzle
Prof. O and Peyton Wall
2024-09-24

A Sliding Puzzle is represented by a string
whose length is a perfect square
of an integer in [2, 6] (i.e., 4, 9, 16, 25, or 36).
It contains only digits (0-9) and capital letters (A-Z),
exactly ONE of which (typically 0) is "empty"
and is represented by a hyphen (-).

On screen, however, the layout is an NxN square.
Legal moves consist of sliding a tile
up, down, left, or right (but never diagonally)
into the empty spot (-).

The puzzle is in the "solved" state when
all its digits and letters are in ascending order
(with digits before letters, as in ASCII and Unicode)
and the empty spot is at the beginning or end
(never in the middle).

References:
https://mathworld.wolfram.com/15Puzzle.html
https://lorecioni.github.io/fifteen-puzzle-game/
https://15puzzle.netlify.app/
"""
import math

def rows_from_puzzle(puzzle : str) -> str:
    r"""Returns a string with a newline between rows of the puzzle.
    >>> rows_from_puzzle('12345678-')
    '123\n456\n78-'
    >>> rows_from_puzzle("12-3")
    '12\n-3'
    >>> rows_from_puzzle("123456789ABCDEF-")
    '1234\n5678\n9ABC\nDEF-'
    """
    size = int(math.sqrt(len(puzzle)))
    rows = [puzzle[i:i+size] for i in range(0, len(puzzle), size)]
    return '\n'.join(rows)
    
def is_solved(puzzle : str) -> bool:
    """Determines whether the puzzle is solved (as defined above).
    >>> is_solved("13245678-")
    False
    >>> is_solved("12345678-")
    True
    >>> is_solved("-12345678")
    True
    >>> is_solved("321-")
    False
    >>> is_solved("123-")
    True
    """
    sorted_puzzle = ''.join(sorted(puzzle.replace('-', ''))) + '-'
    return puzzle == sorted_puzzle or puzzle == '-' + sorted_puzzle[:-1]

def is_legal_move(puzzle : str, tile_to_move : str) -> bool:
    """Determines whether it is possible to move tile_to_move into the empty spot.
    >>> is_legal_move("12345678-", "8")
    True
    >>> is_legal_move("12345678-", "6")
    True
    >>> is_legal_move("12345678-", "5")
    False
    >>> is_legal_move("12345678-", "-")
    False
    >>> is_legal_move("123456789ABCDEF-", "F")
    True
    >>> is_legal_move("123456789ABCDEF-", "E")
    False
    """

    if tile_to_move == "-":
        return False
    
    size = int(len(puzzle) ** 0.5)
    empty_idx = puzzle.index('-')
    tile_idx = puzzle.index(tile_to_move)

    row_diff = abs(tile_idx // size - empty_idx // size)
    col_diff = abs(tile_idx % size - empty_idx % size)

    return (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1)

def puzzle_with_move(puzzle : str, tile_to_move : str) -> str:
    """Move tile_to_move into the empty slot (-).
    >>> puzzle_with_move("12345678-", "8")
    '1234567-8'
    >>> puzzle_with_move("123-45678", "3")
    '12-345678'
    >>> puzzle_with_move("123456789ABCDEF-", "F")
    '123456789ABCDE-F'
    >>> puzzle_with_move("12-34", "2")
    '1-234'
    """
    if tile_to_move == "-":
        return puzzle
    
    size = int(len(puzzle) ** 0.5)
    empty_idx = puzzle.index('-')
    tile_idx = puzzle.index(tile_to_move)

    puzzle_list = list(puzzle)
    puzzle_list[empty_idx], puzzle_list[tile_idx] = puzzle_list[tile_idx], puzzle_list[empty_idx]
    
    return ''.join(puzzle_list)

def space_puzzle(puzzle : str) -> str:
    r"""
    >>> space_puzzle('12345678-')
    ' 1 2 3 \n 4 5 6 \n 7 8 -'
    
    """
    return " " + " ".join(rows_from_puzzle(puzzle))

def play_puzzle(puzzle : str) -> None:
    moves = 0
    while not is_solved(puzzle):
        print(f"\nCurrent puzzle state:\n{space_puzzle(puzzle)}")
        tile_to_move = "-"
        moves += 1
        print(f"Move #{moves}")
        while not is_legal_move(puzzle, tile_to_move):
            tile_to_move = input("Which tile would you like to move into the empty spot? ")        
        puzzle = puzzle_with_move(puzzle, tile_to_move)
    print(f"\nSolved!\n{space_puzzle(puzzle)}")
    print(f"You solved the puzzle in {moves} moves!")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    play_puzzle("1-32")