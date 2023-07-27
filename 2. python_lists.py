# Time : 5 minutes
def main(N):
    lst = []
    for i in range(N):
        line = input().split()
        command = line[0]        
        
        if len(line) == 2:
            line[1] = int(line[1])
        elif len(line) == 3:
            line[1] = int(line[1])
            line[2] = int(line[2])
        
        if command == 'insert':
            lst.insert(line[1],line[2])
        elif command == 'print':
            print(lst)
        elif command == 'remove':
            lst.remove(line[1])
        elif command == 'append':
            lst.append(line[1])
        elif command == 'sort':
            lst.sort()
        elif command == 'pop':
            lst.pop()
        elif command == 'reverse':
            lst.reverse()
        

if __name__ == '__main__':
    N = int(input())
    main(N)
