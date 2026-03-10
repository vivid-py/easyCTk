import customtkinter as ctk
class App(ctk.CTk):
	def __init__(self, width: int=400, height: int=400, title: str="easyCTk App", resizable: bool=True):
		super().__init__()
		self.resizable(resizable,resizable)
		self.geometry(f"{width}x{height}")
		self.title(f"{title}")
	def _applyLayout(self, row: int=0, column: int=0, method: str="pack", widget: str=""):
		if method == "grid":
			widget.grid(row=row, column=column, padx=10, pady=10)
		elif method == "pack":
			widget.pack()	
	def button(self, text: str="Button",command: str=None, color: str="red", hover: str="darkred", method: str="pack", row: int=0, column: int=0):
		btn = ctk.CTkButton(self, text=text, command = command, fg_color=color, hover_color=hover)
		self._applyLayout(widget=btn, method=method, column=column, row=row)
		return btn
	def label(self, text: str = "Label", method: str="pack", column: int=0, row: int=0):
		label = ctk.CTkLabel(self, text=text )
		self._applyLayout(widget=label, method=method, column=column, row=row)
		return label
	def entry(self, placeholder_text: str="Entry", method: str="pack", column: int=0, row: int=0):
		entry = ctk.CTkEntry(self,placeholder_text=placeholder_text)
		self._applyLayout(widget=entry, method=method, column=column, row=row)
		return entry
	def checkbox(self, text: str="Checkbox", method: str="pack", column: int=0, row: int=0):
		checkbox = ctk.CTkCheckBox(self, text=text, )
		self._applyLayout(widget=checkbox, method=method, column=column, row=row)
		return checkbox
	def switch(self, text: str="Switch", method: str="pack", column: int=0, row: int=0):
		switch = ctk.CTkSwitch(self, text=text)
		self._applyLayout(widget=switch, method=method, column=column, row=row)
		return switch
	def run(self):
		self.mainloop()
