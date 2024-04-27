from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram.types import FSInputFile

from tg_bot.service import Database

from tg_bot.states import SettingsSG, StartParsingSG, MainMenuSG

from tg_bot.states import SettingsSG, StartParsingSG, MainMenuSG

from tg_bot.parser import parse_cert, parse_decl
from datetime import date
from typing import Any
from tg_bot.config.config import load_config, Config
from tg_bot.dto import FiltersDTO
import os
import asyncio

config: Config = load_config('tg_bot/.env')

async def start_parsing(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    if callback.from_user.id not in config.tg_bot.admin_ids:
        await callback.answer(text='Недостаточно прав!')
    else:
        if button.widget_id == 'start_parsing_d':
            await dialog_manager.start(state=StartParsingSG.input_requests, data={'pars_mode': 'decl'})
        else:
            await dialog_manager.start(state=StartParsingSG.input_requests, data={'pars_mode': 'cert'})
            
async def select_filters(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=SettingsSG.choiсe_settings)

async def clear_all_filters(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    db: Database = dialog_manager.middleware_data.get('db')
    db.clear_all_filters(user_id=callback.from_user.id)
    await callback.answer('Фильтры были очищены')

def check_count_requests(text: Any):
    if int(text) not in range(1, 1001):
        raise ValueError
    
async def set_count_requests(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str
):  
    db: Database = dialog_manager.middleware_data.get('db')
    answer_message = await message.answer('Статус парсинга: Запуск...')
    parser_settings = db.get_all_filters(
        user_id=message.from_user.id,
        mode='id'
    )
    reg_date_max, reg_date_min, end_date_max, end_date_min = None, None, None, None
    if parser_settings['Дата регестрации']:
        reg_date = [date.fromisoformat(i) for i in parser_settings['Дата регестрации'].split(',')]
        reg_date_max, reg_date_min = max(reg_date).strftime('%Y-%m-%d'), min(reg_date).strftime('%Y-%m-%d')
    if parser_settings['Дата окончания']:
        end_date = [date.fromisoformat(i) for i in parser_settings['Дата окончания'].split(',')]
        end_date_max, end_date_min = max(end_date).strftime('%Y-%m-%d'), min(end_date).strftime('%Y-%m-%d')
    filters = FiltersDTO(
        status=parser_settings['Статус'],
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
        count_requests=int(message.text),
        row_sertificate=parser_settings['Номер сертификата']
    )
    if dialog_manager.start_data['pars_mode'] == 'decl':
        path_to_file = parse_decl(
            Filters=filters,
            user_id=message.from_user.id,
            message_id=message.message_id
        )
    else:
        path_to_file = parse_cert(
            Filters=filters,
            user_id=message.from_user.id,
            message_id=answer_message.message_id
        )
    file = FSInputFile(path=path_to_file)
    await message.bot.send_document(
        chat_id=message.from_user.id,
        document=file
    )
    await asyncio.sleep(2)
    try:
        os.remove(path=path_to_file)
    except Exception as error:
        print(error)
    await dialog_manager.start(state=MainMenuSG.menu)
    

async def error_input(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str 
):
    await message.answer('Введите число от 1 до 1000')

async def no_requests(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    await message.answer(text='Вы ввели вообще не количество запросов')

