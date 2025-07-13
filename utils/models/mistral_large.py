import os

import requests
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(
    api_key=api_key,
)


def chat_to_mistral_large(prompt="You are a helpful assistant", content="Hello, Mistral"):
    chat_response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},

        ]
    )

    return chat_response.choices[0].message.content


def chat_to_mistral_large_2(prompt="You are a helpful assistant", content="Hello, Mistral"):
    url = "https://api.mistral.ai/v1/agents/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "agent_id": "ag:f5769176:20250713:untitled-agent:5f6ca21e"
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())


if __name__ == '__main__':
    # print(chat_to_mistral_large())

    print(chat_to_mistral_large_2())
