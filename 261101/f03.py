days = 1
aTime = 12
bTime = 18

while days % aTime != 0 or days % bTime != 0:
    days += 1
print(f"{days} nap után találkoznak újra a rajtvonalnál.")
