import time

from flask import Blueprint, request, render_template
from exts import db
from getdatafuns import pageNumber, getjson_stocklist
from models import Stockdata
from utils import restful

bp = Blueprint("front", __name__, url_prefix='/')


@bp.route('/getdata/',methods=['GET', 'POST'])
def getdata():
    return render_template('front/get_data.html')

@bp.post('/getdatalist/')
def getlist():
    user = request.form.get('user')
    password = request.form.get('password')
    # 更新数据库
    if user == 'wsy' and password == 'mtjb1..':
        print('ok')
        try:
            totolPage = pageNumber()
            for page in range(totolPage):
                list_pages = getjson_stocklist(page + 1)
                for lists_page in list_pages:
                    SECURITY_CODE = lists_page['SECURITY_CODE']
                    print(SECURITY_CODE)
                    SECURITY_NAME_ABBR = lists_page['SECURITY_NAME_ABBR']
                    # 判断是否已经在数据库，
                    li = db.session.query(Stockdata).filter_by(SECURITY_CODE=SECURITY_CODE).first()
                    if not bool(li):
                        # li.SECURITY_CODE = SECURITY_CODE
                        # li.SECURITY_NAME_ABBR = SECURITY_NAME_ABBR
                        # db.session.commit()
                        stockdata = Stockdata(SECURITY_CODE=SECURITY_CODE, SECURITY_NAME_ABBR=SECURITY_NAME_ABBR)
                        db.session.add(stockdata)
                        db.session.commit()
                    # time.sleep(3)
        except Exception as e:
            print(e)
    else:
        return restful.params_error(message='账号或密码错误')
    return restful.ok(message='finished update_list')