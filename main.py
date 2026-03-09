import customtkinter as ctk
class App(ctk.CTk):
	def __init__(self, width: int=400, height: int=400, title: str="easyCTk App", resizable: bool=True):
		super().__init__()
		self.resizable(resizable,resizable)
		self.geometry(f"{width}x{height}")
		self.title(f"{title}")
	def button(self, text: str,command: None):
		btn = ctk.CTkButton(self, text=text, command = command)
		btn.pack()
		return btn
	def label(self, text: str):
		label = ctk.CTkLabel(self, text=text)
		label.pack()
		return label
	def entry(self, placeholder_text: str):
		entry = ctk.CTkEntry(self,placeholder_text=placeholder_text)
		entry.pack()
		return entry
	def checkbox(self):
		checkbox = ctk.CTkCheckBox(self)
		checkbox.pack()
		return checkbox

win = App()
win.mainloop()
