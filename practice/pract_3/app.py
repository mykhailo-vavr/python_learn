from linkedList import LinkedList
from functionsForOptions import FuncForOptions

# input data C:\python_learn_lnu\practice\pract_3\data\data.json


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
        "0": functions.f0,
    }.get(option)


def start(list):
    print("""Choose the option:
          1. Strategy 1 to set data(iterator)
          2. Strategy 2 to set data(file)
          3. Generate data
          4. Remove data
          5. Remove data in range
          6. Get count of unique elems (task)
          7. Show list
          0. Exit""")

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
