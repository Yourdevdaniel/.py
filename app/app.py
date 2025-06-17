import customtkinter as ctk


class App(ctk.ctk):
    def __init__(self):
        super().__init__()
#fazer funções aqui
def button_callback():
    print("Botão pressionado")



app = ctk.CTk()
app.title("Meu aplicativo")
app.geometry("400x300")

button = ctk.CTkButton(app, text="meu botão", command=button_callback) #ctk.Ctkbutton(app, texto="texto do botao", command=função que o botão ira fazer)
button.grid(row=0, column=0, padx=20, pady=20)
app.grid_columnconfigure(0, weight=1)

checkbox_1 = ctk.CTkCheckBox(app, text="checkbox")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = ctk.CTkCheckBox(app, text="checkbox2")
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

#final do loop
app.mainloop()


