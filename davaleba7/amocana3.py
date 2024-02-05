def reverse_string(string):
    if string == "":
        return ""
    return reverse_string(string[1:]) + string[0]


print(reverse_string("Hello"))
