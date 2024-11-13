---
title: 🌐 Multilingual MMLU Benchmark Leaderboard
emoji: 🏆
colorFrom: pink
colorTo: purple
sdk: gradio
app_file: app.py
pinned: true
license: apache-2.0
description: "Compare multilingual models on the MMLU benchmark leaderboard across languages and tasks"
tags:
  - multilingual
  - benchmark
  - MMMLU
  - leaderboard
  - machine learning
---

# Multilingual MMLU Benchmark Leaderboard

Welcome to the **Multilingual MMLU Benchmark Leaderboard**! This leaderboard is designed to assess the performance of both open-source and closed-source language models on the **Multilingual MMLU (Massive Multitask Language Understanding)** benchmark. The benchmark evaluates the memorization, reasoning, and linguistic capabilities of models across a wide range of languages, making it a crucial tool for comparing multilingual AI performance.

## Overview

The **Multilingual MMLU Benchmark** is a comprehensive evaluation platform for AI models, assessing their general knowledge and ability to handle diverse tasks across **57 distinct domains**. These tasks range from elementary-level knowledge to more advanced subjects such as law, physics, history, and computer science. With this leaderboard, we aim to provide an accessible and reliable way for developers, researchers, and organizations to compare language models' multilingual understanding and reasoning abilities.

## Evaluation Scope

### Key Features:
- **Multilingual Coverage**: The leaderboard evaluates language models on **14 different languages**, including widely spoken languages such as English, Spanish, Arabic, and Chinese, as well as languages with fewer resources like Swahili and Yoruba.
- **Diverse Domains**: The benchmark includes tasks across 57 domains, ensuring that models are tested on a wide range of topics, from elementary knowledge to complex professional fields.
- **Comprehensive QA Tasks**: The evaluation focuses on **Question Answering (QA)** tasks, where models answer questions based on general knowledge in various domains. This helps assess both the depth and breadth of the model's knowledge.
  
### Languages Covered:
The leaderboard includes models evaluated on the following languages:

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

## How It Works

### Submitting Models
To evaluate your model on the Multilingual MMLU Benchmark, you can submit it through the **"Submit here"** tab on the leaderboard. The evaluation process will run your model through a series of tests across the 57 domains in the 14 supported languages. Results will be provided on the leaderboard, with detailed scores for each language and domain.

### Evaluation Process
We use the **OpenCompass framework** to automate the evaluation process. This framework enables efficient execution of multiple tests across different languages and domains, ensuring scalability and reproducibility. The following is the evaluation setup:

- **Evaluation Method**: All tasks are evaluated using a 5-shot setting.
- **Normalization**: Results are normalized using the following formula:
  ```plaintext
  normalized_value = (raw_value - random_baseline) / (max_value - random_baseline)

## Evaluation Details

### For Generative Tasks:
- **Random Baseline**: `random_baseline = 0`

### For Multiple-Choice QA Tasks:
- **Random Baseline**: `random_baseline = 1/n`, where `n` is the number of choices.

### Aggregated Results:
Scores for each language are averaged across all tasks to provide a comprehensive model evaluation.

## Results

- **Numerical Results**: You can access the detailed evaluation results in the [results dataset](#).
- **Community Queries**: Track ongoing tasks and request status in the [requests dataset](#).

## Reproducibility

To ensure reproducibility, we provide a fork of the **lm_eval** framework, which allows you to recreate the evaluation setup and results on your own models. While not all contributions are integrated into the main repository, our fork contains all the necessary updates for evaluation.

For detailed setup instructions and to reproduce results on your local machine, please refer to our [lm_eval fork](#).

## Acknowledgements

This leaderboard was developed as part of the **#ProjectName**, led by **[OrganizationName]**, and has benefited from the support of high-quality evaluation datasets donated by the following institutions:

- [Institution 1]
- [Institution 2]
- [Institution 3]
- [Institution 4]
- [Institution 5]
- [Institution 6]
- [Institution 7]

We also thank **[Institution1]**, **[Institution2]**, and **[Institution3]** for sponsoring inference GPUs, which were crucial for running the large-scale evaluations.

### Special Thanks to the Contributors:
- **Task Implementation**: [Name1], [Name2], [Name3]
- **Leaderboard Implementation**: [Name4], [Name5]
- **Model Evaluation**: [Name6], [Name7]
- **Communications**: [Name8], [Name9]
- **Organization & Collaboration**: [Name10], [Name11], [Name12]

For more information on the datasets, please refer to the **Dataset Cards** available in the "Tasks" tab and the **Citations** section below.

## Collaborate

We are always looking for collaborators to expand the range of evaluated models and datasets. If you would like us to include your evaluation dataset or contribute in any other way, please feel free to get in touch!

Your feedback, suggestions, and contributions are more than welcome! Visit our **[Community Page]** to share your thoughts, or feel free to open a pull request (PR).

Thank you for your interest in the **Multilingual MMLU Benchmark Leaderboard**. Let’s work together to advance multilingual AI capabilities!

For more details on dataset authors and dataset cards, please refer to the "Tasks" tab.