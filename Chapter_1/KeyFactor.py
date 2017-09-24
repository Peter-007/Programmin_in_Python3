# coding=utf-8
# 重要的事情说三遍！！！
# 所有"数据项"都是"数据类型"（类）的"对象"（实例）
# All python data items are objects(also called instance) of a particular data type (also called a class)
# 例如：'hello'：就是str类的一个实例，或则说是字符串数据类型的一个对象

# 关键要素1:数据类型
def Piece1_DataTypes():
    # int的大小中取决于内存，可以表示很大的数
    # 2的217次方，pow(2,217)
    bigNumber = 210624583337114373395836055367340864637790190801098222508621955072L

    # 类型转换
    x = int("45 ")
    a = str(213)

# 关键要素2: 对象引用
def Piece2_ObjectReferences():
    # 动态数据类型
    route = 567
    print(route,type(route))
    route = 'North'
    print(route,type(route))

# 关键要素3:组合数据类型
# 列表和元组存放的是对象的引用，并不是真正的数据项内容。
def Piece3_CollectionDataTypes():
    # tuple元组, 一个元素的元组中必须加上","
    a = ('one')
    print(a,type(a),len(a))
    b = ('one',)
    print(b,type(b),len(b))

    # 所有"数据项"都是"数据类型"（类）的"实例"（对象）
    # list列表
    b = ['jack','tom']
    b.append('rose')        #创建列表方法一
    list.append(b,'frank')  #创建列表方法二
    b.insert(0,'peter')
    b[1] = 'smith'

    print(b)

# 关键要素4:逻辑运算符
def Pieces4_LogicalOperations():

    # Identity Operator
    a = ['jack', 'tom']
    b = ['jack', 'tom']
    print(a is b)   # False

    b = a
    print(a is b)   # True

    x = 'some'
    y = None
    print(x is not None, y is None)

    # Comparison Operators
    a = 2
    b = 6
    print(a == b,
          a < b, a <= b,
          a > b, a >= b,
          a != b)

    name1 = 'jack'
    name2 = 'jack'
    name3 = 'jack '  #多了一个空格
    print(name1 is name2, name1 == name2, name1 == name3.strip())




Piece1_DataTypes()
Piece2_ObjectReferences()
Piece3_CollectionDataTypes()
Pieces4_LogicalOperations()
