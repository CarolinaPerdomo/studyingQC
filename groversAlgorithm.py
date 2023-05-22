# Import different modules from Qiskit and other libraries.

from qiskit import * # Imports all classes, functions, and constants.
from qiskit.extensions import * # Imports the extension's module from the Qiskit.
from qiskit import QuantumCircuit, ClassicalRegister, execute, Aer # Commonly used classes and functions.
from qiskit.compiler import transpile, assemble # To compile and optimize quantum circuits.
from qiskit.tools.jupyter import * # To plot and visualize quantum circuits and data within this Jupyter notebook.
from qiskit.visualization import * # Imports some visualization tools.
from qiskit.visualization import array_to_latex # Function used to convert a NumPy array into a LaTeX string rep.
from IPython.display import display, Latex # To display mathematical equations in LaTeX format within a Jupyter Notebook.
from qiskit.quantum_info import Operator # This class is used to define quantum operators.
from qiskit.providers.aer.library import save_statevector # Save the statevector of a quantum circuit after it has been executed
import numpy as np # NumPy

class circuitGrover:
    def __init__(self, n, m, s):
        self.n = n
        self.m = m
        self.s = [s]  # According to Grover's original article, the state is described by an n bit binary string.

    def Uw(self, n, m, s):
        qc = QuantumCircuit(self.n, name='U_w') # We create a new quantum circuit with n qubits and the given name.
        Uw = np.identity(self.m) # np array with size m × m, where m is the number of possible states of the n qubits.

        for i in self.s: # This loop applies the oracle to the qubits whose indices are in the s list.
            i = i.strip("'") # Remove '
            index = int(i[::-1] , 2) # Convert binary string to int.
            Uw[index][index]=-1 # Puts a negative phase on the corresponding state vector in the Uw matrix.

        qc.unitary(Operator(Uw), range(self.n)) # Converts the array Uw to an Operator that can be used by the unitary method.
        return qc # Returns oracle circuit Uw.

    def Us(self, n):
        qc=QuantumCircuit(self.n,name='Us') # New qc object with n qubits and name 'Us'.
        qc.h(range(self.n)) # To create a uniform superposition of all possible states.

        #qc.append(self.Uw(),range(self.n)) # We apply a circuit that adds a negative phase to the states orthogonal to '000'.

        orthogonal = ['0' * self.n]
        # Construct a specific Uw circuit based on the number of qubits (n)
        specific_Uw = self.Uw(self.n, self.m, orthogonal)

        qc.append(specific_Uw, range(self.n))  # Apply the specific Uw circuit

        qc.h(range(self.n)) # Again, we put the qubits in a uniform superposition.
        return qc

    def grover(self, execution=None):
        times = int(np.sqrt(self.m))
        times = int(times)

        if execution == 'svs': # Circuit in the statevector_simulator
            qc = QuantumCircuit(self.n)
            for i in range(self.n):
                qc.h(i)

            # Apply Uw and Us repeatedly for the calculated number of optimal iterations times:
            for i in range(times):
                qc.append(self.Uw(self.n, self.m, self.s), [i for i in range(self.n)])
                qc.append(self.Us(self.n), [i for i in range(self.n)])

        else:
            qc = QuantumCircuit(self.n, self.n)
            for i in range(self.n):
                qc.h(i)

            for i in range(times):
                qc.append(self.Uw(self.n, self.m, self.s), [i for i in range(self.n)])
                qc.append(self.Us(self.n), [i for i in range(self.n)])
            for i in range(self.n):
                qc.measure(i, i)

        backend = Aer.get_backend('statevector_simulator')
        state = execute(qc, backend, shots=1).result().get_statevector()
        # latex = array_to_latex(state, prefix="\\vert \psi\\rangle =", max_size=40)

        # stateEnd = display(latex)

        return state

# Prompt the user to input the values of n, m, and s
n = int(input("Enter the number of qubits of the basis: "))
m = 2**n
s = input("Enter the state you search (inside quotes) from that basis: ")

circuit = circuitGrover(n=n, m=m, s=s)

# Run the Grover's algorithm circuit using the user-provided values
print(circuit.grover())