import AnalysisLyrics
import numpy as np

lyrics = []
MakeLyrics = []
ProblemValue = []
problem = []

def start(f,files):
	#가사를 리스트로 옮기기
	while True:
		line = f.readline()
		if not line:
			break
		files.append(line[:-1])
	f.close()
	return files

def checkP(problem):
	global lyrics
	#가장 큰 상관계수쪽으로 리턴
	global ProblemValue
	f = open("many-lyrics.txt")
	lyrics = start(f,lyrics)
	
	for i in range(len(lyrics)):
		ReValue = 0
		#가장 상관계수가 큰 조건에 맞게 가사에 대한 return값을 Revalue에 저장
		if problem[0] == "Linelen":
			ReValue = len(lyrics[i])
		elif problem[0] == "KEP":
			ReValue = AnalysisLyrics.KEP_cal(lyrics[i])
		elif problem[0] == "Spacelen":
			ReValue = AnalysisLyrics.Spacelen_cal(lyrics[i])
		elif problem[0] == "complexity":
			ReValue = AnalysisLyrics.Complexity_cal(lyrics[i])
		else:
			return "no"
		ProblemValue.append(ReValue)
	return ProblemValue

def Make(ProblemValue,lyrics):
	AV = np.mean(ProblemValue)
	SD = np.std(ProblemValue) #표편
	#두 합이 상위 16% 정도
	i = 0
	plus = 0
	#너무 글이 많으면 치기 힘들 수 있으니 알아서 바꾸기 바람
	Limit = 20
	f = open("upgrade/lyrics.txt",'w')
	for ly in lyrics:
		#상위 16%정도만 가지고 만들기
		if ProblemValue[i] > AV + SD:
			f.write(ly)
			f.write("\n")
			plus += 1
		i += 1
		if plus > Limit:
			break
	f.close()		
	print(AV,"< >",SD)
	return AV+SD

# 문제 값 받기
f = open("Association_analysis")
problem = start(f,problem)
checkP(problem)
Make(ProblemValue,lyrics)
