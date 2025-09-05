import os

from openai import OpenAI

from settings import settings_1, setting_1

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

T = settings_1[setting_1]['t']
P = settings_1[setting_1]['p']


def chat_to_gpt4o(prompt="You are a helpful assistant", content="Hello, GPT"):
    completion = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=2048,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        stream=False,
        temperature=T,
        top_p=P,
    )

    return completion.choices[0].message.content


if __name__ == '__main__':
    print(chat_to_gpt4o())
