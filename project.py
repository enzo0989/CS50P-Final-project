import argparse, sys
import csv, re
import pandas as pd
from tabulate import tabulate

def main():
    # Initialization of the program, it let's you pick either to load a previous list or to create a new one.
    parser = argparse.ArgumentParser(description="Creates a Todo list to achieve your goals.")

    parser.add_argument("--create", metavar="create", type=str, help="Creates a new list. It must come with a name for the list. e.g tasks for the week.")
    parser.add_argument("--load", metavar="load", type=str, 
                        help="Loads a list. The file loaded must be inside the project directory and must have been made with this program.")

    args = parser.parse_args()


    if args.create:
        create()
    elif args.load:
        load(args.load)

def create():
        with open("TodoList.csv", "w") as file_list:
            key_writer = csv.writer(file_list)
            key_writer.writerow(["N°","task","date"])
        action(file_list.name)
        
def load(filename): 
    ...

def action(list):
    i = 0
    while True:
        try:
            prompt = input("What kind of action do you want to perform?: ")
            if prompt == "add":
                # i is used to enumerate the tasks. 
                i += 1
                add(i,list)
            elif prompt == "modify":
                modify(list)
            elif prompt == "delete":
                delete(list)
            elif prompt == "view":
                view(list)
            else:
                pass

        except EOFError:
            break


def add(n,file):
    with open(file, "a") as task_add:
        task = input("What task do you want to add?: ")
        date = input("by which day do you think you should finish this task?: ")

        writer = csv.DictWriter(task_add, fieldnames=["N°","task", "date"])
        writer.writerow({"N°": n,"task": task,"date": date})

    

def modify(list):
    old_task = int(input("Number of the task you want to modify: ")) - 1
    new_task = input("new task: ")
    
    df = pd.read_csv(list)
    df.loc[old_task,"task"] = new_task
    df.to_csv(list, index=False)

def delete(list):
    ...

def view(list):
    view_list = []
    with open(list, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            view_list.append({"N°":row["N°"],"task":row["task"],"date": row["date"]})
    print(tabulate(view_list, tablefmt="heavy_grid" ,headers="keys"))


if __name__ == "__main__":
    main()