from exts import db


class Stockdata(db.Model):
    __tablename__ = 'jcgstockdata'
    # stock 代码
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # stock code number
    SECURITY_CODE = db.Column(db.String(50), unique=True, nullable=True)
    # stock 名称
    SECURITY_NAME_ABBR = db.Column(db.String(50), nullable=True)
    # 市场标签 沪，深，创，科创
    # markettag = db.Column(db.String(50), nullable=True)
    # 数据
    PRICE_datajson = db.Column(db.JSON)
    INCOME_datajson = db.Column(db.JSON)

    def __repr__(self):
        return f'<Stockdatabase {self.SECURITY_CODE}>'


class Stockdataprocess(db.Model):
    __tablename__ = 'stockdataprocess'
    # stock 代码
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # stock code number
    SECURITY_CODE = db.Column(db.String(50), unique=True, nullable=True)
    # stock 名称
    SECURITY_NAME_ABBR = db.Column(db.String(50), nullable=True)
    # 市场标签 沪，深，创，科创
    # markettag = db.Column(db.String(50), nullable=True)
    # 数据的处理主要是将股票价格与营业收入对齐。
    PRICE_dataprocess = db.Column(db.JSON)
    INCOME_dataprocess = db.Column(db.JSON)