import math
from fractions import Fraction
print("\033[5;34;41m - - - - - - - - - -计算信息增益程序- - - - - - - - -\033[0m")
num = 0
t = input("请按\033[1;31m 1\033[0m 开始程序: ")
while int(t) != 0:
    b = 0
    c = input("\033[1;33m 请输入Ent(D)D的分类数目:\033[0m ")
    #计算信息增益第一部分
    for n in range(1, int(c) + 1):
        a = input("\033[1;34m 请输入你的第%d个计算值（p(%d)）:\033[0m" % (n, n))
        d = float(Fraction(a))
        b = b - d * math.log(d, 2)
        if n < int(c):
            print("\033[1;35m Ent(D)的第%d个计算结果为：\033[0m" % n, b)
        else:
            b = round(b, 3)
            print("\033[1;36m Ent(D)的值为：%.3f\033[0m" % b)
    # 下面开始计算信息增益的第二部分

    # c1 = input("\033[1;33m 请输入Ent(D)D的每个属性取值对应的分类数目:\033[m ")
    c2 = input("\033[1;33m 请输入属性a的取值数目:\033[0m ")
    b2 = 0
    for n2 in range(1, int(c2) + 1):
        c1 = input("\033[1;33m 请输入Ent(D%d)D的每个属性取值对应的分类数目:\033[0m " % n2)
        b1 = 0
        # 这部分计算每个属性分支的信息熵
        for n1 in range(1, int(c1) + 1):
            a1 = input("\033[1;34m 请输入你的第%d个计算值（p(%d)）:\033[0m" % (n1, n1))
            d1 = float(Fraction(a1))
            b1 = b1 - d1 * math.log(d1, 2)
            if n1 < int(c1):
                print("\033[1;35m Ent(D(%d))的第%d个计算结果为：\033[0m" % (n2, n1), b1)
            else:
                b1 = round(b1, 3)
                print("\033[1;36m Ent(D(%d))的值为：%.3f\033[0m" % (n2, b1))
        a2 = input("\033[1;34m 请输入你的第%d个计算值（D(%d)/D）:\033[0m" % (n2, n2))
        d2 = float(Fraction(a2))
        b2 = b2 + d2 * b1
        if n2 < int(c2):
            print("\033[1;35m 信息增益第二项属性a的%d项计算之和为：\033[0m" % n2, b2)
        else:
            print("\033[1;36m 信息增益第二项属性a的值为：\033[0m", b2)

            print(
                "\033[1;33m ------------------------------------------------------------------------"
                "-----------------\033[0m")
            print("\033[1;31m 无缺失值的信息增益Gain = %.3f\033[0m" % round((b - b2), 3))
            p = float(Fraction(input("\033[1;31m 请输入p的值: \033[0m")))
            print("\033[1;31m 该属性的最终信息增益Gain = %.3f\033[0m" % round(p*(b - b2), 3))
            print(
                "\033[1;33m ------------------------------------------------------------------------"
                "-----------------\033[0m")
    #print("continue")
    num += 1
    print("\033[1;33m -----------------------------------------------------------------------------------------\033[0m")
    t=input("\033[1;30m 已计算出第\033[0m \033[1;31m %d \033[0m \033[1;30m 个信息增益是否继续，继续请按\033[0m\033[1;31m"
            " 1 \033[0m 终止请按\033[1;31m 0 \033[0m : " % num)
    print("\033[1;33m -----------------------------------------------------------------------------------------\033[0m")
print("\033[1;35m 程序结束！\033[0m")