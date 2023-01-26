import math

print('Welcome to the Velocity Calculator!')
print('###################################\n')

print('Please enter the following:\n')

mass = float(input('Mass (in kg): '))
gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
time = float(input('Time (in seconds): '))
density = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
cross_section_area = float(input('Cross sectional area (in m^2): '))
drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

inner_value_of_c = .5*density*cross_section_area*drag
velocity_in_t = (math.sqrt(mass*gravity/inner_value_of_c)) * (1 - math.exp(-math.sqrt(mass*gravity*inner_value_of_c)/mass*time))

print(f'The inner value of c is: {inner_value_of_c:.3f}')
print(f'The velocity after {time} is: {velocity_in_t:.3f} m/s')