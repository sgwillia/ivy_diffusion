""" A solver for the 1D diffusion equation"""
import numpy as np
# it's a style in python to have two lines between import and function, and two lines between functions 
np.set_printoptions(formatter={"float":"{: 6.1f}".format}) # makin print look nicer - if the value of the arrays are type float, they will take 6 stapes with 1 digit to the right of the point


def solve1d(concentration, spacing, time_step, diffusivity):
    #pass # pass as a place holder
    flux = -diffusivity * np.diff(concentration) / spacing # remember to import numpy
    concentration[1:-1] -=  time_step * np.diff(flux) / spacing # fixed boundary conditions at end of domain, only looking at C between
    # C[1:-1] = C[1:-1] - dt * np.diff(q) / dx # same as above line - see C[1:-1] on both sides so can use -=
    return concentration # for numpy array this isnt actually necessary due to pass by reference... but we are explicit here that C = concentration
    
    
def _example(): # style convention - underscore infront tells people this isnt intended for public use
    D = 100
    Lx = 10 
    dx = 0.5 # grid spacing
    C1 = 500 # left boundary condition
    C2 = 0 # right boundary condition
    C = np.empty(Lx)
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx / D / 2.1 # time step using stability criterea from the notebook - this is a numerical thing that varies per model
    print(C) # inital concentration
    
    for _ in range(1,5): #iterates 4 times
        C = solve1d(C, dx, dt, D) # C-> concentration, dx-> spacing, etc
        print(C) # concentration after calling solve1d
    
    
if __name__ == "__main__":
    _example()