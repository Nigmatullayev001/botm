from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton("Buyurtma berish 🛍"), KeyboardButton("Ma'lumot ℹ️"))
    rkm.row(KeyboardButton("Sozlamalar⚙️"), KeyboardButton("Feedback 📩"))
    return rkm


def settings():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton("Ismni o'zgartirish  ✏️"),
            KeyboardButton("Telefon raqamni o'zgartirish  📱", request_contact=True))
    rkm.row(KeyboardButton("Tilni o'zgartirish  🇺🇿"), KeyboardButton("Ortga ⬅️"))
    return rkm


def feedback():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton("Bekor qilish ❌"))
    return rkm


def back():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton("Ortga ⬅️"))
    return rkm


def lang():
    ikm = InlineKeyboardMarkup()
    ikm.row(InlineKeyboardButton(text="English 🇺🇸", callback_data="eng"))
    ikm.row(InlineKeyboardButton(text="O'zbekcha 🇺🇿", callback_data="uzb"))
    ikm.row(InlineKeyboardButton(text="Russian 🇷🇺", callback_data="rus"))
    return ikm


def insta():
    ikm = InlineKeyboardMarkup()
    ikm.row(InlineKeyboardButton(text="Instagram🚀", url="https://www.instagram.com/letsfood_tashken"))
    return ikm
