import numpy, sys, time
import matplotlib.pyplot as plt

if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

# 横軸の上限
N = int(sys.argv[1])

# 実行時間のリスト / 縦軸
times = []

# n×nの行列積の計算
for n in range(N) :
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C
    
    # ALEX_COMMENT: given you used = numpy.zeros() above,
    #               do you need to initialize c below?
    #         Other than that, it all looks good!

    # 行列の初期化
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    # 行列の計算
    for i in range(n) :
      for j in range(n) :
        for k in range(n):
          c[i, j] += a[i, k] * b[k, j]

    end = time.time()
    times.append(end - begin)


# horizontal axis of the graph
n_list = list(range(N))

plt.scatter(n_list, times)

plt.xlabel("size of square matrix")
plt.ylabel("time(s)")
plt.savefig("HW1.png")
