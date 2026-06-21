
<div align="center">

# AniForge

**An AI-powered CLI tool to instantly generate and execute Python animations and simulations.**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-API-412991.svg?logo=openai&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

---

## Overview

**AniForge** is a command-line application that acts as your personal technical animator. You simply describe the simulation or visual effect you want to see, and AniForge uses Large Language Models (LLMs) to write and execute the Python code on the fly. 

It utilizes a robust two-step pipeline:
1. **Prompt Engineering:** It first takes your vague description and expands it into a highly detailed, step-by-step programming prompt.
2. **Code Generation & Execution:** It feeds the refined prompt back into the LLM to generate pure, executable Python code (using `pygame`, `turtle`, or `matplotlib`), which is then instantly run on your machine.

## Features

* **Multi-Model Support:** Choose between DeepSeek-R1 (via OpenRouter) for highly accurate reasoning, or GPT-4/Gemini-1.5-Pro (via g4f providers) for faster generation.
* **Auto-Refining Prompts:** Never worry about writing perfect prompts. AniForge acts as an expert scientific programmer to expand your simple ideas into rigid functional specifications before generating the code.
* **Instant Execution:** Bypasses the copy-paste loop. The generated code is cleaned and executed immediately right in your terminal.
* **Library Flexibility:** Automatically utilizes the best tool for the job, whether it's 2D game graphics (`pygame`), simple drawings (`turtle`), or scientific graphing (`matplotlib`).

## Security Warning

**Use with caution.** This application uses Python's `exec()` function to run AI-generated code directly on your machine. While the system prompts instruct the LLM to only write visual animations, you should never run AI-generated code with elevated/administrator privileges, as LLMs can hallucinate unpredictable commands.

## Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/AniForge.git](https://github.com/yourusername/AniForge.git)
cd AniForge

```

**2. Install dependencies**
Make sure you have the required AI clients and graphical libraries installed:

```bash
pip install openai g4f pygame matplotlib

```

*(Note: `turtle` is included in the standard Python library).*

**3. Configure your API Keys**
Open the `aniforge.py` (or whatever you named the script) file and replace the placeholder API key in the `DeepSeek` class with your actual OpenRouter API key:

```python
self.client = OpenAI(
    api_key="YOUR_OPENROUTER_API_KEY_HERE", 
    base_url="[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)"
)

```

## Usage

Run the script from your terminal:

```bash
python aniforge.py

```

**Example Workflow:**

1. The CLI will prompt you to choose a model:
```text
Models:
 1.Deepseek (More accurate, slow)
 2.Other (Can cause error, fast)

Choose a model (1 / 2): 1

```


2. Describe your desired animation:
```text
🎬 Describe your animation: a solar system simulation with earth and mars orbiting the sun

```


3. Watch as AniForge rewrites your prompt into a technical specification, generates the code, and launches the animation window instantly!

## 🤝 Contributing

Contributions are welcome! If you want to add support for more free providers in the `g4f` pipeline, improve the prompt-engineering instructions, or add safety sandboxing for the `exec()` function, or anything, feel free to open a pull request.

## 📄 License

This project is licensed under the [MIT License]

