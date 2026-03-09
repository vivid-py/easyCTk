import customtkinter as ctk



class App(ctk.CTk):
	def __init__(self, width: int, height: int, title: str):
		super().__init__()
		self.geometry(f"{width}x{height}")
		self.title(f"{title}")

win = App(400,400, "hz")

win.mainloop()