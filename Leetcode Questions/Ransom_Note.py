# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


def canConstruct(ransomNote, magazine):
    magazineCounter = {}
    # method 1
    # for char in magazine:
    #     if char in magazineCounter:
    #         magazineCounter[char] += 1
    #     else:
    #         magazineCounter[char] = 1
    # method 2
    for char in magazine:
        magazineCounter[char] = 1 + magazineCounter.get(char, 0)
    print(magazineCounter)
    for note in ransomNote:
        if note not in magazineCounter:
            return False
        elif magazineCounter[note] == 1:
            del magazineCounter[note]
        else:
            magazineCounter[note] -= 1
    return True
    

    

ransomNote = "a"
magazine = "aa"
# canConstruct(ransomNote, magazine)
print(canConstruct(ransomNote, magazine))
        