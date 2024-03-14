import flet as ft

def main(page: ft.Page):
    page.title = "Cajero automático"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    billetes = [10000, 20000, 50000, 100000]
    cantidad = [0, 0, 0, 0]
    retiro = 0
    cantidad_text1 = ft.Text(value=str(cantidad[0]))
    cantidad_text2 = ft.Text(value=str(cantidad[1]))
    cantidad_text3 = ft.Text(value=str(cantidad[2]))
    cantidad_text4 = ft.Text(value=str(cantidad[3]))

    opciones_retiro = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option(text="20.000", key="20000"),
            ft.dropdown.Option(text="50.000", key="50000"),
            ft.dropdown.Option(text="100.000", key="100000"),
            ft.dropdown.Option(text="200.000", key="200000"),
            ft.dropdown.Option(text="500.000", key="500000"),
            ft.dropdown.Option(text="1.000.000", key="1000000"),
        ],
    )

    def retirar(e):
        nonlocal retiro, cantidad, billetes
        nonlocal cantidad_text1, cantidad_text2, cantidad_text3, cantidad_text4
        if retiro > 0:
            for i in range(4):
                for j in range(i, 4):
                    if retiro >= billetes[j]:
                        retiro -= billetes[j]
                        cantidad[j] += 1
                    if retiro == 0:
                        break
                    if j == 3 and i == 3 and retiro > 0:
                        retirar(e)
        cantidad_text1.value = str(cantidad[0])
        cantidad_text2.value = str(cantidad[1])
        cantidad_text3.value = str(cantidad[2])
        cantidad_text4.value = str(cantidad[3])
        page.update()

    def before_retirar(e):
        nonlocal cantidad, retiro, opciones_retiro
        cantidad = [0, 0, 0, 0]
        if opciones_retiro.value is not None:
            retiro = int(opciones_retiro.value)
        else:
            retiro = 0
        retirar(e)    
    
    page.add(
        ft.Row([
            ft.Text("¿Cuanto desea retirar?", style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)),
            opciones_retiro,
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([   
            ft.Column([
                ft.Text("Billetes de 10.000"),
                cantidad_text1,
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Column([
                ft.Text("Billetes de 20.000"),
                cantidad_text2,
            ], alignment=ft.MainAxisAlignment.CENTER,),
            ft.Column([
                ft.Text("Billetes de 50.000"),
                cantidad_text3,
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Column([
                ft.Text("Billetes de 100.000"),
                cantidad_text4,
            ],alignment=ft.MainAxisAlignment.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.FloatingActionButton(text="Retirar", on_click= lambda e: before_retirar(e)),
    )

ft.app(target=main)