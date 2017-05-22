#AnalysisLyrics.py
import AnalysisScore
import re

#전체가사
lyrics = []
#줄별글자수
Linelen=[]
#한영비율
KEP=[]
#띄어쓰기 수
Spacelen=[]
#복잡도
complexity=[]

def start():
	global lyrics
	f = open("lyrics.txt")
	#가사를 리스트로 옮기기
	while True:
		line = f.readline()
		if not line:
			break
		lyrics.append(line[:-1])
	f.close()
	return lyrics
	
####################################### 수행

#한영비율 계산
def KEP_cal(strings):
	en = re.compile('[a-zA-Z]')
	enlen = len(en.findall(strings))
	ko = re.compile('[ㄱ-ㅣ가-힣]')
	kolen = len(ko.findall(strings))
	if not enlen:
		return 100
	elif not kolen:
		return 0
	else:
		#중간 값 50를 기준으로 한영비율만큼 + -
		diff = ko - en
		if diff > 0:
			return 50+(diff/(ko+en))*50
		elif diff < 0:
			return 50-(diff/(ko+en))*50
		else:
			return 50
		return kolen/enlen

#띄어쓰기 계산
def Spacelen_cal(strings):
	return strings.count(' ')

#복잡도 계산
def Complexity_cal(strings):
	#받침이 있는 한글
	su = re.compile('[각-깋낙-닣닥-딯락-맇막-밓박-빟삭-싷악-잏작-짛착-칳팍-핗 탁-탛팍-핗학-힝]')
	lens = len(su.findall(strings))
	#마침 규칙을 생각해봐야될 거 같음 
	lens = 0
	return lens

#평균 점수
AVscore = AnalysisScore.convert()

#총합 계산
def Four_information():
	start()
	global lyrics
	global Linelen
	global KEP
	global Spacelen
	global complexity
	global AVscore
	i=0
	for ly in lyrics:
		Linelen.append(len(ly))	
		KEP.append(KEP_cal(ly))
		Spacelen.append(Spacelen_cal(ly))
		complexity.append(Complexity_cal(ly))
	print("ok"*15)
	print(AVscore)
	print(Linelen)
	print(KEP)
	print(Spacelen)
	print(complexity)
	#해당 값을 csv파일로 저장
	f = open("Statistical_Value.csv",'w')
	#시계열방식으로 저장
	f.write("Kinds,line,score\n")
	for i in range(len(lyrics)):
		if len(AVscore) <= i: break
		f.write("AVscore")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(AVscore[i]))
		f.write("\n")
		
		f.write("Linelen")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(Linelen[i]))
		f.write("\n")

		f.write("KEP")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(KEP[i]))
		f.write("\n")
		
		f.write("Spacelen")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(Spacelen[i]))
		f.write("\n")

		f.write("complexity")
		f.write(",")
		f.write(str(i))
		f.write(",")
		f.write(str(complexity[i]))
		f.write("\n")
	f.close()
	return Linelen, KEP, Spacelen, complexity

