from mpmath import mp

digits = input("How many digits do you want to inspect (n)? : ")
mp.dps = digits
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     #stores how often each number is used in pi
base10 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pi = str(mp.pi)

for number in pi:
    if number in base10:    # prevents unexpected failures
        count[int(number)] = count[int(number)] + 1

distributionPercentage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for index in range(len(distributionPercentage)):
    distributionPercentage[index] = str(count[index] / int(digits) * 100)[:4] + "%"

print(base10)
print("Count of Number: " + str(count))
print("Percentage: " + str(distributionPercentage))

