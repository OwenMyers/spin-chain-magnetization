# Description:
# This program finds the matrix representation of a Hamiltonian for one dimensinal, S=1/2, antiferromagnetic
# Heisenberg chain.
# PERIODIC boundary conditions
# NEAREST NEIGHBOR interations

import bitTwiddl as bitT
import pylab as pl

def main():

    # N is the number of spins in our system
    N = 3

    # Make The appropriatly sized array to stor the valus of the matrix form of the hamiltonian
    H = pl.zeros([2**N,2**N])

    # This first loop is a loop over all states in the system where the states are made with
    # integers but ultimately represented in binary
    for a in range(2**N):

        # This next loop is the sum in the Hamiltonian. within it we do our operations on the
        # appropriate states and in the end the compleation of this loop gives us our Hamiltonian
        # matrix elements from the basis ket a. The reason there is not an imput of two basis states
        # (which is what you might expect from <a|H|a'> where a does not nesassaraly equal a') is
        # becasue we can look at the Hamiltonian and see which elements are going to be non zero and
        # include this knolege in the code so we are not running trivial, and pointless,
        # calculations. If It were not particularly obvios we would do the calculations in their
        # full glory
        
        # save the state a in a string containing its binary representation so we can work either
        # with the integer number a or its binary representation. The string from tcbin has been
        # fliped so that the spin states are located in the string as basis state would normaly be
        # set up (from left to right). This makes using i and j indicies esier.
        bitString = bitT.tcbin(a)
        astr = bitString[::-1]

        for i in range(N):

            # we define j as the next spin and only the next spin. This is just for nerest neighbor
            # interactions. The modulus operator is so that when we get to the end of the chain we
            # include the last interation which is the one between the spin at the end and the fist
            # spin. This is for PERIODIC interactions only
            j = (i+1)%N

            # The next couple of lines of code are where we calculate the matrix elements and a
            # couple of clever tricks from Anders W. Sandvik's paper "Computational Studies of
            # Quatum Spin Systems are used.
            # First: by inspection we see that if we are looking at at a state represented in binary
            # we see that for a specific i and j (where j = i+1) only terms where the spin state at i is
            # the same as that at j will contribute positive terms in the diagonal. This is taken
            # care of with the following argument:
            if ( astr[i] == astr[j] ):
                H[a,a] += 1.0/4.0

            # if i and j are different then only one negative sign pops out from the Sz operator and
            # we need to subtract off (1/2)*(1/2) = 1/4.
            # Also if i and j are different we can see that <a|Si(raise)*Sj(lower)|a'> can be non
            # zero. specificaly it is non zero when a' is a but with the ith and jth spins fliped.
            # This is all encoded in the following:
            else:
                H[a,a] += -.25
                b = bitT.bitFlip(a,i,j)
                H[a,b] = .5

    # see if its symetric
    seeSym = True
    for l in range(2**N):
        for k in range(2**N):
            seeSym = seeSym == (H[l,k] == H[k,l])
    print(seeSym)
    print(H)
        

if __name__ == '__main__':
    main()
