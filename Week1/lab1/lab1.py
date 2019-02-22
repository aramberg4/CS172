import spellchecker
SP = spellchecker.spellchecker("english_words.txt")
#print(SP)


def get_file():
    while True:
        try:
            path = input("Enter the name of the file to read: ")
            file = open(path,'r')
            return file
            break
        except Exception as e:
            print("Sorry that file name was not valid see error:" + str(e))
            continue


print("Welcome to Spellchecker!")
file = get_file()
lineNum = 0
numWordGood = 0
numWordBad = 0
for line in file:
    lineNum += 1
    for word in line.split():
        if SP.check(word):
            numWordGood += 1
        else:
            numWordBad += 1
            print("Possible Spelling Error on line " + str(lineNum)+": " + word)

print(numWordGood, "words passed spell checker.")
print(numWordBad,  "word failed spell checker.")
print("%.2f" % (numWordGood / (numWordGood + numWordBad) * 100), "% of the words passed.", sep='')