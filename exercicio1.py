import customtkinter as ctk 

janela=ctk.CTk()
janela.geometry("600x400")

janela.title("Painel de Controle")

Sistema_Gestao = ctk.CTkLabel(
    janela, text="Sistema de Gestão", font=("Roboto",30, "bold")
)

Versao = ctk.CTkLabel(
    janela, text="Versão 1.0 - [Pablo]", font=("Roboto",14)
)

comandos = ctk.CTkLabel(
    janela, text="Aguardando comandos...", font=("Roboto",14)
)

Sistema_Gestao.pack(pady=30)
Versao.pack(pady=5)
comandos.pack(pady=5)


janela.mainloop()