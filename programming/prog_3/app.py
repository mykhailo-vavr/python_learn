from programming.prog_3.mainClasses.hotel import Hotel
from programming.prog_3.supportClasses.collection import Collection
from programming.prog_3.supportClasses.validation import Validation

# use for input "C:/python_learn_lnu/programming/prog_3/data/testData.json"
# use for output "C:/python_learn_lnu/programming/prog_3/data/outputData.json"
# use to fill collection "C:/python_learn_lnu/programming/prog_3/data/data.json"

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

    def getIdAndPath(methodName):
        print(f"Id for {methodName}:")
        id = input()
        Validation.isInteger(id)
        id = int(id)
        Validation.isInRange(id, 0)
        return id

    def getPath(isInPath=False, isOutPath=False):
        inPath, outPath = "", ""
        if isInPath:
            print("Write path to input data:")
            inPath = input()
        if isOutPath:
            print("Write path to output data:")
            outPath = input()
        return inPath, outPath


    option = input()

    if option == '1':
        print("String for find:")
        str = input()
        collection.find(str)
    elif option == '2':
        print("Attribute for sort:")
        attr = input()
        collection.sort(attr)
    elif option == '3':
        id = getIdAndPath("delete")
        inPath, outPath = getPath()
        collection.delete(id, outPath)
    elif option == '4':
        inPath, outPath = getPath(True)
        collection.add(inPath, outPath)
    elif option == '5':
        id = getIdAndPath("change")
        inPath, outPath = getPath(True)
        collection.change(id, inPath, outPath)
    elif option == '6':
        collection.show()
    elif option == '0':
        exit()
    else:
        print("Choose correct option")
        start(collection)
    start(collection)


collection = Collection(Hotel)
path = "C:/python_learn_lnu/programming/prog_3/data/data.json"
collection.set_items_from_file(path)
start(collection)
