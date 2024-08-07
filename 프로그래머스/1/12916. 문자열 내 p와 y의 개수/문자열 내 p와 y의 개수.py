from collections import Counter

def solution(s):
#     p_cnt = 0
#     y_cnt = 0
#     find_list = ["p","y"]
    
#     for sen in s:
#         sen = sen.lower()
#     if sen == "p":
#         p_cnt += 1
#     if sen == "y":
#         y_cnt += 1
    
#     if p_cnt == y_cnt:
#         return True
#     else:
#         return False
    return True if s.lower().count("p") == s.lower().count("y") else False 