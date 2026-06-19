from openai import OpenAI
from g4f.client import Client
from g4f.Provider import Yqcloud , OIVSCode , Dynaspark , MetaAI, TeachAnything, DeepInfraChat, PollinationsAI

# client_1 = OpenAI(api_key="API_KEY_HERE", base_url="https://openrouter.ai/api/v1")
# client_2 = OpenAI(api_key="API_KEY_HERE", base_url="https://api.deepseek.com")
class DeepSeek :
    def __init__(self):
        self.client = OpenAI(
            api_key="API_KEY_HERE", 
            base_url="https://openrouter.ai/api/v1")

    def genCode(self, improved_prompt):
        response = self.client.chat.completions.create(
        model= "deepseek/deepseek-r1:free",
        messages=[
                    
                    {"role": "system",
                    "content": (
                        "You are a professional Python developer who strictly outputs only executable code.\n"
                        "NEVER use HTML, JS, or any non-Python language.\n"
                        "When given a prompt, return ONLY the full, runnable Python script as a string, using correct syntax and indentation.\n"
                        "Do not include:\n"
                        "- Markdown blocks like ```python\n"
                        "- Any explanations, comments, titles, or extra messages\n"
                        "- Print statements regarding functionality\n\n"
                        "You are generating code that will be directly executed using Python's `exec()` function.\n"
                        "The code *only* involve libraries such as pygame, turtle, or matplotlib or depending on the request.\n"
                        "Assume the required library is already installed.\n"
                        "End the code cleanly — do not append anything after the program finishes."
                    )},
                    {"role": "user",
                    "content": f"Write a complete Python script using pygame/matplotlib/turtle to {improved_prompt}. Return ONLY the code, nothing else."}],
        
        ) 
        final =  response.choices[0].message.content
        print(final)
        return final

    def genPrompt(self, user_input):
        system_prompt = """ You are an expert in scientific programming and simulation with Python.

                            Your task is to rephrase and expand vague animation or simulation descriptions into detailed, structured programming **prompts**specifically for code generation.

                            Make sure the prompt:
                            - Clearly states the type of animation or simulation (e.g., physics, graph, visual effect)
                            - Breaks the task into sequential steps or logic (1., 2., 3., etc.)
                            - Mentions the correct Python libraries to be used (e.g., pygame, matplotlib, turtle)
                            - Defines conditions, transitions, or stopping rules precisely
                            

                            Only output the improved **prompt** as a **single-line string**, ready for LLM code generation. No explanations.
                            """

        response = self.client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ]
        )

        improved_prompt = response.choices[0].message.content.strip()
        print("🔁 Rewritten Prompt:\n", improved_prompt)
        return self.genCode(improved_prompt)
    
    
class  ChatGPT:

    def genCode(self, improved_prompt,provider_cls, m):

        response = Client(provider=provider_cls).chat.completions.create(
        model= m,
        messages=[
                    
                    {"role": "system",
                    "content": (
                        "You are a professional Python developer who strictly outputs only executable code.\n"
                        "NEVER use HTML, JS, or any non-Python language.\n"
                        "When given a prompt, return ONLY the full, runnable Python script as a string, using correct syntax and indentation.\n"
                        "Do not include:\n"
                        "- Markdown blocks like ```python\n"
                        "- Any explanations, comments, titles, or extra messages\n"
                        "- Print statements regarding functionality\n\n"
                        "You are generating code that will be directly executed using Python's `exec()` function.\n"
                        "The code *only* involve libraries such as pygame, turtle, or matplotlib depending on the request.\n"
                        "Assume the required library is already installed.\n"
                        "End the code cleanly — do not append anything after the program finishes."
                    )},
                    {"role": "user",
                    "content": f"Write a complete Python script using pygame/matplotlib/turtle to {improved_prompt}. Return ONLY the code, nothing else."}],
        
        ) 
        final =  response.choices[0].message.content
        print(final)
        return final



    def genPrompt(self, user_input,provider_cls,m):
        system_prompt = """ You are an expert in scientific programming and simulation with Python.

                            Your task is to rephrase and expand vague animation or simulation descriptions into detailed, structured programming **prompts**specifically for code generation.

                            Make sure the prompt:
                            - Clearly states the type of animation or simulation (e.g., physics, graph, visual effect)
                            - Breaks the task into sequential steps or logic (1., 2., 3., etc.)
                            - Mentions the correct Python libraries to be used (e.g., pygame, matplotlib, turtle)
                            - Defines conditions, transitions, or stopping rules precisely
                            

                            Only output the improved **prompt** as a **single-line string**, ready for LLM code generation. No explanations.
                            """

        response = Client(provider=provider_cls).chat.completions.create(
            model= m,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ]
        )

        improved_prompt = response.choices[0].message.content.strip()
        print("🔁 Rewritten Prompt:\n", improved_prompt)
        return self.genCode(improved_prompt, provider_cls,m)

deepseek_engiene = DeepSeek()
chatgpt_engiene = ChatGPT()


while True:
    print('''Models:\n  1.Deepseek (More accurate , slow)\n  2.Other (Can cause error, fast)\n\n''')
    try:
        option1 = int(input("Choose a model (1 / 2): "))
        match option1 :
            case 1:
                user_input = input("\n🎬 Describe your animation: " )
                result = deepseek_engiene.genPrompt(user_input)
            case 2:
                print ("Select model:\n 1.gpt-4\n 2.gemini-1.5-pro\n")
                try:
                    option2 = int(input("Enter 1 / 2 : "))
                    user_input = input("\n🎬 Describe your animation: " )
                    match option2:
                        case 1:
                            result = chatgpt_engiene.genPrompt(user_input, "Yqcloud", "gpt-4")
                        case 2:
                            result = chatgpt_engiene.genPrompt(user_input, "TeachAnything", "gemini-1.5-pro")
                        case _:
                            print("\nInvalid input")
                except ValueError:
                    continue
            case _:
                print("\nInvalid input")

        code= result.strip("```python").strip("```").strip()

        try:
            exec (code)

        except Exception as e:
            print("🔥 Code execution failed:")
            print(e)
    except:
        continue
