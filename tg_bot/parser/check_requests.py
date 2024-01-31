import requests

json_data = {
        'size': 1000,
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

with open('proxy.txt', 'r', encoding='utf-8') as file:
    proxyy_ = file.readlines()[-1].strip()
proxy = dict(http=proxyy_,
             https=proxyy_)

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJmNGJiNmVhMS0wNGZiLTRkZTEtYThkZS0xM2E5OTJkMjQ3OGIiLCJzdWIiOiJhbm9ueW1vdXMiLCJleHAiOjE3MDY3NTA2MzV9.cHxx1BtXZ7BSEWehKsPwRyLYQPDbuJtFLoi2TDoeNCzRN0RfNNnCeU5rkKwZyRIXU5Quov05-rB41VfeOP6E_w',
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

response = requests.post(
                    'https://pub.fsa.gov.ru/api/v1/rds/common/declarations/get',
                    headers=headers,
                    json=json_data,
                proxies=proxy,verify=False
            )
print('Поисковой запрос',response)