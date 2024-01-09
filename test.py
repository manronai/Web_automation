#from numberofmembersfinder import checklinks
#ch = checklinks()
#c = ch.Link('https://www.facebook.com/profile.php?id=100028074671683')
#print(c)
import re
def vowelfinder(sentence):
    rs = r'[aeiouyAEIOUY]'
    r = sentence
    p = len(r) - 1
    for ii, i in enumerate(r):
        if i == ' ':
            #print(ii-1)
            #print(r[ii - 1])
            if re.match(rs, r[ii - 1]):
                va1 = True
                #print(va1)
                return va1
            else:
                pass
                #print(False)
    #print(p)
    #print(r[p])
    if re.match(rs, r[p]):
        va1 = True
        #print(va1)
        return va1
    else:
        pass
        #print(False)

#if vowelfinder('Ahmed Banu'):
    #print('female')