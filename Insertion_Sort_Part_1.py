def insertionSort1(n, arr):
    val = arr[-1]
    
    for i in range(len(arr) - 1, 0, -1):
        if val < arr[i - 1]:
            arr[i] = arr[i - 1]
            print(*arr)
        else:
            arr[i] = val
            print(*arr)  
            break
    else:
        arr[0] = val
        print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
