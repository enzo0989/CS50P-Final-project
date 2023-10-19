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
        action(create(args.create))
    elif args.load:
        action(load(args.load))


# Used in the beginning of the program 

def create(name):
    with open(name + ".csv", "w") as file_list:
        #creates the needed keys for the csv file#
        key_writer = csv.writer(file_list)
        key_writer.writerow(["task","date", "state"])
    return file_list.name 
        
def load(filename):
    try:
        with open(filename, "r") as loaded_list:
            return loaded_list.name 
    except FileNotFoundError:
        sys.exit("The file that you are trying to load doesn't exist.")        
            #-----#

def action(list):
    show_actions()
    while True:
        try:
            prompt = input("\naction: ")
            match prompt:
                case "add":
                    add(list) 
                case "mod":
                    modify(list)
                case "del":
                    delete(list)
                case "state":
                    state(list)
                case "view":
                    view(list)
                case "act":
                    show_actions()
                case "exit":
                    sys.exit("\nYour file will be saved to load it later.\nHave a good day :)")
                case _:
                    pass
        except EOFError:
            break


def add(file):
    with open(file, "a") as task_add:
        while True:
            try:
                task = input("New Task: ")
                date = input("Date to complete it(DD-MM-YYYY): ")

                if task_validation(task) and date_validation(date):
                    writer = csv.DictWriter(task_add, fieldnames=["task", "date", "state"])
                    writer.writerow({"task": task,"date": date, "state": "unfinished"})
                    return True
                else:
                    raise ValueError()
                
            except ValueError:
                print("\nNot a valid date or task.\nTask: Letters and numbers only. \nDate: DD-MM-YYYY format and greater than 2022. \n")
                return False
                

def modify(list):
    try:
        df = pd.read_csv(list)
        num_mod = int(input("Number of the task you want to modify: "))
        
        if number_validation(df,num_mod):
            new_task = input("new task: ")
            if task_validation(new_task):
                # Replaces the task in num_mod position in the task column with a new task. 
                # e.g if num_mod is equal to 1, the task N°1 will be replaces with the value of new_task.
                df.loc[num_mod,"task"] = new_task
                df.to_csv(list, index=False)
                return True
            else:
                print("\nThe task is not valid.\nTask: Letters and numbers only.\n")
                raise ValueError()
        else:
            print("\nThe task has to exist.") 
            raise ValueError()

    except ValueError:
        return False


def delete(list):
    while True:
        try:
            del_num = int(input("Number of the task you want to delete: "))
            df = pd.read_csv(list)

            if number_validation(df,del_num):
                # Uses del_num as an index and deletes the entire row in that position. e.g del_num = 2, all the content in the row N°2 gets deleted.
                df = df.drop(df.index[del_num])
                df.to_csv(list, index=False)
                print("\nTask deleted successfully!")
                return True
            else:
                raise ValueError()
        except ValueError:
            print("\nThe task has to exist.\n")
            pass


def view(list):
    view_list = []
    with open(list, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            view_list.append({"task":row["task"],"date": row["date"], "state": row["state"]})
    print("\n")
    print(tabulate(view_list, tablefmt="fancy_grid", headers="keys", showindex="always"),"\n")


def state(list):
    while True:
        try:
            df = pd.read_csv(list)
            num_state = int(input("Number of the task you completed: "))
            
            if number_validation(df,num_state):
                # Uses num_state as an index and sets that row state value to finished.    
                df.loc[num_state,"state"] = "finished"
                df.to_csv(list, index=False)
                print("\nState changed successfully!")
                return True
            else:
                raise ValueError()

        except ValueError:
            print("\nThe task has to exist. \n")
            pass


def show_actions():
    action_list = {"actions": ["add","mod","del","state","view","act","exit"], 
                    "result": ["Creates a new task with a date and a state.","Modifies a task.", "Deletes a task.", "Marks a task as completed.",
                                "Shows the current list.","Shows all the possible actions.","Saves the list and exists the program."]}
    
    print("\n")
    print(tabulate(action_list, tablefmt="fancy_grid", headers="keys"))


# Functions created because their content repeated in multiple parts of the project.

def task_validation(string):
    task_pattern = r"^[a-zA-Z0-9 ]*$"
    if re.match(task_pattern,string):
        return True

def date_validation(date):
    date_pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-(20)[2-9]\d$"
    if re.match(date_pattern,date):
        return True

def number_validation(df,n):
    if n > len(df) - 1 or n < 0:
        return False
    else:
        return True
    

if __name__ == "__main__":
    main()