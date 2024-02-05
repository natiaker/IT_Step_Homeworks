import functools

lst = [-1, 2, 3, -4, 5, 7, -11]

# თუ სიიდან მარტო დადებითი რიცხვები უნდა დააბრუნოს, მაშინ:
positive_list = functools.reduce(lambda acc, x: acc + [x] if x > 0 else acc, lst, [])

# თუ სიიდან უნდა დააბრუნოს რიცხვის დადებითი მნიშვნელობები, მაშინ:
# positive_list = functools.reduce(lambda acc, x: acc + [x] if x > 0 else acc + [abs(x)], lst, [])

print(list(positive_list))
