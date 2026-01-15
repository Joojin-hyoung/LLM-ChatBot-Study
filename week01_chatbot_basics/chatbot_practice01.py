def chatbot(user_input, state):
    if state["user_name"] is None:
        state["user_name"] = user_input
        return f"{state['user_name']}님 반가워요!", state
    
    return f"{state['user_name']}님, 무슨 도움이 필요하세요?", state

def run_practice():
    print("연습용 챗봇입니다. (exit 입력 시 종료)")

    state = {
        "user_name":None
    }

    while True:
        user_input = input("You: ")

        response, state = chatbot(user_input, state)
        if response == "bye":
            print("Bot: 종료합니다.")
            break

        print(f"Bot: {response}")

if __name__ == "__main__":
    run_practice()