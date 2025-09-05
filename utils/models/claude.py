import os

import anthropic

from settings import settings_1, setting_1

client = anthropic.Anthropic(
    # defaults to os.environ.get("CLAUDE_API_KEY")
    api_key=os.environ.get('CLAUDE_API_KEY'),
)

T = settings_1[setting_1]['t']
P = settings_1[setting_1]['p']


def chat_to_claude(prompt="You are a helpful assistant", content="Hello, Claude"):
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        system=prompt,
        messages=[
            {"role": "user", "content": content},
        ],
        stream=False,
        temperature=T,
        top_p=P,
    )

    return message.content[0].text


if __name__ == '__main__':
    print(chat_to_claude())
