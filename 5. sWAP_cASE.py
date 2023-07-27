# Time : 5 min
def swap_case(s):
    ret = ''
    for i in range(len(s)):
        if s[i].islower(): 
            ret = ret + s[i].upper()
        else:
            ret = ret + s[i].lower()            
    return ret

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
