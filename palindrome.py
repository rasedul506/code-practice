# Palindrome
def isPalindrom(word: str):
    if not word: return False

    for i in range(0, len(word)//2):
        if word[i] != word[-1-i]:
            return False
    return True
    
print(isPalindrom('asdfggfdsa'))
