import csv
import os 



with open('election_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  

    tvotes = 0
    candidates = {}


    for row in reader:
        candidate = row[2]
        tvotes += 1
        candidates[candidate] = candidates.get(candidate, 0) + 1

    
print("Election Results")

print("-------------------------")

results = []
for candidate, votes in candidates.items():
    percentage = (votes / tvotes) * 100
    results.append((candidate, percentage, votes))

    print(f"Total Votes: {tvotes}")
    print("-------------------------")
    for candidate, percentage, votes in results:
     print(f"{candidate}: {percentage:.3f}% ({votes})")


winner = max(results, key=lambda x: x[2])

print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")