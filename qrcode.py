# 여기에 코드를 입력하세요.

# 충남대학교 도서관 어플리케이션과 충남대학교 공식 앱에 뜨는
# 본인 확인용 QR코드 생성 코드입니다.

# 이미지가 다운로드 되면 성공입니다.

# 제작자 : 화학과 24 최민서

# 필요한 라이브러리를 import합니다.
import base64
import time, datetime

# 교번 또는 학번을 입력받습니다.
studentID = str(input("학번 또는 교번을 입력하십시오 : "))

timeStamp = str(int(datetime.datetime.now().timestamp()))

# 코드 형식 조합 후 Base64 형식으로 암호화합니다.
rawCode = str(studentID+"^"+timeStamp)

encodedCode = rawCode.encode('UTF-8')

resultCode = base64.b64encode(encodedCode)

resultCodeString = resultCode.decode('ascii')

print(resultCodeString)

# QR코드를 표출합니다.
import qrcode
image = qrcode.make(resultCodeString)
image.save("result.png")