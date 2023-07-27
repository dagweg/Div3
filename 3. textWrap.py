# Time: 3 mins

import textwrap

def wrap(string, max_width):
    ret = ''
    for i in range(len(string)):
        ret = ret + string[i]
        if (i+1) % max_width == 0:
            ret = ret + '\n'
        
    return ret

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
