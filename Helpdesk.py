import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You can type whatever help you want"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Help desk Management")

demo.launch(share=True)