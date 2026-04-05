import flet as ft

class Home_view():
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        ui_text = ft.Text(value="HOME PAGE")
        ui_config_button = ft.ElevatedButton("CONFIG", on_click=self.go_config)
        return ft.Column(
            [
                ui_text,
                ui_config_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    async def go_config(self, e):
        await self.page.push_route("/config")