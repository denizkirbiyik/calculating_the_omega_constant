import decimal

inf1 = int(input("What number should be substituted for infinity in the limit? : "))
iter1 = int(input("How many iterations of the algorithm do you want to compute? : "))
start = decimal.Decimal(0.5)

def e_def(inf):
    e = ((1+(1/decimal.Decimal(inf)))**inf);
    return e
euler = e_def(inf1)
def newton_raphson(guess):
    omega_f = euler**(-guess)
    return omega_f
def compf(in1, iter):
    omega_n = in1
    for i in range(iter):
        omega_n = newton_raphson(omega_n)
    return omega_n
print(compf(start, iter1))
