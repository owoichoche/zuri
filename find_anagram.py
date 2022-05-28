# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] see my code below

    list1 = list(word)
    list2 = list(anagram)

    #sort the strings
    list1.sort()
    list2.sort()
    
    position = 0
    matches = True

    while position < len(word) and matches:
        if list1[position]==list2[position]:
            position = position + 1
        else:
            matches = False
    return matches

print(find_anagram('below','elbow'))

