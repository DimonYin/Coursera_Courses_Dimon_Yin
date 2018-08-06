
count = 0

def square(x):
    global count
    count += 1
    print(count)
    return x**2

print (square(square(square(square(3)))))