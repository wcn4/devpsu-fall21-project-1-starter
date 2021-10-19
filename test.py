def test():
    alphabetDict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        alphabetDict[alphabet[i]] = i
    return alphabetDict

print(test())
