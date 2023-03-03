class Merchandise:
    def __init__(self,para_number,para_name,para_volume):
        self.number = para_number
        self.name = para_name
        self.volume = para_volume
    def Introduction(self):
        return "Nhap vao so luong " + self.name
goods = Merchandise(12,"Duong",1)

print(goods.Introduction())
print(Merchandise.Introduction(goods))