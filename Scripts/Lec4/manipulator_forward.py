import numpy as np
import matplotlib.pyplot as plt
import math

# define parameters for the two-link
l1 = 1
l2 = 1
theta1 = 0.5
theta2 = math.pi/2

# prepping to get homogenous transformation
c1 = math.cos(theta1)
s1 = math.sin(theta1)

c2 = math.cos(theta2)
s2 = math.sin(theta2)

O_01 = [0, 0]
O_12 = [l1, 0]

H_01 = np.array([[c1, -s1, O_01[0]],
                 [s1, c1, O_01[1]],
                 [0, 0, 1]])

H_12 = np.array([[c2, -s2, O_12[0]],
                 [s2, c2, O_12[1]],
                 [0, 0, 1]])

H_02 = np.matmul(H_01, H_12)

# origin in world frame
origin = [0, 0]

# end of link 1 in world frame
P_1 = np.array([l1, 0, 1])
P_1 = np.transpose(P_1)

P_0 = np.matmul(H_01, P_1)
p = [P_0[0], P_0[1]]

# end of link 2 in world frame
Q_2 = np.array([l2, 0, 1])
Q_2 = np.transpose(Q_2)
Q_0 = np.matmul(H_02, Q_2)

q = [Q_0[0], Q_0[1]]

# draw line from origin to end of link1
plt.plot([origin[0], p[0]], [origin[1], p[1]], color="red", linewidth=5)

# draw line from end of link1 to end of link2
plt.plot([p[0], q[0]], [p[1], q[1]], color="blue", linewidth=5)

plt.xlabel('x')
plt.ylabel('y')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid()
plt.gca().set_aspect('equal')

plt.show(block=False)
plt.pause(5)
plt.close()


