import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def chat_to_deepseek_v3(prompt="You are a helpful assistant", content="Hello, Deepseek"):
    response = client.chat.completions.create(
        model="deepseek-chat",  # DeepSeek-V3-0324
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        stream=False,
    )

    return response.choices[0].message.content


if __name__ == '__main__':
    print(chat_to_deepseek_v3())
