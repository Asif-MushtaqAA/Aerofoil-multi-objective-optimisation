# Aerofoil-multi-objective-optimisation
Aerofoil optimisation for increasing C_L and reducing aerofoil cross-section area using Multi-Objective Modified Cuckoo Search algorithm and several modes

Modes available:  
1. DNN-Driven CFD Framework (MDDF)  
In this mode, the DNN model drives the optimisation process, with periodic CFD evaluations to assure accuracy. Specifically, CFD validation is performed on every fifth and final five generations of the optimisation process. This strategy provides high fidelity by using the CFD solver intermittently, ensuring that the results remain accurate throughout the optimisation process while avoiding the computational cost of constant CFD evaluations.

2. DNN-Only Framework (MDOF)  
To further accelerate the optimisation, a DNN-only mode, where the DNN model predicts aerodynamic performance throughout the optimisation process. This mode provides a lightweight option with substantially lower computational overhead while retaining reasonable accuracy in most cases.

3. CFD-based Framework (MFF)  
A pure CFD based optimisation approach.

DNN_Only is available in repository titled "DNN-Only-Framework".  
Link: https://github.com/Asif-MushtaqAA/DNN-Only-Framework  

FLITE2DonPY is available in repository titled "FLITE2D-on-Py".  
Link: https://github.com/Asif-MushtaqAA/FLITE2D-on-Py  

Add repository titled "Aerofoil-Generator" in a folder titled "libairfoil-master" for the provided airfoil_generator.py to function properly.        
Link: https://github.com/Asif-MushtaqAA/Aerofoil-Generator	

Note: Make sure to use correct paths for added repositories and download any repositories required for the above mentioned repositories to function properly.  

# Test Case  
1. Aerofoil-	NACA 0012  
2. Mach-	0.5  
3. Angle of Attack-	4°  
4. C_L-	0.56925  
5. C_D-	0.03786  
6. L/D-	15.0357  
7. Area- 0.08093    
