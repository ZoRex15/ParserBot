from aiogram import Router


from .main_menu import main_menu_router
from .start.dialogs import start
from .start.handlers import router as start_router
from .settings import settings_router