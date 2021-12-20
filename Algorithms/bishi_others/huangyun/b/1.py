def foo(x):
    def bar():
        return x+1
    return bar()

if __name__ == '__main__':
    for i in range(3):
        print(i, foo(i))

        fee = [1, 2, 3, 4, 5, 6, 7]
        print([fee[i] for i in [6,4,2,0]])
        print(fee[:4])