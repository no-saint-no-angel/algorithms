
def area(k, b):
    b_static = b
    def mid_x(k, x1, x2):
        x = (x1+x2)/2
        y1 = x**k - b_static+x
        if abs(y1) < (10**(-6))/(2*b_static):
            return x
        else:
            if y1 < 0:
                x1 = x
            else:
                x2 = (x+x2)/2
            return mid_x(k, x1, x2)
    x = mid_x(k, 0, b_static)
    area = (1/(k+1))*x**(k+1) + ((1/2)*b_static**2)-((-1/2)*x**2+b_static*x)
    area = format(area, '.10f')
    return area

print(area(6, 4))


