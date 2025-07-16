import os

from utils import jsonUtil
from utils.models.claude import chat_to_claude
from utils.models.deepseek_v3 import chat_to_deepseek_v3
from utils.models.glm_4_plus import chat_to_glm4_plus
from utils.models.gpt_4o import chat_to_gpt4o
from utils.models.qwen3 import chat_to_qwen3

prompt = """
Please organize the following oral narrative into a well-structured and fluently written oral history text. Maintain the original speaker's tone and emotions, and do not fabricate or invent any details. Use a first-person perspective, and preserve authentic life details.
Before writing, please consider the following points:
1、Clarify the speaker's basic identity and life background (e.g., age, occupation, family situation)
2、Organize the narrative along a clear timeline (e.g., structured as “early life, middle years, later years”)
3、Preserve the speaker’s emotions and colloquial style (e.g., hesitations, sighs, exclamations), and avoid overformalizing the language
4、Structure the text into clear paragraphs, each focusing on one theme—avoid overly long or undivided blocks of text
5、Do not add any information that is not present in the original material. Only organize what is already there.
The output should be written in Chinese.
"""
models = ["gpt-4o", "deepseek-v3", "qwen3", "glm-4-plus", "claude"]  # 目前可以使用的模型

input_path = "./input"  # 可以替换为你的文件夹路径
output_path = "./output"  # 可以替换为你的文件夹路径
target_models = ["gpt-4o"]  # 需要使用的模型


def generate(model_name, content):
    if model_name == "gpt-4o":
        return chat_to_gpt4o(prompt, content)
    elif model_name == "deepseek-v3":
        return chat_to_deepseek_v3(prompt, content)
    elif model_name == "qwen3":
        return chat_to_qwen3(prompt, content)
    elif model_name == "glm-4-plus":
        return chat_to_glm4_plus(prompt, content)
    elif model_name == "claude":
        return chat_to_claude(prompt, content)
    else:
        return "null"


def find_model(model_name):
    try:
        return models.index(model_name)
    except ValueError:
        return 0


if __name__ == '__main__':
    # 遍历文件夹
    for root, dirs, files in os.walk(input_path):
        for file in files:
            # 检查文件扩展名（不区分大小写）
            if file.lower().endswith('.json'):
                # 读取文件
                full_path = os.path.join(root, file)
                json_data = jsonUtil.read_json_file(full_path)

                # 处理数据
                for model in target_models:
                    processed_data = []
                    for datum in json_data:
                        file_id = datum["file_id"]
                        original_context = datum["context"]
                        generated_text = generate(model, original_context)

                        json_object = {"file_id": file_id, "original_context": original_context,
                                       "generated_text": generated_text}
                        processed_data.append(json_object)

                    name, ext = os.path.splitext(file)
                    jsonUtil.write_json_file(f"{output_path}/{name}_{find_model(model)}{ext}", processed_data)
                    print(model + " done")
