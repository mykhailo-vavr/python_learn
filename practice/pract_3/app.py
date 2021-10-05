from linkedList import LinkedList
from functionsForOptions import FuncForOptions

def options(option, list):
    functions = FuncForOptions(list)
    return {
        "1": functions.f1,
        "2": functions.f2,
        "3": functions.f3,
        "4": functions.f4,
        "5": functions.f5,
        "6": functions.f6,
        "7": functions.f7,
        "8": functions.f8,
        "9": functions.f9
    }.get(option)


def start(list):
    print("""Choose the option:
          1. Get data from keyboard
          2. Generate an data in range [a, b]
          3. Insert data
          4. Remove data
          5. Get count of unique elems (task)
          6. Show list
          7. Exit
          
          8. Get data from keyboard(using generator)
          9. Generate an data in range [a, b](using generator)""")

    option = input()
    method = options(option, list)
    if method:
        method()
    else:
        print("Choose correct option")
        start(list)
    start(list)


list = LinkedList()
start(list)
