input_sentence = str(input("Enter a sentence: "))
# input_sentence = "The wind howled and howled all night long"
input_sentence_lower = input_sentence.lower()
input_sentence_list = input_sentence_lower.split()
input_sentence_dict = {}


def count_words(lst, dictionary):
    for item in lst:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary


print(count_words(input_sentence_list, input_sentence_dict))
