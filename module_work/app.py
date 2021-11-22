from VaccinationPointRequest import VaccinationPointRequest
from Collection import Collection
from FuncForOpts import FuncForOptions

# use for output "C:\python_learn_lnu\module_work\output.json"
# use to fill collection "C:\python_learn_lnu\module_work\input.json"


def options(option, collection):
    functions = FuncForOptions(collection)
    return {
        "1": functions.f1,
        "2": functions.f2,
        "3": functions.f3,
        "0": functions.f0,
    }.get(option)


def start(collection):
    print("""
Choose the option:
    1. Show collection
    2. Show hour with the largest number of orders
    3. Write to file point with the largest number of orders
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


if __name__ == "__main__":
    path = "C:\python_learn_lnu\module_work\input.json"
    collection = Collection(VaccinationPointRequest, path)

    start(collection)