import sys

def rush(x, y):
    '''
    Display a square pattern based on x(width) and y(height)
    Args:
        x:(int): Width of the square
        y(int): Height f the square
    '''
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for i in range(y):
        if i == 0 or i == y - 1:
            # Top or Bottom row
            if x == 1:
                print("o")
            else:
                print("o" + "-" * (x - 2) + "o")
        else:
            # Middle rows
            if x == 1:
                print("|")
            else:
                print("|" + " " * (x - 2) + "|")