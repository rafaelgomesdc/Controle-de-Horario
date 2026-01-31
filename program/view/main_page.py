import time
import flet as ft
import asyncio

def view(page):
    page.title = "Projeto Controle de Horário"

    #Timer
    running = False
    seconds = 45
    minutes = 59
    hours = 0

    ui_timer = ft.Text(value=f"{hours}:{minutes}:{seconds}", size=100)

    async def timer():
        nonlocal running, seconds, minutes, hours
        while running:
            await asyncio.sleep(1)

            if seconds > 58:
                minutes += 1
                seconds = 0
            if minutes > 59:
                hours += 1
                minutes = 0

            seconds += 1
            ui_timer.value = f"{hours}:{minutes}:{seconds}"
            page.update()

    def start():
        nonlocal running

        if not running:
            running = True
            page.run_task(timer)

    def stop():
        nonlocal running
        running = False

    page.add(
        ui_timer,
        ft.Row([
            ft.ElevatedButton("Start", on_click=start),
            ft.ElevatedButton("Stop", on_click=stop)
            ])
    )
    page.update()

ft.app(target=view)