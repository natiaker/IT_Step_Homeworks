lines = {
    2: 'მეორე',
    8: 'მერვე',
    10: 'მეათე',
    13: 'მეცამეტე',
    17: 'მეჩვიდმეტე'
}

with open("text_file2.txt", "w") as file:
    for i in range(1, 21):
        if i in lines:
            file.write(lines[i])
        file.write('\n')
