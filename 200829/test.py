# import arrow
#
# utc = arrow.utcnow()
# print (utc)
#
# korea = utc.to("Asia/Seoul")
# print (korea.format("HH시 mm분 ss초 입니다!"))
# print (korea.timestamp)

now = arrow.utcnow().to("Asia/Seoul")
s = now.timestamp
ms = int(now.format("SSS"))
print(s*1000+ms)
