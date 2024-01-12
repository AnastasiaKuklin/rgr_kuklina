import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from aiogram.filters import Command, StateFilter
# from config_reader import config
from keyboards.for_questions import get_yes_no_kb
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.storage.memory import MemoryStorage
from states import question
from aiogram.fsm.context import FSMContext
# from db import cmd_staer_db
from config import host, user, password, db_name
import mysql.connector
from mysql.connector import errorcode


logging.basicConfig(level=logging.INFO)

bot = Bot("6363160747:AAGyssU1JFJQxBF_uzRYFHNknPmCZ8TD-WY")

dp = Dispatcher(storage=MemoryStorage())

router = Router()

# DB CONNECT
try:
    datab = mysql.connector.connect(
      host=host,
      user=user,
      passwd=password,
      database=db_name,
      auth_plugin='mysql_native_password'
    )
    print("ok")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Что-то не так с вашим именем пользователя или паролем")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("База данных не существует")
  else:
    print(err)

cursor = datab.cursor()


dog_z = 0
dog_d = 0
dog_sh = 0

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "-Привет, я бот помогающий определить самую подходящую породу собак для вас, хотите начать?",
        reply_markup=get_yes_no_kb())
    cursor = datab.cursor(buffered=True)
    cursor.execute("""SELECT * FROM `bot_table` WHERE chat_id = (%s)""", (message.chat.id,))
    datab.commit()
    data = cursor.fetchone()
    if not data:
        cursor.execute("""INSERT INTO `bot_table` (chat_id) VALUES (%s)""", (message.chat.id,))
        datab.commit()
    
    
    
@router.message(StateFilter(None), F.text.lower() == "да")
async def start_yes(message: Message, state: FSMContext):
    await message.answer(
        "Это здорово! Первый вопрос. В одном доме с вами живут маленькие дети?")
    await state.set_state(question.starting_question)
    
@router.message(StateFilter(None), F.text.lower() == "нет")
async def start_no(message: Message):
    await message.answer(
        "Жаль...",)
    
    
    
    

@router.message(question.starting_question, F.text.lower() == "да")
async def first_yes(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET first_question = 1 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вам бы понравилось часто вычесывать совю собачку?")
    await state.set_state(question.first_question)
    
@router.message(question.starting_question, F.text.lower() == "нет")
async def first_no(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET first_question = 0 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вам бы понравилось часто вычесывать совю собачку?")
    await state.set_state(question.first_question)
    
    
    
    
@router.message(question.first_question, F.text.lower() == "да")
async def second_yes(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET second_question = 1 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Любите обнимать огромного плюшевого медведя?")
    await state.set_state(question.second_question)
    
@router.message(question.first_question, F.text.lower() == "нет")
async def second_no(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET second_question = 0 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Любите обнимать огромного плюшевого медведя?")
    await state.set_state(question.second_question)
    
    
    
    
@router.message(question.second_question, F.text.lower() == "да")
async def third_yes(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET third_question = 1 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вы живете в совём доме с дворовой территорией?")
    await state.set_state(question.third_question)
    
    
@router.message(question.second_question, F.text.lower() == "нет")
async def third_no(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET third_question = 0 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вы живете в совём доме с дворовой территорией?")
    await state.set_state(question.third_question)
    
    
    

@router.message(question.third_question, F.text.lower() == "да")
async def fourth_yes(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET fourth_question = 1 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вам необходим надежный охранник и защитник рядом?")
    await state.set_state(question.fourth_question)
    
@router.message(question.third_question, F.text.lower() == "нет")
async def fourth_no(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET fourth_question = 0 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вам необходим надежный охранник и защитник рядом?")
    await state.set_state(question.fourth_question)
    
    
    
    
@router.message(question.fourth_question, F.text.lower() == "да")
async def fifth_yes(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET fifth_question = 2 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вы мечтаете носить на ручках своего питомца?")
    await state.set_state(question.fifth_question)
    
@router.message(question.fourth_question, F.text.lower() == "нет")
async def fifth_no(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET fifth_question = 0 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вы мечтаете носить на ручках своего питомца?")
    await state.set_state(question.fifth_question)
    
    
    

@router.message(question.fifth_question, F.text.lower() == "да")
async def sixth_yes(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET sixth_question = 1 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вам свойственен активный образ жизни?")
    await state.set_state(question.sixth_question)
    
@router.message(question.fifth_question, F.text.lower() == "нет")
async def sixth_no(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET sixth_question = 0 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Вам свойственен активный образ жизни?")
    await state.set_state(question.sixth_question)
    
    
    
    
@router.message(question.sixth_question, F.text.lower() == "да")
async def seventh_yes(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET seventh_question = 1 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Гости в вашем доме - частое дело?")
    await state.set_state(question.seventh_question)
    
@router.message(question.sixth_question, F.text.lower() == "нет")
async def seventh_no(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET seventh_question = 0 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Гости в вашем доме - частое дело?")
    await state.set_state(question.seventh_question)
    
    
@router.message(question.seventh_question, F.text.lower() == "да")
async def last_yes(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET eight_question = 1 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Хотите получать рассылку о бездомных собачках, чтобы быть готовым их приютить?")
    await state.set_state(question.mailing)
    
@router.message(question.seventh_question, F.text.lower() == "нет")
async def last_no(message: Message, state: FSMContext):
    await message.answer(
        "Хотите получать рассылку о бездомных собачках, чтобы быть готовым их приютить?")
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET eight_question = 0 WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await state.set_state(question.mailing)
    
    

@router.message(question.mailing, F.text.lower() == "да")
async def last_yes(message: Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET users_agree = 'да' WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await message.answer(
        "Готово! Чтобы узнать результат отправьте мне комануд /ready", reply_markup=ReplyKeyboardRemove())
    await state.set_state(question.ready)
    
    
@router.message(question.mailing, F.text.lower() == "нет")
async def last_no(message: Message, state: FSMContext):
    await message.answer(
        "Готово! Чтобы узнать результат отправьте мне комануд /ready", reply_markup=ReplyKeyboardRemove())
    cursor = datab.cursor(buffered=True)
    cursor.execute("UPDATE `bot_table` SET users_agree = 'нет' WHERE chat_id = (%s)", (message.chat.id,))
    datab.commit()
    await state.set_state(question.ready)
    

@router.message(question.ready, Command("ready"))
async def cmd_ready(message: types.Message, state: FSMContext):
    cursor = datab.cursor(buffered=True)
    cursor.execute("""SELECT first_question FROM `bot_table` WHERE chat_id = (%s)""", (message.chat.id,))
    datab.commit()
    first = cursor.fetchone()
    cursor = datab.cursor(buffered=True)
    cursor.execute("""SELECT second_question FROM `bot_table` WHERE chat_id = (%s)""", (message.chat.id,))
    datab.commit()
    second = cursor.fetchone()
    cursor = datab.cursor(buffered=True)
    cursor.execute("""SELECT third_question FROM `bot_table` WHERE chat_id = (%s)""", (message.chat.id,))
    datab.commit()
    third = cursor.fetchone()
    cursor = datab.cursor(buffered=True)
    cursor.execute("""SELECT fourth_question FROM `bot_table` WHERE chat_id = (%s)""", (message.chat.id,))
    datab.commit()
    fourth = cursor.fetchone()
    cursor = datab.cursor(buffered=True)
    cursor.execute("""SELECT fifth_question FROM `bot_table` WHERE chat_id = (%s)""", (message.chat.id,))
    datab.commit()
    fifth = cursor.fetchone()
    cursor = datab.cursor(buffered=True)
    cursor.execute("""SELECT sixth_question FROM `bot_table` WHERE chat_id = (%s)""", (message.chat.id,))
    datab.commit()
    sixth = cursor.fetchone()
    cursor = datab.cursor(buffered=True)
    cursor.execute("""SELECT seventh_question FROM `bot_table` WHERE chat_id = (%s)""", (message.chat.id,))
    datab.commit()
    seventh = cursor.fetchone()
    cursor = datab.cursor(buffered=True)
    cursor.execute("""SELECT eight_question FROM `bot_table` WHERE chat_id = (%s)""", (message.chat.id,))
    datab.commit()
    eight = cursor.fetchone()
    
    z=first + third + seventh
    sh = second + sixth + eight
    d = fourth + fifth
    
    if z>sh and z>d:
        await message.answer(
        "Вам больше всего подходит Золотистый ретривер!")
    elif sh>z and sh>d:
        await message.answer(
        "Вам больше всего подходит Шпиц!")
    elif d>sh and d>z:
        await message.answer(
        "Вам больше всего подходит Доберман!")
    else:
        await message.answer(
        "Упс!Ваш результат не однозначен... Наверное вам подойдет любая собачка, которая нуждается в помощи")
    await state.clear()
    
    
    
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())