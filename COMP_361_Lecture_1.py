from numpy import zeros, shape, array, dot
def product(a, b):
    n, p1 = shape(a)
    p2, m = shape(b)
    assert(p1 == p2)
    c = zeros((n, m))
    for i in range(n):
        for j in range(m):
            c[i, j] = dot(a[i],b[:, j])
            return c

a = array([[1, 2, 3],[4, 5, 6]])
b = array([[1,2],[4,5],[7,8]])

c = product(a, b)

print(c)


