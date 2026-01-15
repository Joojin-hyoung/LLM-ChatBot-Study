def simple_chatbot(user_input: str) -> str:
    """
    Docstring for simple_chatbot
    
    :param user_input: Description
    :type user_input: str
    :return: Description
    :rtype: str
    """
    if "안녕" in user_input:
        return "안녕하세요!"
    elif "이름" in user_input:
        return "저는 연습용 챗봇입니다."
    elif "종료" in user_input or "exit" in user_input:
        return "bye"
    else:
        return "아직 그 질문은 잘 모르겠어요."

def run_chatbot():
    print("챗봇을 시작 합니다.(종료하려면 'exit' 입력)")

    while True:
        user_input = input("You: ")

        response = simple_chatbot(user_input)
        if response == "bye":
            print("Bot: 대화를 종료합니다.")
            break

        print(f"Bot: {response}")

if __name__=="__main__":
    run_chatbot()