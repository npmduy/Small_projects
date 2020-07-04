import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(initial_ty, file=sys.stderr, flush=True)
    print(initial_tx, file=sys.stderr, flush=True)
    if initial_tx != light_x:
        if initial_tx < light_x:
            if initial_ty < light_y:
                print('SE')
            elif initial_ty > light_y:
                print("NW")
            else:
                print("E")
        else:
            if initial_ty < light_y:
                print('SW')
            elif initial_ty > light_y:
                print("NE")
            else:
                print("W")
    elif initial_ty != light_y:
        if initial_ty < light_y:
            if initial_tx < light_x:
                print('SE')
            elif initial_tx > light_x:
                print("NW")
            else:
                print("S")
        else:
            if initial_tx < light_x:
                print('SW')
            elif initial_tx > light_x:
                print("NE")
            else:
                print("N")
