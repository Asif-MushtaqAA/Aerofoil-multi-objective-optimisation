import numpy as np
import os

def load_airfoil_geometry(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    coordinates = []
    for line in lines:
        data = line.split()
        if len(data) == 2:
            x = float(data[0])
            y = float(data[1])
            coordinates.append([x, y])
    return np.array(coordinates)

def calculate_area(airfoil_number, geo_path = 'E:/SU/Dis/libairfoil-master/data_geometry'):
    
    airfoil_path = os.path.join(geo_path, f'{airfoil_number}.txt')
    coords = load_airfoil_geometry(airfoil_path)
    
    # Calculate the x and y differences
    x = coords[:, 0]
    y = coords[:, 1]
    
    # Compute the shoelace sum
    area = np.sum(x[:-1] * y[1:] - y[:-1] * x[1:])
    
    # Add the last term to complete the polygon
    area += x[-1] * y[0] - y[-1] * x[0]
    
    # Return the absolute value divided by 2
    return abs(area) / 2.0


# Example implementation to calculate area
#from area_calculator import calculate_area
#area = calculate_area(1)
#print(f"The internal area of the airfoil is: {area}")
