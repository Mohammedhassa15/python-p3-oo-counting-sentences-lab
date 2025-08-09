import re

class MyString:
    def __init__(self, value=""):
        self._value = None
        self.value = value  # Uses setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return isinstance(self.value, str) and self.value.endswith(".")

    def is_question(self):
        return isinstance(self.value, str) and self.value.endswith("?")

    def is_exclamation(self):
        return isinstance(self.value, str) and self.value.endswith("!")

    def count_sentences(self):
        if not self.value or not isinstance(self.value, str):
            return 0
        sentences = re.split(r'[.!?]+', self.value.strip())
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
