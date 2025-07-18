print("\nSimple To Do in CLI - Task 2\n")
print("==============================")   

while True:
    #printing the entries from data.txt
    print("Your To Do List:")
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            print(f"{i+1}. {line.strip()}")
    print("\n")

    #printing the options for action
    print("Enter your choice\n1.Add\n2.delete")
    a = int(input("\n  -> "))

    if a == 1:
        task = input("Enter the task to add: ")
        with open("data.txt", "a") as file:
            file.write("\n" + task)
    if a == 2:
        task = input("Enter the task no. you want to delete: ")
        with open("data.txt", "r") as file:
            lines = file.readlines()
        with open("data.txt", "w") as file:
            for i,line in enumerate(lines):
                if i+1 != int(task):
                    file.write(line)

    print("==============================")   