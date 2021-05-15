import numpy, sys, time
import matplotlib.pyplot as plt

if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

# upper limit on the horizontal axis
N = int(sys.argv[1])

# list of execution time / vertical axis of the graph
times = []

# n: size of matrix
for n in range(N) :
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    # matrix calculation
    for i in range(n) :
      for j in range(n) :
        for k in range(n):
          c[i, j] += a[i, k] * b[k, j]

    end = time.time()
    times.append(end - begin)
    
    print("time: %.6f sec" % (end - begin))

# horizontal axis of the graph
n_list = list(range(N))

plt.plot(n_list, times)
plt.xlabel("size of square matrix")
plt.ylabel("time(s)")
plt.show()
