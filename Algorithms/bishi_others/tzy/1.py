

def getstr(comand):
    nums = len(comand)
    str = []
    for i in range(int(nums/2)):
        tmp = comand[2*i]*int(comand[2*i+1])
        str.extend(tmp)
    return ''.join(str)

if __name__ == '__main__':

    a = "A3B5c2"
    print(getstr(a))