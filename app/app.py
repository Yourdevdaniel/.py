import customtkinter as ctk

#fazer funções aqui
def button_callback():
    print("Botão pressionado")



app = ctk.CTk()
app.title("Meu aplicativo")
app.geometry("400x300")

button = ctk.CTkButton(app, text="meu botão", command=button_callback) #ctk.Ctkbutton(app, texto="texto do botao", command=função que o botão ira fazer)
button.grid(row=0, column=0, padx=20, pady=20)
app.grid_columconfigure(0, weight=1)





#final do loop
app.mainloop()


