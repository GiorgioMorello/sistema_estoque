from tkinter import *
from functions import WindowFunctions

class App(Tk, WindowFunctions):

    def __init__(self):
        super().__init__()
        self.title('Controle de Estoque')
        self.geometry('711x646')
        self.configure(background='#dddddd')
        self.canvas = Canvas(self.master, width=771, height=646)
        self.background_img = PhotoImage(file='img/background.png')

        self.img0 = PhotoImage(file='img/img0.png')
        self.btn_0 = Button(image=self.img0, command=self.visualizar_insumo, relief='flat')

        self.img1 = PhotoImage(file='img/img1.png')
        self.btn_1 = Button(image=self.img1, command=self.deletar_insumo, relief='flat')

        self.img2 = PhotoImage(file='img/img2.png')
        self.btn_2 = Button(image=self.img2, command=self.consumir_insumo, relief='flat')

        self.img3 = PhotoImage(file='img/img3.png')
        self.btn_3 = Button(image=self.img3, command=self.add_insumo, relief='flat')

        self.textbox_img = PhotoImage(file=f"img/img_textBox0.png")
        self.entry1_img = PhotoImage(file=f"img/img_textBox1.png")
        self.entry2_img = PhotoImage(file=f"img/img_textBox2.png")
        self.entry3_img = PhotoImage(file=f"img/img_textBox3.png")
        self.entry4_img = PhotoImage(file=f"img/img_textBox4.png")

        self.textbox = Text(bg="#ffffff", fg='#000000', highlightthickness=0)
        self.nome_insumo = Entry(bd=0, bg="#ffffff", highlightthickness=0)
        self.data_insumo = Entry(bd=0, bg="#ffffff", highlightthickness=0)
        self.lote_insumo = Entry(bd=0, bg="#ffffff", highlightthickness=0)
        self.qtde_insumo = Entry(bd=0, bg="#ffffff", highlightthickness=0)



    # pos: {x: val, y: val, width: val, height: val}
    def btn_place(self, btns: list):
        btn_places = [{'x': 479, 'y': 195, 'width': 178, 'height': 38},
                      {'x': 247, 'y': 197, 'width': 178, 'height': 36},
                      {'x': 479, 'y': 123, 'width': 178, 'height': 35},
                      {'x': 247, 'y': 125, 'width': 178, 'height': 34},
                      ]

        for i, btn in enumerate(btns):
            btn.place(x=btn_places[i]['x'],
                      y=btn_places[i]['y'],
                      width=btn_places[i]['width'],
                      height=btn_places[i]['height']
                      )

    def set_entry(self, entrys: list):
        entry_places = [{'x': 250, 'y': 502, 'width': 410, 'height': 114},
                        {'x': 377, 'y': 278, 'width': 280, 'height': 31},
                        {'x': 377, 'y': 324, 'width': 280, 'height': 31},
                        {'x': 377, 'y': 372, 'width': 280, 'height': 31},
                        {'x': 377, 'y': 420, 'width': 280, 'height': 31},
                        ]
        for i, entry in enumerate(entrys):
            entry.place(x=entry_places[i]['x'],
                        y=entry_places[i]['y'],
                        width=entry_places[i]['width'],
                        height=entry_places[i]['height'],
                        )

    def img_render(self, img_list: list):
        img_places = [{'x': 355.5, 'y': 323},
                      {'x': 455, 'y': 560},
                      {'x': 517, 'y': 294.5},
                      {'x': 517, 'y': 340.5},
                      {'x': 517, 'y': 388.5},
                      {'x': 517, 'y': 436.5},
                      ]

        for i, img in enumerate(img_list):
            self.canvas.create_image(img_places[i]['x'], img_places[i]['y'], image=img)




    def create_canvas(self):
        self.canvas.place(x=0, y=0)
        self.img_render([self.background_img, self.textbox_img,
                         self.entry1_img, self.entry2_img,
                         self.entry3_img, self.entry4_img])

        self.btn_place([self.btn_0, self.btn_1, self.btn_2, self.btn_3])
        self.set_entry([self.textbox, self.nome_insumo, self.data_insumo, self.lote_insumo, self.qtde_insumo])

        return self.canvas
