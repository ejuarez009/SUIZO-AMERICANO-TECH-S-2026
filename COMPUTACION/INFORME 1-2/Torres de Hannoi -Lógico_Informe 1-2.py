def hannoi(a, b, c, n: int):
    if n == 1:
        print(f"Mover: {a}, hacia: {c}")
    else:
        hannoi(a, c, b, n - 1)
        hannoi(a, b, c, 1)
        hannoi(b, a, c, n - 1)


hannoi("t1", "t2", "t3", 3)
