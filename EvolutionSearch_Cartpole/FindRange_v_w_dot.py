import math

g = 9.8
m_c = 1.0
m_p = 0.1
m_t = m_c + m_p
l = 0.5
tou = 0.02
F = [-10,10]
state = [0,0,0,0]        #[x,v,angle,ang_vel]
actions = [0,1]          #default left,1 if right

step = 0

#Find range of v and ang_vel
for a in [0,1]:
    state = [0,0,0,0]
    while((state[0] >= -2.4 and state[0] <= 2.4) and (state[2] <= math.pi/15 and state[2] >= -math.pi/15) and step <= 500):
        #print(step, state)
        v = state[1]
        w_dot = state[3]
        action = a
        b = (F[action] + m_p*l*(state[3]**2)*math.sin(state[2]))/m_t
        c = (g*math.sin(state[2])-math.cos(state[2])*b)/(l*(4/3-(m_p*math.cos(state[2])**2)/m_t))
        d = b-(m_p*l*c*math.cos(state[2]))/m_t

        state[0] = state[0]+tou*state[1]
        state[1] = state[1]+tou*d
        state[2] = state[2]+tou*state[3]
        state[3] = state[3]+tou*c
        step += 1

    if a==0:
        v_min = v
        w_dot_max = w_dot
    if a==1:
        v_max = v
        w_dot_min = w_dot

print("v_minimum: ", round(v_min,5))
print("v_maximum: ", round(v_max, 5))
print("Angular_velocity_minimum: ",round(w_dot_min,5))
print("Angular_velocity_maximum: ",round(w_dot_max,5))