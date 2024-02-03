from aiogram import Router

from .dialogs import (
    start_parsing_dialog,
    main_menu
)

main_menu_router = Router()

main_menu_router.include_routers(
    main_menu,
    start_parsing_dialog

)