
# Finding Missing Numbers in a Sequence

nums = [1, 2, 4, 5, 7]
missing_sequence = []

minimum = min(nums)
maximum = max(nums)

for x in range(minimum, maximum + 1 ):
    if x not in nums:
        missing_sequence.append(x)
print("missing sequence : ", missing_sequence)

