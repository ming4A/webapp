from ext import db
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(50))
    pw = db.Column(db.String(25))
    area = db.Column(db.Integer)
    '''total = db.Column(db.Float)
    '''total_m means total of current month'''
    total_m = db.Column(db.Float)'''
    def __init__(self,name,pw,consump):
        self.name = name
        self.pw = pw
        self.total_m = self.total_m + consump
class Commodit(db.Model):
    __tablename__ = "commodit"
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(50))
    describe = db.Column(db.String(1000))
    points = db.Column(db.Float)
    times = db.Column(db.Integer)
    price = db.Column(db.Float)
    vol = db.Column(db.Integer)
    #vol_m represents the volume of this month
    vol_m = db.Column(db.Integer)
    stock_amount = db.Column(db.Integer)
    def __init__(self,name,describe,)
class Userlikes(db.Model):
    __tablename__ = "userlikes"
    user_id = db.Column(Integer,db.ForeignKey("user.id"))
    commodit_id = db.Column(Integer,db.ForeignKey("commodit.id"))
    id = db.Column(Integer,primary_key = True,autoincrement = True)
    vol = db.Column(Integer)
    user = db.relationship("User",back_populates = "userlikes")
    commodit = db.relationship("commodit",back_populates = "userlikes")
    def __init__(self,user_id,commodit_id,increment):
        self.commodit_id = commodit_id
        self.user_id = user_id
        self.vol = self.vol + increment
class Order(db.Model):
    __tablename__ = "orderglance"
    order_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    total = db.Column(db.Float)
class Order_Info(db.Model):
    __tablename__ = "orderinfo"
    order_id = db.Column(db.Integer,db.ForeignKey("orderglance.order_id"))
    commodit_id = db.Column(db.Integer,db.ForeignKey("commodit.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    enum = db.Column(db.Integer)
    eprice = db.Column(db.Float)
    area = db.Column(db.Integer)
    #relevant
    orderglance = db.relationship("Order",back_populates = "orderinfo")
    commodit = db.relationship("Commodit",back_populates = "orderinfo")
    user = db.relationship("User",back_populates = "orderinfo")
    def __init__(self,6)
Order.Info = db.relationship("Order_Info",order_by = Order_Info.enum,back_populates = "user")
'''
class comments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    commodit_id = db.Column(db.Integer,db.ForeignKey("commodit.id"))
    comment = db.Column(db.String(500))
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    user = db.relationship("User",back_populates = "comments")
    commodit = db.relationship("Commodit",back_populates = "comments")
    def __init__(self,user_id,commodit_id,comment):
        self.user_id = user_id
        self.commodit_id = commodit_id
        self.comment = comment
'''

