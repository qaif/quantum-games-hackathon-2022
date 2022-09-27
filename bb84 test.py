# show that bb84 can be done effectively, including the encryption and decryption stages (by 2!)

# be sure to cite all sources. The code will change considerably in order to meet our needs
# but this is where the first part came from:
# https://www.qmunity.tech/tutorials/quantum-key-distribution-with-bb84

from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from numpy.random import randint
import numpy as np
import itertools
from qiskit.providers.aer import QasmSimulator
import operator
num_qubits = 32

alice_basis = np.random.randint(2, size=num_qubits)
alice_state = np.random.randint(2, size=num_qubits)
bob_basis = np.random.randint(2, size=num_qubits)


print (f"Alice's State:\t", np.array2string(alice_state))
print (f"Alice's Bases:\t", np.array2string(alice_basis))
print (f"Bob's Bases:\t",np.array2string(bob_basis))

def bb84_circuit(state, basis, measurement_basis):
    '''
    # state: array of 0s and 1s denoting the state to be encoded
    # basis: array of 0s and 1s denoting the basis to be used for encoding
    # 0 -> Computational Basis
    # 1 -> Hadamard Basis
    # meas_basis: array of 0s and 1s denoting the basis to be used for measurement
    # 0 -> Computational Basis
    # 1 -> Hadamard Basis
    '''
    num_qubits = len(state)

    bb84_circuit = QuantumCircuit(num_qubits)

    # Sender prepares qubits
    for i in range(len(basis)):
        if state[i] == 1:
            bb84_circuit.x(i)
        if basis[i] == 1:
            bb84_circuit.h(i)


    # Measuring action performed by Bob
    for i in range(len(measurement_basis)):
        if measurement_basis[i] == 1:
            bb84_circuit.h(i)


    bb84_circuit.measure_all()

    return bb84_circuit


circuit = bb84_circuit(alice_state, alice_basis, bob_basis)
key = execute(circuit.reverse_bits(),backend=QasmSimulator(),shots=1).result().get_counts().most_frequent()
encryption_key = ''
for i in range(num_qubits):
    if alice_basis[i] == bob_basis[i]:
         encryption_key += str(key[i])
print(f"Key: {encryption_key}")
print("")
print("")

# https://github.com/VoxelPixel/CiphersInPython/blob/master/XOR%20Cipher.py
def cipher_encryption(msg,key):
    print(msg)
    encrypt_hex = ""
    key_itr = 0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[key_itr])
        # zfill will pad a single letter hex with 0, to make it two letter pair
        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            # once all of the key's letters are used, repeat the key
            key_itr = 0

    print("Encrypted Text: {}".format(encrypt_hex))
    return format(encrypt_hex)

def cipher_decryption(msg,key):

    hex_to_uni = ""
    for i in range(0, len(msg), 2):
        hex_to_uni += bytes.fromhex(msg[i:i+2]).decode('utf-8')

    decryp_text = ""
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
        # zfill will pad a single letter hex with 0, to make it two letter pair
        decryp_text += chr(temp)
        key_itr += 1
        if key_itr >= len(key):
            # once all of the key's letters are used, repeat the key
            key_itr = 0

    print("Decrypted Text: {}".format(decryp_text))
    return format(decryp_text)


a= cipher_encryption("romeo, o romeo",encryption_key)
c=cipher_decryption(a,encryption_key)





exit()




