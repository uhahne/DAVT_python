import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, x_i, y_i):
    n = len(x_i)
    m = len(x)
    y = np.zeros(m)
    for i in range(n):
        p = lagrange_polynomial(i, x, x_i)
        y += y_i[i] * p
    return y

def lagrange_polynomial(j, x, x_i):
    n = len(x_i)
    p = 1
    for m in range(n):
        if m != j:
            p *= (x - x_i[m]) / (x_i[j] - x_i[m])
    return p

# test data
data = [2,4,3,1]
support = [0,1,2,3]
test_support = np.array([4, 5])

data = [2,1,0,2]
support = [0,3,4,5]
test_support = np.array([1,2])

# compute Lagrange polynomial
n = 256
x = np.linspace(-0.2,5.2,n,endpoint=True)
y = lagrange(x, support, data)
#l_0 = lagrange_polynomial(0, x, support)
#l_1 = lagrange_polynomial(1, x, support)
#l_2 = lagrange_polynomial(2, x, support)
#l_3 = lagrange_polynomial(3, x, support)

# setup plot with axes
fig, ax = plt.subplots( nrows=1, ncols=1 )
ax.plot (x, y, color='blue', alpha=1.00)
ax.axhline(1, color='black',linewidth=0.5)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)

# plot Lagrange polynomials
#ax.plot (x, l_0, color='yellow', alpha=1.00)
#ax.plot (x, l_1, color='orange', alpha=1.00)
#ax.plot (x, l_2, color='green', alpha=1.00)
#ax.plot (x, l_3, color='darkgreen', alpha=1.00)

# plot data points
ax.scatter(support, data, color='orange', zorder=5)

# compute and plot data points for x=4 and x=5
xx = test_support
yy = lagrange(xx, support, data)
ax.scatter(xx, yy, color='red', zorder=5)

plt.show()
fig.savefig('foo.png', bbox_inches='tight')
