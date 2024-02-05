with open("text_file.txt", 'r') as file1, open("text_file2.txt", 'r') as file2:
    content1 = file1.read()
    content2 = file2.read()

    merged_content = content1 + '\n' + content2

with open("combined_file.txt", "w") as combined_file:
    combined_file.write(merged_content)

with open("combined_file.txt", "r") as combined_file:
    print(combined_file.read())
