# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def are_anagram1(string1, string2):
    # [assignment] Add your code here
    return sorted(string1) == sorted(string2)

print(are_anagram1("secure", "rescue"))

