class Product():
    # コンストラクタ
    def __init__(self, name, price, area) :
        self.name = name
        self.price = price
        self.area = area
    
    # 商品紹介メソッド
    def introduction(self):
        print(f"{self.area}産 {self.name}は，本日{self.price}円です．")
        
# Productクラスを継承したPrice_Change_Productクラス
class Price_Change_Product(Product):
    def __init__(self, name, price, area, price_change):
        super().__init__(name, price, area)
        self.price_change = price_change
    
    # 商品紹介 & 値上げか値下げかのお知らせメソッド
    def notice(self):
        # 親クラスのメソッドを継承
        super().introduction()
        
        # 値上げか値下げかで条件分岐
        if self._price_change > 0:
            print(f"{self.name}は{self.price_change}円値上がりしました．")
        else:
            discount = - self._price_change
            print(f"{self.name}は{discount}円引きなので，お買い得です．ぜひお買い求めください．")
            
# 親クラスを継承した子クラス１
class Price_Change_Product_2(Product):
    def __init__(self, name, price, area, discount):
        super().__init__(name, price, area)
        self.discount = discount
    
    # 親クラスのメソッドを上書き
    def introduction(self):
        print(f"{self.area}産 {self.name}は，本日{self.discount}円引きの{self.price}円です．")

# 親クラスを継承した子クラス２
class Campaign_Product(Product):
    def __init__(self, name, price, area, campaign_name):
        super().__init__(name, price, area)
        self.campaign_name = campaign_name
    
    # 親クラスのメソッドを上書き
    def introduction(self):
        print(f"{self.area}産 {self.name}は，本日{self.campaign_name}の{self.price}円です．")
        
