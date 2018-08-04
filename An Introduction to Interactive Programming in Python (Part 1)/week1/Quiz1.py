import math

def f(x):
    a = -5*x**5 + 69*x**2 - 47

    return a

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    fv = present_value*(1+rate_per_period)**periods

    return fv

def calculation(n,s):
    a = n*s**2/(4*math.tan(math.pi/n))

    return a

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

def project_to_distance(point_x,point_y,distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print(point_x * scale, point_y * scale)