import itertools

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    #You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
    #Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. 
    #Here, 0<=i<=x, 0<=j<=y, 0<=k<=z. Please use list comprehensions rather than multiple loops, as a learning exercise.
    
   
    #added 1 to preserve the uppser limit, therefore if x=1 then the range will be (0,2) there fore the value will be 0 and 1
    x_range = range(x + 1)
    y_range = range(y + 1)
    z_range = range(z + 1)
    
    #print(x_range, y_range, z_range)
    
    #itertools.product() does the permutation of all values.Using list comprehension to get a list of lists after permutation.
    perm_list = [list(l) for l in itertools.product(x_range, y_range, z_range)]
    
    #print(perm_list) #=> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    
    #doing if sum(row) != n removes the inner list whose components sum == n
    sorted_list = [inr_lst for inr_lst in perm_list if sum(inr_lst) != n]
    
    print(sorted_list)