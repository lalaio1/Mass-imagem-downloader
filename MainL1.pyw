import os
import requests
import customtkinter as ctk
from tkinter import END, messagebox
def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        with open(save_path, 'wb') as file:
            file.write(response.content)
        return True
    except Exception as e:
        print(f"Erro ao baixar a imagem: {e}")
        return False
def process_links():
    links = text.get("1.0", END).strip().split('\n')
    if not os.path.exists('imagens'):
        os.makedirs('imagens')
    total_links = len(links)
    text_status.delete('1.0', END)
    for i, link in enumerate(links, start=1):
        if link:
            filename = os.path.join('imagens', os.path.basename(link))
            try:
                if download_image(link, filename):
                    text_status.insert(END, f"({i}/{total_links}) Baixado: {link}\n")
                else:
                    text_status.insert(END, f"({i}/{total_links}) Erro ao baixar: {link}\n")
            except Exception as e:
                text_status.insert(END, f"({i}/{total_links}) Erro: {link} - {str(e)}\n")
            finally:
                text_status.see(END)

    messagebox.showinfo("Conclusão", "Processamento de links concluído!")
def disable_fullscreen(event):
    return "break"
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue") 
root = ctk.CTk()
root.title("Downloader de Imagens")
root.resizable(False, False)
root.bind("<F11>", disable_fullscreen)
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)
label = ctk.CTkLabel(master=frame, text="Insira os links das imagens (um por linha):")
label.pack(pady=12, padx=10)
text = ctk.CTkTextbox(master=frame, height=200)
text.pack(pady=12, padx=10)
btn_download = ctk.CTkButton(master=frame, text="Baixar Imagens", command=process_links)
btn_download.pack(pady=12, padx=10)
text_status = ctk.CTkTextbox(master=frame, height=200)
text_status.pack(pady=12, padx=10)
root.mainloop()
