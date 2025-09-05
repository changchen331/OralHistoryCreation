import os

from prompts import prompt_2, prompt_1
from settings import setting_1, settings_1
from utils import jsonUtil
from utils.models.claude import chat_to_claude
from utils.models.deepseek_v3 import chat_to_deepseek_v3
from utils.models.glm_4_plus import chat_to_glm4_plus
from utils.models.gpt_4o import chat_to_gpt4o
from utils.models.qwen3 import chat_to_qwen3

INPUT_PATH = "./input"  # 可以替换为你的文件夹路径
OUTPUT_PATH = "./output"  # 可以替换为你的文件夹路径

PROMPT = prompt_2  # 要使用的 prompt
SETTING = settings_1[setting_1]["name"]

MODELS = ["gpt-4o", "deepseek-v3", "qwen3", "glm-4-plus", "claude"]  # 目前可以使用的模型
target_models = ["deepseek-v3", "qwen3", "glm-4-plus"]  # 需要使用的模型


def generate(model_name, content):
    if model_name == "gpt-4o":
        return chat_to_gpt4o(PROMPT, content)
    elif model_name == "deepseek-v3":
        return chat_to_deepseek_v3(PROMPT, content)
    elif model_name == "qwen3":
        return chat_to_qwen3(PROMPT, content)
    elif model_name == "glm-4-plus":
        return chat_to_glm4_plus(PROMPT, content)
    elif model_name == "claude":
        return chat_to_claude(PROMPT, content)
    else:
        return "null"


def find_model(model_name):
    try:
        return MODELS.index(model_name)
    except ValueError:
        return -1


if __name__ == '__main__':
    # 遍历文件夹
    for root, dirs, files in os.walk(INPUT_PATH):
        for file in files:
            # 检查文件扩展名（不区分大小写）
            if file.lower().endswith('.json'):
                json_data = jsonUtil.read_json_file(os.path.join(root, file))  # 读取文件
                name, ext = os.path.splitext(file)

                # 处理数据
                for model in target_models:
                    processed_data = []
                    for datum in json_data:
                        o_c = datum["context"]
                        g_t = generate(model, o_c)
                        json_object = {"file_id": datum["file_id"], "original_context": o_c, "generated_text": g_t}
                        processed_data.append(json_object)

                    # jsonUtil.write_json_file(f"{OUTPUT_PATH}/{name}_{find_model(model)}{ext}", processed_data)
                    jsonUtil.write_json_file(f"{OUTPUT_PATH}/{name}_{model}_{SETTING}{ext}", processed_data)
                    print(model + " done")
