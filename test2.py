f = open("Score-record.txt", 'r')
#txt파일 받고
ReadScore=[]
#파일 받은 거 다 숫자 배열로 저장
ReadAllScore=[[0]*5]

#txt파일로 받기
while True:
	line = f.readline()
	if not line: break
	ReadScore.append(line)

print(len(ReadScore)," ",ReadScore)
#나중에는 줄 수로 계산
ScoreLen = 5


Slist = [0]*ScoreLen
test = ReadScore[0]
test = test.split(' ')
for i in range(0,ScoreLen):
	Slist[i] = int(test[i])
print(Slist)
ReadAllScore.append(Slist)
ReadAllScore.append(Slist)
print(Slist[0]+32)
print(ReadAllScore)
