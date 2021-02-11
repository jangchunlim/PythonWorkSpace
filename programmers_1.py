import collections
def solution(participant, completion):
    ct1 = collections.Counter(participant)
    ct2 = collections.Counter(completion)
    answer = ", ".join(list((ct1-ct2).elements()))
    return answer

print(", ".join(solution(['mislav', 'stanko', 'mislav', 'jangchun', 'jangchun', 'ana'],['stanko', 'ana', 'mislav'])))
print(solution(['leo', 'kiki', 'eden'],['kiki', 'eden']))
print(solution(['mislav', 'stanko', 'mislav', 'jangchun', 'jangchun', 'ana'],['stanko', 'ana', 'mislav']))