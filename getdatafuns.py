#get stock_list from eastmoney web
import numpy as np
import requests
import json
from fake_useragent import UserAgent
from datetime import datetime
import pandas as pd


def getjson_stocklist(page):
    # ua = UserAgent()
    url = 'https://datacenter-web.eastmoney.com/api/data/v1/get?'
    headers = {
        'Cookie': 'qgqp_b_id=b87cee305c38b309d852cce9e3b9fb61; em_hq_fls=js; ct=weXh0EQEmoADGO5LvfNOBZ00awO1CghuGXp-jR4XkXyXyQiyq1UIBQGMwjHdwtQN0AxwgO3fMWl9uzOeSp1sA52HHwpu8MNWr3ICGvzljGkN9qBV9nuk_H1-S3SGS528HyXckjxHXxkfqofmcIJgcDWWh-wcXz34JiIVVwxjgQY; ut=FobyicMgeV6oOlrtxUaVoieuvidY5esdMCb41if8eqJiqFkwjYg2XAbdyOr2X4dfFAuLZp6zEVvi6dzeDfXQ-AmvlHTZlZ3bcLhnG2QmQB3OEIitjRXjxmZdVjfgoTl0R9Og4o-lLlFot79Tn7wCWlEmBE-Xgvm3SmKy2u_2-TT13T3Di_nblC7WJodHxryF1X8Pl-UvxHe5Ba7LrbinuGObOU_DTORRbA7CCJ680VXlO_XrihmSuhjM8Lv31Xbr4c5cw7OSmrJV114RfOXqtdOJA8M5cx0c; emshistory=%5B%22600168%22%2C%22600166%22%5D; st_si=96747731529293; st_asi=delete; HAList=ty-1-688678-%u798F%u7ACB%u65FA%2Cty-1-000001-%u4E0A%u8BC1%u6307%u6570%2Cty-0-300059-%u4E1C%u65B9%u8D22%u5BCC%2Cty-1-600166-%u798F%u7530%u6C7D%u8F66%2Cty-1-600168-%u6B66%u6C49%u63A7%u80A1%2Cty-1-600660-%u798F%u8000%u73BB%u7483%2Cty-0-300229-%u62D3%u5C14%u601D%2Cf-0-000001-%u4E0A%u8BC1%u6307%u6570; st_pvi=95106582090246; st_sp=2021-08-10%2015%3A37%3A11; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=29; st_psi=20230505193615554-111000300841-6619305167; JSESSIONID=BE177C063CC1A664DE227D3C0F355DCD',
        'Referer': 'https://data.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        # 'User-Agent': ua.random,
        'Connection': 'close'
    }
    params = {
        'callback': 'jQuery112306043219290326622_1683286330609',
        'sortColumns': 'SECURITY_CODE',
        'sortTypes': '1',
        'pageSize': '50',
        'pageNumber': str(page),  # 第几页
        'reportName': 'RPT_HOLDERNUMLATEST',
        'columns': 'SECURITY_CODE,SECURITY_NAME_ABBR,END_DATE,INTERVAL_CHRATE,AVG_MARKET_CAP,AVG_HOLD_NUM,TOTAL_MARKET_CAP,TOTAL_A_SHARES,HOLD_NOTICE_DATE,HOLDER_NUM,PRE_HOLDER_NUM,HOLDER_NUM_CHANGE,HOLDER_NUM_RATIO,END_DATE,PRE_END_DATE',
        # 'columns': 'SECURITY_CODE,SECURITY_NAME_ABBR',
        'quoteColumns': 'f2,f3',
        'quoteType': '0',
        'source': 'WEB',
        'client': 'WEB',
    }
    response = requests.get(url=url, headers=headers, params=params)
    data = response.text
    # print(response.status_code)
    # print(response.url)
    # print(response.text)
    data = data[42:-2]  #将返回字符串转换为json格式
    data_dict = json.loads(data) # 转化为字典
    qc_data =data_dict["result"]
    # if qc_data:
    #     continue
    # else:
    qc_data_value = qc_data["data"]
    return qc_data_value


#get stock_list from eastmoney web
def pageNumber():
    # ua = UserAgent()
    url = 'https://datacenter-web.eastmoney.com/api/data/v1/get?'
    headers = {
        'Cookie': 'qgqp_b_id=b87cee305c38b309d852cce9e3b9fb61; em_hq_fls=js; ct=weXh0EQEmoADGO5LvfNOBZ00awO1CghuGXp-jR4XkXyXyQiyq1UIBQGMwjHdwtQN0AxwgO3fMWl9uzOeSp1sA52HHwpu8MNWr3ICGvzljGkN9qBV9nuk_H1-S3SGS528HyXckjxHXxkfqofmcIJgcDWWh-wcXz34JiIVVwxjgQY; ut=FobyicMgeV6oOlrtxUaVoieuvidY5esdMCb41if8eqJiqFkwjYg2XAbdyOr2X4dfFAuLZp6zEVvi6dzeDfXQ-AmvlHTZlZ3bcLhnG2QmQB3OEIitjRXjxmZdVjfgoTl0R9Og4o-lLlFot79Tn7wCWlEmBE-Xgvm3SmKy2u_2-TT13T3Di_nblC7WJodHxryF1X8Pl-UvxHe5Ba7LrbinuGObOU_DTORRbA7CCJ680VXlO_XrihmSuhjM8Lv31Xbr4c5cw7OSmrJV114RfOXqtdOJA8M5cx0c; emshistory=%5B%22600168%22%2C%22600166%22%5D; st_si=96747731529293; st_asi=delete; HAList=ty-1-688678-%u798F%u7ACB%u65FA%2Cty-1-000001-%u4E0A%u8BC1%u6307%u6570%2Cty-0-300059-%u4E1C%u65B9%u8D22%u5BCC%2Cty-1-600166-%u798F%u7530%u6C7D%u8F66%2Cty-1-600168-%u6B66%u6C49%u63A7%u80A1%2Cty-1-600660-%u798F%u8000%u73BB%u7483%2Cty-0-300229-%u62D3%u5C14%u601D%2Cf-0-000001-%u4E0A%u8BC1%u6307%u6570; st_pvi=95106582090246; st_sp=2021-08-10%2015%3A37%3A11; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=29; st_psi=20230505193615554-111000300841-6619305167; JSESSIONID=BE177C063CC1A664DE227D3C0F355DCD',
        'Referer': 'https://data.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        # 'User-Agent': ua.random,
        'Connection': 'close'
    }
    params = {
        'callback': 'jQuery112306043219290326622_1683286330609',
        'sortColumns': 'SECURITY_CODE',
        'sortTypes': '1',
        'pageSize': '50',
        'pageNumber': '1',  # 第1页
        'reportName': 'RPT_HOLDERNUMLATEST',
        'columns': 'SECURITY_CODE,SECURITY_NAME_ABBR,END_DATE,INTERVAL_CHRATE,AVG_MARKET_CAP,AVG_HOLD_NUM,TOTAL_MARKET_CAP,TOTAL_A_SHARES,HOLD_NOTICE_DATE,HOLDER_NUM,PRE_HOLDER_NUM,HOLDER_NUM_CHANGE,HOLDER_NUM_RATIO,END_DATE,PRE_END_DATE',
        'quoteColumns': 'f2,f3',
        'quoteType': '0',
        'source': 'WEB',
        'client': 'WEB',
    }
    response = requests.get(url=url, headers=headers, params=params)
    data = response.text
    data = data[42:-2]  #将返回字符串转换为json格式
    data_dict = json.loads(data) # 转化为字典
    qc_data =data_dict["result"]
    pagenumber =qc_data["pages"]
    return pagenumber


def getjson_stockincome(codenumber):
    ua = UserAgent()
    url = 'https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/lrbAjaxNew?'
    headers = {
        'Cookie': 'qgqp_b_id=b87cee305c38b309d852cce9e3b9fb61; em_hq_fls=js; ct=weXh0EQEmoADGO5LvfNOBZ00awO1CghuGXp-jR4XkXyXyQiyq1UIBQGMwjHdwtQN0AxwgO3fMWl9uzOeSp1sA52HHwpu8MNWr3ICGvzljGkN9qBV9nuk_H1-S3SGS528HyXckjxHXxkfqofmcIJgcDWWh-wcXz34JiIVVwxjgQY; ut=FobyicMgeV6oOlrtxUaVoieuvidY5esdMCb41if8eqJiqFkwjYg2XAbdyOr2X4dfFAuLZp6zEVvi6dzeDfXQ-AmvlHTZlZ3bcLhnG2QmQB3OEIitjRXjxmZdVjfgoTl0R9Og4o-lLlFot79Tn7wCWlEmBE-Xgvm3SmKy2u_2-TT13T3Di_nblC7WJodHxryF1X8Pl-UvxHe5Ba7LrbinuGObOU_DTORRbA7CCJ680VXlO_XrihmSuhjM8Lv31Xbr4c5cw7OSmrJV114RfOXqtdOJA8M5cx0c; emshistory=%5B%22600168%22%2C%22600166%22%5D; st_si=96747731529293; st_asi=delete; HAList=ty-1-688678-%u798F%u7ACB%u65FA%2Cty-1-000001-%u4E0A%u8BC1%u6307%u6570%2Cty-0-300059-%u4E1C%u65B9%u8D22%u5BCC%2Cty-1-600166-%u798F%u7530%u6C7D%u8F66%2Cty-1-600168-%u6B66%u6C49%u63A7%u80A1%2Cty-1-600660-%u798F%u8000%u73BB%u7483%2Cty-0-300229-%u62D3%u5C14%u601D%2Cf-0-000001-%u4E0A%u8BC1%u6307%u6570; st_pvi=95106582090246; st_sp=2021-08-10%2015%3A37%3A11; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=29; st_psi=20230505193615554-111000300841-6619305167; JSESSIONID=BE177C063CC1A664DE227D3C0F355DCD',
        'Referer': 'https://data.eastmoney.com/',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'User-Agent': ua.random,
        'Connection': 'close'

    }
    if codenumber[0] == '8':  # 剔除新三板
        pass
    elif codenumber[0] == '6':  # 主板
        code = 'SH' + codenumber
    else:
        code = 'SZ' + codenumber
    print(code)
    time_string = ['-03-31', '-06-30', '-09-30', '-12-31']  # 特定格式
    now = datetime.now()
    current_year = now.year  # 获取当前年份
    imcomelist = []
    data = {}
    # #从1990年开始，不足的数据将为空，需要跳过。
    for year in range(1990, current_year + 1, 1):
        for m in range(4):
            dataes = str(year) + time_string[m]
            # print(dataes)
            # dataes='2023-3-31'
            params = {
                'companyType': '4',
                'reportDateType': '0',
                'reportType': '1',
                'dates': dataes,
                'code': code,  # 第几页
            }
            response = requests.get(url=url, headers=headers, params=params)
            # print(response.status_code)
            # print(response.url)
            # print(response.text)
            result_json = response.text
            # print(result_json)
            result_dict = json.loads(result_json)
            # print(result_dict['data'])
            # print(type(result_dict))
            # 判断KEY 是否存在
            if 'data' in result_dict:
                data = result_dict['data'][0]
            else:
                pass
            imcomelist.append(data)
            # time.sleep(3)
    # imcomejson = json.dumps(imcomelist) #列表转json
    return imcomelist


def getjson_stockprice(codenumber):
    ua = UserAgent()
    url = 'http://21.push2his.eastmoney.com/api/qt/stock/kline/get?'
    headers = {
            'Cookie': 'qgqp_b_id=b87cee305c38b309d852cce9e3b9fb61; em_hq_fls=js; ct=weXh0EQEmoADGO5LvfNOBZ00awO1CghuGXp-jR4XkXyXyQiyq1UIBQGMwjHdwtQN0AxwgO3fMWl9uzOeSp1sA52HHwpu8MNWr3ICGvzljGkN9qBV9nuk_H1-S3SGS528HyXckjxHXxkfqofmcIJgcDWWh-wcXz34JiIVVwxjgQY; ut=FobyicMgeV6oOlrtxUaVoieuvidY5esdMCb41if8eqJiqFkwjYg2XAbdyOr2X4dfFAuLZp6zEVvi6dzeDfXQ-AmvlHTZlZ3bcLhnG2QmQB3OEIitjRXjxmZdVjfgoTl0R9Og4o-lLlFot79Tn7wCWlEmBE-Xgvm3SmKy2u_2-TT13T3Di_nblC7WJodHxryF1X8Pl-UvxHe5Ba7LrbinuGObOU_DTORRbA7CCJ680VXlO_XrihmSuhjM8Lv31Xbr4c5cw7OSmrJV114RfOXqtdOJA8M5cx0c; st_si=99026570019922; HAList=ty-1-600166-%u798F%u7530%u6C7D%u8F66%2Cty-1-600660-%u798F%u8000%u73BB%u7483%2Cty-0-300229-%u62D3%u5C14%u601D%2Cf-0-000001-%u4E0A%u8BC1%u6307%u6570; emshistory=%5B%22600166%22%5D; st_pvi=95106582090246; st_sp=2021-08-10%2015%3A37%3A11; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=10; st_psi=2023042709494629-113200301201-9045204979; st_asi=delete',
            'Referer': 'http://quote.eastmoney.com/',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'User-Agent': ua.random,
            }
    if codenumber[0] == '6':
        code = '1.'+codenumber
    else:
        code = '0.'+codenumber
    params = {
            'cb': 'jQuery3510406753977783055331682559914408',
            'secid': code,
            'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
            'fields1': 'f1,f2,f3,f4,f5,f6',
            'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
            'klt': '101',
            'fqt': '1',
            'beg': '0',
            'end': '20500101',
            'smplmt': '999999', #采样，决定返回的数据长度，默认值为460，可能导致数据不足，可调整为较大的值。
            'lmt': '1000000',
            '_': '1682559914436',
            }
    response = requests.get(url=url, headers=headers, params=params)
    data = response.text
    data = data[41:-2]  #将返回字符串转换为json格式
    return data


def dataprocess(PRICE_datajson,INCOME_datajson):
    # print(PRICE_datajson)
    # print(INCOME_datajson)
    PRICE_datajson = json.loads(PRICE_datajson)
    klines = PRICE_datajson['data']['klines']
    # print(klines)
    klines_time = []
    klines_price = []
    for kline in klines[1:]:
        kline_split = kline.split(",")
        klines_time.append(kline_split[0])
        klines_price.append(kline_split[2])
    priceprocess = [klines_time, klines_price]
    # 获取经营数据
    report_date = []
    # 扣非净利润
    DEDUCT_PARENT_NETPROFIT = []
    # 营业收入
    OPERATE_INCOME = []
    # 营业利润
    OPERATE_PROFIT = []
    income_json_datas = INCOME_datajson
    #剔除空值
    m = 0
    while not income_json_datas[m]:
        m = m + 1
        # print(m)
    income_json_data_1 = income_json_datas[m]  #获取第一个不为空的报告
    report_date_1 = income_json_data_1['REPORT_DATE'][0:10] #获取第一个不为空的报告日期
    #赋第一个值
    report_date.append(report_date_1)
    if income_json_data_1['DEDUCT_PARENT_NETPROFIT']:
        DEDUCT_PARENT_NETPROFIT.append(round(income_json_data_1['DEDUCT_PARENT_NETPROFIT'] / 100000000, 3))
    else:
        # 如果是空则位0
        DEDUCT_PARENT_NETPROFIT.append(0)
    if income_json_data_1['OPERATE_INCOME']:
        OPERATE_INCOME.append(round(income_json_data_1['OPERATE_INCOME'] / 100000000, 3))
    else:
        OPERATE_INCOME.append(0)
    if income_json_data_1['OPERATE_PROFIT']:
        OPERATE_PROFIT.append(round(income_json_data_1['OPERATE_PROFIT'] / 100000000, 3))
    else:
        OPERATE_PROFIT.append(0)
        #去除重复值
    n = 0
    for income_json_data in income_json_datas[m:-1]:
        report_date_current = income_json_data['REPORT_DATE'][0:10]
        # 判断是否重复
        if report_date[n] != report_date_current:
            report_date.append(report_date_current)
            # 判断是否为空
            if income_json_data['DEDUCT_PARENT_NETPROFIT']:
                DEDUCT_PARENT_NETPROFIT.append(round(income_json_data['DEDUCT_PARENT_NETPROFIT'] / 100000000, 3))
            else:
                #如果是空则位0
                DEDUCT_PARENT_NETPROFIT.append(0)
            if income_json_data['OPERATE_INCOME']:
                OPERATE_INCOME.append(round(income_json_data['OPERATE_INCOME'] / 100000000, 3))
            else:
                OPERATE_INCOME.append(0)
            if income_json_data['OPERATE_PROFIT']:
                OPERATE_PROFIT.append(round(income_json_data['OPERATE_PROFIT'] / 100000000, 3))
            else:
                OPERATE_PROFIT.append(0)
            n = n + 1
        else:
            continue
    #将经营数据转换为季度，通过年的确定来判断，如果年份相同则减，不同则保持
    #获取第一个数据,初始化
    incomeprocess = [report_date, DEDUCT_PARENT_NETPROFIT, OPERATE_INCOME, OPERATE_PROFIT]
    # year = incomeprocess[0][0][0:4]
    # print(year)
    report_date_q = []
    # 扣非净利润
    DEDUCT_PARENT_NETPROFIT_q = []
    # 营业收入
    OPERATE_INCOME_q = []
    # 营业利润
    OPERATE_PROFIT_q = []
    report_date_q.append(incomeprocess[0][0])
    DEDUCT_PARENT_NETPROFIT_q.append(incomeprocess[1][0])
    OPERATE_INCOME_q.append(incomeprocess[2][0])
    OPERATE_PROFIT_q.append(incomeprocess[3][0])
    i=0
    for date,ded,income,profit in zip(incomeprocess[0][1:-1],incomeprocess[1][1:-1],incomeprocess[2][1:-1],incomeprocess[3][1:-1]):  #incomeprocess[0]报告日期数组
        date_year = date[0:4]
        # print(date_year,report_date_q[i][0:4])
        if report_date_q[i][0:4] != date_year:
            report_date_q.append(date)
            DEDUCT_PARENT_NETPROFIT_q.append(ded)
            OPERATE_INCOME_q.append(income)
            OPERATE_PROFIT_q.append(profit)
        else:
            report_date_q.append(date)
            DEDUCT_PARENT_NETPROFIT_q.append(ded-DEDUCT_PARENT_NETPROFIT_q[i])
            print(ded, DEDUCT_PARENT_NETPROFIT_q[i])
            OPERATE_INCOME_q.append(income-OPERATE_INCOME_q[i])
            OPERATE_PROFIT_q.append(profit-OPERATE_PROFIT_q[i])
        i=i+1
        # print(date,ded,income,profit)
    incomeprocess_q = [report_date_q, DEDUCT_PARENT_NETPROFIT_q, OPERATE_INCOME_q, OPERATE_PROFIT_q]
    return priceprocess, incomeprocess_q


if __name__ == '__main__':
    totolPage = pageNumber()
    for page in range(totolPage):
        list_pages = getjson_stocklist(page+1)
        for lists_page in list_pages:
            SECURITY_CODE = lists_page['SECURITY_CODE']
            SECURITY_NAME_ABBR = lists_page['SECURITY_NAME_ABBR']