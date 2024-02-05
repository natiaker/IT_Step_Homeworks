lst = ["moon", "rotator", "duck", "noon", "wow", "word"]

isPalindrome = list(filter(lambda txt: txt == txt[::-1], lst))
print(isPalindrome)
