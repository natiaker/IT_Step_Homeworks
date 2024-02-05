with open("text_file.txt", "w") as file:
    for i in range(1, 1001):
        file.write(f"{i} ნომერი ხაზი\n")

with open("text_file.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        print(i)
    num_of_lines = len(lines)
    print(f"ხაზების რაოდენობა: {num_of_lines}")
