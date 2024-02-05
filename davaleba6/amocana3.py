n_count = int(input("შეიყვანეთ რიცხვი: "))

if n_count <= 0:
    n_count = int(input("შეიყვანეთ მხოლოდ დადებითი რიცხვი: "))


def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a)
        c = a + b
        a = b
        b = c


fibonacci(n_count)
