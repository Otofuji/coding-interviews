def is_permutation_of_palindrome(phrase: str) -> bool:
    alphabet = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(phrase)):
        
        j = ord(phrase[i]) #https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
        if j >= 65 and j <= 90:
            j = j - 65
            if alphabet[j] == 0:
                alphabet[j] = 1
            else:
                alphabet[j] = 0
        elif j >=  97 and j <= 122:
            j = j-97
            if alphabet[j] == 0:
                alphabet[j] = 1
            else:
                alphabet[j] = 0
        
    count = alphabet.count(1)
    if (count > 1):
        return False
    return True

