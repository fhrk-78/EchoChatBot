import openai

# APIキーを設定します。
openai.api_key = "###"

user_response = input(f"You (ChatGPT): ")

# 対話セッションを開始します。
response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=user_response
)
chat_response = response.choices[0]["message"]["content"].strip()

# ChatGPTからの返答を出力します。
print(chat_response)