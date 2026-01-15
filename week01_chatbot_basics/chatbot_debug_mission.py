class ChatState:
    def __init__(self):
        self.user_name = None
        self.step = "ask_name"


def chatbot(user_input, state: ChatState):
    if state.step == "ask_name":
        state.user_name = user_input
        state.step = "chat"
        return f"{state.user_name}님 반가워요!"

    if state.step == "chat":
        return f"{state.user_name}님, 질문을 입력해주세요."


state = ChatState()

print("Bot: 안녕하세요! 이름을 입력해주세요.")

while True:
    user_input = input("You: ")

    if user_input == "exit":
        print("Bot: 종료합니다.")
        break

    response = chatbot(user_input,state )
    print("Bot:", response)
