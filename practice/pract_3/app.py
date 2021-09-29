from linkedList import LinkedList
from validation import Validation

def start(list):
    print("""Choose the option:
          1. Get data from keyboard
          2. Generate an data in range [a, b]
          3. Insert data
          4. Remove data
          5. Get count of unique elems (task)
          6. Show list
          7. Exit""")

    def getInt(message, isPositive=True):
        print(message)
        value = input()
        Validation.isInteger(value)
        value = int(value)
        if isPositive:
            Validation.isInRange(value, 0)
        return int(value)

    option = input()

    if option == "1":
        count = getInt("Count of new items:")
        list.getDataFromKeyboard(count)
    elif option == "2":
        count = getInt("Count of new items:")
        a = getInt("First limit:", False)
        b = getInt("Second limit:", False)
        list.generateDataInRange(a,b,count)
    elif option == "3":
        index = getInt("Index of elem to insert")
        print("Data to insert")
        data = input()
        list.insert(data, index)
    elif option == "4":
        index = getInt("Index of elem to remove")
        list.remove(index)
    elif option == "5":
        print(list.getCountOfUniqieElems())
    elif option == "6":
        list.show()
    elif option == "7":
        exit()
    else:
        print("Choose correct option")
        start(list)
    start(list)

list = LinkedList()
start(list)


# list.getDataFromKeyboard(3)
# list.show()