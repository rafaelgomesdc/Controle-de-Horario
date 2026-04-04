import flet as ft
from app.view import home, config

def Route(page):
    match page.route: #Verifica a rota (route) atual
        case "/home":
            page.controls.clear()
            view = home.Home_view(page)
            page.add(view.build())
        case "/config":
            page.controls.clear()
            view = config.Config_view(page)
            page.add(view.build())
    
    page.update()