# Program to find all substrings of a string

def find_substrings(s):
    substrings = []
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    return substrings

# Usage example
string = input("Enter a string: ")
result = find_substrings(string)

print("\nAll substrings are:")
for sub in result:
    print(sub)
