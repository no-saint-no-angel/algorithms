
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving %s" % a + " from %s" % c)
        hanoi(n-1, b, a, c)

num = hanoi(3, "A", "B", "C")