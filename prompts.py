prompt_1 = """
Please organize the following oral narrative into a well-structured and fluently written oral history text. Maintain the original speaker's tone and emotions, and do not fabricate or invent any details. Use a first-person perspective, and preserve authentic life details.
Before writing, please consider the following points:
1、Clarify the speaker's basic identity and life background (e.g., age, occupation, family situation)
2、Organize the narrative along a clear timeline (e.g., structured as “early life, middle years, later years”)
3、Preserve the speaker’s emotions and colloquial style (e.g., hesitations, sighs, exclamations), and avoid overformalizing the language
4、Structure the text into clear paragraphs, each focusing on one theme—avoid overly long or undivided blocks of text
5、Do not add any information that is not present in the original material. Only organize what is already there.
The output should be written in Chinese.
"""

prompt_2 = """
请你扮演一位口述历史整理专家。你的任务是将一段口述叙事整理成结构清晰、流畅易读的口述历史文本。

【核心原则】
1.  **绝对忠实**：必须严格基于提供的原始文本，**不得添加、编造或推断任何原文中不存在的信息、细节和观点**。仅能进行整理、分段和语法上的最小必要调整。
2.  **保留原味**：必须使用**第一人称“我”**，并全力保留叙述者独特的**语气、情感、用词习惯和口语风格**（例如：“可累了”、“真是没想到啊”）。
3.  **逻辑清晰**：使杂乱的口述变得有条理，便于阅读。

【整理步骤】
1.  **分析背景**：从叙述中提炼出讲述者的基本身份背景（如大致年龄、职业、家庭情况）。
2.  **确定结构**：
    -   如果叙述中有时间线索，请按时间顺序（如“童年时期”、“青年时代”、“后来”）组织内容。
    -   如果叙述是围绕主题展开，请按逻辑主题（如“学手艺的经历”、“家庭生活”、“难忘的人”）组织内容。
    -   **不必强行创造时间线**。
3.  **优化可读性**：
    -   将文本划分为**多个段落**，每个段落只聚焦一个事件或一个主题。
    -   **酌情处理**：保留所有富有情感和特色的口语表达，但可以精简过于频繁、影响阅读的无意义语气词（如“呃”、“那个”）。
4.  **最终检查**：确保成品读起来仍然是那个讲述者在亲切地说话，只是他的话被更有条理地记录了下来。

【输出要求】
-   语言：中文
-   视角：第一人称
-   格式：段落清晰，无过长段落。
"""

prompt_3 = """
Act as an oral history archival expert. Your task is to organize a piece of oral narrative into a well-structured, fluent, and readable oral history text.

【Core Principles】
1、Absolute Fidelity: You must strictly base the output on the provided original text. The addition, fabrication, or inference of any information, details, or opinions not present in the original source is strictly prohibited. You are only permitted to organize, segment, and make minimal necessary grammatical adjustments.
2、Preserve the Original Voice: The output must use the first-person perspective ("我"-"I") and strive to retain the narrator's unique tone, emotions, diction, and colloquial style (e.g., "可累了" - "it was so tiring", "真是没想到啊" - "I really didn't expect that").
3、Logical Clarity: Transform the unstructured oral account into a logically organized text that is easy to read.

【Organization Steps】
1、Analyze the Background: Extract the narrator's basic background information (e.g., approximate age, occupation, family situation) from the narrative.
2、Determine the Structure:
    a)If the narrative contains chronological cues, organize the content accordingly (e.g., "Childhood," "Young Adulthood," "Later Years").
    b)If the narrative revolves around themes, organize the content by logical themes (e.g., "Learning a Trade," "Family Life," "Unforgettable People").
    c)Do not force the creation of a timeline if one is not evident.
3、Optimize Readability:
    a)Divide the text into multiple paragraphs, with each paragraph focusing on a single event or theme.
    b)Use discretion: Preserve all emotionally charged and characteristic colloquial expressions, but you may refine overly frequent and meaningless filler words (e.g., "呃", "那个", "uh," "um," "like") if they significantly hinder readability.
4、Final Review: Ensure the final output still sounds like the narrator speaking intimately, merely recorded in a more organized manner.

【Output Requirements】
1、Language: The final output text must be written in Chinese.
2、Perspective: First-Person ("I"-"我")
3、Format: Clear paragraph structure, without excessively long blocks of text.
"""
