import os
import sys
from typing import Optional

from dotenv import load_dotenv

from my_deepl import DeeplTranslator
from my_openai import OpenAiGenerator

load_dotenv()

translator_api_key: Optional[str] = os.getenv("TRANSLATOR_API_KEY")
generator_api_key: Optional[str] = os.getenv("GENERATOR_API_KEY")

if translator_api_key is None or generator_api_key is None:
    print("API_KEY enviroment variable is Not Found")
    sys.exit()

translator = DeeplTranslator("EN-US", translator_api_key)
generator = OpenAiGenerator(generator_api_key)

input_text: str = input("prompt >> ")
prompt_en: str = str(translator.translate(input_text))
completion = generator.generate(prompt_en)

print("=== Result ===")
print(completion.choices[0].text)
