import time

point = 0
f = open("lyrics.txt")
lyrics = []
timez = []

while True:
	line = f.readline()
	if not line:
		break
	lyrics.append(line[:-1])
f.close()

input("Chat a lyrics:")
start = time.time()

for ly in lyrics:
	answer = 0
	stL = time.time()
	print(ly)
	lc = input("")
	if lc == ly:
		answer = 1
	point += answer
	edL = time.time()
	timez.append(answer*len(lyrics)/(edL-stL))


end = time.time()
et = end - start
et = format(et, ".2f")
print("Chat : ", et,"second\n",point,"point")
for t in timez:
	print(t)
print("정확도 : ",point/len(lyrics))
print(sum(timez))
