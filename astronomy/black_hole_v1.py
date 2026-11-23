"""Date : 28 july 2026


Black hole simulator that calculates the Schwarzschild radius using real-world data (NASA). 
Comparison of stellar and supermassive black holes, visualised using Matplotlib on a logarithmic scale."
"""
import matplotlib.pyplot as plt

#------ information point --------#

# Schwarzschild radius formula = radius = 2 * G * mass / c**2
# For this test, we will use the mass of the Sun, which is 1.989e30

# We’re going to define the data I need to code this simulator

G = 0.0000000000667 # constant
c = 300000000  # speed of light in m/s
solar_mass = 1.989e30
masses = [solar_mass, solar_mass*21, solar_mass*6.3, solar_mass*9, solar_mass * 4.3e6, solar_mass*6.9e9, solar_mass*20e9,
         solar_mass*66e9, solar_mass*100e9]
names = ["Soleil", "Cygnus X-1","GRO J1655-40","V404 Cygni", "Sagittarius A*", "M87*", "NGC 4889","TON 618","Phoenix A"]

# Here, we’re going to define the function that will calculate the radius of S as a function of the sun

def black_hole(masses):
    radius = 2*G*masses/c**2
    return round(radius)



for i in range(len(names)):
    print(names[i], ":", black_hole(masses[i]), "m")



# Here, we’re going to try to draw a dot for each black hole

radii = [2948, 61911, 18573, 26533, 12677002000, 20342166000000,58962800000000, 194577240000000,294814000000000]

plt.scatter(names,radii, s=800)

plt.title("Black Hole Schwarzschild Radius - Stellar vs Supermassive (log scale)")
plt.yscale('log')
plt.show()
