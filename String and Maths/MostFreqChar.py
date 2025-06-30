def MostFreqChar(str):
    map = {}
    for i in range(len(str)):
        if str[i] not in map:
            map[str[i]] = i
        else :
            return str[i]
    return "none"
        
str = input("Enter the string : ")
print("Output : "+ MostFreqChar(str=str))