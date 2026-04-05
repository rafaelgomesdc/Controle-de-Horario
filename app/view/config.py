import flet as ft

class Config_view():
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        ui_text = ft.Text(value="CONFIG PAGE")
        ui_home_button = ft.ElevatedButton("HOME", on_click=self.go_home)
        return ft.Column(
            [
                ui_text,
                ui_home_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    async def go_home(self, e):
        await self.page.push_route("/home")