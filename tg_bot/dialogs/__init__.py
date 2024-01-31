from aiogram import Router


from .main_menu.dialogs import main_menu
from .start.dialogs import start
from .start.handlers import router as start_router
from .settings import settings_router