# Author: Owen Myers

#-------------------------------------------------------------------------------------------------
# The purpose of this function is:
#   For a given nuber of spins up this function outputs an array of the different states with the
#   same number of spins up. These all also have the same total magnitization (that is the point). States
#   in array are represented as integers and the array is ordered in such a way that:
#           stateArr[i] < stateArr[i+1]

import pylab as pl
import bitTwiddl as bitT

def SameMagStates(nUp,N):

    """The purpose of this function is:
            For a given nuber of spins up this function outputs an array of the different states with the
            same number of spins up. These all also have the same total magnitization (that is the point). States
            in array are represented as integers and the array is ordered in such a way that:
                             stateArr[i] < stateArr[i+1]
            The legth of the array gives the number of states with the same magnitization
            
            It is nessasary to note that the input variable N is not the number of spins in the
            chain but the integer number that represests the largest energy state in binary form

            example:
                for N = 1       binary representation = 1       (2^1 - 1)
                for N = 3       binary representation = 11      (2^2 - 1)
                for N = 7       binary representation = 111     (2^3 - 1)
                    .                   .                           .
                    .                   .                           .
                    .                   .                           .
    """
    
    # initalize the variable for holding the integers whos binary representations are the states
    # with total magnitization assosiated with nUp (the number of up spins for that magnitization)
    stateArr = pl.array([])
    


    for i in range(N+1): # include N

        # get i in its binary representation and revers the order of the string so that we can pull
        # the appropriate binary values out of the appropriate place. really the string flipping is
        # just done for convinience and there are othere ways of dealling with it but i like this
        # way
        tempbin = bitT.tcbin(i)
        binFlipped = tempbin[::-1]
        
        # we want the find all the states in our system that have number of up spins equal to the
        # inputed nUp. "1" represents up so if nUp == sum of ones in a state then that state is part
        # of our magnitization block
        sumOfOnes = 0
        # the minus 2 here is to deal with the "0b" that is going to appear at the end of our string
        for l in range(len(binFlipped)-2):
            sumOfOnes += int(binFlipped[l])

        if sumOfOnes == nUp:
            stateArr = pl.append(stateArr, i)
    
    return stateArr
#-------------------------------------------------------------------------------------------------

# This fuction uses a bisectional search to find the location of a state in an orderd array. In
# order for a biisctional search to work the array needs to be orderd in the folowing fassion:
#           stateArr[i] < stateArr[i+1]
# The function returns the location of the state "state" in the inputed array
# 
# An additional note on this function is the way in which we devide integers:
#               a/2 = (a-1)/2    --> for a an odd integer
# This is, by default the way python already deals with integer division so no additional code is
# needed to make sure this happens but it is worth noting that the use of this propertie is
# intentional

def bisecSearch(state,stateArr):
    """
    This fuction uses a bisectional search to find the location of a state in an orderd array. In
    order for a biisctional search to work the array needs to be orderd in the folowing fassion:
           stateArr[i] < stateArr[i+1]
    The function returns the location of the state "state" in the inputed array
    """ 

    minVal = 0 
    maxVal = len(stateArr)-1
    
    # initalize number to be our check location and to be the next "min" or "max" value. It is
    # always going to be half the total interval size.
    checkNum = minVal + (maxVal - minVal)/2
   
    # This loop is what is going to keep bisecting the array and checking to see if we have found
    # our value.
    while True:
        checkNum = minVal + (maxVal - minVal)/2
        
        # this if statement makes sure we dont accedently operate outside of the states of interest
        # (need this because bitFlip fuction will make a state that is out of bounds if it operats
        # on the largest state of the set. If you need to remember this just take the max state in
        # stateArr and use bitFlip on it. The state it returns will not be in the array
        if(int(stateArr[maxVal]) < state):
            break

        # check end points
        if(int(stateArr[minVal]) == state):
            checkNum = minVal
            break
        # check end points 
        if(int(stateArr[maxVal]) == state):
            checkNum = maxVal
            break

        if(state > int(stateArr[checkNum])):
            minVal = checkNum - 1
        elif(state < int(stateArr[checkNum])):
            maxVal = checkNum + 1
        else:
            break
        
        

    return checkNum


#-------------------------------------------------------------------------------------------------

# This fuction returns the Hamiltonian for a particulat magnitization block. The array of the states
# that share some magnitization (mz) are passed into the fuctipon that the compleated hamiltonian
# will be passed back. The inputs rquired by the fuction are just the array of states and the number
# of atoms in the chain. For better descriptions of the creation of the hamiltonian see coments in
# ??????????????????????? (need to get the name. . . no internet right now)

def magBlockHamiltonian(stateArr,N):
    """
    This fuction returns the Hamiltonian for a particular magnitization block. The array of the states
    that share some magnitization (mz) are passed into the fuctipon that the compleated hamiltonian
    will be passed back. The inputs rquired by the fuction are just the array of states and the
    number N (described below).
 
    It is nessasary to note that the input variable N is not the number of spins in the
    chain but the integer number that represests the largest energy state in binary form

    example:
        for N = 1       binary representation = 1           (2^1 - 1)
        for N = 3       binary representation = 11          (2^2 - 1)
        for N = 7       binary representation = 111         (2^2 - 1)
            .                   .                               .
            .                   .                               .
            .                   .                               .
    """

    # print(stateArr)
    # print(N)
    
    
    # initiallize hamiltonian block
    H = pl.zeros([len(stateArr),len(stateArr)])
    # print(H)
    
    # Loop over all states and all pairs of spins in each state to find hamiltonian
    for a in range(len(stateArr)):
        
        # looping over i here which is the location of the bits in the binary
        # representation. Here We have the loops going over len(bin(N)) - 2  because the bin
        # fuction will return the binary valure of N and then we need to subtract 2 from the "0b" in the binary
        # representation. This works because the bin fuction does not pad with zeros and therefore
        # the length of our largenst number will be the length of all of our strings when we use the
        # tcbin fuction which keeps the zeros.
        for i in range(len(bin(N))-2):
            j = i + 1
                
            # Need to make a string so we can accsess the spins of the state. need to use the
            # fliped output of tcbin
            tempBitStr = bitT.tcbin(int(stateArr[a]))
            bitStr = tempBitStr[::-1]

            # if the two ajacent spins are equal -> add 1/4th to hamaltonian at location
            # assosiated with that diagonal state        
            if ( bitStr[i] == bitStr[j] ):
                H[a,a] += 1.0/4.0

            # if the two ajacent spins are NOT equal then we have an of diagonal element in our
            # hamiltonian and we need to -1/4 from that diagonal elemennt of the Hamiltonian
            else:

                H[a,a] += -1.0/4.0
                # get the off diagonal state by flipping the two u,j spins
                offDiagState = bitT.bitFlip(int(stateArr[a]),i,j)

                # use our bisec search algorithm to find the location of the new state in our
                # stateArr. It will be there because all of the states in the statArr have the same
                # magnitization and flipping the spins conserves the magnitization.
                b = bisecSearch(int(offDiagState),stateArr)
                
                # Now that we have the location of our noew state in stateArr we want to make the
                # hamiltonian at the location a,b equal to 1/2 (what our off diagonal elements are)
                # but the important thing to notice is that we have grouped this magnitization into
                # a single block. We could have used the integer value of the "offDiagSate"" as our
                # location but then we would not have the states grouped into block. In other words
                # that would have been our first method. This segments the hamiltonian into a basis
                # in wich all magnitizations (mz) fall into the same block.
                H[a,b] = 1.0/2.0        
    

    return H
