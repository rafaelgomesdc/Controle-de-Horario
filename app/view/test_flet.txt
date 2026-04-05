import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def view(page: ft.Page):
    row = ft.Row()
    page.add(row)

    for i in range(100):
        row.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                width=100,
                height=100,
                #alignment=ft.alignment.Center,
                bgcolor=ft.Colors.AMBER_100,
                border=ft.border.all(2, ft.Colors.AMBER_600)
            )
            
        )

    page.update()

ft.app(target=view)