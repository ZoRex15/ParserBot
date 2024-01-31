from aiogram.types import CallbackQuery, Message
from aiogram_dialog.widgets.kbd import Button, Select
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from aiogram_dialog import DialogManager, StartMode

from states import (StatusSG,
                    TypeOfDeclarationSG,
                    TypeOfObjectDeclarationSG, 
                    TypeOfTheApplicant, 
                    TechRegSG,
                    TheOriginOfTheProductSG,
                    UnifiedListOfEAEUProductsSG,
                    SingleListOfProductsOfTheRussianFederation,
                    InputDataSG,
                    GroupsOfProductsOfTheRussianFederation,
                    GroupsOfProductsOfTheEAEU
                    )
from service.service import Database
from lexicon import *
from typing import Any
from datetime import date



async def status(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=StatusSG.choice_status)

async def type_of_declaration(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=TypeOfDeclarationSG.choice_type_of_declaration)

async def type_of_object_declaration(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=TypeOfObjectDeclarationSG.choice_type_of_object_declaration)

async def type_of_the_applicant(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=TypeOfTheApplicant.choice_type_of_the_applicant)

async def tech_reg(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=TechRegSG.choice_tech_reg)

async def the_origin_of_the_product(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=TheOriginOfTheProductSG.choice_the_origin_of_the_product)

async def unified_list_of_eaeu_products(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=UnifiedListOfEAEUProductsSG.choice_unified_list_of_eaeu_products)

async def a_single_list_of_products_of_the_russian_federation(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=SingleListOfProductsOfTheRussianFederation.choice_a_single_list_of_products_of_the_russian_federation)

async def input_data_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=InputDataSG.menu)

async def input_data_regestration(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=InputDataSG.input_data_regestration)

async def input_data_end(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=InputDataSG.input_data_end)

async def groups_of_products_of_the_russian_federation(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=GroupsOfProductsOfTheRussianFederation.choice_groups_of_products_of_the_russian_federation)

async def groups_of_products_of_the_eaeu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=GroupsOfProductsOfTheEAEU.choice_groups_of_products_of_the_eaeu)
 
async def back(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.done()

async def clear_filters(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    Database.clear_filters(
        user_id=callback.from_user.id,
        setting_id=callback.data.split('_')[-1]
    )
    await callback.answer('Фильтры были очищенны')

async def set_status(callback: CallbackQuery, widget: Select,
                             dialog_manager: DialogManager, item_id: str):
    
    Database.set_filter(user_id=callback.from_user.id,
                        setting_name='Статус',
                        filter=STATUS[item_id],
                        filter_id=item_id)
    await callback.answer(text=STATUS[item_id])

async def set_type_of_declaration(callback: CallbackQuery, widget: Select,
                             dialog_manager: DialogManager, item_id: str):
    Database.set_filter(user_id=callback.from_user.id,
                        setting_name='Тип декларации',
                        filter=TYPE_OF_DECLARATION[item_id],
                        filter_id=item_id)
    await callback.answer(text=TYPE_OF_DECLARATION[item_id])

async def set_type_of_object_declaration(callback: CallbackQuery, widget: Select,
                             dialog_manager: DialogManager, item_id: str):
    Database.set_filter(user_id=callback.from_user.id,
                        setting_name='Тип объекта декларирования',
                        filter=TYPE_OF_OBJECT_DECLARATION[item_id],
                        filter_id=item_id)
    await callback.answer(text=TYPE_OF_OBJECT_DECLARATION[item_id])

async def set_type_of_the_applican(callback: CallbackQuery, widget: Select,
                                   dialog_manager: DialogManager, item_id: str):
    Database.set_filter(user_id=callback.from_user.id,
                        setting_name='Вид заявителя',
                        filter=TYPE_OF_THE_APPLICAN[item_id],
                        filter_id=item_id)
    await callback.answer(text=TYPE_OF_THE_APPLICAN[item_id])

async def set_tech_reg(callback: CallbackQuery, button: Button,
                        dialog_manager: DialogManager):
    
    Database.set_filter(
        user_id=callback.from_user.id,
        setting_name='Технический регламент',
        filter=TECH_REG[callback.data],
        filter_id=callback.data
    )
    await callback.answer(text=TECH_REG[callback.data])

async def set_the_origin_of_the_product(callback: CallbackQuery, button: Button,
                        dialog_manager: DialogManager):
    Database.set_filter(
        user_id=callback.from_user.id,
        setting_name='Происхождение продукции',
        filter=COUNTRY[callback.data],
        filter_id=callback.data
    )
    await callback.answer(text=COUNTRY[callback.data])

async def set_unified_list_of_eaeu_products(callback: CallbackQuery, button: Button,
                        dialog_manager: DialogManager):
    Database.set_filter(
        user_id=callback.from_user.id,
        setting_name='Единый перечень продукции ЕАЭС',
        filter=UNIFIED_LIST_OF_EAEU_PRODUCTS[callback.data],
        filter_id=callback.data
    )
    await callback.answer(text=UNIFIED_LIST_OF_EAEU_PRODUCTS[callback.data])

async def set_a_single_list_of_products_of_the_russian_federation(callback: CallbackQuery, button: Button,
                        dialog_manager: DialogManager):
    Database.set_filter(
        user_id=callback.from_user.id,
        setting_name='Единый перечень продукции РФ',
        filter=A_SINGLE_LIST_OF_PRODUCTS_OF_THE_RUSSIAN_FEDERATION[callback.data],
        filter_id=callback.data
    )
    await callback.answer(text=A_SINGLE_LIST_OF_PRODUCTS_OF_THE_RUSSIAN_FEDERATION[callback.data])

def date_check(text: Any):
    first_date, second_date = text.split(',')
    try:
        date.fromisoformat(first_date)
        date.fromisoformat(second_date)
    except:
        raise ValueError
    
async def set_regestration_date(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str
):
    Database.clear_filters(
        user_id=message.from_user.id,
        setting_id='9'
    )
    Database.set_filter(
        user_id=message.from_user.id,
        setting_name='Дата регестрации',
        filter=message.text
    )
    await dialog_manager.switch_to(InputDataSG.menu)

async def set_date_end(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str
):
    Database.clear_filters(
        user_id=message.from_user.id,
        setting_id='10'
    )
    Database.set_filter(
        user_id=message.from_user.id,
        setting_name='Дата окончания',
        filter=message.text
    )
    await dialog_manager.switch_to(InputDataSG.menu)

async def error_date(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str 
):
    await message.answer('Вы ввели некорректную дату. Попробуйте ещё раз')

async def no_date(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    await message.answer(text='Вы ввели вообще не дату!')

async def back_to_input_data_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(InputDataSG.menu)

async def clear_date_filters(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    Database.clear_filters(
        user_id=callback.from_user.id,
        setting_id='9'
    )
    Database.clear_filters(
        user_id=callback.from_user.id,
        setting_id='10'
    )
    await callback.answer('Фильтры были очищенны')

async def set_groups_of_products_of_the_russian_federation(callback: CallbackQuery, button: Button,
                        dialog_manager: DialogManager):
    Database.set_filter(
        user_id=callback.from_user.id,
        setting_name='Группы продукции РФ',
        filter=GROUPS_OF_PRODUCTS_OF_THE_RUSSIAN_FEDERATION[callback.data],
        filter_id=callback.data
    )
    await callback.answer(text=GROUPS_OF_PRODUCTS_OF_THE_RUSSIAN_FEDERATION[callback.data])

async def set_groups_of_products_of_the_eaeu(callback: CallbackQuery, button: Button,
                        dialog_manager: DialogManager):
    Database.set_filter(
        user_id=callback.from_user.id,
        setting_name='Группы продукции ЕАЭС',
        filter=GROUPS_OF_PRODUCTS_OF_THE_EAEU[callback.data],
        filter_id=callback.data
    )
    await callback.answer(text=GROUPS_OF_PRODUCTS_OF_THE_EAEU[callback.data])