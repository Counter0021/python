def main():
    while True:
        key = str(input("Press R to read a file\nPress E to enter data\nPress L to leave the program\n"))
        key = key.lower()
        execute(key)


def readfile():
   print ("read")


def enterdata():
    print ("enter")


dictOfCommands = {
    'r': readfile,
    'e': enterdata,
    'l': exit
}


def execute(command):
    dictOfCommands[command]()


main()