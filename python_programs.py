

# 1  reverse only letters which string is having letters and symbols.

def reverse_only_letters(s):
    # Convert string to a list to allow modification
    letters = [c for c in s if c.isalpha()]
    result = ""
    
    # Iterate through the string and replace letters with those from the reversed list
    for c in s:
        if c.isalpha():
            result=result+letters.pop()  # Pop from the end of letters list (reversed order)
        else:
            result=result+c  # Keep non-letter characters as they are

    return result

input_str = "ab-cd$abc_xyz@"
print("Output:", reverse_only_letters(input_str))

# second way to this program.

def reverse_only_letters(s):
    # Convert string to a list to allow modification
    letters = [c for c in s if c.isalpha()]
    result = []
    
    # Iterate through the string and replace letters with those from the reversed list
    for c in s:
        if c.isalpha():
            result.append(letters.pop())  # Pop from the end of letters list (reversed order)
        else:
            result.append(c)  # Keep non-letter characters as they are

    return ''.join(result)

# Example usage
input_str = "ab-cd"
print("Output:", reverse_only_letters(input_str))



# 2. Here's a Python program implementing the baseball game scoring system based on the operations C, D, and +.
# C: Removes the last score from the stack.
# D: Doubles the last score and adds it as a new score.
# +: Adds the last two scores and appends the result as a new score.
# Any number string is converted to an integer and added to the stack as a new score.

def cal_points(operations):
    stack = []
    
    for op in operations:
        if op == 'C':
            if stack:
                stack.pop()
        elif op == 'D':
            if stack:
                stack.append(2 * stack[-1])
        elif op == '+':
            if len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    
    return sum(stack)

# Example usage
operations = ["5", "-2", "4", "C", "D", "+"]
print("Final Score:", cal_points(operations))


# 3. Python function that processes a list of students with their names and scores. 
# find names of all students with the second-lowest score. 


def aldata(students):
    # Step 1: Extract all scores, remove duplicates, and sort them
    unique_scores = sorted(set(score for name, score in students))
    
    # Step 2: Find the second-lowest score
    if len(unique_scores) > 1:
        second_lowest = unique_scores[1]
    else:
        second_lowest = unique_scores[0]

    # Step 3: Find all student names with the second-lowest score
    expected_names = sorted([name for name, score in students if score == second_lowest])
    
    # Step 4: Print the names in alphabetical order
    for name in expected_names:
        print(name)


if __name__ == '__main__':
    students = []
    for _ in range(int(input("Enter the number of students: "))):
        name = input("Enter the student's name: ")
        score = float(input("Enter the student's score: "))
        students.append([name, score])
    
    aldata(students)


#4.  target and sum problem

def two_sum(nums, target):
    num_map = {}
    li=[]

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            # print(num_map)
            li.append([num_map[complement], i])
        num_map[num] = i
    print(num_map)
    return li


num = [1,2,3,4,5]
target=6
print(two_sum(num,target))


# 5. 3D coordinates program

def generate_3d_coordinates(x_max, y_max, z_max, a_max,target_sum):
    """Generates 3D coordinates where the sum of coordinates is not equal to the target sum.

    Args:
        x_max: Maximum value for x-coordinate.
        y_max: Maximum value for y-coordinate.
        z_max: Maximum value for z-coordinate.
        target_sum: Target sum to avoid.

    Returns:
        A list of 3D coordinate tuples.
    """

    return [(x, y, z,a) for x in range(x_max + 1) 
                   for y in range(y_max + 1) 
                   for z in range(z_max + 1) 
                   for z in range(a_max + 1) 
                   if x + y + z+a != target_sum]


# # Example usage:
x, y, z, a, target_sum = 2,2,2,2,3
coordinates = generate_3d_coordinates(x, y, z, a, target_sum)
print(coordinates)


# 6. remove zero and add it in the end.

li=[1,2,3,0,3,5,0,2,1]
for i in li:
    if i==0:
        li.remove(i)
        li.append(i)
print(li)

n = int(input())
arr = map(int, input().split())
print(type(arr))

# 7 . 

def runnerup(arr):
    a=0
    b=0
    for i in list(arr):
        if i>a:
            b=a
            a=i
        elif i>b and i<a:
            b=i
    print(b)
            
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(arr[1])
    # print(arr)
    # for i in arr:
    #     print(i)
    runnerup(arr)




#8. index of max and min values

numbers=[100,200,50,1,100]

max_val=float('-inf')
min_val=float('inf')
max_index=0
min_index=0

# Loop through the list to find min and max values
for i in range(1, len(numbers)):
    if numbers[i] < min_val:
        min_val = numbers[i]
        min_index = i
    if numbers[i] > max_val:
        max_val = numbers[i]
        max_index = i

print("Minimum value:", min_val, "at index:", min_index)
print("Maximum value:", max_val, "at index:", max_index)
