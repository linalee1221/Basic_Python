# 코드에 설명을 추가하고 싶을때는 주석을 사용
# 주석 색깔 변경은 Window->Preference->pydev->edit
# ->comment 선택 후 우측 색깔 변경
# 샾 기호 오른쪽부터는 전부 주석처리되며, 이 경우
# 인터프리터는 주석을 코드로 인식하지 않는다.
'''
여러줄 주석은 삼중따옴표로 처리한다.
이 경우 줄마다 #을 작성할 필요 없이
여는 삼중따옴표와 닫는 삼중따옴표만 작성하면
이 사이의 모든 자료가 일괄적으로 주석처리가 된다.
'''
# 불필요한 공백은 에러를 유발함.
#    print(1+2)
print("안녕하세요?")

a = 1; b = 2; # 여러 명령을 한 줄에 작성시 세미콜론이나 콤마로 구분

# 파이썬은 대/소문자를 구분한다.
# 따라서 명령어는 대/소문자까지 일치해야 한다.
# Print(1+2)
# PRINT(1+2) # ctrl + / 를 누르면 지정 영역 일괄 주석 처리
print(1+2)

Apple = "사과"
apple = "애플"

print(Apple)
print(apple)
    