import os

import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("CLAUDE_API_KEY")
    api_key=os.environ.get('CLAUDE_API_KEY'),
)


def chat_to_claude(prompt="You are a helpful assistant", content="Hello, Claude"):
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system=prompt,
        messages=[
            {"role": "user", "content": content},
        ],
    )

    return message.content[0].text


if __name__ == '__main__':
    print(chat_to_claude())
