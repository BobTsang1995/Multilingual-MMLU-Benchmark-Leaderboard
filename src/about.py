from dataclasses import dataclass
from enum import Enum

@dataclass
class Task:
    benchmark: str
    metric: str
    col_name: str


# Select your tasks here
# ---------------------------------------------------
class Tasks(Enum):
    # task_key in the json file, metric_key in the json file, name to display in the leaderboard 
    task0 = Task("mmmlu", "acc", "MMMLU")
    # task1 = Task("mmlu", "acc", "MMLU")
    # task2 = Task("cmmlu", "acc", "CMMLU")
    task3 = Task("mmmlu_ar", "acc", "MMMLU_AR")
    task4 = Task("mmmlu_bn", "acc", "MMMLU_BN")
    task5 = Task("mmmlu_de", "acc", "MMMLU_DE")
    task6 = Task("mmmlu_es", "acc", "MMMLU_ES")
    task7 = Task("mmmlu_fr", "acc", "MMMLU_FR")
    task8 = Task("mmmlu_hi", "acc", "MMMLU_HI")
    task9 = Task("mmmlu_id", "acc", "MMMLU_ID")
    task10 = Task("mmmlu_it", "acc", "MMMLU_IT")
    task11 = Task("mmmlu_ja", "acc", "MMMLU_JA")
    task12 = Task("mmmlu_ko", "acc", "MMMLU_KO")
    task13 = Task("mmmlu_pt", "acc", "MMMLU_PT")
    task14 = Task("mmmlu_sw", "acc", "MMMLU_SW")
    task15 = Task("mmmlu_yo", "acc", "MMMLU_YO")
    task16 = Task("mmmlu_zh", "acc", "MMMLU_ZH")
NUM_FEWSHOT = 5 # Change with your few shot
# ---------------------------------------------------



# Your leaderboard name
TITLE = """<h1 align="center" id="space-title">Multilingual MMLU Benchmark Leaderboard</h1>"""

# What does your leaderboard evaluate?
INTRODUCTION_TEXT = """
**Multilingual MMLU Benchmark Leaderboard:** This leaderboard is dedicated to evaluating the performance of both open-source and closed-source language models on the Multilingual MMLU benchmark. It assesses their memorization, reasoning, and linguistic capabilities across a wide range of languages. The leaderboard consolidates multiple MMLU datasets, originally created or manually translated into various languages, to provide a comprehensive evaluation of multilingual understanding in LLMs.
"""
INTRODUCTION_TEXT_ZH = """
**多语言 MMLU 基准榜单：** 这是一个开放的评测榜单，旨在评估开源和闭源语言模型在多语言 MMLU 基准测试中的表现，涵盖记忆、推理和语言能力。该榜单整合了多个 MMLU 数据集，这些数据集最初为多种语言创建或手动翻译，旨在全面评估大规模语言模型在多语言理解上的能力。
"""
# Which evaluations are you running? how can people reproduce what you have?
# TODO: Update number of benchmarks
LLM_BENCHMARKS_TEXT = """
## 💡 About "Multilingual Benchmark MMLU Leaderboard"

- Press release: [TBD - XXX](#), [TBD - XXX](#), [TBD - XXX](#), [TBD - XXX](#)
- YouTube: [TBD - XXX](#)

### Overview
The **Multilingual Massive Multitask Language Understanding (MMMLU)** benchmark is a comprehensive evaluation platform designed to assess the general knowledge capabilities of AI models across a wide range of domains. It includes a series of **Question Answering (QA)** tasks across **57 distinct domains**, ranging from elementary-level knowledge to advanced professional subjects such as law, physics, history, and computer science.

### Translation Effort
For this evaluation, we used the **OpenAI MMMLU dataset**, which has been extensively curated and tested for a multilingual understanding of AI models. The dataset includes 14 different languages and is specifically designed to assess how well AI models can handle a wide range of general knowledge tasks across 57 domains. 

While the translation of the test set was performed by OpenAI, it ensures a high level of accuracy and reliability for evaluating multilingual models. By leveraging this pre-existing, professionally curated dataset, we aim to focus on model performance across multiple languages, without the need for additional translations from our side.

### Commitment to Multilingual AI
By focusing on human-powered translations and publishing both the translated test sets and evaluation code, we aim to promote the development of AI models that can handle multilingual tasks with greater accuracy. This reflects our commitment to improving AI’s performance in underrepresented languages and making technology more inclusive and effective globally.

### Locales Covered
The MMMLU benchmark includes a test set translated into the following locales:
- **AR_XY**: Arabic
- **BN_BD**: Bengali
- **DE_DE**: German
- **ES_LA**: Spanish
- **FR_FR**: French
- **HI_IN**: Hindi
- **ID_ID**: Indonesian
- **IT_IT**: Italian
- **JA_JP**: Japanese
- **KO_KR**: Korean
- **PT_BR**: Brazilian Portuguese
- **SW_KE**: Swahili
- **YO_NG**: Yoruba
- **ZH_CN**: Simplified Chinese

### Purpose
The MMMLU Leaderboard aims to provide a unified benchmark for comparing AI model performance across these multiple languages and diverse domains. With the inclusion of the **QA task** across **57 domains**, it evaluates how well models perform in answering general knowledge questions in multiple languages, ensuring a high standard of multilingual understanding and reasoning.

### Goals
Our primary goal is to provide a reliable comparison for AI models across different languages and domains, helping developers and researchers evaluate and improve their models’ multilingual capabilities. By emphasizing high-quality translations and including a broad range of topics, we strive to make AI models more robust and useful across diverse communities worldwide.

### 🤗 How it works

Submit a model for automated evaluation on our clusters on the "Submit here" tab!

### 📈 Tasks

We evaluate models on a variety of key benchmarks, with a focus on **Multilingual Massive Multitask Language Understanding (MMLU)** and its variants, including MMLU, C-MMLU, ArabicMMLU, KoreanMMLU, MalayMMLU, and others. These benchmarks assess general knowledge across a wide range of topics from 57 categories, such as law, physics, history, and computer science.

The evaluation is performed using the [OpenCompass framework](https://github.com/open-compass/opencompass), a unified platform for evaluating language models across multiple tasks. OpenCompass allows us to execute these evaluations efficiently and at scale, covering multiple languages and benchmarks.

For detailed information on the tasks, please refer to the "Tasks" tab in the OpenCompass framework.

Notes:
- The evaluations are all 5-shot.
- The results are normalized with the following formula: `normalized_value = (raw_value - random_baseline) / (max_value - random_baseline)`, where `random_baseline` is `0` for generative tasks and `1/n` for multi-choice QA  with `n` choices.
- Results are aggregated by calculating the average of all the tasks for a given language.

### 🔎 Results

You can find:

- Detailed numerical results in the [results dataset](link_to_results)
- Community queries and running status in the [requests dataset](link_to_requests)

### ✅ Reproducibility

To reproduce the results, you can use [our fork of lm_eval](#), as not all of our PRs are currently integrated into the main repository.

## 🙌 Acknowledgements

This leaderboard was developed as part of the [#ProjectName](link_to_project) led by [OrganizationName](link_to_organization) thanks to the donation of high-quality evaluation datasets by:

- [Institution 1](link_to_institution_1)
- [Institution 2](link_to_institution_2)
- [Institution 3](link_to_institution_3)
- [Institution 4](link_to_institution_4)
- [Institution 5](link_to_institution_5)
- [Institution 6](link_to_institution_6)
- [Institution 7](link_to_institution_7)
- [Institution 8](link_to_institution_8)
- [Institution 9](link_to_institution_9)

The entities above are ordered chronologically by the date they joined the project. However, the logos in the footer are ordered by the number of datasets donated.

Thank you in particular to:
- Task implementation: [Name 1], [Name 2], [Name 3], [Name 4], [Name 5], [Name 6], [Name 7], [Name 8], [Name 9], [Name 10]
- Leaderboard implementation: [Name 11], [Name 12]
- Model evaluation: [Name 13], [Name 14], [Name 15], [Name 16], [Name 17]
- Communication: [Name 18], [Name 19]
- Organization & colab leads: [Name 20], [Name 21], [Name 22], [Name 23], [Name 24], [Name 25], [Name 26], [Name 27], [Name 28], [Name 29], [Name 30]

For information about the dataset authors please check the corresponding Dataset Cards (linked in the "Tasks" tab) and papers (included in the "Citation" section below). We would like to specially thank the teams that created or open-sourced their datasets specifically for the leaderboard (in chronological order):
- [Dataset1 Placeholder] and [Dataset2 Placeholder]: [Team members placeholder]
- [Dataset3 Placeholder], [Dataset4 Placeholder] and [Dataset5 Placeholder]: [Team members placeholder]
- [Dataset6 Placeholder]: [Team members placeholder]

We also thank [Institution1 Placeholder], [Institution2 Placeholder], [Organization Placeholder], [Person1 Placeholder], [Person2 Placeholder] and [Institution3 Placeholder] for sponsoring the inference GPUs.

## 🚀 Collaborate!

We would like to create a leaderboard as diverse as possible, reach out if you would like us to include your evaluation dataset!

Comments and suggestions are more than welcome! Visit the [👏 Community](<Community Page Placeholder>) page, tell us what you think about La Leaderboard and how we can improve it, or go ahead and open a PR!

Thank you very much! 💛

"""

LLM_BENCHMARKS_TEXT_ZH = """
## 💡 关于 "多语言基准 MMLU 排行榜"

- 新闻稿：[待定 - XXX](#), [待定 - XXX](#), [待定 - XXX](#), [待定 - XXX](#)
- YouTube：[待定 - XXX](#)

### 概述
**多语言大规模多任务语言理解 (MMMLU)** 基准是一个全面的评估平台，旨在评估 AI 模型在各个领域的通用知识能力。它包括一系列跨越 **57 个不同领域** 的 **问答 (QA)** 任务，从基础知识到法律、物理、历史、计算机科学等高级专业主题。

### 翻译工作
对于本次评估，我们使用了 **OpenAI MMMLU 数据集**，该数据集已经广泛策划并测试了 AI 模型的多语言理解能力。该数据集包括 14 种不同的语言，专门设计用来评估 AI 模型在 57 个领域中处理各种通用知识任务的能力。

尽管测试集的翻译是由 OpenAI 执行的，但它确保了评估多语言模型的高准确性和可靠性。通过利用这个预先存在的、专业策划的数据集，我们旨在专注于模型在多种语言中的表现，而无需我们额外进行翻译工作。

### 致力于多语言 AI
通过专注于人工翻译并公开翻译后的测试集和评估代码，我们旨在促进能够处理多语言任务的 AI 模型的开发，并使其更加准确。这也体现了我们在改善 AI 在低资源语言中的表现以及推动全球技术包容性方面的承诺。

### 涵盖的语言区域
MMMLU 基准包括以下语言区域的翻译测试集：
- **AR_XY**：阿拉伯语
- **BN_BD**：孟加拉语
- **DE_DE**：德语
- **ES_LA**：西班牙语
- **FR_FR**：法语
- **HI_IN**：印地语
- **ID_ID**：印尼语
- **IT_IT**：意大利语
- **JA_JP**：日语
- **KO_KR**：韩语
- **PT_BR**：巴西葡萄牙语
- **SW_KE**：斯瓦希里语
- **YO_NG**：约鲁巴语
- **ZH_CN**：简体中文

### 目的
MMMLU 排行榜旨在为比较 AI 模型在这些多语言和多领域中的表现提供统一的基准。通过包括 **57 个领域** 中的 **问答任务**，它评估了模型在多语言中回答通用知识问题的能力，确保了多语言理解和推理的高标准。

### 目标
我们的主要目标是为 AI 模型在不同语言和领域中的表现提供可靠的比较，帮助开发者和研究人员评估和提高他们模型的多语言能力。通过强调高质量的翻译和包括广泛的主题，我们努力使 AI 模型在全球不同社区中更加稳健和有用。

### 🤗 工作原理

在 "提交这里" 标签页上提交模型进行自动评估！

### 📈 任务

我们评估模型在多个关键基准上的表现，重点关注 **多语言大规模多任务语言理解 (MMLU)** 及其变体，包括 MMLU、C-MMLU、阿拉伯语 MMLU、韩语 MMLU、马来语 MMLU 等。 这些基准评估了来自 57 个类别（如法律、物理、历史和计算机科学等）的一般知识。

评估使用 [OpenCompass 框架](https://github.com/open-compass/opencompass) 执行，该平台统一了对语言模型的多任务评估。OpenCompass 使我们能够高效地、大规模地执行这些评估，覆盖多种语言和基准。

有关任务的详细信息，请参见 OpenCompass 框架中的 "任务" 标签页。

注：
- 所有评估均为 5-shot 任务。
- 结果采用以下公式标准化：`normalized_value = (raw_value - random_baseline) / (max_value - random_baseline)`，其中 `random_baseline` 对于生成任务为 `0`，对于多选 QA 为 `1/n`（`n` 为选择数）。
- 结果通过计算给定语言的所有任务的平均值来汇总。

### 🔎 结果

你可以找到：

- 详细的数值结果在 [结果数据集](link_to_results)
- 社区查询和运行状态在 [请求数据集](link_to_requests)

### ✅ 可复现性

要复现结果，你可以使用 [我们 fork 的 lm_eval](#)，因为并非所有的 PR 都已集成到主仓库中。

## 🙌 致谢

这个排行榜是 [#ProjectName](link_to_project) 项目的一部分，由 [OrganizationName](link_to_organization) 领导，感谢以下机构捐赠了高质量的评估数据集：

- [机构 1](link_to_institution_1)
- [机构 2](link_to_institution_2)
- [机构 3](link_to_institution_3)
- [机构 4](link_to_institution_4)
- [机构 5](link_to_institution_5)
- [机构 6](link_to_institution_6)
- [机构 7](link_to_institution_7)
- [机构 8](link_to_institution_8)
- [机构 9](link_to_institution_9)

这些实体按加入项目的时间顺序排列，然而页脚的 logo 排列顺序是按照捐赠数据集的数量。

特别感谢：
- 任务实现：[姓名 1]，[姓名 2]，[姓名 3]，[姓名 4]，[姓名 5]，[姓名 6]，[姓名 7]，[姓名 8]，[姓名 9]，[姓名 10]
- 排行榜实现：[姓名 11]，[姓名 12]
- 模型评估：[姓名 13]，[姓名 14]，[姓名 15]，[姓名 16]，[姓名 17]
- 沟通：[姓名 18]，[姓名 19]
- 组织与协作领导：[姓名 20]，[姓名 21]，[姓名 22]，[姓名 23]，[姓名 24]，[姓名 25]，[姓名 26]，[姓名 27]，[姓名 28]，[姓名 29]，[姓名 30]

有关数据集作者的信息，请查看相应的数据集卡片（可以在 "任务" 标签页中找到）以及论文（在 "引用" 部分提供）。我们特别感谢那些为排行榜专门创建或开源其数据集的团队（按时间顺序）：
- [数据集1 占位符] 和 [数据集2 占位符]： [团队成员占位符]
- [数据集3 占位符]，[数据集4 占位符] 和 [数据集5 占位符]： [团队成员占位符]
- [数据集6 占位符]： [团队成员占位符]

我们还感谢 [机构1 占位符]，[机构2 占位符]，[组织占位符]，[人员1 占位符]，[人员2 占位符] 和 [机构3 占位符] 提供推理 GPU 支持。

## 🚀 合作！

我们希望创建一个尽可能多样化的排行榜，欢迎联系我们如果你希望我们将你的评估数据集包含在内！

评论和建议非常欢迎！请访问 [👏 社区](<Community Page Placeholder>) 页面，告诉我们你对 La 排行榜的看法以及我们如何改进，或者直接打开一个 PR！

非常感谢！ 💛
"""

EVALUATION_QUEUE_TEXT = """
## Some good practices before submitting a model

### 1) Make sure you can load your model and tokenizer using AutoClasses:
```python
from transformers import AutoConfig, AutoModel, AutoTokenizer
config = AutoConfig.from_pretrained("your model name", revision=revision)
model = AutoModel.from_pretrained("your model name", revision=revision)
tokenizer = AutoTokenizer.from_pretrained("your model name", revision=revision)
```
If this step fails, follow the error messages to debug your model before submitting it. It's likely your model has been improperly uploaded.

Note: make sure your model is public!
Note: if your model needs `use_remote_code=True`, we do not support this option yet but we are working on adding it, stay posted!

### 2) Convert your model weights to [safetensors](https://huggingface.co/docs/safetensors/index)
It's a new format for storing weights which is safer and faster to load and use. It will also allow us to add the number of parameters of your model to the `Extended Viewer`!

### 3) Make sure your model has an open license!
This is a leaderboard for Open LLMs, and we'd love for as many people as possible to know they can use your model 🤗

### 4) Fill up your model card
When we add extra information about models to the leaderboard, it will be automatically taken from the model card

## In case of model failure
If your model is displayed in the `FAILED` category, its execution stopped.
Make sure you have followed the above steps first.
If everything is done, check you can launch the EleutherAIHarness on your model locally, using the above command without modifications (you can add `--limit` to limit the number of examples per task).
"""

CITATION_BUTTON_LABEL = "Copy the following snippet to cite these results"
CITATION_BUTTON_TEXT = r"""
"""
EVALUATION_QUEUE_TEXT_ZH = """
## 提交模型前的一些良好实践

### 1) 确保你可以使用 AutoClasses 加载你的模型和分词器：
```python
from transformers import AutoConfig, AutoModel, AutoTokenizer
config = AutoConfig.from_pretrained("your model name", revision=revision)
model = AutoModel.from_pretrained("your model name", revision=revision)
tokenizer = AutoTokenizer.from_pretrained("your model name", revision=revision)
```
如果此步骤失败，请按照错误信息进行调试，可能是你的模型上传不正确。

注意：确保你的模型是公开的！ 注意：如果你的模型需要 use_remote_code=True，目前我们不支持该选项，但我们正在努力添加此功能，请保持关注！

2) 将你的模型权重转换为 safetensors
这是一个新的权重存储格式，加载和使用时更安全、更快速。它还将允许我们将模型的参数数量添加到 Extended Viewer 中！

3) 确保你的模型具有开放许可！
这是一个针对开放 LLM 的排行榜，我们希望尽可能多的人知道他们可以使用你的模型 🤗

4) 填写你的模型卡
当我们将额外的信息添加到排行榜时，它将自动从模型卡中获取。

模型失败时的处理
如果你的模型出现在 FAILED 分类中，表示其执行停止。 首先确保你已经遵循了上述步骤。 如果一切都完成，检查你是否可以使用上面的命令在本地启动 EleutherAIHarness 来测试你的模型（你可以添加 --limit 来限制每个任务的示例数）。 """

CITATION_BUTTON_LABEL = "复制以下代码引用这些结果"
CITATION_BUTTON_TEXT = r"""
"""
LOGOS = [
    "logo/HuggingFace.png",
    "logo/openai-logo.png",
    "logo/logo_qwen.png",
    "logo/CAIS.png"
]