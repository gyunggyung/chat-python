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

#나중에는 줄 수로 계산
ScoreLen = 5

for i in range(0, len(ReadScore)):
	Slist = [i]*ScoreLen
	test = ReadScore[i]
	test = test.split(' ')
	for i in range(0,ScoreLen):
		Slist[i] = int(test[i])
	ReadAllScore.append(Slist)
	print(ReadAllScore)
	print("-"*5)
