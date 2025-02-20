# -*- coding: utf-8 -*-
"""cod week4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aJovMvPbK10VU2-eOuCER6N_MSF56yMU
"""

#Q1 Identify yourself for grading

def WhoAmI():
  return('jz3378')

print(WhoAmI())

#Q2 getBondPrice

def getBondPrice(y, face, couponRate, m, ppy=1):
    bondPrice = 0
    C = (couponRate * face) / ppy
    n = m * ppy
    r = y / ppy

    for i in range(1, n + 1):
        bondPrice += C / (1 + r) ** i

    bondPrice += face / (1 + r) ** n

    return bondPrice

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy=1
ppy=2

print(getBondPrice(y, face, couponRate, m, ppy=1))
print(getBondPrice(y, face, couponRate, m, ppy=2))



#Q3 getBondDuration


def getBondDuration(y, face, couponRate, m, ppy=1):
    C = (couponRate * face) / ppy
    n = m * ppy
    rate = y / ppy

    pv_cashflows = 0
    wpv_cashflows = 0

    for i in range(1, n + 1):
      pv_cf = C / (1 + rate) ** i
      pv_cashflows += pv_cf
      wpv_cashflows += i * pv_cf


    pv_face = face / (1 + rate) ** n
    pv_cashflows += pv_face
    wpv_cashflows += n * pv_face


    duration = wpv_cashflows / pv_cashflows

    return duration

# Test values
y = 0.03  # 3% YTM
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

print(getBondDuration(y, face, couponRate, m, ppy=1))


# Q4 E

def GetBondPrice_E(face, couponRate, m, yc):

    C = couponRate * face
    bondPrice = 0

    for t, y_t in enumerate(yc, start=1):
        pv_cf = C / (1 + y_t) ** t
        bondPrice += pv_cf

    pv_face = face / (1 + yc[-1]) ** len(yc)
    bondPrice += pv_face

    return bondPrice

# Test values
yc = [0.01, 0.015, 0.02, 0.025, 0.03]
face = 2000000
couponRate = 0.04

GetBondPrice_E(face, couponRate, len(yc), yc)
print(GetBondPrice_E(face, couponRate, len(yc), yc))


# Q5 Z

def GetBondPrice_Z(face, couponRate, times, yc):

    C = couponRate * face
    bondPrice = 0

    for t, y_t in zip(times[: -1], yc[: -1]):
        pv_cf = C / (1 + y_t) ** t
        bondPrice += pv_cf

    pv_face = (C + face) / (1 + yc[-1]) ** times[-1]
    bondPrice += pv_face

    return bondPrice

# Test values
yc = [0.01, 0.015, 0.02, 0.025, 0.03]
times=[1, 1.5, 3, 4, 7]
face = 2000000
couponRate = 0.04

GetBondPrice_Z(face, couponRate, times, yc)
print(GetBondPrice_Z(face, couponRate, times, yc))

# Q6  Fizzbuzz

def FizzBuzz(start, finish):

    outlist = []

    for i in range(start, finish + 1):
        if i % 3 == 0 and i %5 == 0:
            outlist.append("fizzbuzz")
        elif i % 3== 0:
            outlist.append("fizz")
        elif i % 5 ==0:
            outlist.append("buzz")
        else:
            outlist.append(i)

    return outlist

print(FizzBuzz(1,100))


# Q7 MatMault1

def MyMatMault1(vec,col):

    return sum(a * b for a, b in zip(vec, col))

# data
vec = [1, 2, 3]
col = [1, 4, 7]


dot_zip = MyMatMault1(vec, col)

print(dot_zip)



#Q8 MatMault2

def MyMatMault2(vec,martix):

    return [sum(a * b for a, b in zip(vec, col)) for col in zip(*martix)]

# data
vec = [1, 2, 3]
martix = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]


dot_zip = MyMatMault2(vec, martix)

print(dot_zip)