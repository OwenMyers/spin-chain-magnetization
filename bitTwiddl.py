


# ------------------------------------------------------------------------------------------------
# First make a new bin function that keeps leading zeros on binary representation. We do this
# because it could be very bad if we were to accedently change the length and representation of our
# bassis states. 
# The first input variable x is the number we would like represented in binary. 
# The second input variable y is the length (with padded zeros) of the binary number. Default is y =
# 8. 
# Might want to add a part for negative x in the future... if so see
# www.barricane.com/bit-twiddling-python.html
def tcbin(x,y=8):
    """This returns the zero paded bit representation of the input number in y bits where y is
    default 8 but can also be input if desired. Currently can only deal with positive #s"""

    if x >= (2**(y-1)) or x < -(2**(y-1) or y < 1):
        raise Exception("Argument outside of range.")

    if x >= 0:

        # the string of bits returned by bin(). This is not padded with zeros yet
        binstr = bin(x)

        # pad  with zeros
        while len(binstr) < y +2:
            binstr = "0b0" + binstr[2:]
        
        return binstr

# ------------------------------------------------------------------------------------------------

def bitFlip(num,i,j):
    """This fuction takes and input integer:
    -> converts the integer bits
    -> flips the i and j components of the bit expressed number
    -> converts the bit number back to an integer and returns that number"""

    # make mask used with exclusive or to perform flip (will be expressed as integer and only turned
    # into bit number when flip is performed
    mask = 2**i + 2**j
    
    # perform flip 
    flipped = int(tcbin(num),2) ^ int(tcbin(mask),2)

    # the flipped number to and integer and return it
    return int(flipped)
    


