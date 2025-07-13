import json
import os


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # 解析JSON内容
            content = json.load(f)
    except Exception as e:
        print(f"读取失败 [{file_path}]: {str(e)}")

    return content


def write_json_file(file_path, content):
    try:
        # 自动创建目录（如果路径不存在）
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 写入 JSON 文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=4, sort_keys=False)
        return True

    except IOError as e:
        print(f"文件写入失败: {str(e)}")
    except Exception as e:
        print(f"未知错误: {str(e)}")

    return False


if __name__ == '__main__':
    print(read_json_file("../input/oral_materials.json"))
    print()
    print(write_json_file("../output/test.json", ""))
