from aiogram_dialog.widgets.kbd import Group, Row, Column, Button
from aiogram_dialog.widgets.text import Const, Format, Multi
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput

from aiogram.types import ContentType

from tg_bot.states import MainMenuSG, StartParsingSG
from .handlers import (
    start_parsing, 
    select_filters, 
    clear_all_filters,
    set_count_requests,
    error_input,
    check_count_requests,
    no_requests
    )
from .getters import get_settings


main_menu = Dialog(
    Window(
        Const('Выбранные фильтры'),
        Format('{settings}'),
        
        Column(
            Button(text=Const('Парсинг: По дикларациям'),
                   id='start_parsing_d',
                   on_click=start_parsing),
            Button(text=Const('Парсинг: По сертификатам'),
                   id='start_parsing_c',
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

start_parsing_dialog = Dialog(
    Window(
        Const('Введите количество'),
        TextInput(
            id='count_inpute',
            type_factory=check_count_requests,
            on_success=set_count_requests,
            on_error=error_input
        ),
        MessageInput(
            func=no_requests,
            content_types=ContentType.ANY
        ),
        state=StartParsingSG.input_requests
    )
)
