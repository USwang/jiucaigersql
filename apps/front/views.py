from flask import Blueprint, request, render_template
from exts import db
from getdatafuns import pageNumber, getjson_stocklist
from models import Stockdata
from utils import restful

bp = Blueprint("front", __name__, url_prefix='/')


@bp.route('/getdata/',methods=['GET', 'POST'])
def getdata():
    return render_template('front/get_data.html')

@bp.route('/getdatalist/')
def get_list():
    username = request.form.get('username')
    password = request.form.get('password')
    # 更新数据库
    if username == 'wsy' and password == 'mtjb1..':
        totolPage = pageNumber()
        for page in range(totolPage):
            list_pages = getjson_stocklist(page + 1)
            for lists_page in list_pages:
                SECURITY_CODE = lists_page['SECURITY_CODE']
                SECURITY_NAME_ABBR = lists_page['SECURITY_NAME_ABBR']
                # 判断是否已经在数据库，
                li = db.session.query(Stockdata).filter_by(SECURITY_CODE=SECURITY_CODE).first()
                if bool(li):
                    li.SECURITY_CODE = SECURITY_CODE
                    li.SECURITY_NAME_ABBR = SECURITY_NAME_ABBR
                    db.session.commit()
                else:
                    stockdata = Stockdata(SECURITY_CODE=SECURITY_CODE, SECURITY_NAME_ABBR=SECURITY_NAME_ABBR)

                    db.session.add(stockdata)
                    db.session.commit()
    else:
        return '用户名或密码不正确'
    return restful.ok(message='finished update_list')