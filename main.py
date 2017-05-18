import time
from pylab import plot, show, title, xlabel, ylabel

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

lines = 1
for kk in score:
	print("line",lines,":",kk)
	lines += 1

# 결과 정의
end = time.time()
et = format(end - start, ".2f")
accuracy = format((point/len(lyrics))*100,".2f")
Avtime = format(sum(timez)/len(lyrics),".2f")
NonChat = end - start - sum(timez)
Allscore = format(sum(score)/len(lyrics)*100,".0f")
print("Chat : ", et,"second\n",point,"/",len(lyrics),"point")
print("정확도 : ",accuracy,"%")
print("평균속도 : ",Avtime,"초")
print("채팅 외 시간 : ",NonChat)
print("점수 : ", Allscore,"점")

# 점수 기록
f = open("Score-record.txt",'a')
for i in y:
	data = "%d\n" % i
	f.write(data)
f.close()

# 줄별 점수를  그래프로 보여주기
title('Score by line')
xlabel('line')
ylabel('score')
plot(score,marker="o")
show()
