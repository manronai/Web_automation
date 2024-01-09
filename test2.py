import re
def fun1():
    i = 0
    yy = open('femaless.txt', 'w')
    ii = r'http'
    for y in open('female.txt'):
        i = i + 1
        rrr = re.match(ii, y)
        # y = y.replace('', '')
        # y = y.replace('', '')
        if not rrr:
            print('w')
        else:
            print(y)
            yy.write(y)

    print(i)
def fun2():
    ii = open('mylinks.txt')
    for i, m in enumerate(ii):
        print(i)
        print(m)
fun2()