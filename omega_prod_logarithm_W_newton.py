import decimal

inf1 = int(input("What number should be substituted for infinity in the limit? : "))
iter1 = int(input("How many iterations of the algorithm do you want to compute? : "))
start = decimal.Decimal(0.5)

def e_def(inf):
    e = ((1+(1/decimal.Decimal(inf)))**inf);
    return e
euler = e_def(inf1)

def newton_raphson(w):
    f = w - ((w*(euler**w))-decimal.Decimal(1))/((euler**w)*(w+1))
    return f
def lambert(guess, iter):
    out1 = guess
    for i in range(iter):
        out1 = newton_raphson(out1)
    return out1

print(lambert(start, iter1))

