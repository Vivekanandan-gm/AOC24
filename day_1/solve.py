first_column = []
second_column = []

with open ("in.txt") as file:
    for line in file:
        val = line.rstrip().split()
        first_column.append(val[0])
        second_column.append(val[1])

first_column.sort()
second_column.sort()

sum = 0
similarity_score = 0
for i in range(len(first_column)):
    sum += abs(int(first_column[i]) - int(second_column[i]))
    similarity_score += int(first_column[i]) * second_column.count(first_column[i])

print(sum)
print(similarity_score)