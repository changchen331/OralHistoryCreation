
# Oral History Formatter

一个用于整理口述史原始内容为规范化文本的自动化工具。该项目基于多种大型语言模型（LLM），实现了批量处理 JSON 格式原始资料并生成结构良好的口述史文本。

## 📌 项目功能

- 自动读取指定文件夹内的 JSON 文件
- 对口述内容调用大语言模型（如 GPT-4o 等）进行文本改写与整理
- 输出格式保持原始信息、不虚构、不添加，仅进行语言风格上的组织与润色
- 支持多种模型，可扩展调用接口
- 最终结果输出为新的 JSON 文件，便于后续归档与查阅

## 🧩 项目结构

```
project_root/
│
├── main.py                      # 主程序入口
├── utils/                       # 工具模块与模型调用封装
│   ├── jsonUtil.py              # JSON 读写操作
│   └── models/
│       ├── claude.py
│       ├── deepseek_v3.py
│       ├── glm_4_plus.py
│       ├── gpt_4o.py
│       ├── mistral_large.py
│       └── qwen3.py
│
├── input/                       # 输入目录（存放原始 JSON 文件）
└── output/                      # 输出目录（保存生成的结果）
```

## 📂 输入数据格式（示例）

每个 JSON 文件包含多个条目，每条数据应包含如下字段：

```json
[
  {
    "file_id": "001",
    "context": "我小时候住在村里……"
  },
  {
    "file_id": "002",
    "context": "到了上世纪八十年代，我们家搬进了县城……"
  }
]
```

## ✅ 输出数据格式（示例）

程序会为每个模型生成一个对应输出文件，如 `filename_0.json`，其结构如下：

```json
[
  {
    "file_id": "001",
    "original_context": "我小时候住在村里……",
    "generated_text": "我出生在一个小村庄……"
  }
]
```

## ⚙️ 使用方法

1. 将原始 JSON 文件放入 `input/` 目录
2. 在 `main.py` 中设定需要调用的模型列表，例如：

```python
models = ["gpt-4o", "deepseek-v3"]
```

3. 运行主程序：

```bash
python main.py
```

4. 查看 `output/` 目录下的生成文件

## 🔧 依赖环境

- Python 3.8+
- OpenAI、DeepSeek、智谱等模型 API 封装（已在 `utils/models/` 中自定义封装）
- 无外部包依赖（如使用本地封装 API，无需安装依赖）

## 📍 注意事项

- 请确保已实现对应模型的 `chat_to_xxx()` 函数
- 如需添加模型，只需在 `utils/models/` 中定义新模型接口，并在 `main.py` 中添加逻辑分支即可

## 📝 License

此项目仅用于学习与研究目的，禁止用于虚构或篡改历史材料。
