# random.choice() 사용 예제 : 랜덤 운세 알아보기
import random 

fortunes = [
    "오늘은 좋은 날이 될 것입니다.",
    "주의해야 할 일이 있을 수 있습니다.",
    "행운이 따르지 않을 수도 있습니다.",
    "뜻밖의 기회가 찾아올 것입니다.",
    "건강에 유의하세요.",
]

def get_fortune():
    return random.choice(fortunes) # 

input("오늘의 운세를 알고 싶으세요? 엔터 키를 누르세요.")
today_fortune = get_fortune()
print("오늘의 운세:", today_fortune)
