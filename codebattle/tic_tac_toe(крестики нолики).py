def solution(game: list) -> str:
    for hor in game:
        if hor[0] == hor[1] == hor[2] != '_':
            return f'{hor[0]} won'

    for ver in range(3):
        if game[0][ver] == game[1][ver] == game[2][ver] != '_':
            return f'{game[0][ver]} won'

    if game[0][0] == game[1][1] == game[2][2] != '_':
        return f'{game[0][0]} won'

    if game[2][0] == game[1][1] == game[0][2] != '_':
        return f'{game[2][0]} won'

    if all([all([x != '_' for x in X]) for X in game]):
        return 'Game over'
    else:
        return 'Next'

assert "X won"  == solution([[""
                              "X","O","X"],["O","X","O"],["_","_","X"]])
assert "O won"  == solution([["X","X","O"],["_","O","_"],["O","X","O"]])
assert "Next"  == solution([["_","O","X"],["X","_","_"],["_","_","O"]])
assert "Game over"  == solution([["X","O","X"],["O","X","X"],["O","X","O"]])
