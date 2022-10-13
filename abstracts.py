from abc import ABC, abstractmethod
from dataclasses import InitVar, dataclass
from typing import Any


@dataclass
class AbstractTranslatorMixin:
    target_lang: str
    api_key: InitVar[str]
    translator: Any


class AbstractTranslator(ABC, AbstractTranslatorMixin):
    @abstractmethod
    def translate(self, text: str, target_lang: str) -> str:
        return ""


@dataclass
class AbstractGeneratorMixin:
    api_key: InitVar[str]
    completion: Any


class AbstractGenerator(ABC, AbstractGeneratorMixin):
    @abstractmethod
    def generate(self, prompt: str) -> Any:
        return {}
