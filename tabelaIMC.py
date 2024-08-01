import flet as ft

class TabelaIMC():

    def __init__(self):
        self.tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("IMC", color=ft.colors.INDIGO_300)),
                ft.DataColumn(ft.Text("Classificação", color=ft.colors.INDIGO_200)),
            ],
            rows=[
                ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Menor que 18.5")),
                            ft.DataCell(ft.Text("Magreza"))
                        ],
                        color=ft.colors.WHITE
                ),
                ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Entre 18.5 e 24.9")),
                            ft.DataCell(ft.Text("Normal"))
                        ],
                        color=ft.colors.WHITE
                ),
                ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Entre 25 e 29.9")),
                            ft.DataCell(ft.Text("Sobrepeso"))
                        ],
                        color=ft.colors.WHITE
                ),
                ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Entre 30 e 39.9")),
                            ft.DataCell(ft.Text("Obesidade"))
                        ],
                        color=ft.colors.WHITE
                ),
                ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Maior que 40")),
                            ft.DataCell(ft.Text("Obesidade Grave"))
                        ],
                        color=ft.colors.WHITE
                ),
            ],
            visible=False,
            border=ft.border.all(1, ft.colors.with_opacity(0.2, ft.colors.BLACK)),
            vertical_lines=ft.BorderSide(1, ft.colors.with_opacity(0.2, ft.colors.BLACK))
        )
    
    def getTabela(self):
        return self.tabela