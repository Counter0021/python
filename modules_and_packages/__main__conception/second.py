import first

print('Top level in second.py')

first.func_1()

if (__name__ == "__main__"):
    print("second.py is being run directly")
else:
    print('second. py has been imported')
