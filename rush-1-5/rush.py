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
        if i == 0:
            # Top row: A...C
            if x == 1:
                print("B")
            else:
                print("A" + "B" * (x - 2) + "C")
        elif i == y - 1:
            # Bottom row: C...A
            if x == 1:
                print("B")
            else:
                print("C" + "B" * (x - 2) + "A")
        else:
            # Middle rows
            if x == 1:
                print("B")
            else:
                print("B" + " " * (x - 2) + "B")