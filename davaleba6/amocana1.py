input_str1 = str(input("input word: "))
input_str2 = str(input("input word: "))


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = str1.lower()
    str2 = str2.lower()
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    print(sorted_str1, sorted_str2)

    if sorted_str1 == sorted_str2:
        return True
    else:
        return False


result = is_anagram(input_str1, input_str2)
print(f"Is anagram: {result}")
