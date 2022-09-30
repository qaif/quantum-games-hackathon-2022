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
        message.append(qc)
    return message

# applies corresponding measurement, simulating result of each qubit upon measurement
# results are stored in bob's rsults
# this is also used to do interception by eve, which will be decided probabilistically
def measure_message(message, bases):
    backend = Aer.get_backend('aer_simulator')
    measurements = []
    for q in range(globals.selectedBit):
        if bases[q] == 0: # measuring in Z-basis
            message[q].measure(0,0)
        if bases[q] == 1: # measuring in X-basis
            message[q].h(0)
            message[q].measure(0,0)
        aer_sim = Aer.get_backend('aer_simulator')
        qobj = assemble(message[q], shots=1, memory=True)
        result = aer_sim.run(qobj).result()
        measured_bit = int(result.get_memory()[0])
        measurements.append(measured_bit)
    return measurements

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

globals.selectedBit = 100 # get this from phase 0
# Step 1
globals.romeo_bits = randint(2, size=globals.selectedBit)
globals.romeo_bases = randint(2, size=globals.selectedBit)

# Step 2
# showing this using a scene after phase 1.
globals.encoded_qbits = encode_message(globals.romeo_bits, globals.romeo_bases) # this is the thing that eavesdropping changes

# Interception!
globals.intercept=False
if random.random() < .33: # eve intercepts the messge 33% of the time
    globals.intercept=True

if(globals.intercept):
    # could also decide to have eve only measure some of the qubits. would be an interesting twist!
    eve_bases = randint(2, size=globals.selectedBit) # doesn't need to be a globals variable because it isn't used more than once
    # this will not be used in the end, but good to have just in case
    intercepted_message = measure_message(globals.encoded_qbits, eve_bases)

# Step 3
globals.juliet_bases = randint(2, size=globals.selectedBit)
globals.juliet_bits = measure_message(globals.encoded_qbits, globals.juliet_bases)

# Step 4 This is the sifting game in
juliet_key = sift(globals.romeo_bases, globals.juliet_bases, globals.juliet_bits) # this is used in phase 4
romeo_key = sift(globals.romeo_bases, globals.juliet_bases, globals.romeo_bits) # this is used to check the player's work in phase 3 and used in p4 too

# Step 5
# this is the choice the user makes in phase 4!
sample_size = 1 # Change this to something lower and see if
                 # Eve can intercept the message without Alice
                 # and Bob finding out
globals.bits_2sample = randint(globals.selectedBit, size=sample_size)

# technically in phas 4, they need to compare these arrays, not their measurements
# these arrays are random choices. this is a safer implementation of bb84 algorithm
globals.juliet_sample = sample_bits(juliet_key, globals.bits_2sample) # should both of them do it? i think we're just showing romeo.
globals.romeo_sample = sample_bits(romeo_key, globals.bits_2sample)

if (globals.intercept):
    if globals.juliet_sample != globals.romeo_sample:
        print("Eve's interference was detected. MAKE THIS DYNAMIC")
    else:
        print("Eve went undetected! (the player can fail)")

if (globals.juliet_sample == globals.romeo_sample):
    print("samples match!")
else:
    print("samples do not match")

# If there is no interference, and the keys don't match perfectly, blame noise
# is the better word decoherence? determine!


string_ints = [str(int) for int in romeo_key]
str_of_ints = ",".join(string_ints)
a_key=str_of_ints

string_ints = [str(int) for int in juliet_key]
str_of_ints = ",".join(string_ints)
b_key=str_of_ints

# there is a global variable for this
globals.to_encrypt="romeo, o romeo"

a = cipher_encryption(globals.to_encrypt,a_key)
c = cipher_decryption(a,b_key)


if(globals.to_encrypt!=c):
    print("the encryption failed! Only {?} % of the characters match")
else:
    print("the encryption was a success!")