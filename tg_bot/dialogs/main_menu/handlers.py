from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram.types import FSInputFile


from service.service import Database

from states import SettingsSG

from parser.main import parser
from datetime import date
import os



async def start_parsing(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    parser_settings = Database.get_all_filters(
        user_id=callback.from_user.id,
        mode='id'
    )
    reg_date_max, reg_date_min, end_date_max, end_date_min = None, None, None, None
    if parser_settings['Дата регестрации']:
        reg_date = [date.fromisoformat(i) for i in parser_settings['Дата регестрации'].split(',')]
        reg_date_max, reg_date_min = max(reg_date).strftime('%Y-%m-%d'), min(reg_date).strftime('%Y-%m-%d')
    if parser_settings['Дата окончания']:
        end_date = [date.fromisoformat(i) for i in parser_settings['Дата окончания'].split(',')]
        end_date_max, end_date_min = max(end_date).strftime('%Y-%m-%d'), min(end_date).strftime('%Y-%m-%d')
    path_to_file = parser(status=parser_settings['Статус'],
           zayvitel=parser_settings['Вид заявителя'],
           tech_reg=parser_settings['Технический регламент'],
           type_decl=parser_settings['Тип декларации'],
           type_obj_decl=parser_settings['Тип объекта декларации'],
           proizhodenie_product=parser_settings['Происхождение продукции'],
           edini_perechen_product_eaes=parser_settings['Единый перечень продукции ЕАЭС'],
           edini_perechen_product_rf=parser_settings['Единый перечень продукции РФ'],
           reg_date_max=reg_date_max,
           reg_date_min=reg_date_min,
           end_date_max=end_date_max,
           end_date_min=end_date_min,
           user_id=callback.from_user.id
           )
    file = FSInputFile(path=path_to_file)
    await callback.bot.send_document(
        chat_id=callback.from_user.id,
        document=file
    )
    try:
        os.remove(path=path_to_file)
    except Exception as error:
        print(error)

async def select_filters(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=SettingsSG.choiсe_settings)

async def clear_all_filters(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    Database.clear_all_filters(user_id=callback.from_user.id)
    await callback.answer('Фильтры были очищены')