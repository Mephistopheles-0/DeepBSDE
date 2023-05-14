# Deep Learning Solutions for Partial Differential Equations
This repository contains Python scripts that implement solutions to several partial differential equations using deep learning. The equations and corresponding scripts are organized into separate folders.

## Equations
The following equations are implemented in this repository:

- Allen-Cahn Equation
- Hamilton-Jacobi-Bellman Equation
- Nonlinear Black-Scholes Equation with Default Risk
- Pricing European Financial Derivatives with Different Interest Rates for Borrowing and Lending
- Multidimensional Burgers-Type PDEs with Explicit Solutions
- Reaction Diffusion Time Dependent Example PDE with Oscillating Explicit Solutions
## Folder Structure
Each equation is organized into its own folder. Each folder contains the following files:

- <code>equation.py</code>: This file contains the definition of the partial differential equation and any necessary boundary conditions.
- <code>solver.py</code>: This file contains the deep learning model that is used to solve the equation.
- <code>plot.py</code>: This file contains code to plot the loss and accuracy of the deep learning model during training.
- <code>parameters.json</code>: This file contains the configuration parameters for the deep learning model and the equation.
- <code>[name_of_equation].py</code>: This file contains the main script that runs the deep learning model to solve the equation.
Usage
To run a script to solve a particular equation, navigate to the corresponding folder and run the command:

<code>python [name_of_equation].py</code>
  
This will execute the script and output the results of the deep learning model solving the equation.

## Configuration
The parameters.json file contains the configuration parameters for the deep learning model and the equation. These parameters can be modified to adjust the behavior of the script.

## Acknowledgments
The scripts in this repository are based on the work of several authors and researchers. We acknowledge their contributions to the field of deep learning for partial differential equations.
