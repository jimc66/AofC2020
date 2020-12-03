# find three numbers in your expense report that meet the same criteria. (2020)
#  what is the product of the three entries that sum to 2020?
data_list = [1975,1600,113,1773,1782,1680,1386,1682,1991,1640,1760,1236,1159,1259,1279,1739,1826,1888,1072,416,1632,1656,1273,1631,1079,1807,1292,1128,1841,1915,1619,1230,1950,1627,1966,774,1425,1983,1616,1633,1559,1925,960,1407,1708,1211,1666,1910,1960,1125,1242,1884,1829,1881,1585,1731,1753,1784,1095,1267,1756,1226,1107,1664,1710,2000,1181,1997,1607,1889,1613,1859,1479,1763,1692,1967,522,1719,1816,1714,1331,1976,1160,1899,1906,1783,1061,2006,1993,1717,2009,1563,1733,1866,1651,1437,1517,1113,1743,1240,1629,1868,1912,1296,1873,1673,1996,1814,1215,1927,1956,1970,1887,1702,1495,1754,1621,1055,1538,1693,1840,1685,1752,1933,1727,1648,1792,1734,1305,1446,1764,1890,1904,1560,1698,1645,1214,1516,1064,1729,1835,1642,1932,1683,962,1081,1943,1502,1622,196,1972,1916,1850,1205,1971,1937,1575,1401,1351,2005,1917,1670,1388,1051,1941,1751,1169,510,217,1948,1120,1635,1636,1511,1691,1589,1410,1902,1572,1871,1423,1114,1806,1282,1193,1974,388,1398,1992,1263,1786,1723,1206,1363,1177,1646,1231,1140,1088,1322]
sum_target = 2020
# note - a cheat, since there is no 1010 in the list, no need to worry about iterating over the list and summing a # on itself
# approach - brute force: iterate through each # with an inner loop that adds the 2nd # until you get to 2020
looper=0
total_num = 0
num_items = len (data_list)
for adder_1 in data_list:
    if total_num == 2020 :
         break  # here we break out of this loop AFTER we've incremented added_1 by 1 too many (unless it's the last item)
    looper = looper+1
    for adder_2 in data_list:
        if total_num == 2020 :
            break  # same deal - breaking after increment
        for adder_3 in data_list:
            total_num=adder_1+adder_2+adder_3
            if (total_num == sum_target) :
                print ("num1:")
                print (adder_1)
                num1=adder_1
                print ("num2: ")
                print ( adder_2)
                num2=adder_2
                print ("num3:")
                print (adder_3)
                num3=adder_3
                break

# print ("done iterating now")
# print (looper)
product_total=num1 * num2 * num3
msg = "number 1: " + str(num1) + "   number 2: " + str(num2) + "   number 3:" + str(num3) + "   Multiplication Total: " + str(product_total)
print (msg)