import math
import numpy as np
import sys
import os
import random

module_path = os.path.abspath(os.path.join('..', 'libairfoil-master'))
if module_path not in sys.path:
    sys.path.append(module_path)
import libairfoil.parsec
# The libairfoil.parsec module is from the repository by mbodmer on GitHub
# GitHub repository: https://github.com/mbodmer/libairfoil/tree/master

def create_and_save_airfoil(jfoil_string, airfoil_number):
    '''
    Create an airfoil from the jfoil_string and save its coordinates to a file.
    
    jfoil_string: The string containing the airfoil parameters.
    airfoil_number: The number of the airfoil to label the file.
    '''
    params_obj = libairfoil.parsec.Parameters()
    params_obj.load_from_javafoil_parsec11(jfoil_string)
    
    airfoil = libairfoil.parsec.Airfoil(params_obj)
    
    theta_up = np.linspace(np.pi, 0, 87)
    x = 0.5 * (1 - np.cos(theta_up))
    
    theta_lo = np.linspace(0, np.pi, 89)
    y = 0.5 * (1 - np.cos(theta_lo))
    y = y[1:-1]
    
    z_up = airfoil.Z_up(x)
    z_lo = airfoil.Z_lo(y)
    
    # Save the coordinates to a text file
    filename = f'./Airfoils/{airfoil_number}.txt'
    with open(filename, 'w') as f:
       
        for coord in zip(x, z_up):
            f.write(f"{coord[0]}     {coord[1]}\n")
        
        for coord in zip(y, z_lo):
            f.write(f"{coord[0]}     {coord[1]}\n")
    
    print(f"Coordinates saved to {filename}")
    
def generate_airfoil_coordinates(sampled_parsec, airfoil_number):
    # R_LE;x_up;z_up;z_xx_up;x_lo;z_lo;z_xx_lo;z_te;dz_te;alpha_te;beta_te   #angles in degrees!
    jfoil_string = 'Parsec-11 [' + ':'.join(map(str, sampled_parsec)) + ']'
    
    # Create and save the airfoil
    create_and_save_airfoil(jfoil_string, airfoil_number)

#example implementation
#sampled_parsec = [0.01736540728136297,0.30871508071198117,0.05935844270798367,-0.39789027673984406,0.3202811385073472,-0.06641941398747805,0.5249841736211653,0.0,0.0,0.02344250623074296,17.23342976000126]
#airfoil_number = 1
#generate_airfoil_coordinates(sampled_parsec, airfoil_number)