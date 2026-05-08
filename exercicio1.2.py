import customtkinter as ctk

cliques=0

janela=ctk.CTk()
janela.geometry("300x400")
janela.title("O Botão Contador")


click = ctk.CTkLabel(
    janela, text = "👇 Clica no Botão 👇", font = ("Comic Sans MS", 50)        
)

click2 = ctk.CTkLabel(
    janela, text = f"Clique Detectados : {cliques}", font = ("Comic Sans MS", 40)
)

click.pack(pady=20)
click2.pack(pady=10)

def contar_cliques():
    global cliques 
    cliques +=1
    print(cliques)
    





janela.mainloop()