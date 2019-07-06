pi = 3.14

def circle(r):
    return pi*r**2

def square(a):
    return a**2

def rectangle(a, b):
    return a*b

def triange(b,h):
    return b*h*0.5

if __name__ == '__main__':
    import sys
    args = sys.argv
    if args[1] == 'circle':
        print(circle(int(args[2])))
    elif args[1] == 'square':
        print(square(int(args[2])))
