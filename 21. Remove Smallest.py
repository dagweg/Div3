for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print("YES")
    else:
        i, j = 0, 1
        while i < j < len(arr):
            if abs(arr[i]-arr[j]) <= 1:
                if arr[i] < arr[j]:
                    arr.pop(i)
                else:
                    arr.pop(j)
            else:
                i += 1
                j += 1
        if len(arr) == 1:
            print("YES")
        else:
            print("NO")
