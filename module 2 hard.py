while True:
    results = []
    n = int(input())
    for i in range(1, 21):
        for k in range(1, 21):
            j = i + k
            if n % j == 0 and i < k:
                results.append(i)
                results.append(k)
            elif n >= 21:
                break

    print(results)







