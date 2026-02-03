# Find the number of lines, words and characters present in the file?
import os

linesCount = 0
wordsCount = 0
charsCount = 0

if os.path.isfile("C:\\Work\\ISP007\\file-handling-temp\\shubham.py"):
    with open('C:\\Work\\ISP007\\file-handling-temp\\shubham.py') as f:
        for line in f:
            linesCount += 1
            charsCount += len(line)
            words = line.split()
            wordsCount += len(words)
else:
    print('file not exist')

print('lines count:', linesCount)
print('chars count:', charsCount)
print('words count:', wordsCount)
