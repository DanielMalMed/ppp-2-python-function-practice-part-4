# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a, b, c):
  return max(a, max(b, c))
print("Solutions for function 1")
print(max_num(2, 5, 3))
print(max_num(1, 2, 3))
print(max_num(44,45,23))
print("")
# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
    if len(list) == 0:
        return 0
    result=list[0]
    if len(list) > 1:
        for i in list[1:]:
            result = result * i
    return result
print("Solutions for function 2")

print(mult_list([2,4,5]))
print(mult_list([]))
print(mult_list([3,6,9]))
print("")

# Write a Python function called rev_string() to reverse a string.

def rev_string(str):
    return str[::-1]

print("Solutions for function 3")
print(rev_string("hello how are you"))
print(rev_string("i was able to reverse this string"))
print(rev_string("desrever saw gnirts siht"))
print("")

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(x, lower, upper):
    if x  in range(lower, upper):
        return "Num is in range"
    else:
        return "Num not in range"

print("Solutions for function 4")
print(num_within(7,5,8))
print(num_within(2,3,5))
print(num_within(3,2,4))     
print("")

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

# def pascal():

# could not figure this one out on my own, had to look at the solution
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)

