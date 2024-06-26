from tkinter import *
from PIL import ImageTk, Image
import requests, json

user=""
bearer=""
api_link="http://127.0.0.1:8000/"
class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        #self.window.state('zoomed')
        self.window.title('SARA')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\agua.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "Bem-Vindo a SARA"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Login", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Nome de usuário", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)


    
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Senha", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.login_action)
        self.login.place(x=20, y=10)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def login_action(self):
        global user, bearer, api_link
        user = self.username_entry.get()
        r = requests.post(api_link+"/api/v1/login/access-token", data={"username":user,"password":self.password_entry.get()})
        if(r.status_code==200):
            bearer= r.json()['access_token']
            clear_screen(self.window)
            GraphsPage(self.window)
        else:
            self.sign_label = Label(self.lgn_frame, text='Usuário e senha não encontrado', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='red')
            self.sign_label.place(x=600, y=520)


class GraphsPage:
    global api_link
    def __init__(self, window):
        global user, bearer
        self.window = window
        # Background image
        self.bg_frame = Image.open('images\\agua.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        #self.bg_panel.pack(fill='both', expand='yes')
        # Layout
        self.toolbar = Frame(self.window, bg="white", height=30)
        self.sidepanel = Frame(self.window, bg='#13209c')
        self.main = Frame(self.window, bg="grey")

        self.window.grid_rowconfigure(1, weight=1, uniform=True)
        self.window.grid_columnconfigure(0, weight=1, uniform=True)
        self.window.grid_columnconfigure(1, weight=3, uniform=True)

        self.warnings_buton = Label(self.sidepanel, bg='#13209c',height=4, width=291)
        self.warnings_buton.place(x=0, y=0)
        self.warnings = Button(self.warnings_buton, text='Avisos', font=("yu gothic ui", 13, "bold"), width=26, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.avisos)
        self.warnings.place(x=10, y=10)

        self.graph_1_buton = Label(self.sidepanel, bg='#13209c',height=4, width=291)
        self.graph_1_buton.place(x=0, y=60)
        self.graph_1 = Button(self.graph_1_buton, text='Estação 1', font=("yu gothic ui", 13, "bold"), width=26, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.graph_1_show)
        self.graph_1.place(x=10, y=10)

        self.graph_2_buton = Label(self.sidepanel, bg='#13209c',height=4, width=291)
        self.graph_2_buton.place(x=0, y=120)
        self.graph_2 = Button(self.graph_2_buton, text='Estação 2', font=("yu gothic ui", 13, "bold"), width=26, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.graph_2_show)
        self.graph_2.place(x=10, y=10)

        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.sidepanel.grid(row=1, column=0, sticky="nsew")
        self.main.grid(row=1, column=1, sticky="nsew")

    def populate_toolbar(self, titulo):
        clear_screen(self.toolbar)
        self.warnings_titulo = Label(self.toolbar, text=f"{titulo} - Logado como {user}", bg="#FFF", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.warnings_titulo.place(x=0, y=0)

    def avisos(self):
        self.populate_toolbar("Avisos")
        clear_screen(self.main)
        self.warnings_text = Label(self.main, text="sadasdasdasdsa", bg='#13209c', fg="#6b6a69",height=4, width=291,font=("yu gothic ui", 13, "bold"))
        self.warnings_text.place(x=0, y=0)

    def graph_1_show(self):
        self.populate_toolbar("Estação 1")
        r = requests.post(api_link+"/api/v1/station/get_station_data?station_id=1&skip=0&limit=100",headers={'Authorization': f'Bearer {bearer}'})
        print(r.json())
        clear_screen(self.main)
        self.graph_1_image = Image.open('images\\graph.png')
        photo = ImageTk.PhotoImage(self.graph_1_image)
        self.graph_1_image_label = Label(self.main, image=photo, bg='#040405')
        self.graph_1_image_label.image = photo
        self.graph_1_image_label.place(x=10, y=10)
    
    def graph_2_show(self):
        self.populate_toolbar("Estação 2")
        clear_screen(self.main)
        self.graph_2_image = Image.open('images\\graph2.png')
        photo = ImageTk.PhotoImage(self.graph_2_image)
        self.graph_2_image_label = Label(self.main, image=photo, bg='#040405')
        self.graph_2_image_label.image = photo
        self.graph_2_image_label.place(x=10, y=10)
        

def clear_screen(window):
    for child in window.winfo_children():
        child.destroy()

def page():
    window = Tk()
    photo = PhotoImage(file = 'images\\icon.png')
    window.wm_iconphoto(False, photo)
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()