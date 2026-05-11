# new_member = input("Enter a new member:") 

# file = open("members.txt", "r")
# members = file.readlines()
# file.close()


# members.append("\n" + new_member) 

# file = open("members.txt", "w")
# file.writelines(members)
# file.close()

member = input("Add a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()