import customtkinter as ctk



class App(ctk.CTk):
	def __init__(self, width: int, height: int, title: str):
		super().__init__()
		self.geometry(f"{width}x{height}")
		self.title(f"{title}")
	def button(self,master: str, text: str, command: None):
		btn = ctk.CTkButton(master= master, text=text, command = command)
		return btn
win.button(win, "Button", None).pack()
win = App(400,400, "hz")

win.mainloop()