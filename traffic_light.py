import time
red_time = 10
green_time = 10
print("\033[H\033[J")
def blinking(coutdown, color):
    while 4 >= (coutdown):
        print("\033[H\033[J")
        time.sleep(0.5)
        if color == " Red ":
            print("\33[31m" + color + str(coutdown) + "\033[0m ", end="\r ", flush=True)
        else: print("\33[92m" + color + str(coutdown) + "\033[0m ", end="\r ", flush=True)
        coutdown = coutdown - 1
        time.sleep(0.5)
        return coutdown

while True:
    for i in range(red_time):
        coutdown = red_time - i
        print("\33[31m" + " Red " + str(coutdown) + "\033[0m ", end="\r ", flush=True)
        time.sleep(1)
        blinking(coutdown, color=" Red ")
    print("\33[93m" + "Yellow  " + "\033[0m")
    time.sleep(2)

    print("\033[H\033[J")

    for i in range(green_time):
        coutdown = green_time - i
        print("\33[92m" + " Green " + str(green_time - i) + "\033[0m ", end="\r ", flush=True)
        time.sleep(1)
        blinking(coutdown, color=" Green ")
    print("\33[93m" + "Yellow  " + "\033[0m")
    time.sleep(2)
    print("\033[H\033[J")