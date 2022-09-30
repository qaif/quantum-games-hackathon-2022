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


























globals.selectedBit = 10 # get this from phase 0



# Step 1
globals.romeo_bits = randint(2, size=globals.selectedBit) # don't need to do this. player picks it in guitar hero
globals.romeo_bases = randint(2, size=globals.selectedBit) # don't need to do this. player picks it in guitar hero

# Step 2
# this line should be run at the end of game 1, so we have the basis qbits for the rest of the
globals.encoded_qbits = encode_message(globals.romeo_bits, globals.romeo_bases) # this is the thing that eavesdropping changes


# Interception! # decide this before phase 2 begins!!!!!!
globals.intercept=False # TURN THIS ONE WHEN TESDTING IS READY FOR IT !
if random.random() < .33: # eve intercepts the messge 33% of the time
    globals.intercept=True

# still before phase 2
if(globals.intercept):
    globals.eve_bases = randint(2, size=globals.selectedBit) # doesn't need to be a globals variable because it isn't used more than once
    intercepted_message = measure_message(globals.encoded_qbits, globals.eve_bases)

# also ahs to happen before phase 2.
# Step 3
globals.juliet_bases = randint(2, size=globals.selectedBit)
globals.juliet_bits = measure_message(globals.encoded_qbits, globals.juliet_bases)

# this has to happen before phase 3
# Step 4 This is the sifting game in
globals.juliet_key = sift(globals.romeo_bases, globals.juliet_bases, globals.juliet_bits) # this is used in phase 4
globals.romeo_key = sift(globals.romeo_bases, globals.juliet_bases, globals.romeo_bits) # this is used to check the player's work in phase 3 and used in p4 too


# Step 5
# this is the choice the user makes in phase 4!
# so in phase 4, romeo must already have his key

# DO NOT LET THE PLAYER SAMPLE MORE BITS THAN EXIST IN THEIR KEYS!!!
# ALSO, 0 IS OKAY

# this is the choice the player makes in phase 4.
globals.sample_size = 2 # Change this to something lower and see if interference is as easy to detect!

# noise can make the keys different sizes i believe. as can interference!
# this picks which bits they WILL compare (like the order basically)
globals.bits_2sample = randint(globals.selectedBit, size=globals.sample_size)

# this ALSO THROWS AWAY THE VALUES IN THE KEYS THAT THEY COMPARE
# SO MUCH NUANCE: COMPARE TOO MANY, YOUR KEY IS REALLY SMALL
# COMPARE TOO FEW, YOUR KEY IS SUBJECT TO NOISE
globals.juliet_sample = sample_bits(globals.juliet_key, globals.bits_2sample)
globals.romeo_sample = sample_bits(globals.romeo_key, globals.bits_2sample)

# this is what romeo and juliet say to each other on the balcony!!!
# this can also be done through eve as the information isn't used anyway!
# technically juliet also has to tell romeo the bases she chose. he sifts before the player sees


# phsae 4 of the game is now over

# phase 5 starts now
# the player just picks yes or no for send the letter, and yes or no for accuse


if (globals.intercept):
    if globals.juliet_sample != globals.romeo_sample:
        print("interference or noise is present, and the player knows it now")
    else:
        print("interference or noise is present, but the player didn't know")

if (globals.juliet_sample == globals.romeo_sample):
    print("samples match perfectly.")
else:
    print("samples do not match perfectly.")

# so why is the below no longer working???

# convert format of the keys so it can work within encryption/decryption functions
string_ints = [str(int) for int in globals.romeo_key]
str_of_ints = ",".join(string_ints)
globals.romeo_key=str_of_ints

string_ints = [str(int) for int in globals.juliet_key]
str_of_ints = ",".join(string_ints)
globals.juliet_key=str_of_ints

# this is the test example message. this is already picked in the game
globals.to_encrypt="romeo, o romeo"

globals.encrypted_text = cipher_encryption(globals.to_encrypt,globals.romeo_key)
globals.decrypted_text = cipher_decryption(globals.encrypted_text,globals.juliet_key)

print("message that was encrypted: ", globals.to_encrypt)
print("encrypted text: ",globals.encrypted_text )
print("decrypted text: ", globals.decrypted_text)
print("romeo's key: ", globals.romeo_key)
print("juliet's key: ",globals.juliet_key)



if(globals.to_encrypt!=globals.decrypted_text):
    print("the encryption failed:   \"", globals.to_encrypt,"\"   is not \""  ,globals.decrypted_text,"\"")
else:
    print("the encryption was a success!")