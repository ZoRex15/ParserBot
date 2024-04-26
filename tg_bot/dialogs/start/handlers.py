from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from tg_bot.states import StartSG, MainMenuSG

router = Router()

@router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)

@router.message(Command(commands=['menu']))
async def send_menu(message: Message, dialog_manager: DialogManager):
    await dialog_manager.done()
    

async def go_to_main_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=MainMenuSG.menu)