def get_average():
    with open("files/bonus11_data.txt", 'r') as file:
        data = file.readlines()
    return data

average = get_average()
print(average)
