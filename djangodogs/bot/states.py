from aiogram.fsm.state import StatesGroup, State

class question(StatesGroup):
    starting_question = State()
    first_question = State()
    second_question = State()
    third_question = State()
    fourth_question = State()
    fifth_question = State()
    sixth_question = State()
    seventh_question = State()
    ready = State()
    mailing = State()
    