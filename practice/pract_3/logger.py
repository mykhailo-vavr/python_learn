class Logger():
    @staticmethod
    def printToFile(path, items):
        try:
            # "a" to add changes
            with open(path, "w") as file:
                file.write(str(items))
        except:
            return -1
