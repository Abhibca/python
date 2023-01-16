'''
    1.hash table
        linear probing
    2.dictionary
        create
        display key
        display value
    3.fibonnaci
    4.print sereis 1,4,9.......n
    5.exit

'''
def hashtable():
    pass
def dictionary():
    d = {}
    n = int(input('How many dictionary do you want to enter : '))
    for i in range(0,n):
        key = input('Enter Key : ')
        value = input('Enter Value : ')
        d.update({key:value})
    print(d)
    print('keys = ',d.keys())
    print('value = ',d.values())
    
def fibonnaci():
    pass
def series():
    pass


while(1):
    print('1.Hash Table')
    print('2.Dictionary')
    print('3.Fibonnaci')
    print('4.Series')
    print('0.Exit')
    ch=input('Enter Your Choice(0 t0 4) : ')

    if ch=='1':
        hashtable()
    elif ch=='2':
        dictionary()
    elif ch=='3':
        fibonnaci()
    elif ch=='4':
        series()
    elif ch=='0':
        break

    print('= = = = = = = = = = = = = = = = =')

