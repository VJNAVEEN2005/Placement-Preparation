def anagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)

print(anagrams("Listen", "silent"))  # Output: True
print(anagrams("hello", "world"))    # Output: False