def fibonacci():
    i = 0
    j = 1
    n = int(input("Enter the range : "))
    next = 0
    print(i)
    print(j)
    for a in range(n):
        next = i + j
        print(next)
        i = j
        j = next
        

fibonacci()