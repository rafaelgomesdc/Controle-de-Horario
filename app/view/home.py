import flet as ft
import asyncio

class Home_view():
    def __init__(self, page: ft.Page):
        self.page = page
        self.running = False;
        self.time = 3600

    def build(self):
        self.ui_clock = ft.Text(value="00:00:00")
        self.ui_bt_clock = ft.ElevatedButton("CLOCK", on_click=self.Clock_Start)
        self.ui_config_button = ft.ElevatedButton("CONFIG", on_click=self.go_config)
        return ft.Column(
            [
                self.ui_clock,
                self.ui_bt_clock,
                self.ui_config_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    async def Run_Clock(self):
        while self.running:
            self.time -= 1

            h = self.time // 3600
            m = (self.time % 3600) // 60
            s = self.time % 60

            self.ui_clock.value = f"{h:02}:{m:02}:{s:02}"
            self.page.update()
            await asyncio.sleep(1)
    
    def Clock_Start(self, e):
        if not self.running:
            self.running = True
            self.page.run_task(self.Run_Clock)
        elif self.running:
            self.running = False
    
    def Clock_Stop(self, e):
        if self.running:
            self.running = False

    async def go_config(self, e):
        await self.page.push_route("/config")