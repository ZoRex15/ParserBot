from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram.types import User
import sqlite3

from service.service import Database
from lexicon import *


async def get_status_settings(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    selected_filters = Database.get_filters(user_id=event_from_user.id,
                                            setting_name='Статус')
    return {'filters': [(text, id) for id, text in STATUS.items()],
            'settings': selected_filters}

async def get_type_of_declaration_settings(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    
    selected_filters = Database.get_filters(user_id=event_from_user.id,
                                            setting_name='Тип декларации')
    return {'filters': [(text, id) for id, text in TYPE_OF_DECLARATION.items()],
            'settings': selected_filters}

async def get_type_of_object_declaration_settings(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    selected_filters = Database.get_filters(user_id=event_from_user.id,
                                            setting_name='Тип объекта декларирования')
    return {'filters': [(text, id) for id, text in TYPE_OF_OBJECT_DECLARATION.items()],
            'settings': selected_filters}

async def get_type_of_the_applican_settings(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    selected_filters = Database.get_filters(user_id=event_from_user.id,
                                            setting_name='Вид заявителя')
    return {
        'filters': [(text, id) for id, text in TYPE_OF_THE_APPLICAN.items()],
        'settings': selected_filters
    }

async def get_tech_reg(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    selected_filters = Database.get_filters(user_id=event_from_user.id,
                                            setting_name='Технический регламент')
    return {'settings': selected_filters}

def create_keyboard_tech_reg(on_click):
    buttons = []
    for id, text in TECH_REG.items():
        buttons.append(
            Button(
                text=Const(text),
                id=str(id),
                on_click=on_click
            )
        )
    return buttons

def create_keyboard_the_origin_of_the_product(on_click):
    buttons = []
    for id, text in COUNTRY.items():
        buttons.append(
            Button(
                text=Const(text),
                id=str(id),
                on_click=on_click
            )
        )
    return buttons

async def get_the_origin_of_the_product_filters(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    selected_filters = Database.get_filters(user_id=event_from_user.id,
                                            setting_name='Происхождение продукции')
    return {'settings': selected_filters}

def create_keyboard_unified_list_of_eaeu_products(on_click):
    buttons = []
    for id, text in UNIFIED_LIST_OF_EAEU_PRODUCTS.items():
        buttons.append(
            Button(
                text=Const(text),
                id=str(id),
                on_click=on_click
            )
        )
    return buttons

async def get_unified_list_of_eaeu_products_filters(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    selected_filters = Database.get_filters(user_id=event_from_user.id,
                                            setting_name='Единый перечень продукции ЕАЭС')
    return {'settings': selected_filters}

def create_keyboard_a_single_list_of_products_of_the_russian_federation(on_click):
    buttons = []
    for id, text in A_SINGLE_LIST_OF_PRODUCTS_OF_THE_RUSSIAN_FEDERATION.items():
        buttons.append(
            Button(
                text=Const(text),
                id=str(id),
                on_click=on_click
            )
        )
    return buttons

async def get_a_single_list_of_products_of_the_russian_federation_filters(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    selected_filters = Database.get_filters(user_id=event_from_user.id,
                                            setting_name='Единый перечень продукции РФ')
    return {'settings': selected_filters}

async def get_dates(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    regestration_date = Database.get_filters(
        user_id=event_from_user.id,
        setting_name='Дата регестрации'
    )
    date_end = Database.get_filters(
        user_id=event_from_user.id,
        setting_name='Дата окончания'
    )
    if regestration_date:
        regestration_date = regestration_date[0].split(',')
    if date_end:
        date_end = date_end[0].split(',')
    return {
        'regestration_date': regestration_date,
        'date_end': date_end
    }

def create_keyboard_groups_of_products_of_the_russian_federation(on_click):
    buttons = []
    for id, text in GROUPS_OF_PRODUCTS_OF_THE_RUSSIAN_FEDERATION.items():
        buttons.append(
            Button(
                text=Const(text),
                id=str(id),
                on_click=on_click
            )
        )
    return buttons

async def get_groups_of_products_of_the_russian_federation(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    settings = Database.get_filters(
        user_id=event_from_user.id,
        setting_name='Группы продукции РФ'
    )
    return {'settings': settings}

def create_keyboard_groups_of_products_of_the_eaeu(on_click):
    buttons = []
    for id, text in GROUPS_OF_PRODUCTS_OF_THE_EAEU.items():
        buttons.append(
            Button(
                text=Const(text),
                id=str(id),
                on_click=on_click
            )
        )
    return buttons

async def get_groups_of_products_of_the_eaeu(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    settings = Database.get_filters(
        user_id=event_from_user.id,
        setting_name='Группы продукции ЕАЭС'
    )
    return {'settings': settings}
