def practice_chatbot(user_input: str) -> str:
    """
    TODO:
    아래 조건을 직접 구현해보세요.
    """

    # Q1. "안녕"이 들어오면 "안녕하세요! 반갑습니다." 출력
    if "안녕" in user_input:
        return "안녕하세요! 반갑습니다."

    # Q2. "도움"이 들어오면 "무엇을 도와드릴까요?" 출력
    elif "도움" in user_input:
        return "무엇을 도와드릴까요?"

    # Q3. "exit" 또는 "종료" 입력 시 "bye" 반환
    elif "exit" in user_input or "종료" in user_input:
        return "bye"

    # Q4. 그 외에는 "잘 이해하지 못했어요." 출력
    else:
        return "잘 이해하지 못했어요."


def run_practice():
    print("연습용 챗봇입니다. (exit 입력 시 종료)")

    while True:
        user_input = input("You: ")

        response = practice_chatbot(user_input)
        if response == "bye":
            print("Bot: 종료합니다.")
            break

        print(f"Bot: {response}")


if __name__ == "__main__":
    run_practice()