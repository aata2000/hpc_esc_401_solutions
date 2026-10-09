import matplotlib.pyplot as plt

threads = [1, 2, 4, 16, 64]

speedup_O0 = [1.00, 2.00, 3.98, 15.72, 26.82]
speedup_O3 = [4.60, 9.17, 17.91, 42.96, 32.04]

plt.plot(threads, speedup_O0, marker="o", label="-O0")
plt.plot(threads, speedup_O3, marker="o", label="-O3")

plt.xlabel("Number of threads")
plt.ylabel("Speedup relative to 1-thread -O0")
plt.title("OpenMP speedup")
plt.legend()
plt.grid()

plt.savefig("speedup.png", dpi=200)
