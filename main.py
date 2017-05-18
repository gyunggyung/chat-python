import time

# 선언 
point = 0
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

#가사쓰기 시작
input("Chat a lyrics:")
start = time.time()

#가사가 끝날 때 까지
for ly in lyrics:
	answer = 0
	stL = time.time()
	print(ly)
	lc = input("")
	# 쓴 가사와 가사가 같으면 점수 올리기
	if lc == ly:
		answer = 1
	point += answer
	edL = time.time()
	#한줄 쓴 시간
	timez.append(edL-stL)
	#점수 계산 글자 수에 맞는 
	score.append(answer*len(lyrics)/(edL-stL))

for kk in score:
	print(kk)

# 결과 정의
end = time.time()
et = format(end - start, ".2f")
accuracy = format((point/len(lyrics))*100,".2f")
Avtime = format(sum(timez)/len(lyrics),".2f")
NonChat = format(end - start - sum(timez),".2f")
Allscore = format(sum(score)/len(lyrics),".2f")
print("Chat : ", et,"second\n",point,"/",len(lyrics),"point")
print("정확도 : ",accuracy,"%")
print("평균속도 : ",Avtime)
print("채팅 외 시간 : ",NonChat)
print("점수 : ", Allscore)
