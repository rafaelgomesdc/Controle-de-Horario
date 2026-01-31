import flet as ft
from functions.clock import Start_counting, Second_counting

def view(page):
    page.title = "Projeto Controle de Horario"
    timer = ft.Text(value="0", size=50)
    bt_start = ft.ElevatedButton("Start", on_click=Start_counting)
    bt_stop = ft.ElevatedButton("Stop", on_click=Second_counting)
    page.add(
        timer,
        bt_start,
        bt_stop
    )
    page.update()

#

ft.app(target=view)