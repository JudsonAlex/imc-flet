import flet as ft


class SectionIMC(ft.Column):
    def __init__(self, imc="0.00") -> None:
        super().__init__()
        self.imc = imc
        print("o valor é", self.imc)
        self.resultado = ft.Column(
            controls=[
                ft.Text("Seu IMC é:"),
                ft.Text(f'{self.imc}')
            ]   
        )
        self.secoes = ft.Row(
        
            controls=[
                ft.Column(
                    controls=[
                        ft.Text('< 18.5'),
                        ft.Container(ft.Text("Abaixo do peso"))
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Text("18.5 - 24.9"),
                        ft.Container(ft.Text("Peso normal"))
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Text("25 - 29.9"),
                        ft.Container(ft.Text("Sobrepeso"))
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Text("30 - 39.9"),
                        ft.Container(ft.Text("Obesidade"))
                    ]
                ),
            ]
        )
        self.controls=[
            self.resultado,
            self.secoes
        ]