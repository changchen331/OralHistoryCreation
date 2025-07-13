import os

from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


def chat_to_qwen3(prompt="You are a helpful assistant", content="Hello, Qwen"):
    completion = client.chat.completions.create(
        # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        model="qwen3-235b-a22b",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
        # Qwen3模型通过enable_thinking参数控制思考过程（开源版默认True，商业版默认False）
        # 使用Qwen3开源版模型时，若未启用流式输出，请将下行取消注释，否则会报错
        extra_body={"enable_thinking": False},
    )
    # return completion.model_dump_json()
    return completion.choices[0].message.content


if __name__ == '__main__':
    print(chat_to_qwen3())
