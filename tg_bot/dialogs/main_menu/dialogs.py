from aiogram_dialog.widgets.kbd import Group, Row, Column, Button
from aiogram_dialog.widgets.text import Const, Format, Multi
from aiogram_dialog import Dialog, Window

from states import MainMenuSG
from .handlers import start_parsing, select_filters, clear_all_filters
from .getters import get_settings


main_menu = Dialog(
    Window(
        Const('Выбранные фильтры'),
        Format('{settings}'),
        
        Column(
            Button(text=Const('Начать парсинг по выбранным фильтрам'),
                   id='start_parsing',
                   on_click=start_parsing),
            Button(text=Const('Выбрать фильтры'),
                              id='select_filters',
                              on_click=select_filters),
            Button(text=Const('Очистить фильтры'),
                   id='clear_all_filters',
                   on_click=clear_all_filters)
            ),
    
        state=MainMenuSG.menu,
        getter=get_settings
    )
)