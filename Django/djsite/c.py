def abd():
    a =  None
    print('in abd() a', id(a), ' ', a)
    def sss():
        z = 1
        print("in sss() z", id(z))
        nonlocal a = 110
        print("in sss() a", id(a))
    sss()
    print('exec sss()', id(a), ' ', a)
abd()