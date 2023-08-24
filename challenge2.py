def getConsonants(word):
    consonants = []
    
    consonant_letters = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    
    for char in word:
        if char in consonant_letters:
            consonants.append(char)
    
    return consonants

consonant_list = getConsonants("hello")
print("Consonants:", consonant_list)
