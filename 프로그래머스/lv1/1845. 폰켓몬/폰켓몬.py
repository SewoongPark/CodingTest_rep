import collections
from itertools import permutations

def solution(nums):
    answer = 0
    counts = (collections.Counter(nums))
    ables = int(len(nums) / 2)
    # perm = permutations(list(answer.keys()), 2)
    # print(perm)
    # 개수가 많은 순서로 선택하여 반환
    answer = list(counts.keys())
    able_ponkemons = answer[:ables]
    return len(able_ponkemons)
    # return answer