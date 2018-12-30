
def reverse(a,b,c):
    return c,b,a


def odd(num):
    result=[]
    for i in num:
        if(i%2==1):
            result.append(i)
    return result

def even(num):
    result=[]
    for i in num:
        if(i%2==0):
            result.append(i)
    return result