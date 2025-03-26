

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
print(input_str)
print("Output--:", reverse_only_letters(input_str))

