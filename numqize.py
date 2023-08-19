# random.randint() 사용 예제 : 1~100까지의 숫자 중 랜덤으로 선택된 숫자를 맞춰라!
import random

def play_guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("1부터 100 사이의 숫자를 맞춰보세요.")

    while True:
        guess = int(input("숫자를 입력하세요: "))
        attempts += 1

        if guess < number:
            print("더 큰 숫자를 선택하세요.")
        elif guess > number:
            print("더 작은 숫자를 선택하세요.")
        else:
            print(f"축하합니다! 숫자 {number}를 맞추셨습니다!")
            print(f"시도 횟수: {attempts}")
            break

# 게임 실행
play_guessing_game()