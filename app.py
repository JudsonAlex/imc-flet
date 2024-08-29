import flet as ft

from tabelaIMC import TabelaIMC
from sectionsIMC import SectionIMC

class App(ft.Column):
    def __init__(self):
        super().__init__()
        self.width = 400
        self.altura = ft.TextField(hint_text="altura", expand=True)
        self.peso = ft.TextField(hint_text="peso", expand=True)
        self.imc = ft.Text('', size=25, weight="BOLD")
        self.button = ft.FloatingActionButton("calcular", width=400, on_click=self.calc_imc)
        self.tabela = TabelaIMC().getTabela()
        self.view2 = SectionIMC()
        self.changed_line = 0
        self.controls = [
            ft.Column(
                controls=[
                    ft.Text("Calcule seu IMC", size=30),
                    ft.Row(
                        controls=[
                            self.altura,
                            self.peso,
                        ]
                    ),
                    self.button,
                    self.imc,
                    self.tabela,
                    self.view2

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]


    def calc_imc(self, e):
        self.imc.value =round(float(self.peso.value) / float(self.altura.value)**2, 2)
        print(self.imc.value)
        self.tabela.visible = True
        self.tabela.rows[self.changed_line].color = ft.colors.WHITE


        if self.imc.value < 18.5:
            self.tabela.rows[0].color = ft.colors.AMBER_100
            self.changed_line = 0
        elif 18.5 < self.imc.value < 24.9:
            self.changed_line = 1
            self.tabela.rows[1].color = ft.colors.GREEN_100
        elif 25 < self.imc.value < 29.9:
            self.changed_line = 2
            self.tabela.rows[2].color = ft.colors.AMBER_100
        elif 30 < self.imc.value < 39.9:
            self.changed_line = 3
            self.tabela.rows[3].color = ft.colors.RED_200
        else:
            self.changed_line = 4
            self.tabela.rows[4].color = ft.colors.RED_400


        #self.imc.value ="IMC: " + str(self.imc.value)
        self.view2 = SectionIMC(self.imc.value)
        self.update()


def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 400
    page.update()


    calculadora = App()

    page.add(calculadora)

ft.app(main)

    
        