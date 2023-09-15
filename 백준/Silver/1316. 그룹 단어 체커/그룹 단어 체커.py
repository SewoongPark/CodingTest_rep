n = int(input())
count = 0

for i in range(n):
    word = input().strip()
    is_group_word = True
    
    for j in range(len(word) - 1):
        if word[j] != word[j + 1] and word[j + 1] in word[:j]:
            is_group_word = False
            break
    
    if is_group_word:
        count += 1

print(count)