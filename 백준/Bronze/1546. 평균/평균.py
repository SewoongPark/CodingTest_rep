n = int(input())
m = list(map(int, input().split()))
n_scores = []

for score in m:
  max_score = round(score / max(m) * 100)
  n_scores.append(max_score)
print(sum(n_scores) / len((n_scores)))