def is_palindrome(word):
    if str.lower(word)==str.lower(word)[::-1]:
        return True
    return False
    
print(is_palindrome('Kayak'))