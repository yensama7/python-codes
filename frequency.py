#calculates the frequency of data in a table
counts = dict()
friends = ['john', 'mary', 'matthew', 'john', 'jeff', 'john', 'daniel']
for x in friends:
    counts[x] = counts.get(x, 0) + 1
print(counts)