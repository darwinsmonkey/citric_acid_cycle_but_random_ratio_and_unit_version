import matplotlib.pyplot as plt
import numpy as np
import SAS1

x = np.linspace(1, 1000, 1000)
y1, y2, y3, y4, y5, y6, y7, y8 = [], [], [], [], [], [], [], []
a1, a2, a3, a4, a5, a6, a7, a8 = 1, 1, 1 ,1, 1, 1, 1 ,1

for i in x:
    y1.append(a1 * 100)
    y2.append(a2 * 100)
    y3.append(a3 * 100)
    y4.append(a4 * 100)
    y5.append(a5 * 100)
    y6.append(a6 * 100)
    y7.append(a7 * 100)
    y8.append(a8 * 100)

    u = SAS1.sas(a1, a2, a3, a4, a5, a6, a7, a8)
    a1, a2, a3, a4, a5, a6, a7, a8 = u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]

#oxaloacetate, citrate, isocitrate, aketoglutarate, succinyl_coa, succinate, fumarate, malate


fig, ax = plt.subplots()

ax.plot(x, y1, label= 'Oxaloacetate')
ax.plot(x, y2, label= 'Citrate')
ax.plot(x, y3, label= 'Isocitrate')
ax.plot(x, y4, label= 'Alpha ketoglutarate')
ax.plot(x, y5, label= 'Succinyl CoA')
ax.plot(x, y6, label= 'Succinate')
ax.plot(x, y7, label= 'Fumarate')
ax.plot(x, y8, label= 'Malate')

plt.xlabel('cycle count')
plt.ylabel('mM')
plt.ylim([0, 200])
plt.legend()
plt.show()
