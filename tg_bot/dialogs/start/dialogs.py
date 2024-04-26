from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import  Button, Column, Multiselect, Group

from .handlers import go_to_main_menu
from .getters import get_user_name
from tg_bot.states import StartSG


start = Dialog(
    Window(Format(text='Привет {name}, <b>чтобы начать пользоваться ботом перейдите в главное меню</b>'),
           Button(text=Const('Главное меню'),
                  id='start',
                  on_click=go_to_main_menu),
                  state=StartSG.start,
                  getter=get_user_name)
)