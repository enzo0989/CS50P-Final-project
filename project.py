import argparse, sys, csv

def main():
    # Initialization of the program, it let's you pick either to load a previous list or to create a new one.
    parser = argparse.ArgumentParser(description="Creates a Todo list to achieve your goals.")

    parser.add_argument("--load", metavar="load", type=str, help="Recreates an old list. The file must have been made using this program and have the CSV extension.")
    parser.add_argument("--create", metavar="create", type=str, help="Creates a new list. It must come with a name for the list. e.g tasks for the week.")
    args = parser.parse_args()


    if args.create:
        print(load(args.create))
    elif args.load:
        print(load(args.load))
    else:
        print("not a valid action")


def create(name):
    
    return f"{name}"

def load(filename):
    # Non essential in this point of the project.
    return f"{filename}"



def action(list):
    int = 0
    while True:
        try:
            action = input("action: ")

            if action == "-add":
                i += 1
                add()
            elif action == "-mod":
                i += 1
                modify()
            elif action == "-del":
                delete()
        except EOFError:
            ...
            # Ask if the user wants to save the list:
            #   if the user writes Y save the file, 
            #   else if the user writes N don't save it.
            #   else prompt again.
            # break the loop.

def add(task, date):
    ...
def modify(number):
    ...

def delete(number):
    ...


if __name__ == "__main__":
    main()