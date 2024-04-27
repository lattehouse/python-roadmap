# if..elif..else
def main():
    a,b=2,5
    result = "b" if(a<b) else "a"
    print('the big value is ',result)
    if(a<b):
        print("a is less than b")
    elif(a==b):
        print("a is same as b")
    else:
        print("a is grater than b")

# switch

def SwitchCase(args):
    switcher = {
        0:'zero',
        1:'one',
        2:'two'
    }
    return switcher.get(args,'none')


if __name__ == "__main__":
    main()
    args = 1
    print(SwitchCase(args))

