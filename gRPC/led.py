from sense_hat import SenseHat

sense = SenseHat()

def checkAirconState(state):
    if state == 1:
        sense.set_pixel(1, 0, (0, 255, 0))
        sense.set_pixel(0, 1, (0, 255, 0))
        sense.set_pixel(0, 2, (0, 255, 0))
        sense.set_pixel(2, 1, (0, 255, 0))
        sense.set_pixel(2, 2, (0, 255, 0))
    elif state == 0:
        sense.set_pixel(1, 0, (255, 0, 0))
        sense.set_pixel(0, 1, (255, 0, 0))
        sense.set_pixel(0, 2, (255, 0, 0))
        sense.set_pixel(2, 1, (255, 0, 0))
        sense.set_pixel(2, 2, (255, 0, 0))
    else:
        print("invalid state")

def checkLightState(state):
    if state == 1:
        sense.set_pixel(5, 0, (0, 255, 0))
        sense.set_pixel(5, 1, (0, 255, 0))
        sense.set_pixel(5, 2, (0, 255, 0))
        sense.set_pixel(6, 2, (0, 255, 0))
        sense.set_pixel(7, 2, (0, 255, 0))
    elif state == 0:
        sense.set_pixel(5, 0, (255, 0, 0))
        sense.set_pixel(5, 1, (255, 0, 0))
        sense.set_pixel(5, 2, (255, 0, 0))
        sense.set_pixel(6, 2, (255, 0, 0))
        sense.set_pixel(7, 2, (255, 0, 0))
    else:
        print("invalid state")

def checkAirconTemp(temp):
    firstDigit  = temp[0]
    secondDigit = temp[1]
    if firstDigit == "1":
        sense.set_pixel(0, 3, (0, 0 ,0))
        sense.set_pixel(0, 4, (0, 0 ,0))
        sense.set_pixel(0, 5, (0, 0 ,0))
        sense.set_pixel(0, 6, (0, 0 ,0))
        sense.set_pixel(0, 7, (0, 0 ,0))
        sense.set_pixel(1, 3, (0, 0 ,255))
        sense.set_pixel(1, 4, (0, 0 ,0))
        sense.set_pixel(1, 5, (0, 0 ,0))
        sense.set_pixel(1, 6, (0, 0 ,0))
        sense.set_pixel(1, 7, (0, 0 ,0))
        sense.set_pixel(2, 3, (0, 0 ,255))
        sense.set_pixel(2, 4, (0, 0 ,255))
        sense.set_pixel(2, 5, (0, 0 ,255))
        sense.set_pixel(2, 6, (0, 0 ,255))
        sense.set_pixel(2, 7, (0, 0 ,255))
    elif firstDigit == "2":
        sense.set_pixel(0, 3, (0, 0 ,255))
        sense.set_pixel(0, 4, (0, 0 ,0))
        sense.set_pixel(0, 5, (0, 0 ,255))
        sense.set_pixel(0, 6, (0, 0 ,255))
        sense.set_pixel(0, 7, (0, 0 ,255))
        sense.set_pixel(1, 3, (0, 0 ,255))
        sense.set_pixel(1, 4, (0, 0 ,0))
        sense.set_pixel(1, 5, (0, 0 ,255))
        sense.set_pixel(1, 6, (0, 0 ,0))
        sense.set_pixel(1, 7, (0, 0 ,255))
        sense.set_pixel(2, 3, (0, 0 ,255))
        sense.set_pixel(2, 4, (0, 0 ,255))
        sense.set_pixel(2, 5, (0, 0 ,255))
        sense.set_pixel(2, 6, (0, 0 ,0))
        sense.set_pixel(2, 7, (0, 0 ,255))
    elif firstDigit == "3":
        sense.set_pixel(0, 3, (0, 0 ,255))
        sense.set_pixel(0, 4, (0, 0 ,0))
        sense.set_pixel(0, 5, (0, 0 ,255))
        sense.set_pixel(0, 6, (0, 0 ,0))
        sense.set_pixel(0, 7, (0, 0 ,255))
        sense.set_pixel(1, 3, (0, 0 ,255))
        sense.set_pixel(1, 4, (0, 0 ,0))
        sense.set_pixel(1, 5, (0, 0 ,255))
        sense.set_pixel(1, 6, (0, 0 ,0))
        sense.set_pixel(1, 7, (0, 0 ,255))
        sense.set_pixel(2, 3, (0, 0 ,255))
        sense.set_pixel(2, 4, (0, 0 ,255))
        sense.set_pixel(2, 5, (0, 0 ,255))
        sense.set_pixel(2, 6, (0, 0 ,255))
        sense.set_pixel(2, 7, (0, 0 ,255))
    else:
        print("system cannot go below 10 degress or above 39")

    if secondDigit == "1":
        sense.set_pixel(5, 3, (0, 0 ,0))
        sense.set_pixel(5, 4, (0, 0 ,0))
        sense.set_pixel(5, 5, (0, 0 ,0))
        sense.set_pixel(5, 6, (0, 0 ,0))
        sense.set_pixel(5, 7, (0, 0 ,0))
        sense.set_pixel(6, 3, (0, 0 ,255))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,0))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,0))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,255))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,255))
        sense.set_pixel(7, 7, (0, 0 ,255))
    elif secondDigit == "2":
        sense.set_pixel(5, 3, (0, 0 ,255))
        sense.set_pixel(5, 4, (0, 0 ,0))
        sense.set_pixel(5, 5, (0, 0 ,255))
        sense.set_pixel(5, 6, (0, 0 ,255))
        sense.set_pixel(5, 7, (0, 0 ,255))
        sense.set_pixel(6, 3, (0, 0 ,255))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,255))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,255))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,255))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,0))
        sense.set_pixel(7, 7, (0, 0 ,255))
    elif secondDigit == "3":
        sense.set_pixel(5, 3, (0, 0 ,255))
        sense.set_pixel(5, 4, (0, 0 ,0))
        sense.set_pixel(5, 5, (0, 0 ,255))
        sense.set_pixel(5, 6, (0, 0 ,0))
        sense.set_pixel(5, 7, (0, 0 ,255))
        sense.set_pixel(6, 3, (0, 0 ,255))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,255))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,255))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,255))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,255))
        sense.set_pixel(7, 7, (0, 0 ,255))
    elif secondDigit == "4":
        sense.set_pixel(5, 3, (0, 0 ,255))
        sense.set_pixel(5, 4, (0, 0 ,255))
        sense.set_pixel(5, 5, (0, 0 ,255))
        sense.set_pixel(5, 6, (0, 0 ,0))
        sense.set_pixel(5, 7, (0, 0 ,0))
        sense.set_pixel(6, 3, (0, 0 ,0))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,255))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,0))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,255))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,255))
        sense.set_pixel(7, 7, (0, 0 ,255))
    elif secondDigit == "5":
        sense.set_pixel(5, 3, (0, 0 ,255))
        sense.set_pixel(5, 4, (0, 0 ,255))
        sense.set_pixel(5, 5, (0, 0 ,255))
        sense.set_pixel(5, 6, (0, 0 ,0))
        sense.set_pixel(5, 7, (0, 0 ,255))
        sense.set_pixel(6, 3, (0, 0 ,255))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,255))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,255))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,0))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,255))
        sense.set_pixel(7, 7, (0, 0 ,255))
    elif secondDigit == "6":
        sense.set_pixel(5, 3, (0, 0 ,255))
        sense.set_pixel(5, 4, (0, 0 ,255))
        sense.set_pixel(5, 5, (0, 0 ,255))
        sense.set_pixel(5, 6, (0, 0 ,255))
        sense.set_pixel(5, 7, (0, 0 ,255))
        sense.set_pixel(6, 3, (0, 0 ,255))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,255))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,255))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,0))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,255))
        sense.set_pixel(7, 7, (0, 0 ,255))
    elif secondDigit == "7":
        sense.set_pixel(5, 3, (0, 0 ,255))
        sense.set_pixel(5, 4, (0, 0 ,0))
        sense.set_pixel(5, 5, (0, 0 ,0))
        sense.set_pixel(5, 6, (0, 0 ,0))
        sense.set_pixel(5, 7, (0, 0 ,0))
        sense.set_pixel(6, 3, (0, 0 ,255))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,0))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,0))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,255))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,255))
        sense.set_pixel(7, 7, (0, 0 ,255))
    elif secondDigit == "8":
        sense.set_pixel(5, 3, (0, 0 ,255))
        sense.set_pixel(5, 4, (0, 0 ,255))
        sense.set_pixel(5, 5, (0, 0 ,255))
        sense.set_pixel(5, 6, (0, 0 ,255))
        sense.set_pixel(5, 7, (0, 0 ,255))
        sense.set_pixel(6, 3, (0, 0 ,255))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,255))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,255))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,255))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,255))
        sense.set_pixel(7, 7, (0, 0 ,255))
    elif secondDigit == "9":
        sense.set_pixel(5, 3, (0, 0 ,255))
        sense.set_pixel(5, 4, (0, 0 ,255))
        sense.set_pixel(5, 5, (0, 0 ,255))
        sense.set_pixel(5, 6, (0, 0 ,0))
        sense.set_pixel(5, 7, (0, 0 ,255))
        sense.set_pixel(6, 3, (0, 0 ,255))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,255))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,255))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,255))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,255))
        sense.set_pixel(7, 7, (0, 0 ,255))
    elif secondDigit == "0":
        sense.set_pixel(5, 3, (0, 0 ,255))
        sense.set_pixel(5, 4, (0, 0 ,255))
        sense.set_pixel(5, 5, (0, 0 ,255))
        sense.set_pixel(5, 6, (0, 0 ,255))
        sense.set_pixel(5, 7, (0, 0 ,255))
        sense.set_pixel(6, 3, (0, 0 ,255))
        sense.set_pixel(6, 4, (0, 0 ,0))
        sense.set_pixel(6, 5, (0, 0 ,0))
        sense.set_pixel(6, 6, (0, 0 ,0))
        sense.set_pixel(6, 7, (0, 0 ,255))
        sense.set_pixel(7, 3, (0, 0 ,255))
        sense.set_pixel(7, 4, (0, 0 ,255))
        sense.set_pixel(7, 5, (0, 0 ,255))
        sense.set_pixel(7, 6, (0, 0 ,255))
        sense.set_pixel(7, 7, (0, 0 ,255))