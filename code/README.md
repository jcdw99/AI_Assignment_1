# Particle Swarm Optimisation: Exploring the Necessity of Velocity Clamping

This project includes a basic PSO implementation, where velocity clamping intensities, and various model parameters can be tuned before execution. The top of the pso.py file houses important global parameters.

functions.py implements various benchmark functions, which are queried from pso.py. The query returns a tuple of 4 elements. The first is a pointer to the benchmark function itself. The second- a function which determines if a vector X is in the domain of the function. The third, is a function to get the lower and upper bounds of the function domain. Finally, the 4th element in the tuple is a string representation of the function name.

## Installation

Ensure the libraries at the top of pso.py are installed. A library can be installed in python using pip3. An example of the numpy installation is given below.

```bash
pip3 install numpy
```

## Usage

To run the program, configure the parameters as desired in pso.py. Once parameters are properly configured, simply execute the following command.
```bash
pip3 pso.py	
```
or, if you want to use the script, simply execute the following..
```
bash run.sh
```
## Contributing
The implementation is completely my own work. I did not outsource code in any way. 

