import csv
import os 



with open('python-challenge/Pyroll/Resources/election_data.csv', 'r') as file:
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


with open('election_results.txt', 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {tvotes}\n")
    text_file.write("-------------------------\n")
    for candidate, percentage, votes in results:
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner[0]}\n")
    text_file.write("-------------------------\n")