from ext import db
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    pw = db.Column(db.String(128))
    area_index = db.Column(db.Integer,db.ForeignKey("area.area_index"),default = 0)
    #total = db.Column(db.Float)
    '''total_m means total of current month'''
    total_m = db.Column(db.Float,default = 0.0)
    area = db.relationship("Area",back_populates = "user")
    def __init__(self,name,pw,email,consump = 0,area_index = 1):
        self.name = name
        self.pw = pw
        self.email = email
        self.total_m = 0.0
        self.total_m = self.total_m + consump
        self.area_index = area_index
    def add_consump(v = 0): 
        self.total_m = self.total_m + v
class Area(db.Model):
    __tablename__ = "area"
    area_index = db.Column(db.Integer,primary_key = True,autoincrement = True)
    area_name = db.Column(db.String(50))
    def __init__(self, area_name):
        self.area_name = area_name
Area.user = db.relationship("User",order_by = User.total_m,back_populates = "area")
    
class Commodit(db.Model):
    __tablename__ = "commodit"
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(50))
    describe = db.Column(db.String(1000))
    points = db.Column(db.Float)
    times = db.Column(db.Integer)
    price = db.Column(db.Float)
    vol = db.Column(db.Integer)
    img_src = db.Column(db.String(500))
    #vol_m represents the volume of this month
    vol_m = db.Column(db.Integer)
    stock_amount = db.Column(db.Integer)
class Userlikes(db.Model):
    __tablename__ = "userlikes"
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    commodit_id = db.Column(db.Integer,db.ForeignKey("commodit.id"))
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    vol = db.Column(db.Integer,default = 0)
    user = db.relationship("User",back_populates = "userlikes")
    commodit = db.relationship("Commodit",back_populates = "userlikes")
    def __init__(self,user_id,commodit_id,increment):
        self.commodit_id = commodit_id
        self.user_id = user_id
        self.vol = self.vol + increment
User.userlikes = db.relationship("Userlikes",order_by = Userlikes.vol,back_populates = "user")
Commodit.userlikes = db.relationship("Userlikes",order_by = Userlikes.vol,back_populates = "commodit")
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
    '''enum means each num'''
    enum = db.Column(db.Integer)
    eprice = db.Column(db.Float)
    area = db.Column(db.Integer)
    #relevant
    orderglance = db.relationship("Order",back_populates = "orderinfo")
    commodit = db.relationship("Commodit",back_populates = "orderinfo")
    user = db.relationship("User",back_populates = "orderinfo")
Order.orderinfo = db.relationship("Order_Info",order_by = Order_Info.enum,back_populates = "orderglance")
Commodit.orderinfo = db.relationship("Order_Info",order_by = Order_Info.enum,back_populates = "commodit")
User.orderinfo = db.relationship("Order_Info",order_by = Order_Info.enum,back_populates = "user")

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

