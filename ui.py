# ui.py
# -----------------------------
# Графический интерфейс симулятора на Tkinter

import tkinter as tk
from gates import AndGate, OrGate, NotGate, XorGate


class LogicSimulatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Симулятор логических вентилей")

        # Переменные для входов
        self.var_a = tk.BooleanVar()
        self.var_b = tk.BooleanVar()
        self.result = tk.StringVar()

        # Тип вентиля
        self.gate_type = tk.StringVar(value="AND")

        # Элементы интерфейса
        self.create_widgets()

        # Инициализация
        self.update_output()

    def create_widgets(self):
        tk.Label(self.root, text="Вход A:").grid(row=0, column=0, sticky="w")
        tk.Checkbutton(self.root, variable=self.var_a, command=self.update_output).grid(row=0, column=1)

        tk.Label(self.root, text="Вход B:").grid(row=1, column=0, sticky="w")
        tk.Checkbutton(self.root, variable=self.var_b, command=self.update_output).grid(row=1, column=1)

        # Меню выбора типа вентиля
        tk.Label(self.root, text="Тип вентиля:").grid(row=2, column=0, sticky="w")
        tk.OptionMenu(self.root, self.gate_type, "AND", "OR", "NOT", "XOR", command=lambda _: self.update_output()).grid(row=2, column=1)

        # Отображение результата
        tk.Label(self.root, text="Результат:").grid(row=3, column=0, sticky="w")
        tk.Label(self.root, textvariable=self.result, font=('Arial', 14, 'bold')).grid(row=3, column=1)

    def update_output(self):
        gate_type = self.gate_type.get()
        a = self.var_a.get()
        b = self.var_b.get()

        # Выбор нужного вентиля
        if gate_type == "AND":
            gate = AndGate("AND")
            gate.inputs = [a, b]
        elif gate_type == "OR":
            gate = OrGate("OR")
            gate.inputs = [a, b]
        elif gate_type == "NOT":
            gate = NotGate("NOT")
            gate.inputs = [a]  # Только один вход
        elif gate_type == "XOR":
            gate = XorGate("XOR")
            gate.inputs = [a, b]
        else:
            self.result.set("Ошибка")
            return

        # Вычисляем результат
        try:
            gate.calculate()
            self.result.set("1" if gate.output else "0")
        except Exception as e:
            self.result.set(f"Ошибка: {e}")
