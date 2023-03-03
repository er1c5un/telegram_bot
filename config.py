'''

Use this token to access the HTTP API:
5502956094:AAEzzRFsu8K1_1cDIWJsCNLcM7XF5osy3z8
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
'''

TOKEN = '5502956094:AAEzzRFsu8K1_1cDIWJsCNLcM7XF5osy3z8'

codes = {
    'AUD': 'Австралийский доллар',
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'AMD': 'Армянский драм',
    'BYN': 'Белорусский рубль',
    'BRL': 'Бразильский реал',
    'GEL': 'Лари',
    'KZT': 'Тенге',
    'CAD': 'Канадский доллар',
    'RUB': 'Российский рубль',
    'UAH': 'Украинская гривна',
    'CNY': 'Китайский юань',
    'GBP': 'Фунт стерлингов Великобритании'
}

additional_codes = {
    'AED': 'Дирхам ОАЭ',
    'AFN': 'Афганский афгани',
    'ALL': 'Албанский лек',
    'AMD': 'Армянский драм',
    'AOA': 'Ангольская кванза',
    'ARS': 'Аргентинский песо',
    'AUD': 'Австралийский доллар',
    'AZN': 'Азербайджанский манат',
    'BDT': 'Бангладешская така',
    'BGN': 'Болгарский лев',
    'BHD': 'Бахрейнский динар',
    'BND': 'Брунейский доллар',
    'BOB': 'Боливийский боливиано',
    'BRL': 'Бразильский реал',
    'BWP': 'Ботсванская пула',
    'BYN': 'Белорусский рубль',
    'CAD': 'Канадский доллар',
    'CDF': 'Конголезский франк',
    'CLP': 'Чилийский песо',
    'COP': 'Колумбийский песо',
    'CRC': 'Костариканский колон',
    'CUP': 'Кубинский песо',
    'CZK': 'Чешская крона',
    'DJF': 'Джибутийский франк',
    'DKK': 'Датская крона',
    'DZD': 'Алжирский динар',
    'EGP': 'Египетский фунт',
    'ETB': 'Эфиопский быр',
    'GEL': 'Грузинский лари',
    'GHS': 'Ганский седи',
    'GMD': 'Гамбийский даласи',
    'GNF': 'Гвинейский франк',
    'HKD': 'Гонконгский доллар',
    'HRK': 'Хорватская куна',
    'HUF': 'Венгерский форинт',
    'IDR': 'Индонезийская рупия',
    'ILS': 'Израильский шекель',
    'INR': 'Индийская рупия',
    'IQD': 'Иракский динар',
    'IRR': 'Иранский риал',
    'ISK': 'Исландская крона',
    'JOD': 'Иорданский динар',
    'KES': 'Кенийский шиллинг',
    'KGS': 'Киргизский сом	',
    'KHR': 'Камбоджийский риель',
    'KPW': 'Северо-корейская вона (КНДР)',
    'KRW': 'Южно-корейская вона (Корея)',
    'KWD': 'Кувейтский динар',
    'KZT': 'Казахстанский тенге',
    'LAK': 'Лаосский кип',
    'LBP': 'Ливанский фунт',
    'LKR': 'Шри-ланкийская рупия',
    'LYD': 'Ливийский динар',
    'MAD': 'Марокканский дирхам',
    'MDL': 'Молдовский лей',
    'MGA': 'Малагасийский ариари',
    'MKD': 'Македонский денар',
    'MNT': 'Монгольский тугрик',
    'MRO': 'Мавританская угия',
    'MUR': 'Маврикийская рупия',
    'MVR': 'Мальдивская руфия',
    'MWK': 'Малавийская квача',
    'MXN': 'Мексиканский песо',
    'MYR': 'Малайзийский ринггит',
    'MZN': 'Мозамбикский метикал',
    'NAD': 'Намибийский доллар',
    'NGN': 'Нигерийская наира',
    'NIO': 'Никарагуанская кордоба',
    'NOK': 'Норвежская крона',
    'NPR': 'Непальская рупия',
    'NZD': 'Ново­зеландский доллар',
    'OMR': 'Оманский риал',
    'PEN': 'Перуанский соль',
    'PHP': 'Филиппинский песо',
    'PKR': 'Пакистанская рупия',
    'PLN': 'Польский злотый',
    'PYG': 'Парагвайский гуарани',
    'QAR': 'Катарский риал',
    'RON': 'Новый румынский лей',
    'RSD': 'Сербский динар',
    'SAR': 'Саудовский риял',
    'SCR': 'Сейшельская рупия',
    'SDG': 'Суданский фунт',
    'SEK': 'Шведская крона',
    'SGD': 'Сингапурский доллар',
    'SLL': 'Сьерра-леонский леоне',
    'SOS': 'Сомалийский шиллинг',
    'SRD': 'Суринамский доллар',
    'SYP': 'Сирийский фунт',
    'SZL': 'Свазилендский лилангени',
    'THB': 'Таиландский бат',
    'TJS': 'Таджикский сомони',
    'TMT': 'Туркменский манат',
    'TND': 'Тунисский динар',
    'TRY': 'Новая турецкая лира',
    'TWD': 'Тайваньский доллар',
    'TZS': 'Танзанийский шиллинг',
    'UGX': 'Угандийский шиллинг',
    'UYU': 'Уругвайский песо',
    'UZS': 'Узбекский сум',
    'VEF': 'Венесуэльский боливар',
    'VND': 'Вьетнамский донг',
    'XAF': 'Франк КФА (Центральная Африка)',
    'XDR': 'СПЗ',
    'XOF': 'Франк КФА (Западная Африка)',
    'YER': 'Йеменский риал',
    'ZAR': 'Южно-африканский рэнд',
    'ZMK': 'Замбийская квача',
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'BYR': 'Белорусский рубль',
    'RUB': 'Российский рубль',
    'UAH': 'Украинская гривна',
    'CNY': 'Китайский юань',
    'GBP': 'Фунт стерлингов Великобритании',
}

crypto_codes = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
    'USDT': 'Tether',
    'BNB': 'BNB',
    'XRP': 'XRP',
    'DOGE': 'Dogecoin',
    'ADA': 'Cardano',
    'SHIB': 'Shiba Inu',
}
