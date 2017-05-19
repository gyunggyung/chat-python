
int = 0
f = open("lyrics.txt")
lyrics = []
timez = []
score = []
#가사를 리스트로 옮기기
while True:
	line = f.readline()
	if not line:
		break
	lyrics.append(line[:-1])
f.close()

print(lyrics)

print("test1 : ",lyrics[0])
print("l[1]  : ",lyrics[1])
