

def meeting_id(str1):
    str_ = str(str1).split('/')
    meeting_id_yes = False
    for _cha in str_:
        if _cha == 'zoom.us' or _cha == 'zoomgov.com':
            meeting_id_yes = True
    if meeting_id_yes == True:
        for _cha1 in str_:
            if len(_cha1)>=9 and len(_cha1)<=11:
                    return _cha1
    else:
        return 0

# line = list(map(list, input().strip().split()))

# line = '23-23+34-34-34'
# line = str(line)
line = input().strip()
str_ = str(line).strip().split('+')


def minur_num(str_):
    if len(str_)>2:
        str_first = str(str_).strip().split('-')
        num_first = int(str_first[0])
        for j in range(1,len(str_first)):
            num_first -= int(str_first[j])
    else:
        num_first = int(str_)
    return num_first
sum = 0
for i in range(len(str_)):
    sum += minur_num(str_[i])

print(sum)
