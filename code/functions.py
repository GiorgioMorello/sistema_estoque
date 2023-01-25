from tkinter import Text, END
import pyodbc
from unidecode import unidecode




class SupFunctions(Text):


    def check_fields(self, data_v, lote, qtde):
        if data_v and lote and qtde:
            return True

    def clear_name(self, name: str):
        clean_name = unidecode(name.title())
        return clean_name

    def text_field(self, text: str, type_text=None):

        if type_text == 'success':
            caixa_texto = Text(
                bd=0,
                bg="#ffffff",
                fg='#00af06',
                highlightthickness=0)

        elif type_text == 'error':
            caixa_texto = Text(
                bd=0,
                bg="#ffffff",
                fg="#ff0000",
                highlightthickness=0)

        caixa_texto.place(
            x=250, y=502,
            width=410,
            height=114
        )

        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", f"{text}")

    def check_name(self, name):
        if len(name) < 2:
            self.text_field(f'O insumo {name} é inválido', type_text='error')
            return True


class DataBaseMixin:
    dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                     "Server=localhost;"
                     "Database=Estoque.db")

    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()



    def inserir(self, item, qtde, data, lote):
        self.cursor.execute(f"""
            INSERT INTO Estoque (Produto, Quantidade, DataValidade, Lote)
            VALUES ('{item}', {qtde}, '{data}', {lote})
        """)
        self.cursor.commit()





    def deletar(self, item, lote):
        self.cursor.execute(f"""
            DELETE FROM Estoque WHERE Produto='{item}' AND Lote={lote}
            """)
        self.cursor.commit()




    def update(self, item, lote, qtde):
        self.cursor.execute(f"""
                UPDATE Estoque SET Quantidade=Quantidade-{qtde}
                WHERE Produto='{item}' AND Lote={lote}
                """)
        self.cursor.commit()



    def read(self, item):
        self.cursor.execute(f"""
                   SELECT * FROM Estoque WHERE Produto='{item}'
                   """)

        dados = self.cursor.fetchall()
        cols = [cols[0] for cols in self.cursor.description]
        return dados, cols


    def check_data(self, item, lote):
        self.cursor.execute(f"""SELECT Produto, Lote FROM Estoque WHERE Produto='{item}' AND Lote={lote}""")
        dados = self.cursor.fetchall()
        if dados:
            return True


    def close_c(self):
        self.cursor.close()
        self.conexao.close()


class WindowFunctions(DataBaseMixin, SupFunctions):

    def add_insumo(self):
        clean_name = self.clear_name(self.nome_insumo.get())
        if self.check_name(clean_name):
            return

        if not self.check_fields(self.data_insumo.get(), self.lote_insumo.get(), self.qtde_insumo.get()):
            self.text_field(f'Preencha todos os campos', type_text='error')
            return

        if self.check_data(clean_name, self.lote_insumo.get()):
            self.text_field('Insumo de mesmo nome e lote já existente', type_text='error')
            return

        try:
            self.inserir(clean_name, self.qtde_insumo.get(), self.data_insumo.get(), self.lote_insumo.get())
            self.text_field(f'O insumo {clean_name} foi adicionado com sucesso', type_text='success')

        except:
            self.text_field('Preencha o formulário novamente', type_text='error')

        return



    def consumir_insumo(self):
        """
        Para consumir um insumo vc deve preencher apenas o campo de nome do insumo, lote
        e a quantidade que quer consumir
        """
        clean_name = self.clear_name(self.nome_insumo.get())

        if len(clean_name) < 2 or len(self.lote_insumo.get()) < 1:
            self.text_field('Insumo Inválido. Digite novamente', type_text='error')
            return

        try:
            self.update(clean_name, self.lote_insumo.get(), self.qtde_insumo.get())

            self.text_field(f'O insumo {clean_name} foi consumido em {self.qtde_insumo.get()} unidades',
                            type_text='success')
        except:
            self.text_field(f'Não foi possivel consumir o insumo. Digite ', type_text='error')




    def deletar_insumo(self):
        """
        Para deletar um insumo vc deve preencher somente o campo do nome do insumo e o número do lote
        """
        clean_name = self.clear_name(self.nome_insumo.get())

        if self.check_name(clean_name):
            return

        try:
            self.deletar(clean_name, self.lote_insumo.get())

            self.text_field(f'O insumo {self.nome_insumo.get().title()} foi excluido com sucesso', type_text='success')
        except:
            self.text_field('O nome ou número de lote inválido. Digite novamente', type_text='error')
            return

        return




    def visualizar_insumo(self):
        clean_name = self.clear_name(self.nome_insumo.get())
        if self.check_name(clean_name):
            return

        try:
            dados, cols = self.read(clean_name)
            text = ""
            # (14, 'Papel', 200.0, '2030-12-20', 32)

            if not dados:
                self.text_field('Insumo não encontrado. Digite novamente', type_text='error')
                return

            for _, nome, qtde, data_v, lote in dados:
                text += f"{cols[1]}: {nome}\n{cols[2]}: {int(qtde)}\n{cols[3]}: {data_v}\n{cols[4]}: {lote}\n\n"

            self.text_field(text, type_text='success')

        except:
            self.text_field(f'Não foi possivel encontrar o insumo de nome {self.nome_insumo.get()} ', type_text='error')


        return
