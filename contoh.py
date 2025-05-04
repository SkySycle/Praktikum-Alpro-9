handle = open('mbox-short.txt', 'r')

count = 0
for line in handle:
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count += 1

print("Jumlah baris 'From ': ", count)
