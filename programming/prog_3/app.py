from programming.prog_3.mainClasses.hotel import Hotel
from programming.prog_3.supportClasses.collection import Collection
from programming.prog_3.supportClasses.funcForOptions import FuncForOptions


# use for input "C:/python_learn_lnu/programming/prog_3/data/testData.json"
# use for output "C:/python_learn_lnu/programming/prog_3/data/outputData.json"
# use to fill collection "C:/python_learn_lnu/programming/prog_3/data/data.json"


def options(option, collection):
    functions = FuncForOptions(collection)
    return {
        "1": functions.f1,
        "2": functions.f2,
        "3": functions.f3,
        "4": functions.f4,
        "5": functions.f5,
        "6": functions.f6,
        "0": functions.f7,
    }.get(option)


def start(collection):
    print("""Choose the option:
    1. Find data in collection
    2. Sort collection
    3. Delete item in collection
    4. Add item in collection
    5. Set new values to item
    6. Show collection
    0. Exit
    """)

    option = input()
    method = options(option, collection)
    if method:
        method()
    else:
        print("Choose correct option")
        start(collection)
    start(collection)


collection = Collection(Hotel)
path = "C:/python_learn_lnu/programming/prog_3/data/data.json"
collection.set_items_from_file(path)
start(collection)
