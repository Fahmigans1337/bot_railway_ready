from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

logging.basicConfig(level=logging.INFO)

API_TOKEN = '8036460983:AAFhjrHeF8vo87VCT3ob-gAmimAH_H8mTqg'

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)

ALLOWED_USERS = [123456789]  # Ganti dengan user_id kamu

async def check_access(message: types.Message):
    if message.from_user.id not in ALLOWED_USERS:
        await message.reply("❌ Anda tidak diizinkan menggunakan bot ini.")
        return False
    return True

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    if not await check_access(message):
        return
    await message.reply("✅ Bot aktif! Gunakan /menu untuk lihat fitur.")

@dp.message_handler(commands=['menu'])
async def menu_handler(message: types.Message):
    if not await check_access(message):
        return
    menu = (
        "📋 *Menu Cek Data:*\n"
        "/ceknopol [plat]\n"
        "/cekbocor [email/nomor/nama]\n"
        "/ceknama [nama lengkap]\n"
        "/ceknomor [no hp]\n"
        "/ceknik [nik e-ktp]"
    )
    await message.reply(menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)