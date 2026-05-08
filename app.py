import customtkinter as ctk 

janela=ctk.CTk()
janela.geometry("500x300")

boas_vindas = ctk.CTkLabel(
    janela, text="Olá mundo!", font=("Arial",24)
)

boas_vindas.pack(pady=20)

janela.mainloop()