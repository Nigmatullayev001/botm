from aiogram.dispatcher.filters.state import State, StatesGroup


# State, StatesGroup
class NameState(StatesGroup):
    name = State()


class Feedback(StatesGroup):
    text = State()
