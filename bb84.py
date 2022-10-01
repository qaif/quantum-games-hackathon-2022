# be sure to cite all sources. The code will change considerably in order to meet our needs
# but this is where the first part came from:
# https://www.qmunity.tech/tutorials/quantum-key-distribution-with-bb84

from qiskit import QuantumCircuit, execute, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from numpy.random import randint
from numpy.random import randint
import numpy as np
import globals
import random
import itertools
from qiskit.providers.aer import QasmSimulator


#The function encode_message below, creates a list of QuantumCircuits,
# # each representing a single qubit in Alice's message:
#  https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
# this takes place before phase 2
def encode_message(bits, bases):
    print("==================== ENCODE MESSAGE ======================")
    message = []
    for i in range(len(bits)):
        qc = QuantumCircuit(1,1)
        if bases[i] == 0: # Prepare qubit in Z-basis
            if bits[i] == 0:
                pass
            else:
                qc.x(0)
        else: # Prepare qubit in X-basis
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        print(qc.count_ops())
        message.append(qc)
    return message

# applies corresponding measurement, simulating result of each qubit upon measurement
# results are stored in bob's rsults
# this is also used to do interception by eve, which will be decided probabilistically
def measure_message(message, bases):
    print("==================== MEASURE MESSAGE ======================")
    backend = Aer.get_backend('aer_simulator')
    measurements = []
    for q in range(len(bases)):
        if bases[q] == 0: # measuring in Z-basis
            message[q].measure(0,0)
        if bases[q] == 1: # measuring in X-basis
            message[q].h(0)
            message[q].measure(0,0)

        print(message[q].count_ops())

        aer_sim = Aer.get_backend('aer_simulator')
        qobj = assemble(message[q], shots=1, memory=True)
        result = aer_sim.run(qobj).result()
        measured_bit = int(result.get_memory()[0])
        measurements.append(measured_bit)
    return measurements

# https://github.com/VoxelPixel/CiphersInPython/blob/master/XOR%20Cipher.py
def cipher_encryption(msg,key):
    print("Cipher encryption : ", msg)
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
    return format(encrypt_hex)

def cipher_decryption(msg,key):
    print("Cipher decryption : ", msg)
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
    return format(decryp_text)

# sifting stage.
def sift(a_bases, b_bases, bits):
    good_bits = []
    for q in range(globals.selectedBit):
        if a_bases[q] == b_bases[q]:
            # If both used the same basis, add
            # this to the list of 'good' bits
            good_bits.append(bits[q])
    return good_bits


# phase 4; comparing random select of bits in their keys
# make sure the sampling is random!
# why is this changing hte keys???
def sample_bits(bits, selection):
    sample = []
    for i in selection:
        # use np.mod to make sure the
        # bit we sample is always in
        # the list range
        i = np.mod(i, len(bits))
        # pop(i) removes the element of the
        # list at index 'i'
        sample.append(bits.pop(i))
    return sample

