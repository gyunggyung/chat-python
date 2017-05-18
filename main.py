import time

point = 0
f = open("lyrics.txt")
lyrics = []
while True:
	line = f.readline()
	if not line:
		break
	lyrics.append(line[:-2])
f.close()

input("Chat a lyrics:")
start = time.time()

for ly in lyrics:
	print(ly)
	lc = input("")
	if lc == ly:
		point += 1

end = time.time()
et = end - start
et = format(et, ".2f")
print("Chat : ", et,"second\n",point,"point")
