def reversePrefix(word, ch):
    stack = []
    index = word.find(ch)
    if index == -1:
        return word

    for i in range(index+1):
        stack.append(word[i])
        
    reverse_str = ""
    
    while stack:
        reverse_str += stack.pop()
        
    return reverse_str+word[index+1:]

word="abcdefg"
ch="d"

ans = reversePrefix(word,ch)
print(f"Reversed Prefix : {ans}")