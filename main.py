# main.py
# -----------------------------
# Точка входа в программу

import tkinter as tk
from ui import LogicSimulatorApp

def main():
    root = tk.Tk()
    app = LogicSimulatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
