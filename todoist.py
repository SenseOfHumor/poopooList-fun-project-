"""
@author: Swapnil Deb
@date: 06/01/2024
This is a fun project 
"""

import math
import os
import random

class Todoist:

    def __init__(self):
        self.todoist = ["NUNKU"]

    def addTask(self, task: str) -> None:
        """Adds a task to the todoist list"""
        self.todoist.append(task)

    def removeTask(self, task: str) -> None:
        """Removes a task from the todoist list"""
        self.todoist.remove(task)

    def removeTaskAtIndex(self, index: int) -> None:
        """Removes a task from the todoist list at a given index"""
        self.todoist.pop(index)

    def printList(self) -> None:
        """Prints the todoist list"""
        print("INCOMPLETE TASKS:\n-----------------")
        count = 1
        for elem in self.todoist:
            print(count,": ",elem)
            count += 1

    def exit_app(self) -> None:
        """Exits the app"""
        print("Exiting the app")
        exit()


#input("Simple TodoList app\nselect an option:\n1. Add a task\n2. Remove a task\n3. Remove a task at a given index\n4. Print the list\n5. Exit\n")

# todoist = Todoist()
# actions = {
#     '1': lambda: todoist.addTask(input("Enter a task: ")),
#     '2': lambda: todoist.removeTask(input("Enter a task to remove: ")),
#     '3': lambda: todoist.removeTaskAtIndex(int(input("Enter an index to remove: "))),
#     '4': todoist.printList,
#     '5': todoist.exit_app,
# }

# while True:
#     choice = input("\nSimple TodoList app\n-------------------\n\n------------------\n|SELECT AN OPTION|\n------------------\n1. Add a task\n2. Remove a task\n3. Remove a task at a given index\n4. Print the list\n5. Exit\n\n")

#     action = actions.get(choice, lambda: print("------------------\n|INVALID CHOICE|\n----------------"))

#     action()
#     if choice == '5':
#         break






