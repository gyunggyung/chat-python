f = open("Score-record.txt", 'r')
#txt파일 받고
ReadScore=[]
#파일 받은 거 다 숫자 배열로 저장 GG
ReadAllScore=[[0]*5]
#문장 별 점수 GG
LineScore=[]

#txt파일로 받기
while True:
	line = f.readline()
	if not line: break
	ReadScore.append(line)
f.close()

#나중에는 줄 수로 계산
ScoreLen = 5

#읽은 파일 줄 수 만큼 반복하면서 
for i in range(len(ReadScore)):
	Slist = [i]*ScoreLen
	test = ReadScore[i]
	test = test.split(' ')
	#배열로 나누고 배열을 문자열로 바꿔서
	for i in range(0,ScoreLen):
		Slist[i] = int(test[i])
	#ReadAllScore에 저장
	ReadAllScore.append(Slist)

for i in range(ScoreLen):
	### 문장 별로
	OneLine=0
	for j in range(len(ReadScore)+1):
		OneLine += ReadAllScore[j][i]
	LineScore.append(OneLine/len(ReadScore))
print(ReadAllScore)
print(len(ReadAllScore))
print(LineScore)


