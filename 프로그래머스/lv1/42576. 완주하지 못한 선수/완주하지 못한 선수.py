import collections

def solution(participant, completion):
    # answer = collections.Counter(participant) - collections.Counter(completion)
    # return list(answer.keys())[0]
    
    participant = sorted(participant)
    completion = sorted(completion)
    
    for part, comp in zip(participant, completion):
        if part != comp:
            return part
    return participant[-1]
    