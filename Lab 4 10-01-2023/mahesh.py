matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#function to check if the given plot is safe to build a building
def is_safe(i, j): 
    # check column 
    for row in range(0,i): 
        if(matrix[row][j] == 1): 
            return False

    # check row 
    for col in range(0,j): 
        if(matrix[i][col] == 1): 
            return False

    # check diagonal 
    for row in range(0, i): 
        for col in range(0, j): 
            if(row+col == i+j or row-col == i-j): 
                if(matrix[row][col] == 1): 
                    return False

    return True

# function to place the building 
def place_building(n): 
    if(n == 0): 
        return True

    #try all plots one by one 
    for i in range(0, 16): 
        for j in range(0, 16): 
            if(is_safe(i, j)): 
                #place building 
                matrix[i][j] = 1

                #recursive check for all other plots 
                if(place_building(n-1)): 
                    return True

                #if not a valid plot, then backtrack 
                matrix[i][j] = 0

    #if no plot is safe, then return false 
    return False

#function to print the matrix 
def print_matrix(): 
    for i in range(0, 16): 
        for j in range(0, 16): 
            print(matrix[i][j], end = " ") 
        print() 

#driver code 
n = 4 # Number of buildings to be constructed 
if(place_building(n)):
    print("The plots in which the buildings should be constructed are:")
    print_matrix()
else:
    print("Construction of 4 buildings is not possible")