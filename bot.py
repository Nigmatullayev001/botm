from logging import basicConfig, getLogger, INFO

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from googletrans import Translator

from keyboard import insta, main_menu, settings, lang, feedback, back
from state import NameState, Feedback

basicConfig(level=INFO)
log = getLogger()
trans = Translator()
storage = MemoryStorage()
BOT_TOKEN = "7399744659:AAFLtn_LDRdlxgP4ERfHSFP-Tsj-XgFadzk"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

# -----------------------------------------------------------------------
txt3 = "Bekor qilindi"

feedback_txt = "Feedback sent"

txt = """Welcome to "Let's Food" - food service and delivery bot! Our bot is ready to offer you different dishes every day according to the menu. We work from 11:00 to 20:00 so that your lunch is tasty and timely.
Details about our menu can be found by following us on Instagram   @letsfood_tashkent (https://www.instagram.com/letsfood_tashkent) , for instruction on how to use the bot press /instruction 
We are ready to satisfy every taste and make your dinner unforgettable!

Also, we are pleased to announce that when ordering more than 5 servings, delivery is free! There are two types of portions in our menu: "Set" and "Half-set".
Serving cost:

"Set" is 40,000 sum

"Partial Set" - 35,000 sum

We guarantee that each meal will be fresh, tasty and prepared with love. We are waiting for your order!

Eat delicious every day
@lester_foods_bot"""

txt2 = """📌 Bu yerda siz bizning restoranimiz haqida ma'lumot olishingiz mumkin    
📞 Phone number: +998(90) 177-73-37
🕐 Ish vaqti: 10:00 - 20:00
⚡️Contact: @letsfood_bot_admin
📲 Bizning ijtimoiy tarmoqlarda kuzating:"""

start_txt = "Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing"

buyurtma_txt = """Noqulaylik uchun uzr, Bugingi taomlar tugadi
Ertaga yangi ta'mlarni sinab ko'ring!
@letsfood_bot"""

sozlamalar_txt = "Sozlamalarni o'zgartirish"

til_txt = "Tilni tanlang:"

feed_txt = "Send your feedback"

name_txt = "Enter your name:"

name_change_txt = "Your name has been changed!"


# ----------------------------------------------------------------------------


@dp.message_handler(commands="start")
async def start(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['trans'] = 'uz'
        await message.answer(trans.translate(start_txt, src='uz', dest=data['trans']).text,
                             reply_markup=main_menu())


@dp.callback_query_handler()
async def callback_func(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "eng":
        await callback.message.delete()
        await callback.message.answer(text="Language changed to 🇺🇸")
        async with state.proxy() as data:
            data['trans'] = 'en'
    elif callback.data == "uzb":
        await callback.message.delete()
        await callback.message.answer(text="Til o'zgartirildi! 🇺🇿")
        async with state.proxy() as data:
            data['trans'] = 'uz'
    elif callback.data == "rus":
        await callback.message.delete()
        await callback.message.answer(text="Язык изменен на 🇷🇺")
        async with state.proxy() as data:
            data['trans'] = 'ru'


@dp.message_handler(Text(equals="Sozlamalar⚙️"))
async def start_bot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(trans.translate(sozlamalar_txt, src='uz', dest=data['trans']).text,
                             reply_markup=settings())


@dp.message_handler(Text(equals="Tilni o'zgartirish  🇺🇿"))
async def start_bot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(trans.translate(til_txt, src='uz', dest=data['trans']).text, reply_markup=lang())


@dp.message_handler(Text(equals="Buyurtma berish 🛍"))
async def start_bot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(trans.translate(buyurtma_txt, src='uz', dest=data['trans']).text)


@dp.message_handler(Text(equals="Buyurtma berish 🛍"))
async def start_bot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer_photo(photo="https://files.fm/u/hr8ab2sxed",
                                   caption=trans.translate(txt, src='en', dest=data['trans']).text,
                                   reply_markup=insta())


@dp.message_handler(Text(equals="Ma'lumot ℹ️"))
async def malumot_bot(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(trans.translate(txt2, src='uz', dest=data['trans']).text, reply_markup=insta())


@dp.message_handler(Text(equals="Feedback 📩"), state=None)
async def malumot_bot(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['button'] = main_menu()
        await message.answer(trans.translate(feed_txt, src='en', dest=data['trans']).text, reply_markup=feedback())
    if message.text == "Bekor qilish ❌":
        txt3 = "Bekor qilindi ❌"
        await message.answer(trans.translate(txt3, src='uz', dest=data['trans']).text, reply_markup=main_menu())
    else:
        await Feedback.text.set()


@dp.message_handler(state=Feedback.text)
async def malumot_bot(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(trans.translate(feedback_txt, src='en', dest=data['trans']).text,
                             reply_markup=main_menu())
    await state.finish()


@dp.message_handler(Text(equals="Ismni o'zgartirish  ✏️"), state=None)
async def malumot_bot(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['button'] = settings()
        await message.answer(trans.translate(name_txt, src='en', dest=data['trans']).text, reply_markup=back())
    await NameState.name.set()


@dp.message_handler(state=NameState.name)
async def malumot_bot(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(trans.translate(name_change_txt, src='en', dest=data['trans']).text,
                             reply_markup=settings())
    await state.finish()


@dp.message_handler(Text(equals="Back ⬅️"), state=None)
async def backs(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(trans.translate(sozlamalar_txt, src='uz', dest=data['trans']).text,
                             reply_markup=main_menu())


@dp.message_handler(Text(equals="Ortga ⬅️"))
async def backs(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(trans.translate(start_txt, src='uz', dest=data['trans']).text, reply_markup=main_menu())


@dp.message_handler(Text(equals="Bekor qilish ❌"), state=None)
async def backs(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(trans.translate(txt3, src='uz', dest=data['trans']).text,
                             reply_markup=main_menu())


if __name__ == '__main__':
    executor.start_polling(dp)
