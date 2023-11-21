def validAnagram(s, t): ## true
    count = [0] * 26

    # Count the frequency of characters in string s
    for x in s:
        count[ord(x) - ord('a')] += 1

    # Decrement the frequency of characters in string t
    for x in t:
        count[ord(x) - ord('a')] -= 1

    # Check if any character has non-zero frequency
    for val in count:
        if val != 0:
            return False
    
    return True

print(validAnagram('', '')) ## True
print(validAnagram('aaz', 'zza')) ## False
print(validAnagram('anagram', 'nagaram')) ## True
print(validAnagram('awesome', 'awesom')) ## False
print(validAnagram('qwerty', 'qeywrt')) ## True
