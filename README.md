# Exploring Quantum Computing: Jupyter notebooks, notes, scripts, among others

A personal repository where I place from time to time some ideas, that I am putting into practice in Quantum Computing. At the moment:

- A notebook where I studied the main ideas of a review on [Variational Quantum Algorithms](https://arxiv.org/abs/2012.09265).
- A small notebook checking with Qiskit when the matrix form of an operator is unitary or hermetic.
- A Python script where I implement Grover's algorithm based on the following references [1](https://arxiv.org/abs/quant-ph/9605043), [2](https://learn.qiskit.org/course/ch-algorithms/grovers-algorithm), and [3](https://samuraigab.medium.com/onde-está-o-wally-algoritmo-quântico-de-busca-grover-71fc82a41baf). This script simulates Grover's algorithm with Qiskit for an arbitrary number of qubits, returning the desired eigenvector in an optimal number of repetitions. For this I create a class where I include both the oracle, the diffuser, and the number of times this circuit will be repeated. The script is executed, and the user enters as parameters number of Qubits as well as the element to be searched (example '110' for 3 qubits, or '01010' for 5 qubits).

I am making this repository public in order to receive feedback and suggestions from the GitHub community on my computational quantum practice. Please feel free to leave comments or open issues if you have any feedback!
