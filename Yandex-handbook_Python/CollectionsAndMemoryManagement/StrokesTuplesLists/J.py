letters = []
counts = []
while (s := input()).strip() != "ФИНИШ":
    for letter in s:
        if letter == " ":
            continue
        letter = letter.lower()

        if letter in letters:
            counts[letters.index(letter)] += 1
        else:
            letters.append(letter)
            counts.append(1)

maxCounts = max(counts)
minletter = "я"
for i in range(len(counts)):
    if counts[i] == maxCounts:
        minletter = min(letters[i], minletter)
print(minletter)