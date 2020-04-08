def dydx(x, y):
    return y + x*y

def main():
    x = INIT_X
    y = INIT_Y 
    while x != STOP_X:
        x += STEP_SIZE
        y += dydx(x,y)*STEP_SIZE
    print(y)
    return 

if __name__ == "__main__":
    STEP_SIZE = 0.1
    INIT_Y = 1
    INIT_X = 0
    STOP_X = 0.5
    main()
    