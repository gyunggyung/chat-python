
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

####################################### 수행

#한영비율 계산
def KEP_cal(strings):
	e = 0
	re = strings
	return e

#띄어쓰기 계산
def Spacelen_cal(strings):
	e = 0
	re = strings
	return e

#복잡도 계산
def Complexity_cal(strings):
	e = 0
	re = strings
	return e

print(len(lyrics))
Linelen=[]
#한영비율
KEP=[]
#띄어쓰기 수
Spacelen=[]
#복잡도
complexity=[]

i=0
for ly in lyrics:
	Linelen.append(len(ly))	
	KEP.append(KEP_cal(ly))
	Spacelen.append(Spacelen_cal(ly)
	complexity.append(Complxity_cal(ly)


print(Linelen)
print("Linelen1 : ",lyrics[0])
print("l[1]  : ",lyrics[1])
