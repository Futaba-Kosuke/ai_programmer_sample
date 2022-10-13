from dataclasses import InitVar, dataclass, field
from typing import Any

import deepl

from abstracts import AbstractTranslator


@dataclass
class DeeplTranslator(AbstractTranslator):
    target_lang: str = "EN-US"
    api_key: InitVar[str] = None
    translator: Any = field(init=False)

    def __post_init__(self, api_key: str) -> None:
        self.translator = deepl.Translator(api_key)

    def translate(self, text: str, target_lang: str = None) -> str:
        if target_lang is None:
            target_lang = self.target_lang
        return self.translator.translate_text(text, target_lang=target_lang)
