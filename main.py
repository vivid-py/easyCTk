import customtkinter as ctk
class App(ctk.CTk):
	def __init__(self, width: int, height: int, title: str, resizable: bool):
		super().__init__()
		self.resizable(resizable,resizable)
		self.geometry(f"{width}x{height}")
		self.title(f"{title}")
	def button(self, text: str,command: None):
		btn = ctk.CTkButton(self, text=text, command = command)
		return btn
	def label(self, text: str):
		label = ctk.CTkLabel(self, text=text)
		return label

