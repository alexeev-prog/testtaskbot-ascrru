from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

default_router = Router()


@default_router.message(Command("chatid"))
async def get_chatid(message: Message):
    await message.answer(f"Chat id: {message.chat.id}")


def create_main_inline_markup() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="📊 Услуги компании", callback_data="services")],
        [InlineKeyboardButton(text="ℹ️ О нас", callback_data="about")],
        [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def create_services_markup() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="👥 Подбор персонала", callback_data="service_1")],
        [
            InlineKeyboardButton(
                text="🔄 Аутсорсинг бизнес-функций", callback_data="service_2"
            )
        ],
        [InlineKeyboardButton(text="💼 Консалтинг", callback_data="service_3")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def create_personal_markup() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text="Подбор руководителей высшего звена",
                url="https://ascr.ru/search_personal/",
            )
        ],
        [
            InlineKeyboardButton(
                text="Подбор высококвалифицированных специалистов",
                url="https://ascr.ru/search_personal/",
            )
        ],
        [InlineKeyboardButton(text="⬅️ Назад к услугам", callback_data="services")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def create_outsourcing_markup() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text="Аутсорсинг кадрового делопроизводства",
                url="https://ascr.ru/outsourcing/",
            )
        ],
        [InlineKeyboardButton(text="IT - сервисы", url="https://ascr.ru/outsourcing/")],
        [
            InlineKeyboardButton(
                text="Юридический аутсорсинг", url="https://ascr.ru/outsourcing/"
            )
        ],
        [
            InlineKeyboardButton(
                text="Аутсорсинг административных функций",
                url="https://ascr.ru/outsourcing/",
            )
        ],
        [InlineKeyboardButton(text="⬅️ Назад к услугам", callback_data="services")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def create_consulting_markup() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Стратегия", url="https://ascr.ru/consalting/")],
        [InlineKeyboardButton(text="Управление", url="https://ascr.ru/consalting/")],
        [InlineKeyboardButton(text="Финансы", url="https://ascr.ru/consalting/")],
        [InlineKeyboardButton(text="Маркетинг", url="https://ascr.ru/consalting/")],
        [InlineKeyboardButton(text="Производство", url="https://ascr.ru/consalting/")],
        [InlineKeyboardButton(text="⬅️ Назад к услугам", callback_data="services")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


@default_router.message(Command("start"))
async def cmd_start(message: Message):
    if message.chat.type != "private":
        await message.answer("Я работаю только в личном чате!")
        return
    await message.answer(
        text="Добро пожаловать в бот компании 'Аналитика'!",
        parse_mode=ParseMode.HTML,
        reply_markup=create_main_inline_markup(),
    )


@default_router.message(Command("services"))
async def cmd_services(message: Message):
    await message.answer(
        text="Выберите категорию услуг:", reply_markup=create_services_markup()
    )


@default_router.callback_query(F.data == "main_menu")
async def main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Добро пожаловать в бот компании 'Аналитика'!",
        reply_markup=create_main_inline_markup(),
    )
    await callback.answer()


@default_router.callback_query(F.data == "services")
async def services_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Выберите категорию услуг:", reply_markup=create_services_markup()
    )
    await callback.answer()


@default_router.callback_query(F.data == "about")
async def about_company(callback: CallbackQuery):
    text = (
        "Основана в 2004 году.\n\n"
        "Мы оказываем профессиональные услуги для развития бизнеса: подбор персонала, "
        "аутсорсинг бизнес-функций и консалтинг. Наши эксперты успешно осуществляют проекты "
        "в управлении персоналом, бухгалтерском учете, юриспруденции, инженерии, продажах, "
        "маркетинге, информационных технологиях, логистике, производстве и др.\n\n"
        "Среди наших Клиентов ведущие предприятия B2B и B2C. Имеем многолетний опыт работы "
        "с ведущими международными холдингами, входящими в рейтинги Forbes, компаниями "
        "среднего бизнеса России и ближнего зарубежья."
    )
    keyboard = [[InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")]]
    await callback.message.edit_text(
        text=text, reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
    )
    await callback.answer()


@default_router.callback_query(F.data == "contacts")
async def company_contacts(callback: CallbackQuery):
    text = (
        "Адрес: 115280, Москва, ул. Ленинская слобода, д.26, БЦ «Омега - 2», корпус А, офис 413.3\n\n"
        "+7 (495) 978 77 26\n"
        "+7 (495) 104 81 89\n"
        "info@ascr.ru"
    )
    keyboard = [[InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")]]
    await callback.message.edit_text(
        text=text, reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
    )
    await callback.answer()


@default_router.callback_query(F.data == "service_1")
async def personal_service(callback: CallbackQuery):
    text = (
        "Мы подбираем персонал любого уровня: линейных специалистов, высшее руководство, "
        "сотрудников, развивающих бизнес, и персонал, поддерживающий предприятие.\n\n"
        "Каждый из наших консультантов является экспертом в своей области, что помогает "
        "понимать специфику Вашего бизнеса и безошибочно подбирать лучших кандидатов."
    )
    await callback.message.edit_text(text=text, reply_markup=create_personal_markup())
    await callback.answer()


@default_router.callback_query(F.data == "service_2")
async def outsourcing_service(callback: CallbackQuery):
    text = (
        "Мы поддерживаем бизнес-процессы кадрового делопроизводства, юридического сопровождения, "
        "информационных технологий, административных, производственных и складских функций.\n\n"
        "Специалисты нашей Компании обеспечивают эффективное выполнение процедур, сокращая "
        "на четверть операционные расходы, и предоставляют постоянный доступ к квалифицированным ресурсам."
    )
    await callback.message.edit_text(
        text=text, reply_markup=create_outsourcing_markup()
    )
    await callback.answer()


@default_router.callback_query(F.data == "service_3")
async def consulting_service(callback: CallbackQuery):
    text = (
        "Мы решаем задачи различной сложности: от повышения эффективности отдельных "
        "фунциональных процессов до поддержки в достижении стратегических целей компании. "
        "Эксперты 'Аналитики' внедряют лучшие международные отраслевые практики для развития "
        "бизнеса и оптимизации управления предприятиями.\n\n"
        "Конечный результат наших услуг – практическое внедрение предлагаемых решений. "
        "Мы не только вырабатываем идеи, мы становимся частью команды Клиента и вместе "
        "добиваемся положительных перемен."
    )
    await callback.message.edit_text(text=text, reply_markup=create_consulting_markup())
    await callback.answer()
