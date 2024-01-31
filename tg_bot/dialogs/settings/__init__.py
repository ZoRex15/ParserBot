from aiogram import Router


from .dialogs import (dialog_settings, 
                      dialog_status, 
                      type_of_declaration_dialog, 
                      type_of_object_declaration_dialog,
                      type_of_the_applicant_dialog,
                      technical_regulation_dialog,
                      the_origin_of_the_product_dialog,
                      unified_list_of_eaeu_products_dialog,
                      a_single_list_of_products_of_the_russian_federation_dialog,
                      input_data_dialog,
                      groups_of_products_of_the_russian_federation_dialog,
                      groups_of_products_of_the_eaeu_dialog)

settings_router = Router()

settings_router.include_routers(
    dialog_settings,
    dialog_status,
    type_of_declaration_dialog,
    type_of_object_declaration_dialog,
    type_of_the_applicant_dialog,
    technical_regulation_dialog,
    the_origin_of_the_product_dialog,
    unified_list_of_eaeu_products_dialog,
    a_single_list_of_products_of_the_russian_federation_dialog,
    input_data_dialog,
    groups_of_products_of_the_russian_federation_dialog,
    groups_of_products_of_the_eaeu_dialog
)
