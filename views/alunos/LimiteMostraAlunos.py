import tkinter as tk
from tkinter import messagebox

class LimiteMostraAlunos():
    def __init__(self, lista):
        messagebox.showinfo("Lista de alunos", lista)