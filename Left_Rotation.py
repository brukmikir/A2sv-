
def rotateLeft(d, arr):
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]
