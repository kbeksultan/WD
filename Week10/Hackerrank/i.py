if __name__ == '__main__':

    n = int(input())
    
    arr = [int(x) for x in input().split()]

    maxi = max(arr)

    for i in sorted(arr)[::-1]:
        if i != maxi:
            print(i)
            break
