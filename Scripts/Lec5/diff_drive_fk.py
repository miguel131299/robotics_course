from matplotlib import pyplot as plt
# from scipy.optimize import fsolve
import math
import numpy as np

def animate(t,z):
    R = 0.1;
    phi = np.arange(0,2*np.pi,0.1)
    x_circle = R*np.cos(phi)
    y_circle = R*np.sin(phi)


    for i in range(0,len(t)):
        x = z[i,0]
        y = z[i,1]
        theta = z[i,2]

        x_robot = x + x_circle
        y_robot = y + y_circle

        x2 = x + R*np.cos(theta)
        y2 = y + R*np.sin(theta)

        line, = plt.plot([x, x2],[y, y2],color="black")
        robot,  = plt.plot(x_robot,y_robot,color='black')
        shape, = plt.plot(z[0:i,0],z[0:i,1],color='red');

        plt.xlim(-2,2)
        plt.ylim(-2,2)
        plt.gca().set_aspect('equal')
        plt.pause(0.2)
        line.remove()
        robot.remove()
        shape.remove()

plt.close()


def euler_integration(tspan,z0,u):
    v = u[0]
    omega = u[1]
    h = time[1]-time[0]

    x0 = z0[0]
    y0 = z0[1]
    theta0 = z0[2]

    xdot_c = v*math.cos(theta0)
    ydot_c = v*math.sin(theta0)
    thetadot = omega

    x1 = x0 + xdot_c*h
    y1 = y0 + ydot_c*h
    theta1 = theta0 + thetadot*h

    z1 = [x1, y1, theta1]
    return z1


#initial condition, [x0, y0, theta0]
z0 = [0, 0, math.pi/2]

#integration time step
h = 0.1

# %%%%% the controls are v = speed and omega = direction
# %%%%%% v = 0.5r(phidot_r + phidot_l)
# %%%%%% omega = 0.5 (r/b)*(phitdot_r - phidot_l)
# %%%%%% these are set below %%%%%%
# %%%%%%% writing letters %%%%%%%
t1 = np.arange(0,1,0.1)
t2 = np.arange(1,2,0.1)
t3 = np.arange(2,3,0.1)
time = np.append(t1,t2)
time = np.append(time,t3)

control_input = np.zeros((len(time), 2)) # [lin vel, ang vel]

for i in range(0,len(t1)):
    # set linear velocity
    control_input[i,0] = 1
for i in range(len(t1),len(t1)+len(t1)):
    # set angular velocity
    control_input[i,1] = math.pi/2
for i in range(len(t1)+len(t2),len(time)):
    # set linear velocity
    control_input[i,0] = 1

states = np.array(z0);
for i in range(0,len(time)-1):
    # u = [0.5, 0] #[v, omega] #test
    z0 = euler_integration([time[i], time[i+1]],z0,[control_input[i,0],control_input[i,1]])
    states = np.vstack([states, z0])

animate(time,states)