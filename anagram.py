def isAnagram (word1, word2):
    wordlist1 = [ c for c in word1.lower()]
    wordlist2 = [ c for c in word2.lower()]
    
    wordlist1.sort()
    wordlist2.sort()

    if word1.lower() == word2.lower():
        return False
    else:
        return wordlist1 == wordlist2



print(isAnagram("pepito", "perrito"))
print(isAnagram("hola", "aloh"))
print(isAnagram("uno", "dos"))
print(isAnagram("roma", "amor"))

