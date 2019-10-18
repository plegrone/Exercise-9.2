fin = open('words.txt')
count_no_e = 0
count = 0
forbidden = 'e'

for line in fin:
    word = line.strip()
    count = count + 1
    if forbidden not in word:
        print(word)
        count_no_e = count_no_e + 1

print('Of the ', count, ' words evaluated')
print('I found ', count_no_e, ' words with no e')
print('And these words represent ', round(count_no_e/count*100, 1), '%',' of the total words analyzed')

        
