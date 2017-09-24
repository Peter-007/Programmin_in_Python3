# coding=utf-8

def Piece1_DataTypes():
    # int的大小中取决于内存，可以表示很大的数
    # 2的217次方，pow(2,217)
    bigNumber = 210624583337114373395836055367340864637790190801098222508621955072L

    # 类型转换
    x = int("45 ")
    a = str(213)


def Piece2_ObjectReferences():
    # 动态数据类型
    route = 567
    print(route,type(route))
    route = 'North'
    print(route,type(route))


def Piece3_CollectionDataTypes():
    # tuple元组, 一个元素的元组中必须加上","
    a = ('one')
    print(a,type(a),len(a))
    b = ('one',)
    print(b,type(b),len(b))

    # list列表 特定



Piece1_DataTypes()
Piece2_ObjectReferences()
Piece3_CollectionDataTypes()
