#AnalysisLyrics.py

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

#총합 계산
def Four_information():
	global lyrics
	global Linelen
	global KEP
	global Spacelen
	global complexity
	i=0
	for ly in lyrics:
		Linelen.append(len(ly))	
		KEP.append(KEP_cal(ly))
		Spacelen.append(Spacelen_cal(ly))
		complexity.append(Complexity_cal(ly))
	print(lyrics)
	return Linelen, KEP, Spacelen, complexity

#print(Linelen)
#print("Linelen1 : ",lyrics[0])
#print("l[1]  : ",lyrics[1])
