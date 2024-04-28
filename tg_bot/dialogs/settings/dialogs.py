from aiogram_dialog import Window, Dialog
from aiogram.enums import ContentType
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import Button, Row, ScrollingGroup, Group, Select
from aiogram_dialog.widgets.input import TextInput, MessageInput
import operator

from tg_bot.states import (SettingsSG, 
                    StatusSG, 
                    TypeOfDeclarationSG, 
                    TypeOfObjectDeclarationSG, 
                    TypeOfTheApplicant, 
                    TechRegSG,
                    TheOriginOfTheProductSG,
                    UnifiedListOfEAEUProductsSG,
                    SingleListOfProductsOfTheRussianFederation,
                    InputDataSG,
                    GroupsOfProductsOfTheRussianFederation,
                    GroupsOfProductsOfTheEAEU,
                    NumberCertificate
                    )

from .handlers import (
    status,
    back,
    set_status,
    type_of_declaration,
    type_of_object_declaration,
    set_type_of_declaration,
    set_type_of_object_declaration,
    type_of_the_applicant,
    set_type_of_the_applican,
    set_tech_reg,
    tech_reg,
    the_origin_of_the_product,
    set_the_origin_of_the_product,
    set_unified_list_of_eaeu_products,
    unified_list_of_eaeu_products,
    set_a_single_list_of_products_of_the_russian_federation,
    a_single_list_of_products_of_the_russian_federation,
    clear_filters,
    input_data_end,
    input_data_regestration,
    date_check,
    set_regestration_date,
    set_date_end, 
    no_date,
    error_date,
    input_data_menu,
    back_to_input_data_menu,
    clear_date_filters,
    set_groups_of_products_of_the_russian_federation,
    groups_of_products_of_the_russian_federation,
    set_groups_of_products_of_the_eaeu,
    groups_of_products_of_the_eaeu,
    is_text,
    correct_certificate,
    error_certificate,
    go_to_number_certificate
    
)
from .getters import (
    get_status_settings,
    get_type_of_declaration_settings,
    get_type_of_object_declaration_settings,
    get_type_of_the_applican_settings,
    create_keyboard_tech_reg,
    get_tech_reg,
    create_keyboard_the_origin_of_the_product,
    get_the_origin_of_the_product_filters,
    create_keyboard_unified_list_of_eaeu_products,
    get_unified_list_of_eaeu_products_filters,
    get_a_single_list_of_products_of_the_russian_federation_filters,
    create_keyboard_a_single_list_of_products_of_the_russian_federation,
    get_dates,
    create_keyboard_groups_of_products_of_the_russian_federation,
    get_groups_of_products_of_the_russian_federation,
    get_groups_of_products_of_the_eaeu,
    create_keyboard_groups_of_products_of_the_eaeu,
    get_selected_number_catertificates
    
    )


dialog_settings = Dialog(
    Window(
        Const('Настройки'),
        Group(
            Row(
                Button(text=Const('Статус'),
                       id='status',
                       on_click=status),
                Button(text=Const('Тип декларации'),
                       id='type_of_declaration',
                       on_click=type_of_declaration),
            ),
            Row(
                Button(text=Const('Вид заявителя'),
                       id='type_of_the_applicant',
                       on_click=type_of_the_applicant),
                Button(text=Const('Технический регламент'),
                       id='tech_reg',
                       on_click=tech_reg),
            ),
            Row(
                Button(text=Const('Тип объекта декларации'),
                       id='type_of_object_declaration',
                       on_click=type_of_object_declaration),
                Button(text=Const('Происхождение продукции'),
                       id='the_origin_of_the_product',
                       on_click=the_origin_of_the_product)
            ),
            Row(
                Button(text=Const('Единый перечень продукции ЕАЭС'),
                       id='unified_list_of_eaeu_products',
                       on_click=unified_list_of_eaeu_products),
                Button(text=Const('Единый перечень продукции РФ'),
                       id='a_single_list_of_products_of_the_russian_federation',
                       on_click=a_single_list_of_products_of_the_russian_federation),
            ),
            Row(
                Button(
                    text=Const('Ввести даты'),
                    id='input_dates',
                    on_click=input_data_menu
                ),
                Button(
                    text=Const('Группы продукции РФ'),
                    id='groups_of_products_of_the_russian_federation',
                    on_click=groups_of_products_of_the_russian_federation
                )
            ),
            Row(
                Button(
                    text=Const('Группы продукции ЕАЭС'),
                    id='groups_of_products_of_the_eaeu',
                    on_click=groups_of_products_of_the_eaeu),
                Button(
                    text=Const('Номер сертификата'),
                    id='certificate_number',
                    on_click=go_to_number_certificate
                )
            ),
        Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
        ),
        state=SettingsSG.choiсe_settings,
    )
)

dialog_status = Dialog(
    Window(
        Format('Статус'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            Select(
                    text=Format('{item[0]}'),
                    id='status_m',
                    item_id_getter=operator.itemgetter(1),
                    items="filters",
                    on_click=set_status
            ),
            width=2),
            Button(text=Const('Очистить фильтры'),
                   id='clear_filters_1',
                   on_click=clear_filters),
            Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
            state=StatusSG.choice_status,
            getter=get_status_settings
        
    )
)

type_of_declaration_dialog = Dialog(
    Window(
        Const('Тип декларации'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            Select(
                    text=Format('{item[0]}'),
                    id='type_of_declaration_m',
                    item_id_getter=operator.itemgetter(1),
                    items="filters",
                    on_click=set_type_of_declaration
            ),
            width=2),
        Button(text=Const('Очистить фильтры'),
                   id='clear_filters_2',
                   on_click=clear_filters),
        Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
        getter=get_type_of_declaration_settings,
        state=TypeOfDeclarationSG.choice_type_of_declaration
    )
)

type_of_object_declaration_dialog = Dialog(
    Window(
        Const('Тип объекта декларирования'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            Select(
                    text=Format('{item[0]}'),
                    id='type_of_object_declaration_m',
                    item_id_getter=operator.itemgetter(1),
                    items="filters",
                    on_click=set_type_of_object_declaration
            ),
            width=2),
        Button(text=Const('Очистить фильтры'),
                   id='clear_filters_5',
                   on_click=clear_filters),
        Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
        getter=get_type_of_object_declaration_settings,
        state=TypeOfObjectDeclarationSG.choice_type_of_object_declaration
    )
)

type_of_the_applicant_dialog = Dialog(
    Window(
        Const('Вид заявителя'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            Select(
                    text=Format('{item[0]}'),
                    id='type_of_the_applican_m',
                    item_id_getter=operator.itemgetter(1),
                    items="filters",
                    on_click=set_type_of_the_applican
            ),
            width=2),
            Button(text=Const('Очистить фильтры'),
                   id='clear_filters_3',
                   on_click=clear_filters),
            Button(text=Const('Назад'),
                    id='back',
                    on_click=back),
        getter=get_type_of_the_applican_settings,
        state=TypeOfTheApplicant.choice_type_of_the_applicant
    )
)

technical_regulation_dialog = Dialog(
    Window(
        Const('Технический регламент'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            ScrollingGroup(
                *create_keyboard_tech_reg(on_click=set_tech_reg),
                id='tech_reg',
                width=2,
                height=7
            ),
            Button(text=Const('Очистить фильтры'),
                   id='clear_filters_4',
                   on_click=clear_filters),
            Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
        ),
        state=TechRegSG.choice_tech_reg,
        getter=get_tech_reg
    )
)

the_origin_of_the_product_dialog = Dialog(
    Window(
        Const('Происхождение продукции'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            ScrollingGroup(
                *create_keyboard_the_origin_of_the_product(on_click=set_the_origin_of_the_product),
                id='the_origin_of_the_product',
                width=2,
                height=15 
            ),
            Button(text=Const('Очистить фильтры'),
                   id='clear_filters_6',
                   on_click=clear_filters),
            Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
        ),
        state=TheOriginOfTheProductSG.choice_the_origin_of_the_product,
        getter=get_the_origin_of_the_product_filters
    )
)

unified_list_of_eaeu_products_dialog = Dialog(
    Window(
        Const('Единый перечень продукции ЕАЭС'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            ScrollingGroup(
                *create_keyboard_unified_list_of_eaeu_products(on_click=set_unified_list_of_eaeu_products),
                id='unified_list_of_eaeu_products',
                width=1,
                height=15
            ),
            Button(text=Const('Очистить фильтры'),
                   id='clear_filters_7',
                   on_click=clear_filters),
            Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
            ),
    state=UnifiedListOfEAEUProductsSG.choice_unified_list_of_eaeu_products,
    getter=get_unified_list_of_eaeu_products_filters
    )
)

a_single_list_of_products_of_the_russian_federation_dialog = Dialog(
    Window(
        Const('Единый перечень продукции РФ'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            ScrollingGroup(
                *create_keyboard_a_single_list_of_products_of_the_russian_federation(on_click=set_a_single_list_of_products_of_the_russian_federation),
                width=1,
                height=15,
                id='a_single_list_of_products_of_the_russian_federation'
            ),
            Button(text=Const('Очистить фильтры'),
                   id='clear_filters_8',
                   on_click=clear_filters),
            Button(text=Const('Назад'),
                   id='back',
                   on_click=back)
        ),
        state=SingleListOfProductsOfTheRussianFederation.choice_a_single_list_of_products_of_the_russian_federation,
        getter=get_a_single_list_of_products_of_the_russian_federation_filters
    )
)

input_data_dialog = Dialog(
    Window(
        Const('Чтобы ввести дату нажмите на кнопку: Ввести дату'),
        Format('Дата регестрации: {regestration_date}'),
        Format('Дата окончания: {date_end}'),
        Button(text=Const('Ввести дату регестрации'),
               id='input_regestration_date', 
               on_click=input_data_regestration),
        Button(text=Const('Ввести дату окончания'),
               id='input_data_end', 
               on_click=input_data_end),
        Button(text=Const('Очистить фильтры'),
                   id='clear_date_filters',
                   on_click=clear_date_filters),
        Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
        state=InputDataSG.menu,
        getter=get_dates
    ),
    Window(
        Const('Введите дату регистрации в формате: ГГГГ-ММ-ДД,ГГГГ-ММ-ДД'),
        Button(text=Const('Назад'),
                        id='back',
                        on_click=back_to_input_data_menu),
        TextInput(
            id='date_input',
            type_factory=date_check,
            on_success=set_regestration_date,
            on_error=error_date
        ),
        MessageInput(
            func=no_date,
            content_types=ContentType.ANY
        ),
        state=InputDataSG.input_data_regestration
    ),
    Window(
        Const('Введите дату окончания в формате: ГГГГ-ММ-ДД,ГГГГ-ММ-ДД'),
        Button(text=Const('Назад'),
                        id='back',
                        on_click=back_to_input_data_menu),
        TextInput(
            id='date_input',
            type_factory=date_check,
            on_success=set_date_end,
            on_error=error_date
        ),
        MessageInput(
            func=no_date,
            content_types=ContentType.ANY
        ),
        state=InputDataSG.input_data_end
    )
)

groups_of_products_of_the_russian_federation_dialog = Dialog(
    Window(
        Const('Группы продукции РФ'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            ScrollingGroup(
                *create_keyboard_groups_of_products_of_the_russian_federation(on_click=set_groups_of_products_of_the_russian_federation),
                width=1,
                height=15,
                id='a_single_list_of_products_of_the_russian_federation'
            ),
            Button(text=Const('Очистить фильтры'),
                   id='clear_filters_11',
                   on_click=clear_filters),
            Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
        ),
        getter=get_groups_of_products_of_the_russian_federation,
        state=GroupsOfProductsOfTheRussianFederation.choice_groups_of_products_of_the_russian_federation
    )
)

groups_of_products_of_the_eaeu_dialog = Dialog(
    Window(
        Const('Группы продукции ЕАЭС'),
        Format('Выбранные фильтры: {settings}'),
        Group(
            ScrollingGroup(
                *create_keyboard_groups_of_products_of_the_eaeu(on_click=set_groups_of_products_of_the_eaeu),
                width=1,
                height=15,
                id='a_single_list_of_products_of_the_eaeu'
            ),
            Button(text=Const('Очистить фильтры'),
                   id='clear_filters_12',
                   on_click=clear_filters),
            Button(text=Const('Назад'),
                   id='back',
                   on_click=back),
        ),
        getter=get_groups_of_products_of_the_eaeu,
        state=GroupsOfProductsOfTheEAEU.choice_groups_of_products_of_the_eaeu
    )
)

number_certificate_dialog = Dialog(
    Window(
        Const('Номер сертификата'),
        Format('Выбранные фильтры: {settings}'),
        TextInput(
            id='choise_number_certificate',
            type_factory=is_text,
            on_success=correct_certificate,
            on_error=error_certificate
        ),
        Button(text=Const('Очистить фильтры'),
                   id='clear_filters_13',
                   on_click=clear_filters),
        Button(text=Const('Назад'),
                id='back',
                on_click=back),
        state=NumberCertificate.choise_number_certificate,
        getter=get_selected_number_catertificates
    )
    
)