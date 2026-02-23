import json
import os
import datetime
filename = "todo.json"



while(True):
    get_task_item_input = int(input(" === Todo List Application === \n 1. Add Todo \n 2. View All Todos \n 3. Mark Todo as Complete \n 4. Delete Todo \n 5. Exit \n Enter your choice : "))
    if(os.path.exists(filename)):
        with open(filename , "r") as file:
            data=json.load(file)
    else:
        data= []
    if get_task_item_input == 1:
        get_task_item = input("Enter Task Description : ")
        storing_dict = {
            "id" : 0 , 
            "task": "",
            "status" : "",
            "created_at" : ""
        }
        data_length = len(data)
        if data_length==0:
            last_item_in_list = 0
        else:    
            last_item_in_list = data[-1]["id"]
        storing_dict["id"] = last_item_in_list + 1  
        storing_dict["task"] = get_task_item
        storing_dict["status"] = "pending"
        created_at = datetime.datetime.now()
        converted_data_time = created_at.strftime("%d/%m/%Y %H:%M:%S")
        storing_dict["created_at"] = converted_data_time
        data.append(storing_dict)
        print(f"To do added suucessfully! ID : {storing_dict["id"]})" )
        with open('todo.json', 'w') as json_file:
            json.dump(data, json_file)
    if get_task_item_input == 2:
        completed_status = []
        pending_status = []
        for item in data:
            status = item["status"]
            if status=="pending":
                completed_status.append(item)
            else:
                pending_status.append(item)    

        for item in completed_status:
            print("[",item["id"] , "]" , item["task"] , "(" ,item["created_at"],")")
        for item in pending_status:
            print("[",item["id"] , "]" , item["task"] , "(" ,item["created_at"],")")

    if get_task_item_input == 3:
        get_id_to_mark_as_complete = int(input("Enter todo ID to mark as complete: "))
        for item in data:
            inserted_id = item["id"]
            if inserted_id == get_id_to_mark_as_complete:
                item["status"] = "completed"
            else:
                continue     
        with open('todo.json', 'w') as json_file:
            json.dump(data, json_file)
    if get_task_item_input == 4:
        get_id_to_delete = int(input("Enter todo ID to delete : "))
        for index , item  in enumerate(data):
            inserted_id = item["id"] # 1 
            if inserted_id not in data:
                print("Item not found ,Please enter another element")
                break
            if inserted_id == get_id_to_delete:
                data.pop(index)
                print(f"Task with ID: {inserted_id} deleted")
            else:
                continue    
        with open('todo.json', 'w') as json_file:
            json.dump(data, json_file)                      
    elif get_task_item_input == 5:  
        exit()







