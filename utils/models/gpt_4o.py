import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def chat_to_gpt4o(prompt="You are a helpful assistant", content="Hello, GPT"):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
    )

    return completion.choices[0].message.content


if __name__ == '__main__':
    print(chat_to_gpt4o())
