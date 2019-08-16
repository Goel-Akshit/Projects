import re #regex library


def perform_calculation():
    global previous #global keyword increase the scope of variables declared to all
    global run

    expression = input(str(previous))

    if expression == "quit":
        print("Calculator Shutdown, Happy Calculation.\n")
        run = False

    elif expression == "reset":
        previous = 0

    else:
        expression = re.sub('[a-zA-Z,:()" "]', '', expression)
        previous = eval(str(previous) + expression)

previous = 0
run = True

print("My Super Calculator: \n")
print("1.quit : to exit \n2.reset : to start from zero\n")

while run:
    perform_calculation()

