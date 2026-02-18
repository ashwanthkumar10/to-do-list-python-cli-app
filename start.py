import json

task_storage = {"name" : ""}


while(True):
    get_task_item_input = int(input(" === Todo List Application === \n 1. Add Todo \n 2. View All Todos \n 3. Mark Todo as Complete \n 4. Delete Todo \n 5. Exit \n Enter your choice : "))
    if get_task_item_input == 1:
        get_task_item = input("Enter Task Description : ")
        task_storage["name"] = get_task_item;
        print(task_storage)
        with open('todo.json', 'w') as json_file:
            json.dump(task_storage, json_file)
    elif get_task_item_input == 5:
        exit()
    else:
        print("let's stop this here \n ")
    







