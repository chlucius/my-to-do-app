FILEPATH = "todos.txt"

def getToDos(filepath=FILEPATH) :
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def writeToDos (toDos, filepath=FILEPATH) :
    with open(filepath, "w") as file:
        file.writelines(toDos)

if __name__ == "__main__" :
    print ("Hello")
    print (getToDos())