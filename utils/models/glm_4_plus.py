import os

from zhipuai import ZhipuAI

from settings import settings_1, setting_1

client = ZhipuAI(
    api_key=os.environ.get("ZHIPU_API_KEY"),  # 请填写您自己的APIKey
)

T = settings_1[setting_1]['t']
P = settings_1[setting_1]['p']


def chat_to_glm4_plus(prompt="You are a helpful assistant", content="Hello, GLM"):
    response = client.chat.completions.create(
        model="glm-4-plus",  # 请填写您要调用的模型名称
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
    print(chat_to_glm4_plus())
