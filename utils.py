import requests
import json
import xmltodict

def currency_rates(currency_name):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url, verify=False)
    #print('Код ответа на запрос к API (http://www.cbr.ru/scripts/XML_daily.asp):', response.status_code)
    temp_content = response.content
    # ответ ролоучаем в виде xml
    # пример
    """
    ValCurs Date="30.04.2022" name="Foreign Currency Market">
     <Valute ID="R01010">
      <NumCode>036</NumCode>
      <CharCode>AUD</CharCode>
      <Nominal>1</Nominal>
      <Name>Австралийский доллар</Name>
     <Value>50,7677</Value>
     </Valute>
      <Valute ID="R01020A">
      <NumCode>944</NumCode>
      <CharCode>AZN</CharCode>
      <Nominal>1</Nominal>
      <Name>Азербайджанский манат</Name>
      <Value>41,7786</Value>
     </Valute>
    """

    find_ok = False

    # Чтобы элегантно превратить XML в словарь будем использовать xmltodict
    dict_result = xmltodict.parse(temp_content)
    # Вытаскиваем из словаря список словарей
    list_valute = dict_result['ValCurs']['Valute']
    for item in list_valute:
        if item['CharCode'] == currency_name:
            print(item['Name'])
            temp_value = str(item['Value'])
            temp_value_float = float(temp_value.replace(',', '.'))
            #print(temp_value_float)
            #print(type(temp_value_float))
            find_ok =True
            break
    if find_ok:
        return temp_value_float
    else:
        return None