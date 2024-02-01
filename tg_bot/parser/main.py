import datetime
import requests
from requests import Session
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import undetected_chromedriver as uc
import time
from anti_useragent import UserAgent
import json
from pprint import pprint
import xlsxwriter
import urllib3
import concurrent.futures
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from itertools import cycle



urllib3.disable_warnings()
c = 0
column = [
 'ID','Тип декларации','Технические регламенты','Группа продукции ЕАЭС','Схема декларирования',	'Тип объекта декларирования',	'Статус декларации',	'Регистрационный номер декларации о соответствии',	'Дата регистрации декларации'	,'Дата окончания действия декларации о соответствии',	'Заявитель','Полное наименование юридического лица',	'ИНН(заявитель)',	'ОГРН(-ИП)(заявитель)',	'Адрес места осуществления деятельности',	'Адрес места нахождения(заявитель)',	'Номер телефона(заявитель)',	'Адрес электронной почты(заявитель)',	'Полное наименование','ИНН(иготовитель)',	'Адрес места нахождения(иготовитель)',	'Адрес производства продукции',	'Номер телефона(иготовитель)',	'Адрес электронной почты(иготовитель)',	'Продукция, ввезена для проведения исследований и испытаний в качестве проб (образцов) для целей подтверждения соответствия?',	'Регистрационный номер таможенной декларации',	'Общее наименование продукции',	'Общие условия хранения продукции',	'Происхождение продукции',	'Размер партии',	'Код ТН ВЭД ЕАЭС',	'Наименование (обозначение) продукции',	'Наименование документа',	'Испытания продукции',	'Наименование испытательной лаборатории'
]

dct_country_ = {'АФГАНИСТАН': '004', 'АЛБАНИЯ': '008', 'АНТАРКТИДА': '010', 'АЛЖИР': '012',
               'АМЕРИКАНСКОЕ САМОА': '016', 'АНДОРРА': '020', 'АНГОЛА': '024', 'АНТИГУА И БАРБУДА': '028',
               'АЗЕРБАЙДЖАН': '031', 'АРГЕНТИНА': '032', 'АВСТРАЛИЯ': '036', 'АВСТРИЯ': '040', 'БАГАМЫ': '044',
               'БАХРЕЙН': '048', 'БАНГЛАДЕШ': '050', 'АРМЕНИЯ': '051', 'БАРБАДОС': '052', 'БЕЛЬГИЯ': '056',
               'БЕРМУДЫ': '060', 'БУТАН': '064', 'БОЛИВИЯ, МНОГОНАЦИОНАЛЬНОЕ ГОСУДАРСТВО': '068',
               'БОСНИЯ И ГЕРЦЕГОВИНА': '070', 'БОТСВАНА': '072', 'ОСТРОВ БУВЕ': '074', 'БРАЗИЛИЯ': '076',
               'БЕЛИЗ': '084', 'БРИТАНСКАЯ ТЕРРИТОРИЯ В ИНДИЙСКОМ ОКЕАНЕ': '086', 'СОЛОМОНОВЫ ОСТРОВА': '090',
               'ВИРГИНСКИЕ ОСТРОВА, БРИТАНСКИЕ': '092', 'БРУНЕЙ-ДАРУССАЛАМ': '096', 'БОЛГАРИЯ': '100', 'МЬЯНМА': '104',
               'БУРУНДИ': '108', 'БЕЛАРУСЬ': '112', 'КАМБОДЖА': '116', 'КАМЕРУН': '120', 'КАНАДА': '124', 'КАБО-ВЕРДЕ': '132',
               'ОСТРОВА КАЙМАН': '136', 'ЦЕНТРАЛЬНО-АФРИКАНСКАЯ РЕСПУБЛИКА': '140', 'ШРИ-ЛАНКА': '144', 'ЧАД': '148', 'ЧИЛИ': '152',
               'КИТАЙ': '156', 'ТАЙВАНЬ (КИТАЙ)': '158', 'ОСТРОВ РОЖДЕСТВА': '162', 'КОКОСОВЫЕ (КИЛИНГ) ОСТРОВА': '166', 'КОЛУМБИЯ': '170',
               'КОМОРЫ': '174', 'МАЙОТТА': '175', 'КОНГО': '178', 'КОНГО, ДЕМОКРАТИЧЕСКАЯ РЕСПУБЛИКА': '180', 'ОСТРОВА КУКА': '184', 'КОСТА-РИКА': '188',
               'ХОРВАТИЯ': '191', 'КУБА': '192', 'КИПР': '196', 'ЧЕХИЯ': '203', 'БЕНИН': '204', 'ДАНИЯ': '208', 'ДОМИНИКА': '212', 'ДОМИНИКАНСКАЯ РЕСПУБЛИКА': '214', 'ЭКВАДОР': '218',
               'ЭЛЬ-САЛЬВАДОР': '222', 'ЭКВАТОРИАЛЬНАЯ ГВИНЕЯ': '226', 'ЭФИОПИЯ': '231', 'ЭРИТРЕЯ': '232', 'ЭСТОНИЯ': '233', 'ФАРЕРСКИЕ ОСТРОВА': '234',
               'ФОЛКЛЕНДСКИЕ ОСТРОВА (МАЛЬВИНСКИЕ)': '238', 'ЮЖНАЯ ДЖОРДЖИЯ И ЮЖНЫЕ САНДВИЧЕВЫ ОСТРОВА': '239', 'ФИДЖИ': '242', 'ФИНЛЯНДИЯ': '246',
               'ЭЛАНДСКИЕ ОСТРОВА': '248', 'ФРАНЦИЯ': '250', 'ФРАНЦУЗСКАЯ ГВИАНА': '254', 'ФРАНЦУЗСКАЯ ПОЛИНЕЗИЯ': '258', 'ФРАНЦУЗСКИЕ ЮЖНЫЕ ТЕРРИТОРИИ': '260',
               'ДЖИБУТИ': '262', 'ГАБОН': '266', 'ГРУЗИЯ': '268', 'ГАМБИЯ': '270', 'ПАЛЕСТИНА, ГОСУДАРСТВО': '275', 'ГЕРМАНИЯ': '276', 'ГАНА': '288', 'ГИБРАЛТАР': '292',
               'КИРИБАТИ': '296', 'ГРЕЦИЯ': '300', 'ГРЕНЛАНДИЯ': '304', 'ГРЕНАДА': '308', 'ГВАДЕЛУПА': '312', 'ГУАМ': '316', 'ГВАТЕМАЛА': '320', 'ГВИНЕЯ': '324', 'ГАЙАНА': '328',
               'ГАИТИ': '332', 'ОСТРОВ ХЕРД И ОСТРОВА МАКДОНАЛЬД': '334', 'ПАПСКИЙ ПРЕСТОЛ (ГОСУДАРСТВО — ГОРОД ВАТИКАН)': '336', 'ГОНДУРАС': '340', 'ГОНКОНГ': '344', 'ВЕНГРИЯ': '348',
               'ИСЛАНДИЯ': '352', 'ИНДИЯ': '356', 'ИНДОНЕЗИЯ': '360', 'ИРАН, ИСЛАМСКАЯ РЕСПУБЛИКА': '364',
               'ИРАК': '368', 'ИРЛАНДИЯ': '372', 'ИЗРАИЛЬ': '376', 'ИТАЛИЯ': '380',
               'КОТ Д’ИВУАР': '384', 'ЯМАЙКА': '388', 'ЯПОНИЯ': '392', 'КАЗАХСТАН': '398',
               'ИОРДАНИЯ': '400', 'КЕНИЯ': '404', 'КОРЕЯ, НАРОДНО-ДЕМОКРАТИЧЕСКАЯ РЕСПУБЛИКА': '408',
               'КОРЕЯ, РЕСПУБЛИКА': '410', 'КУВЕЙТ': '414', 'КИРГИЗИЯ': '417', 'ЛАОССКАЯ НАРОДНО-ДЕМОКРАТИЧЕСКАЯ РЕСПУБЛИКА': '418',
               'ЛИВАН': '422', 'ЛЕСОТО': '426', 'ЛАТВИЯ': '428', 'ЛИБЕРИЯ': '430', 'ЛИВИЯ': '434', 'ЛИХТЕНШТЕЙН': '438', 'ЛИТВА': '440',
               'ЛЮКСЕМБУРГ': '442', 'МАКАО': '446', 'МАДАГАСКАР': '450', 'МАЛАВИ': '454', 'МАЛАЙЗИЯ': '458', 'МАЛЬДИВЫ': '462', 'МАЛИ': '466',
               'МАЛЬТА': '470', 'МАРТИНИКА': '474', 'МАВРИТАНИЯ': '478', 'МАВРИКИЙ': '480', 'МЕКСИКА': '484', 'МОНАКО': '492', 'МОНГОЛИЯ': '496',
               'МОЛДОВА, РЕСПУБЛИКА': '498', 'ЧЕРНОГОРИЯ': '499', 'МОНТСЕРРАТ': '500', 'МАРОККО': '504', 'МОЗАМБИК': '508', 'ОМАН': '512', 'НАМИБИЯ': '516',
               'НАУРУ': '520', 'НЕПАЛ': '524', 'НИДЕРЛАНДЫ': '528', 'КЮРАСАО': '531',
               'АРУБА': '533', 'СЕН-МАРТЕН (нидерландская часть)': '534',
               'БОНЭЙР, СИНТ-ЭСТАТИУС И САБА': '535', 'НОВАЯ КАЛЕДОНИЯ': '540',
               'ВАНУАТУ': '548', 'НОВАЯ ЗЕЛАНДИЯ': '554', 'НИКАРАГУА': '558', 'НИГЕР': '562',
               'НИГЕРИЯ': '566', 'НИУЭ': '570', 'ОСТРОВ НОРФОЛК': '574', 'НОРВЕГИЯ': '578',
               'СЕВЕРНЫЕ МАРИАНСКИЕ ОСТРОВА': '580', 'МАЛЫЕ ТИХООКЕАНСКИЕ ОТДАЛЕННЫЕ ОСТРОВА СОЕДИНЕННЫХ ШТАТОВ': '581', 'МИКРОНЕЗИЯ, ФЕДЕРАТИВНЫЕ ШТАТЫ': '583', 'МАРШАЛЛОВЫ ОСТРОВА': '584', 'ПАЛАУ': '585', 'ПАКИСТАН': '586',
               'ПАНАМА': '591', 'ПАПУА-НОВАЯ ГВИНЕЯ': '598', 'ПАРАГВАЙ': '600', 'ПЕРУ': '604', 'ФИЛИППИНЫ': '608', 'ПИТКЕРН': '612', 'ПОЛЬША': '616', 'ПОРТУГАЛИЯ': '620', 'ГВИНЕЯ-БИСАУ': '624', 'ТИМОР-ЛЕСТЕ': '626', 'ПУЭРТО-РИКО': '630', 'КАТАР': '634', 'РЕЮНЬОН': '638', 'РУМЫНИЯ': '642', 'РОССИЯ': '643', 'РУАНДА': '646', 'СЕН-БАРТЕЛЕМИ': '652', 'СВЯТАЯ ЕЛЕНА, ОСТРОВ ВОЗНЕСЕНИЯ, ТРИСТАН-ДА-КУНЬЯ': '654', 'СЕНТ-КИТС И НЕВИС': '659', 'АНГИЛЬЯ': '660', 'СЕНТ-ЛЮСИЯ': '662', 'СЕН-МАРТЕН': '663', 'СЕН-ПЬЕР И МИКЕЛОН': '666', 'СЕНТ-ВИНСЕНТ И ГРЕНАДИНЫ': '670', 'САН-МАРИНО': '674', 'САН-ТОМЕ И ПРИНСИПИ': '678', 'САУДОВСКАЯ АРАВИЯ': '682', 'СЕНЕГАЛ': '686', 'СЕРБИЯ': '688', 'СЕЙШЕЛЫ': '690', 'СЬЕРРА-ЛЕОНЕ': '694', 'СИНГАПУР': '702', 'СЛОВАКИЯ': '703', 'ВЬЕТНАМ': '704', 'СЛОВЕНИЯ': '705', 'СОМАЛИ': '706', 'ЮЖНАЯ АФРИКА': '710', 'ЗИМБАБВЕ': '716', 'ИСПАНИЯ': '724', 'ЮЖНЫЙ СУДАН': '728', 'СУДАН': '729', 'ЗАПАДНАЯ САХАРА': '732', 'СУРИНАМ': '740', 'ШПИЦБЕРГЕН И ЯН МАЙЕН': '744', 'ЭСВАТИНИ': '748', 'ШВЕЦИЯ': '752', 'ШВЕЙЦАРИЯ': '756', 'СИРИЙСКАЯ АРАБСКАЯ РЕСПУБЛИКА': '760', 'ТАДЖИКИСТАН': '762', 'ТАИЛАНД': '764', 'ТОГО': '768', 'ТОКЕЛАУ': '772', 'ТОНГА': '776', 'ТРИНИДАД И ТОБАГО': '780', 'ОБЪЕДИНЕННЫЕ АРАБСКИЕ ЭМИРАТЫ': '784', 'ТУНИС': '788', 'ТУРЦИЯ': '792', 'ТУРКМЕНИЯ': '795', 'ОСТРОВА ТЕРКС И КАЙКОС': '796', 'ТУВАЛУ': '798', 'УГАНДА': '800', 'УКРАИНА': '804', 'РЕСПУБЛИКА СЕВЕРНАЯ МАКЕДОНИЯ': '807', 'ЕГИПЕТ': '818', 'СОЕДИНЕННОЕ КОРОЛЕВСТВО': '826', 'ГЕРНСИ': '831', 'ДЖЕРСИ': '832', 'ОСТРОВ МЭН': '833', 'ТАНЗАНИЯ, ОБЪЕДИНЕННАЯ РЕСПУБЛИКА': '834', 'СОЕДИНЕННЫЕ ШТАТЫ': '840', 'ВИРГИНСКИЕ ОСТРОВА, США': '850', 'БУРКИНА-ФАСО': '854', 'УРУГВАЙ': '858', 'УЗБЕКИСТАН': '860', 'ВЕНЕСУЭЛА БОЛИВАРИАНСКАЯ РЕСПУБЛИКА': '862', 'УОЛЛИС И ФУТУНА': '876', 'САМОА': '882', 'ЙЕМЕН': '887', 'ЗАМБИЯ': '894', 'АБХАЗИЯ': '895', 'ЮЖНАЯ ОСЕТИЯ': '896', 'ДНР': '897', 'ЛНР': '898'}
dct_country = {}
for key, value in dct_country_.items():
    dct_country[value] = key


def parser(user_id: int, status: list = [],zayvitel: list = [],tech_reg: list = [],type_decl: list = [],type_obj_decl: list = [],proizhodenie_product: list = [],edini_perechen_product_eaes: list = [],
           edini_perechen_product_rf:list = [],reg_date_min: str = '',reg_date_max: str = '',end_date_min: str = '',end_date_max: str = '',group_product_rf: list = [],group_product_eaes: list = []):
    token = ''
    def get_token():
        print('запустили селениум')
        service = Service()
        start = time.perf_counter()
        while True:
            try: 
                with webdriver.Chrome(service=service) as driver:
                    driver.get("https://pub.fsa.gov.ru/rds/declaration")
                    time.sleep(3)
                    token = driver.execute_script("return localStorage.getItem('fgis_token');")
                    if token:
                        driver.close()
                        print(time.perf_counter() - start)
                        return token
                        break
                    driver.close()
            except Exception as error:
                print(100)
                print(f"Ошибка: {error}")

    token = get_token()

    cookies = {
        '_ym_uid': '1705671501665048053',
        '_ym_d': '1705671501',
        'BITRIX_SM_GUEST_ID': '26303853',
        'BITRIX_SM_LAST_VISIT': '19.01.2024%2016%3A38%3A31',
        'BITRIX_SM_LAST_ADV': '5_Y',
        'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A44%2C%22EXPIRE%22%3A1705697940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
        '_ym_isad': '1',
        'JSESSIONID': '17EAAC22F70159CC8793BDDF503B1AEF',
        'show_new_design': 'yes',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJlNzI0Y2NjYy1lYzIzLTRkYmEtOWRlMi1lYjg5OTg0ZmZlYzQiLCJzdWIiOiJhbm9ueW1vdXMiLCJleHAiOjE3MDY1NzU1NDR9.PAraj4rfGWJXCXM5awmLPKaiibHI4bbcied3aHs29Re2eXdFtqkw5ihkemXEIjDXU3U_dbgfCLR4KkR2hkB_CQ',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'Origin': 'https://pub.fsa.gov.ru',
        'Connection': 'keep-alive',
        'Referer': 'https://pub.fsa.gov.ru/rds/declaration',
        # 'Cookie': '_ym_uid=1705671501665048053; _ym_d=1705671501; BITRIX_SM_GUEST_ID=26303853; BITRIX_SM_LAST_VISIT=19.01.2024%2016%3A38%3A31; BITRIX_SM_LAST_ADV=5_Y; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A44%2C%22EXPIRE%22%3A1705697940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_isad=1; JSESSIONID=17EAAC22F70159CC8793BDDF503B1AEF; show_new_design=yes',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    headers['Authorization'] = token
    print(headers['Authorization'])
    with open('tg_bot/parser/col.txt','r',encoding='utf-8') as file:
        col = file.readlines()[0]
    print(col)
    json_data = {
        'size': int(col),
        'page': 0,
        'filter': {
            'status': [
            ],
            'idDeclType': [],
            'idCertObjectType': [],
            'idProductType': [],
            'idGroupRU': [],
            'idGroupEEU': [],
            'idTechReg': [
            ],
            'idApplicantType': [],
            'regDate': {
                'minDate': None,
                'maxDate': None,
            },
            'endDate': {
                'minDate': None,
                'maxDate': None,
            },
            'columnsSearch': [],
            'idProductOrigin': [],
            'idProductEEU': [],
            'idProductRU': [],
            'idDeclScheme': [],
            'awaitForApprove': None,
            'awaitOperatorCheck': None,
            'editApp': None,
            'violationSendDate': None,
            'isProtocolInvalid': None,
            'checkerAIResult': None,
            'checkerAIProtocolsResults': None,
            'checkerAIProtocolsMistakes': None,
            'hiddenFromOpen': None,
        },
        'columnsSort': [
            {
                'column': 'declDate',
                'sort': 'DESC',
            },
        ], #status: list = [],zayvitel: list = [],tech_reg: list = [],type_decl: list = [],type_obj_decl: list = [],proizhodenie_product: list = [],edini_perechen_product_eaes: list = [],
           #edini_perechen_product_rf:list = [],reg_date_min: str = '',reg_date_max: str = '',end_date_min: str = '',end_date_max: str = '',group_product_rf: list = [],group_product_eaes: list = []
    }
    json_data['filter']['status'].extend(status)
    json_data['filter']['idDeclType'].extend(type_decl)
    json_data['filter']['idTechReg'].extend(tech_reg)
    json_data['filter']['idApplicantType'].extend(zayvitel)
    json_data['filter']['idCertObjectType'].extend(type_obj_decl)
    json_data['filter']['idProductOrigin'].extend(proizhodenie_product)
    json_data['filter']['idProductEEU'].extend(edini_perechen_product_eaes)
    json_data['filter']['idProductRU'].extend(edini_perechen_product_rf)
    json_data['filter']['idGroupRU'].extend(group_product_rf)
    json_data['filter']['idGroupEEU'].extend(group_product_eaes)
    json_data['filter']['regDate']['minDate'] = reg_date_min
    json_data['filter']['regDate']['maxDate'] = reg_date_max
    json_data['filter']['endDate']['minDate'] = end_date_min
    json_data['filter']['endDate']['maxDate'] = end_date_max
    with open('tg_bot/parser/proxy.txt','r',encoding='utf-8') as file:
        proxyy_ = list(map(lambda x: x.strip(), file.readlines()[1:]))
    proxy = cycle(proxyy_)

    ua = UserAgent()
    headers['User-Agent'] = ua.random
    while True:
        try:
            proxi = next(proxy)
            proxy_ye = dict(http=f'socks5://{proxi}',
                            https=f'socks5://{proxi}')
            response = requests.post(
                    'https://pub.fsa.gov.ru/api/v1/rds/common/declarations/get',
                    headers=headers,
                    json=json_data,
                proxies=proxy_ye,verify=False
            )
            print('Поисковой запрос',response)
            items = response.json().get('items')
            break
        except Exception as ex:
            proxi = next(proxy)
            time.sleep(1)
            print(ex)
            print('error у поискового запроса')
    flattens = []
    def start(item):
        break_count = 0
        global c
        while True:
            try:
                proxi = next(proxy)
                proxy_ye = dict(http=f'socks5://{proxi}',
                                https=f'socks5://{proxi}')
                json_data_mult = {
                    'items': {
                        'validationScheme2': [
                            {
                                'id': [
                                ],
                                'fields': [
                                    'id',
                                    'masterId',
                                    'name',
                                    'validityTerm',
                                    'isSeriesProduction',
                                    'isBatchProduction',
                                    'isOneOffProduction',
                                    'isProductSampleTesting',
                                    'isBatchProductTesting',
                                    'isOneOffProductTesting',
                                    'isAccreditationLab',
                                    'isApplicantManufacturer',
                                    'isApplicantProvider',
                                    'isPresenceOfProxy',
                                    'isApplicantForeign',
                                    'isApplicantEeuMember',
                                ],
                            },
                        ],
                        'tnved': [
                            {
                                'id': [
                                ],
                                'fields': [
                                    'id',
                                    'masterId',
                                    'name',
                                    'code',
                                    'hidden',
                                ],
                            },
                        ],
                    },
                }

                status_ = {}
                status = {'Черновик': 20, 'Отправлен': 13, 'Удалён': 18, 'Действует': 6, 'Прекращён': 14, 'Приостановлен': 15,
                 'Частично приостановлен': 19, 'Возобновлён': 3, 'Продлён': 16, 'Архивный': 1,
                 'Направлено уведомление о прекращении': 10, 'Выдано предписание': 5, 'Ожидает проверки оператора реестра': 42,
                 'Недействителен': 11}
                for key,value in status.items():
                    status_[value] = key
                id = item.get("id")
                url = f'https://pub.fsa.gov.ru/rds/declaration/view/{id}/common' # ID(url)
                type_declaration = item.get("declType") # Тип декларации
                tech_reglament = item.get("technicalReglaments") # Технические регламенты
                group_eac = item.get("group")  #Группа продукции ЕАЭС
                scheme_decl = '' #Нужно с ещё одного апи брать инфу
                dot = item.get("declObjectType") # Тип объекта декларирования
                sd = status_[item.get('idStatus')] # Статус декларации
                rnd = item.get('number') # Регистрационный номер декларации о соответствии
                ddr = item.get('declDate') # Дата регистрации декларации
                ddre = item.get('declEndDate') # Дата окончания действия декларации о соответствии
                headers['User-Agent'] = ua.random
                resp = requests.get(f'https://pub.fsa.gov.ru/api/v1/rds/common/declarations/{id}',headers=headers,verify=False,proxies=proxy_ye) # Делаем запрос к продукту
                print(f'Запрос к продукту {resp}')
                resp = resp.json()
                decl_id = resp.get('idDeclScheme')
                json_data_mult['items']['validationScheme2'][0]['id'].append(decl_id)
                zayv = resp.get('applicant').get('shortName') # Заявитель
                fzv = resp.get('applicant').get('fullName') #Полное наименование юридического лица
                inn = item.get('creatorInn') # ИНН(заявитель)
                ogrn = item.get('creatorInn') # ОГРН(-ИП)(заявитель)
                amod = ''  # Адрес места осуществления деятельности
                amn = ''  # Адрес места нахождения(заявитель)
                addres = resp.get('applicant').get('addresses') # сайт отдает два адреса,понимаем какой из них amon и amn и добавляем в список # Не записываем в ексель
                for itemm_ in addres:
                    addr_type = itemm_.get('idAddrType')
                    if addr_type == 3:
                        amod = itemm_.get('fullAddress')
                    elif addr_type == 1:
                        amn = itemm_.get('fullAddress')
                nomer = '' #Номер телефона(заявитель)
                pochta = '' #Адрес электронной почты(заявитель)
                tel_poc = resp.get('applicant').get('contacts')  # сайт отдает телефон и почту,понимаем какой из них nomer и pochta и добавляем в список # Не записываем в ексель
                for itemm_ in tel_poc:
                    addr_type = itemm_.get('idContactType')
                    if addr_type == 1:
                        nomer = itemm_.get('value')
                    elif addr_type == 4:
                        pochta = itemm_.get('value')

                full_name = item.get('manufacterName') #Полное наименование
                inn_izgotovitel = resp.get('manufacturer').get('inn') # ИНН(изготовитель)
                adr_izg = [] #Адрес места нахождения(иготовитель)
                adrs_izg_no_ex = resp.get('manufacturer').get('addresses') #АДРЕСЫ места нахождения(изготовителя) Не записываем это в ексель!
                for itemm_ in adrs_izg_no_ex:
                    adr_izg.append(itemm_.get('fullAddress'))
                adr_izg = list(map(lambda x: '' if x is None else x, adr_izg))
                adr_izg = '|'.join(adr_izg)

                adr_proizv_pr = [] # Адрес производства продукции
                adrs_proizv_pr = resp.get('manufacturerFilials') # АДРЕСЫ производства продукции Не записываем в ексель
                for itemm_ in adrs_proizv_pr:
                    adrs = itemm_.get('addresses') # АДРЕСЫ ЕЩЁ ГЛУБЖЕ производства продукции Не записываем в ексель
                    for itemm__ in adrs:
                        adr_proizv_pr.append(itemm__.get('fullAddress'))

                adr_proizv_pr = list(map(lambda x: '' if x is None else x, adr_proizv_pr))
                adr_proizv_pr = '|'.join(adr_proizv_pr) #Адрес производства продукции

                nomer_izg = ''  # Номер телефона(иготовитель)
                pochta_izg = ''  # Адрес электронной почты(иготовитель)
                tel_poc_izg = resp.get('manufacturer') if resp.get('manufacturer') else []  # сайт отдает телефон и почту,понимаем какой из них nomer и pochta и добавляем в список # Не записываем в ексель
                for itemm_ in tel_poc_izg.get('contacts'):
                    addr_type = itemm_.get('idContactType')
                    if addr_type == 1:
                        nomer_izg = itemm_.get('value')
                    elif addr_type == 4:
                        pochta_izg = itemm_.get('value')


                idcct = [] # Продукция, ввезена для проведения исследований и испытаний в качестве проб (образцов) для целей подтверждения соответствия? idcct - idDocConfirmCustomType

                labs = resp.get('testingLabs')
                for lab in labs:
                    pole = lab.get('importedForResearchTesting')
                    if pole:
                        idcct.append('да')
                    else:
                        idcct.append('нет')

                idcct = list(map(lambda x: '' if x is None else x, idcct))
                idcct = '|'.join(idcct)

                rntd  = [] # Регистрационный номер таможенной декларации
                labs = resp.get('testingLabs') # Лабы
                for lab in labs:
                    pole = lab.get('docConfirmCustom')
                    for pole_ in pole:
                        pole_ = pole_.get('customInfo')
                        for pole1 in pole_:
                            reg_nomer_tamozh_decl = pole1.get('customDeclNumber')#reg_nomer_tamozh_decl
                            rntd.append(reg_nomer_tamozh_decl)

                rntd = list(map(lambda x: '' if x is None else x, rntd))
                rntd  = '|'.join(rntd)

                obsh_np = resp.get('product').get('fullName') #Общее наименование продукции
                obsh_u_xp = resp.get('product').get('storageCondition') #Общие условия хранения продукции
                proiz_country = '' # Происхождение продукции
                proiz_country = dct_country[resp.get('product').get('idProductOrigin')] #Происхождение продукции
                razmer_p = resp.get('product').get('batchSize') # Размер партии
                id_tn_ved = resp.get('product').get('identifications') #Код ТН ВЭД ЕАЭС # НЕ ЗАПИСЫВАЕМ ЭТО ПОЛЕ В ЕКСЕЛЬ
                tnved = []
                ids = []
                for i in id_tn_ved:
                    id = i.get('idTnveds')
                    ids.extend(id)
                json_data_mult['items']['tnved'][0]['id'].extend(ids)
                headers['User-Agent'] = ua.random
                proxi = next(proxy)
                proxy_ye = dict(http=f'socks5://{proxi}',
                                https=f'socks5://{proxi}')

                mult_resp = requests.post('https://pub.fsa.gov.ru/nsi/api/multi', headers=headers, json=json_data_mult,verify=False,proxies=proxy_ye)
                print(f'mult resp {mult_resp}')
                mult_resp = mult_resp.json()
                tnved_no = mult_resp.get('tnved')
                for i in tnved_no:
                    tnved.append(f'{i.get("code")}{i.get("name")}')
                scheme = mult_resp.get('validationScheme2')
                for i in scheme:
                    scheme_decl = i.get('name')
                tnved = list(map(lambda x: '' if x is None else x, tnved))
                tnved = '|'.join(tnved)
                name_production_ = [] #Наименование (обозначение) продукции
                np1_ = resp.get('product').get('identifications')
                for pole in np1_:
                    name_production_.append(pole.get('name'))
                name_production_  = list(map(lambda x: '' if x is None else x, name_production_ ))
                name_production_ = '|'.join(name_production_) #Наименование (обозначение) продукции

                name_document = [] #Наименование документа
                nd_ = resp.get('product').get('identifications')
                for pole in nd_:
                    document = pole.get('documents')
                    for poledoc in document:
                        name_document.append(poledoc.get('name'))

                name_document = list(map(lambda x:'' if x is None else x,name_document))
                name_document = '|'.join(name_document)

                statustestinglabs = item.get('statusTestingLabs') #Испытания продукции
                name_lab_testing = []
                nlt1_ = resp.get('testingLabs')
                for lab in nlt1_:
                    name_lab_testing.append(lab.get('fullName'))
                name_lab_testing = list(map(lambda x: '' if x is None else x, name_lab_testing))
                name_lab_testing = '|'.join(name_lab_testing)
                flattens.append([url, type_declaration, tech_reglament, group_eac, scheme_decl, dot, sd, rnd, ddr, ddre,
                                zayv, fzv, inn, ogrn, amod, amn, nomer, pochta, full_name, inn_izgotovitel, adr_izg,
                                adr_proizv_pr, nomer_izg, pochta_izg, idcct, rntd, obsh_np, obsh_u_xp, proiz_country,
                                razmer_p,tnved,name_production_,name_document,statustestinglabs,name_lab_testing])
                print(f'{c}/{col}')
                time.sleep(0.5)
                c += 1
                break
            except Exception as ex:
                proxi = next(proxy)
                time.sleep(3)
                break_count += 1
                if break_count >= 30:
                    break
                print(ex)
                print('error')

    list_ = items  # сюда вставляешь то что прогоняешь через фор смотри где больше ссылок собрано
    print('Сейчас начнем')
    # print(len(list_))
    CONNECTIONS = 1  # колличетсво потоков
    out = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = {executor.submit(start, url): url for url in list_}
        done, _ = concurrent.futures.wait(future_to_url, return_when=concurrent.futures.ALL_COMPLETED)
        for future in done:
            try:
                data = future.result()
            except Exception as exc:
                data = str(type(exc))
                print(exc)
            finally:
                print('Возникла ошибка')
                out.append(data)
    date = datetime.date.today().strftime("%Y%m%d")
    workbook = xlsxwriter.Workbook(f"output{user_id}.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.set_column(0, 34, 100)

    worksheet.write_row(0, 0,
                        column)
    # Используем цикл for для перебора строк из csv файла
    for r, row in enumerate(flattens):
        for c, col in enumerate(row):
            worksheet.write(r + 1, c, col)

        # Сохраняем и закрываем xlsx файл
    workbook.close()

    return f"output{user_id}.xlsx"



#response = requests.post('https://marketchameleon.com/Reports/AfterHoursSummaryData',headers=headers, data=data,cookies=cookies)

#print(response)