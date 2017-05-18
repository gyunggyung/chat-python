f = open("lyrics.txt")
lyrics = []
word = 0

while True:
	line = f.readline()
	if not line:
		break
	lyrics.append(line[:-2])
	word += len(line[:-2])
f.close()

for i in lyrics:
	print(i)
print("줄 수 : ",len(lyrics))
print("글자 수 : ",word)

rr = "안녕하세요"
rrr = "hi"
rrrr = "안i"
print (len(rr), len(rrr), len(rrrr))
