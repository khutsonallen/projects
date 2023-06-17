def triplefib(n):
    from matplotlib import pyplot as plt
    x = 1 #sets term's position in triple fibonacci sequence
    y = 0 #first term
    a = 0 #second term
    b = 1 #third term
    t = [x] #makes list for x-coordinates
    p = [y] #makes list for y-coordinates
    while x < n:
        print(a, "")
        x = x + 1
        y = a+b+y #sets next term to the three previous ones
        a = b
        b = y
        t.append(x)
        p.append(y)
    plt.plot(t,p)
    plt.xlabel('Position')
    plt.ylabel('Term')
    plt.title('Triple Termed Fibonacci Sequence')
    plt.show()
triplefib(10)
