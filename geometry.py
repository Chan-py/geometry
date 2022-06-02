import matplotlib.pyplot as plt
import numpy as np
x1 = [0]
y1 = [0]
x2 = [0]
y2 = [0]
print('A벡터 값을 입력하세요 (x값과 y값 모두 자연수여야 함')
a, b = map(int, input().split())
x1.append(a)
y1.append(b)
print('B벡터 값을 입력하세요 (x값과 y값 모두 자연수여야 함')
c, d = map(int, input().split())
x2.append(c)
y2.append(d)
mx = max(x1[1], y1[1], x2[1], y2[1]) * 11/10
plt.axis([0, mx, 0, mx])
plt.gca().set_aspect('equal', adjustable = 'box')
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.legend(['A vector', 'B vector'])
plt.grid()
def Getpowlen(x, y):
  return x**2 + y**2
if Getpowlen(x1[1], y1[1]) <= Getpowlen(x2[1], y2[1]):
  first = (x1[1], y1[1])
  second = (x2[1], y2[1])
else:
  first = (x2[1], y2[1])
  second = (x1[1], y1[1])
m = (-1) * second[0]/second[1] if second[1] != 0 else 0
meetx = (m*first[0] - first[1]) / (m + 1/m)
meety = meetx * (-1/m)
if first[0] < meetx:
  x3 = np.arange(first[0], meetx + 0.01, 0.01)
else:
  x3 = np.arange(meetx, first[0] + 0.01, 0.1)
n = first[1] - (m*first[0])
y3 = [(m*num + n) for num in x3]
plt.axis([0, mx, 0, mx])
plt.gca().set_aspect('equal', adjustable = 'box')
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.legend(['A vector', 'B vector'])
plt.scatter(meetx, meety, c = 'm')
plt.grid()
print('계산을 통해 구한 내적값은 {}이다.'.format(x1[1] * x2[1] + y1[1] * y2[1]))
A_vec = Getpowlen(second[0], second[1]) ** (1/2)
B_cos_vec = Getpowlen(meetx, meety) ** (1/2)
print('그래프를 통해 구한 내적값은 {}이다.'.format(A_vec * B_cos_vec))
print('이를 통해 내적의 원리를 알 수 있다')