'''
PROGRAM TO CONVERT BINARY TO DECIMAL
'''
def bin_2_dec(num,binary = None):
    '''
    FUNCTION WHICH PRINTS THE BINARY IN STRING FORMAT
    '''
    if binary == None:
        binary = [num]
    
    remainder = int(num%2)
    quotient = int((num-(num%2))/2)
    
    #TO INSERT EVERY ELEMENT IN REVERSE MANNER
    binary.insert(0,str(remainder))
    
    #RECURSION
    if quotient != 0:
        return bin_2_dec(quotient,binary)
    
    #ENDING RECURSION
    if quotient == 0:
        original_num = binary.pop(-1)
        print(f"{original_num} to binary --> {' '.join(binary)}")


def enter_num():
    '''
    FUNCTION TO VALIDATE AND RETURN THE USER INPUT
    '''
    while True:
        try:
            num = int(input('Enter an Integer: '))

        except:
            print('INVALID INPUT')
            continue

        else:
            break

    return num


if __name__ == '__main__':

    integer = enter_num()

    bin_2_dec(integer)
