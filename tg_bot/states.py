from aiogram.fsm.state import StatesGroup, State


class StartSG(StatesGroup):
    start = State()

class MainMenuSG(StatesGroup):
    menu = State()
    
class SettingsSG(StatesGroup):
    choiсe_settings = State()
    
class StatusSG(StatesGroup):
    choice_status = State()

class TypeOfDeclarationSG(StatesGroup):
    choice_type_of_declaration = State()

class TypeOfObjectDeclarationSG(StatesGroup):
    choice_type_of_object_declaration = State()

class TypeOfTheApplicant(StatesGroup):
    choice_type_of_the_applicant = State()

class TechRegSG(StatesGroup):
    choice_tech_reg = State()

class TheOriginOfTheProductSG(StatesGroup):
    choice_the_origin_of_the_product = State()

class UnifiedListOfEAEUProductsSG(StatesGroup):
    choice_unified_list_of_eaeu_products = State()

class SingleListOfProductsOfTheRussianFederation(StatesGroup):
    choice_a_single_list_of_products_of_the_russian_federation = State()

class InputDataSG(StatesGroup):
    menu = State()
    input_data_regestration = State()
    input_data_end = State()

class GroupsOfProductsOfTheRussianFederation(StatesGroup):
    choice_groups_of_products_of_the_russian_federation = State()

class GroupsOfProductsOfTheEAEU(StatesGroup):
    choice_groups_of_products_of_the_eaeu = State()
