from decimal import Decimal, getcontext


def eulernumber(d):
    dd = d
    n = 4
    while dd > 1:
        dd /= 8
        n += 1
    getcontext().prec = d+n
    x = Decimal(1)/Decimal(1 << n)
    eps = Decimal(1)/Decimal(1 << (1 + (10*d) / 3))
    term = x
    expsum = Decimal(1) + x
    m = 2
    while term > eps:
        term *= x / Decimal(m)
        m += 1
        expsum += term
    for k in range(n):
        expsum *= expsum
    getcontext().prec = d
    expsum += Decimal(0)
    return expsum


if __name__ == "__main__":
    for k in range(1, 6):
        print(k, eulernumber(4*k))

    for k in range(10, 13):
        print(k, eulernumber(4*k))
