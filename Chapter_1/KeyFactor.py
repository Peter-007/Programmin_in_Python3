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
def Piece4_LogicalOperations():

    # 身份操作符：Identity Operator
    a = ['jack', 'tom']
    b = ['jack', 'tom']
    print(a is b)   # False

    b = a
    print(a is b)   # True

    x = 'some'
    y = None
    print('Identity operator', x is not None, y is None)

    # 比较操作符：Comparison Operators
    a = 2
    b = 6
    print(a == b,
          a < b, a <= b,
          a > b, a >= b,
          a != b)
    # compare string
    name1 = 'jack'
    name2 = 'jack'
    name3 = 'jack '  #多了一个空格
    print('compare string', name1 is name2, name1 == name2, name1 == name3.strip())

    score = 86
    print( 'chained compare', 60 < score < 90)

    # 成员操作符：membership Operator
    p = ('one',1,'abc')
    print('membership operaor1', 1 in p, 'on' in p)

    str1 = 'The membership operator'
    print('membership operaor2', 'ship' in str1)

    #逻辑运算符：and, or, not
    a1 = 5
    a2 = 2
    a3 = 0
    print('Logical operator1', a1 and a2, a2 and a1, a1 or a2, a2 or a1)
    print('Logical operator2', a1 and a3, a3 and a1, a1 or a3, a3 or a1)
    print('Logical operator3', not a1, not a2, not a3)

# 关键要素5:控制流语句
def Piece5_ControlFlowStatements():
    lines = 1800
    if lines < 1000:
        print('small')
    elif lines < 5000:
        print('medium')
    else:
        print('large')

    i = 0
    while i < 10:
        i += 1
        if 4 < i < 7:
            continue
        print('while i=%d' % i)

    else:
        print('while is end')

    for j in range(10):
        print('for i=%d' % j)
    else:
        print('for end')


Piece1_DataTypes()
Piece2_ObjectReferences()
Piece3_CollectionDataTypes()
Piece4_LogicalOperations()
Piece5_ControlFlowStatements()
