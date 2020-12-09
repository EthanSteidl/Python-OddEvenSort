def oddEvenSort(a):
    sorted = False
    while (sorted==False):
        sorted = True
        for i in range(1, len(a)-1, 2):
            if(a[i+1] < a[i]):
                a[i], a[i+1] = a[i+1],a[i]
                sorted = False
        for i in range(0, len(a)-1, 2):
            if(a[i+1] < a[i]):
                a[i], a[i+1] = a[i+1],a[i]
                sorted = False