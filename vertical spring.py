# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:53:47 2022

@author: MUSTAFA
"""

""" Euler- Cromer Method is used in the code below."""

import matplotlib.pyplot as plt
import numpy as np
import math

# Define the constants of the motion:
    
k_spring= 750 # in N/m.
m_object= 1 # in kg.
g= 9.8 # in m/s^2.
y_0= -0.005 # in m # Displacement is downwards, so it is negative.
y_eq= m_object*g/k_spring # Displacement from the unstrecthed length.
# Define the initial conditions:
y_spring= y_eq-y_0 # initial stretching amount in the spring.
y_i= y_0  # inital displacement.
v_i= 0 # inital velocity is zero.
a_i= -k_spring*y_i/m_object # Inital net acceleration is upwards, so it is positive.
t_i= 0 # in seconds.
e_i= m_object*g*y_0+ (1/2)*m_object*v_i**2+ (1/2)*k_spring*y_spring**2 
# Note that reference level is the equilibrium line (y_0).
# Define the time step for Euler- Cromer Method:
    
tau= 0.005

# Declare a list for the time with inital condition:

time=[t_i]

# Declare lists for the position, velocity and mechanical energy with initial conditions:
    
vel= [v_i]
pos= [y_i]
energy=[e_i]

# Apply Euler- Cromer Method:   
for n in range (1, 101): # Let total number of steps be n_max= 100.
     
     new_vel=v_i+tau*a_i
     new_pos=y_i+tau*new_vel
     e_new= m_object*g*y_i+ (1/2)*m_object*v_i**2+ (1/2)*k_spring*(y_eq-y_i)**2 
     # Filling the lists:
     vel.append(new_vel)
     pos.append(new_pos)
     energy.append(e_new)
     time.append(n*tau)
     # Updating the variables:
     v_i=new_vel
     a_i= -k_spring* new_pos/m_object
     y_i=new_pos
     
plt.plot(time,energy, 'r--', label='Numeric Energy')



 
# Declaring a time array for the exact calculation:
timee= np.arange(0, 0.5+tau, tau)
# Initial conditions:
y_0=-0.005
v_0= 0
# Empty lists for exact velocity,position and mechanical energy:
v_list=[]
pos_list=[]
en_list=[]

# Filling the empty lists with for loop:
for t in timee:

    position=y_0*math.cos(math.sqrt(k_spring/m_object)*t)
    velocity= -y_0*math.sqrt(k_spring/m_object)*math.sin(math.sqrt(k_spring/m_object)*t)
    energy= m_object*g*position+ (1/2)*m_object*velocity**2+ (1/2)*k_spring*(y_eq-position)**2 
    v_list.append(velocity)
    pos_list.append(position)
    en_list.append(energy)
    

    
# Plotting the results:

plt.plot(timee,en_list,'b--', label='Exact Energy')  
plt.legend()
plt.xlabel('Time')
plt.ylabel('Mechanical Energy')
plt.title('Exact vs Numeric Mechanical Energy (Euler-Cromer Method)')
plt.show()

plt.plot(timee,v_list, 'b--', label='Exact Velocity')
plt.plot(time,vel, 'r.',label='Numeric Velocity') 
plt.xlabel('Time')
plt.ylabel('Velocity')  
plt.title('Exact vs Numeric Velocity (Euler-Cromer Method)') 
plt.legend()
plt.show()

plt.plot(timee, pos_list, 'b--', label='Exact Position')
plt.plot(time,pos, 'r.', label='Numeric Position')
plt.xlabel('Time')
plt.ylabel('Position')  
plt.title('Exact vs Numeric Position (Euler-Cromer Method)')
plt.legend()
plt.show()    
     

----------------------------------------------


""" Euler Method is used in the code below."""

import matplotlib.pyplot as plt
import numpy as np
import math

# Define the constants of the motion:
    
k_spring= 750 # in N/m.
m_object= 1 # in kg.
g= 9.8 # in m/s^2.
y_0= -0.005 # in m # Displacement is downwards, so it is negative.
y_eq= m_object*g/k_spring # Displacement from the unstrecthed length.
# Define the initial conditions:
y_spring= y_eq-y_0 # initial stretching amount in the spring.
y_i= y_0  # inital displacement.
v_i= 0 # inital velocity is zero.
a_i= -k_spring*y_i/m_object # Inital net acceleration is upwards, so it is positive.
t_i= 0 # in seconds.
e_i= m_object*g*y_0+ (1/2)*m_object*v_i**2+ (1/2)*k_spring*y_spring**2 
# Note that reference level is the equilibrium line (y_0).
# Define the time step for Euler Method:
    
tau= 0.0005

# Declare a list for the time with inital condition:

time=[t_i]

# Declare lists for the position, velocity and mechanical energy with initial conditions:
    
vel= [v_i]
pos= [y_i]
energy=[e_i]

# Apply Euler Method:   
for n in range (1, 101): # Let total number of steps be n_max= 100.
     
     new_vel=v_i+tau*a_i
     new_pos=y_i+tau*v_i
     e_new= m_object*g*y_i+ (1/2)*m_object*v_i**2+ (1/2)*k_spring*(y_eq-y_i)**2 
     # Filling the lists:
     vel.append(new_vel)
     pos.append(new_pos)
     energy.append(e_new)
     time.append(n*tau)
     # Updating the variables:
     v_i=new_vel
     a_i= -k_spring* new_pos/m_object
     y_i=new_pos

plt.plot(time,energy, 'r--', label='Numeric Energy')

# Declaring a time array for the exact calculation:
timee= np.arange(0, 0.5+tau, tau)
# Initial conditions:
y_0=-0.005
v_0= 0
# Empty lists for exact velocity,position and mechanical energy:
v_list=[]
pos_list=[]
en_list=[]

# Filling the empty lists with for loop:
for t in timee:

    position=y_0*math.cos(math.sqrt(k_spring/m_object)*t)
    velocity= -y_0*math.sqrt(k_spring/m_object)*math.sin(math.sqrt(k_spring/m_object)*t)
    energy= m_object*g*position+ (1/2)*m_object*velocity**2+ (1/2)*k_spring*(y_eq-position)**2 
    v_list.append(velocity)
    pos_list.append(position)
    en_list.append(energy)
    
    
# Plotting the results:

plt.plot(timee,en_list,'b--', label='Exact Energy')  
plt.legend()
plt.xlabel('Time')
plt.ylabel('Mechanical Energy')
plt.title('Exact vs Numeric Mechanical Energy (Eulers Method)')
plt.show()

plt.plot(timee,v_list, 'b--', label='Exact Velocity')
plt.plot(time,vel, 'r.',label='Numeric Velocity') 
plt.xlabel('Time')
plt.ylabel('Velocity')  
plt.title('Exact vs Numeric Velocity (Eulers Method)') 
plt.legend()
plt.show()

plt.plot(timee, pos_list, 'b--', label='Exact Position')
plt.plot(time,pos, 'r.', label='Numeric Position')
plt.xlabel('Time')
plt.ylabel('Position')  
plt.title('Exact vs Numeric Position (Eulers Method)')
plt.legend()
plt.show()    


--------------------------------------------


""" Leap- Frog method is used in the code below."""

import matplotlib.pyplot as plt
import numpy as np
import math

# Define the constants of the motion:
    
k_spring= 750 # in N/m.
m_object= 1 # in kg.
g= 9.8 # in m/s^2.
y_0= -0.005 # in m # Displacement is downwards, so it is negative.
y_eq= m_object*g/k_spring # Displacement from the unstrecthed length.
# Define the initial conditions:
y_spring= y_eq-y_0 # initial stretching amount in the spring.
y_i= y_0  # inital displacement.
v_i= 0 # inital velocity is zero.
a_i= -k_spring*y_i/m_object # Inital net acceleration is upwards, so it is positive.
t_i= 0 # in seconds.
e_i= m_object*g*y_0+ (1/2)*m_object*v_i**2+ (1/2)*k_spring*y_spring**2 
# Note that reference level is the equilibrium line (y_0).
# Define the time step for Leap- Frog Method:
    
tau= 0.005

# Declare a list for the time with inital condition:

time=[t_i]

# Declare lists for the position, velocity and mechanical energy with initial conditions:
    
vel= [v_i]
pos= [y_i]
energy=[e_i]

# Apply Leap- Frog Method:   

v_back= v_i-tau*a_i/2 # Back step for velocity borrowed from Euler Method.

for n in range (1, 101): # Let total number of steps be n_max= 100.

     velcty=v_back+tau*a_i # Calculating v_2, v_4, ...
     vel.append(velcty) # Filling velocity list.

     poss=y_i+tau*velcty # Calculating r_3, r_5, ...
     pos.append(poss) # Filling position list (poss stands for position).
     # Calculating mechanic energy
     e_new= m_object*g*poss+ (1/2)*m_object*velcty**2+ (1/2)*k_spring*(y_eq-poss)**2
     energy.append(e_new) # Filling energy list.
     time.append(n*tau) # Filling time list.
    
     # Updating the variables:
     v_back= velcty
     y_i=poss
     a_i=-k_spring*y_i/m_object



plt.plot(time,energy, 'r--', label='Numeric Energy')




# Declaring a time array for the exact calculation:
timee= np.arange(0, 0.5+tau, tau)
# Initial conditions:
y_0=-0.005
v_0= 0
# Empty lists for exact velocity,position and mechanical energy:
v_list=[]
pos_list=[]
en_list=[]

# Filling the empty lists with for loop:
for t in timee:

    position=y_0*math.cos(math.sqrt(k_spring/m_object)*t)
    velocity= -y_0*math.sqrt(k_spring/m_object)*math.sin(math.sqrt(k_spring/m_object)*t)
    energy= m_object*g*position+ (1/2)*m_object*velocity**2+ (1/2)*k_spring*(y_eq-position)**2 
    v_list.append(velocity)
    pos_list.append(position)
    en_list.append(energy)
    
    
# Plotting the results:

plt.plot(timee,en_list,'b--', label='Exact Energy')  
plt.legend()
plt.xlabel('Time')
plt.ylabel('Mechanical Energy')
plt.title('Exact vs Numeric Mechanical Energy (Leap- Frog Method)')
plt.show()

plt.plot(timee,v_list, 'b--', label='Exact Velocity')
plt.plot(time,vel, 'r.',label='Numeric Velocity') 
plt.xlabel('Time')
plt.ylabel('Velocity')  
plt.title('Exact vs Numeric Velocity (Leap- Frog Method)') 
plt.legend()
plt.show()

plt.plot(timee, pos_list, 'b--', label='Exact Position')
plt.plot(time,pos, 'r.', label='Numeric Position')
plt.xlabel('Time')
plt.ylabel('Position')  
plt.title('Exact vs Numeric Position (Leap- Frog Method)')
plt.legend()
plt.show()    

----------------------------------------------

""" Vervet Method used in the code below."""

import matplotlib.pyplot as plt
import numpy as np
import math

# Define the constants of the motion:
    
k_spring= 750 # in N/m.
m_object= 1 # in kg.
g= 9.8 # in m/s^2.
y_0= -0.005 # in m # Displacement is downwards, so it is negative.
y_eq= m_object*g/k_spring # Displacement from the unstrecthed length.
# Define the initial conditions:
y_spring= y_eq-y_0 # initial stretching amount in the spring.
y_i= y_0  # inital displacement.
v_i= 0 # inital velocity is zero.
a_i= -k_spring*y_i/m_object # Inital net acceleration is upwards, so it is positive.
t_i= 0 # in seconds.
e_i= m_object*g*y_0+ (1/2)*m_object*v_i**2+ (1/2)*k_spring*y_spring**2 
# Note that reference level is the equilibrium line (y_0).
# Define the time step for Vervet Method:
    
tau= 0.005

# Declare a list for the time with inital condition:

time=[t_i]

# Declare lists for the position, velocity and mechanical energy with initial conditions:
    
vel= [v_i]
pos= [y_i]
energy=[e_i]

# Apply Vervet Method:   

y_0= y_i- tau*v_i+(tau**2/2)*a_i # A good starting point for Vervet method.

for n in range (1, 101): # Let total number of steps be n_max= 100.
     
     poss=2*y_i-y_0+(tau**2)*a_i# Calculating r_3, r_5, ...
     velcty=(poss-y_0)/(2*tau)
     vel.append(velcty) # Filling velocity list.

     pos.append(poss) # Filling position list (poss stands for position).
     # Calculating mechanic energy
     e_new= m_object*g*poss+ (1/2)*m_object*velcty**2+ (1/2)*k_spring*(y_eq-poss)**2
     energy.append(e_new) # Filling energy list.
     time.append(n*tau) # Filling time list.
    
     # Updating the variables:
     y_0= y_i
     y_i= poss
     a_i=-k_spring*y_i/m_object



plt.plot(time,energy, 'r--', label='Numeric Energy')




# Declaring a time array for the exact calculation:
timee= np.arange(0, 0.5+tau, tau)
# Initial conditions:
y_0=-0.005
v_0= 0
# Empty lists for exact velocity,position and mechanical energy:
v_list=[]
pos_list=[]
en_list=[]

# Filling the empty lists with for loop:
for t in timee:

    position=y_0*math.cos(math.sqrt(k_spring/m_object)*t)
    velocity= -y_0*math.sqrt(k_spring/m_object)*math.sin(math.sqrt(k_spring/m_object)*t)
    energy= m_object*g*position+ (1/2)*m_object*velocity**2+ (1/2)*k_spring*(y_eq-position)**2 
    v_list.append(velocity)
    pos_list.append(position)
    en_list.append(energy)
    
# Plotting the results:

plt.plot(timee,en_list,'b--', label='Exact Energy')  
plt.legend()
plt.xlabel('Time')
plt.ylabel('Mechanical Energy')
plt.title('Exact vs Numeric Mechanical Energy (Vervet Method)')
plt.show()

plt.plot(timee,v_list, 'b--', label='Exact Velocity')
plt.plot(time,vel, 'r.',label='Numeric Velocity') 
plt.xlabel('Time')
plt.ylabel('Velocity')  
plt.title('Exact vs Numeric Velocity (Vervet Method)') 
plt.legend()
plt.show()

plt.plot(timee, pos_list, 'b--', label='Exact Position')
plt.plot(time,pos, 'r.', label='Numeric Position')
plt.xlabel('Time')
plt.ylabel('Position')  
plt.title('Exact vs Numeric Position (Vervet Method)')
plt.legend()
plt.show()    
     
# Name: Ahmet Mustafa Baraz
# Date: 07.10.2021
# Title of the Program: Vertical mass-spring system.






    




