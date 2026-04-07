import flet as ft
import asyncio

class Home_view():
    def __init__(self, page: ft.Page):
        self.page = page
        self.running = False
        self.time = 8 * 3600

    def build(self):
        self.ui_clock = ft.Text(value="00:00:00", size=20)
        self.ui_timer = ft.Text(value="08:00:00", size=40)
        self.ui_bt_timer = ft.ElevatedButton("CLOCK", on_click=self.timer_to_active)
        self.ui_config_button = ft.ElevatedButton("CONFIG", on_click=self.go_config)
        return ft.Column(
            [
                self.ui_clock,
                self.ui_timer,
                self.ui_bt_timer,
                self.ui_config_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    async def run_timer(self):
        while self.running:
            self.time -= 1

            h = self.time // 3600
            m = (self.time % 3600) // 60
            s = self.time % 60

            self.ui_timer.value = f"{h:02}:{m:02}:{s:02}"
            self.page.update()
            await asyncio.sleep(1)

    async def clock(self):
        while True:
            h = 0
            m = 0
            s = 0
    
    def timer_to_active(self, e):
        if not self.running:
            self.running = True
            self.page.run_task(self.Run_Clock)
        elif self.running:
            self.running = False

    async def go_config(self, e):
        await self.page.push_route("/config")