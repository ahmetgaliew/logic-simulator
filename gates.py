# gates.py
# -----------------------------
# Модуль с описанием логических вентилей

class Gate:
    """Базовый класс логического вентиля"""
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.output = False

    def calculate(self):
        pass


class AndGate(Gate):
    def calculate(self):
        self.output = all(self.inputs)


class OrGate(Gate):
    def calculate(self):
        self.output = any(self.inputs)


class NotGate(Gate):
    def calculate(self):
        if len(self.inputs) != 1:
            raise ValueError("NOT gate должен иметь ровно один вход")
        self.output = not self.inputs[0]


class XorGate(Gate):
    def calculate(self):
        if len(self.inputs) != 2:
            raise ValueError("XOR gate должен иметь два входа")
        self.output = self.inputs[0] != self.inputs[1]
