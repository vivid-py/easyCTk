import customtkinter as ctk
class App(ctk.CTk):
	def __init__(self, width: int=400, height: int=400, title: str="easyCTk App", resizable: bool=True):
		super().__init__()
		self.resizable(resizable,resizable)
		self.geometry(f"{width}x{height}")
		self.title(f"{title}")
	def button(self, text: str="Button",command: str=None, color: str="red", hover: str="darkred", row: int=0, column: int=0, method: str="pack"):
		btn = ctk.CTkButton(self, text=text, command = command, fg_color=color, hover_color=hover)
		if method == "pack":
			btn.pack()
		elif method == "grid":
			btn.grid(row=row, column=column, padx=10, pady=10)
		return btn
	def label(self, text: str = "Label"):
		label = ctk.CTkLabel(self, text=text )
		label.pack()
		return label
	def entry(self, placeholder_text: str="Entry"):
		entry = ctk.CTkEntry(self,placeholder_text=placeholder_text)
		entry.pack()
		return entry
	def checkbox(self, text: str="Checkbox"):
		checkbox = ctk.CTkCheckBox(self, text=text)
		checkbox.pack()
		return checkbox
	def run(self):
		self.mainloop()

a = App()

a.label("Label")
a.button("Button")
a.checkbox()
a.entry()

a.run()