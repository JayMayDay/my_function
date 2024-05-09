# 주석은 한줄로 사용할 때는 #을 사용합니다.
"""
주석을 복수의 줄로 사용할 때는 " 세 개를 이용합니다.
그리고 이것은 가이드라고도 불립니다.
"""
def factorial(x):
    if x<=1:
        return 1
    else :
        return x*factorial()