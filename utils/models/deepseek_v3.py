import os

from openai import OpenAI

from settings import setting_1, settings_1

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

T = settings_1[setting_1]['t']
P = settings_1[setting_1]['p']


def chat_to_deepseek_v3(prompt="You are a helpful assistant", content="Hello, Deepseek"):
    response = client.chat.completions.create(
        model="deepseek-chat",  # DeepSeek-V3-0324
        max_tokens=2048,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        stream=False,
        temperature=T,
        top_p=P,
    )

    return response.choices[0].message.content


if __name__ == '__main__':
    print(chat_to_deepseek_v3())
