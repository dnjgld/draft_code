def generate_rotations_and_sort(x):
    n = len(x)
    
    # generate all rotations of the string x
    A = [x[i:] + x[:i] for i in range(n)]
    
    # sort the rotations lexicographically
    A_sorted = sorted(A)
    
    return A, A_sorted

def extract_y_and_L(A_sorted, x):
    # extract the last character of each rotation to form y
    y = ''.join([row[-1] for row in A_sorted])
    
    # find L, the index of the original string x in the sorted list
    L = A_sorted.index(x)
    
    return y, L

# x = "abacbbacb"
x = "The cat chasing that rat"
# x = "ababbcbac"

A, A_sorted = generate_rotations_and_sort(x)
y, L = extract_y_and_L(A_sorted, x)

print("Original Rotations:")
for rotation in A:
    print(rotation)

print("\nSorted Rotations:")
for sorted_rotation in A_sorted:
    print(sorted_rotation)

print(f"\n(y, L) = ({y}, {L})")