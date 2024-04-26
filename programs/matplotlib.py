from matplotlib import pyplot as plt

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.bar(a, b, width=0.5)
plt.plot(a, b)
plt.show()
