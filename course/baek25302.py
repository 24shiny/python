# a : the total number of stds
# b : the number of stds who win an award
a, b = map(int, input().split())
# scores of stds
scores = list(map(int, input().split()))
print(scores)
# sort the scores in the descending order
scores.sort(reverse=True)
print(scores)
# cutline
print(scores[b-1])
