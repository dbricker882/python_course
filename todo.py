###############################################
# Day 1
###############################################

# user_prompt = "Enter a todo:"

# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3]

# print(todos)
# print(type(todo1)) 

###############################################
# Day 2
###############################################

# user_prompt = "Enter a todo:"

# todos = []

# while True:
#     todo = input(user_prompt)
#     print(todo.capitalize())
#     todos.append(todo)

# ###############################################
# # Day 3
# ###############################################

# todos = []

# while True:
#     user_action = input("Type add, show, or exit:")
#     user_action = user_action.strip()
    
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ")
#             todos.append(todo.capitalize())
#         case "show" | "display":
#             for item in todos:
#                 print(item)
#         case "exit":
#             break

###############################################
# Day 4
###############################################

# todos = []

# while True:
#     user_action = input("Type add, show, edit, or exit:")
#     user_action = user_action.strip()
    
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ")
#             todos.append(todo.capitalize())
#         case "show" | "display":
#             for item in todos:
#                 print(item)
#         case "edit":
#             for item in todos:
#                 print(item)
#             number = int(input("Number of the todo to edit: "))
#             new_todo = input("Enter new todo: ")
#             todos[number-1] = new_todo.capitalize()
#             for item in todos:
#                 print(item)
#         case "exit":
#             break
        
###############################################
# Day 5
###############################################

# todos = []

# while True:
#     user_action = input("Type add, show, edit, complete or exit:")
#     user_action = user_action.strip()
    
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ")
#             todos.append(todo.capitalize())
#         case "show" | "display":
#             for index, item in enumerate(todos):
#                 row = f"{index + 1}-{item}"
#                 print(row)
#         case "edit":
#             number = int(input("Number of the todo to edit: "))
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo.capitalize()
#         case "complete":
#             number = int(input("Number of the todo to complete: "))
#             number = number - 1
#             todos.pop(number)
#         case "exit":
#             break
        
# Day 5 Bonus

# waiting_list = ["ben", "sen", "john"]
# waiting_list.sort()

# for index, item in enumerate(waiting_list):
#     row = f"{index + 1}.{item.capitalize()}"
#     print(row)

###############################################
# Day 6
###############################################
# file = open("todos.txt", "r")
# todos = file.readlines()
# file.close()
        
# while True:
#     user_action = input("Type add, show, edit, complete or exit:")
#     user_action = user_action.strip()
    
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ") + "\n"
            
#             todos.append(todo.capitalize())
            
#             file = open("todos.txt", "w")
#             file.writelines(todos)
#             file.close()
#         case "show" | "display":
#             for index, item in enumerate(todos):
#                 row = f"{index + 1}-{item}"
#                 print(row)
#         case "edit":
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1
#             new_todo = input("Enter new todo: ") + "\n"
#             todos[number] = new_todo.capitalize()
#         case "complete":
#             number = int(input("Number of the todo to complete: "))
#             number = number - 1
#             todos.pop(number)
#         case "exit":
#             break

###############################################
# Day 7
###############################################
# file = open("todos.txt", "r")
# todos = file.readlines()
# file.close()
        
# while True:
#     user_action = input("Type add, show, edit, complete or exit:")
#     user_action = user_action.strip()
    
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ") + "\n"
            
#             todos.append(todo.capitalize())
            
#             file = open("todos.txt", "w")
#             file.writelines(todos)
#             file.close()
#         case "show" | "display":
#             for index, item in enumerate(todos):
#                 item = item.strip('\n')
#                 row = f"{index + 1}-{item}"
#                 print(row)
#         case "edit":
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1
#             new_todo = input("Enter new todo: ") + "\n"
#             todos[number] = new_todo.capitalize()
#         case "complete":
#             number = int(input("Number of the todo to complete: "))
#             number = number - 1
#             todos.pop(number)
#         case "exit":
#             break


###############################################
# Day 8
###############################################
# with open('todos.txt' , 'r') as file:
#     todos = file.readlines()
        
# while True:
#     user_action = input("Type add, show, edit, complete or exit:")
#     user_action = user_action.strip()
    
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ") + '\n'
            
#             todos.append(todo.capitalize())
            
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)

#         case "show" | "display":
#             for index, item in enumerate(todos):
#                 item = item.strip('\n')
#                 row = f"{index + 1}-{item}"
#                 print(row)

#         case "edit":
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1
#             new_todo = input("Enter new todo: ") + '\n'
#             todos[number] = new_todo.capitalize()

#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)

#         case "complete":
#             number = int(input("Number of the todo to complete: "))
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)

#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)

#             message = f"Todo {todo_to_remove} was removed from the list."
#             print(message)

#         case "exit":
#             break

###############################################
# Day 9
###############################################
# with open('todos.txt' , 'r') as file:
#     todos = file.readlines()
        
# while True:
#     user_action = input("Type add, show, edit, complete or exit:")
#     user_action = user_action.strip()
    

#     if "add" in user_action:
#         todo = user_action[4:]
        
#         todos.append(todo.capitalize())
        
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)

#     elif "show" in user_action or "display" in user_action:
#         for index, item in enumerate(todos):
#             item = item.strip('\n')
#             row = f"{index + 1}-{item}"
#             print(row)

#     elif "edit" in user_action:
#         number = int(user_action[5:])
#         number = number - 1
#         new_todo = input("Enter new todo: ") + '\n'
#         todos[number] = new_todo.capitalize()

#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)

#     elif "complete" in user_action:
#         number = number = int(user_action[9:])
#         index = number - 1
#         todo_to_remove = todos[index].strip('\n')
#         todos.pop(index)

#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)

#         message = f"Todo {todo_to_remove} was removed from the list."
#         print(message)

#     elif "exit" in user_action:
#         break
#     else:
#         print("Command is not valid.")

###############################################
# Day 10
###############################################
with open('todos.txt' , 'r') as file:
    todos = file.readlines()
        
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    

    if user_action.startswith('add'):
        todo = user_action[4:]
        
        todos.append(todo.capitalize() + '\n')
        
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ") + '\n'
            todos[number] = new_todo.capitalize()

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
        continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")