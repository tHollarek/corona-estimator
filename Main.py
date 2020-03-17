import matplotlib.pyplot as plt
import numpy as np
import scipy.special
import ntpath
import os
from scipy.odr import *
from scipy.optimize import curve_fit
from DataFile import *

topFolderPath = 'G:\\OneDrive\\Desktop\\Coding_Projects\\Python\\CornavirusModel'
scale = 1/1000.

# Performs a regression of the xList and yList with a given fit function: 'fkt'
# Returns the parameter array of the fit function in the order listed in 'fkt' and then graphs function
# Function has to be of the form: def fit(x,a,b,c,...), initalparams as tuples (a,b,c..)
def generalRegression(xList, yList,xerr,yerr, xUnit, yUnit, fkt, functionname, initialparams, figName):
    # Transform your data in a numpy array of floats so the curve_fit can work
    xList = np.array(xList, dtype=float)
    yList = np.array(yList, dtype=float)
    f = plt.figure()

    yList = [y*scale for y in yList]
    # Optimierung Vornehmen und plotten
    fitParams, fitCovar = curve_fit(fkt, xList, yList,initialparams)
    plt.errorbar(xList, yList,yerr = yerr, xerr=xerr,fmt='x',label = 'DataSet')
    plt.plot(xList,fkt(xList, *fitParams), 'r-', label=functionname)


    # Summing over relative errors in regression
    relError = 0
    deltaList = fkt(xList, *fitParams) - yList
    for i in range(len(deltaList)):
        relError += deltaList[i] / yList[i]
    relError = relError / len(deltaList)

    i = 0
    """
    ax = f.add_subplot(111)
    for param in fitParams:
        param = round(param,3)
        plt.text(0.8, 0.775 - i / 8., chr(97 + i) + '= ' + str(round(param, 8)), fontsize=12, transform=ax.transAxes)
        i += 1
    """
    plt.legend()
    plt.xlabel(xUnit, fontsize=18)
    plt.ylabel(yUnit, fontsize=18)
    plt.savefig(topFolderPath + figName)
    plt.show()

    print('Values for ' + figName)
    for j in range(len(fitParams)):
        print(str(j) + 'th parameter = ' + str(fitParams[j]) + ' \pm ' +  str(np.sqrt(fitCovar[j][j])))

    return fitParams,fitCovar

# Setting x0 to the point at which we expect the turning point:
# Since 28th day corresponds to 13.03 and countermeasures were enforced on 10.03
# We will run with a good approximation of one week and two week after meaning 32 and 39

#Wendepunkt am 18.03, 25.03, 05.04
def logisticFunct(x,L,k,x0):
    return L/(1+np.exp(-k*(x-x0)))

def logisticFunctGood(x,L,k):
    return L/(1+np.exp(-k*(x-32)))

def logisticFunctBad(x,L,k):
    return L/(1+np.exp(-k*(x-39)))

def logisticFunctApocalyptic(x,L,k):
    return L/(1+np.exp(-k*(x-50)))

def calculateValues(L,k,x0):
    dayList = np.arange(1,101,1)
    yList = [logisticFunct(x,L,k,x0) for x in dayList]
    return yList


#Wendepunkt am 26.03,02.04,13.04
def logisticFunctGoodGer(x,L,k):
    return L/(1+np.exp(-k*(x-40)))

def logisticFunctBadGer(x,L,k):
    return L/(1+np.exp(-k*(x-47)))

def logisticFunctApocalypticGer(x,L,k):
    return L/(1+np.exp(-k*(x-58)))




"""
L = 20000
k = 0.3
x0 = 28
yList = [logisticFunct(x,L,k,x0) for x in dayList]
plt.plot(dayList,yList)
plt.show()

plt.plot(dayList,germanyCases)
plt.show()"""

dayList = np.arange(1,41,1)
#southCoreaCases = generalRegression(dayList,southCoreaCases,0,0,'Days','Cases',logisticFunct,'LogisticFunct',(50000*scale,0.01,20),'Good Logistic Growth')
"""
italyRegress = generalRegression(dayList,italyCases,0,0,'Days','Cases',logisticFunctBad,'LogisticFunct',(50000*scale,0.01),'Bad Logistic Growth')
italyRegress = generalRegression(dayList,italyCases,0,0,'Days','Cases',logisticFunctApocalyptic,'LogisticFunct',(50000*scale,0.01),'Apocalyptic Logistic Growth')


gerRegress = generalRegression(dayList,germanyCases,0,0,'Days','Cases',logisticFunctGoodGer,'LogisticFunct',(50000*scale,0.01),'Good Logistic Growth')
gerRegress = generalRegression(dayList,germanyCases,0,0,'Days','Cases',logisticFunctBadGer,'LogisticFunct',(50000*scale,0.01),'Bad Logistic Growth')
gerRegress = generalRegression(dayList,germanyCases,0,0,'Days','Cases',logisticFunctApocalypticGer,'LogisticFunct',(50000*scale,0.01),'Apocalyptic Logistic Growth')
"""

yList1 = calculateValues(61596,0.2262134725567856,32)
yList2 = calculateValues(186292,0.2029092,39)
yList3 = calculateValues(1340980,0.194872,50)
yList4 = calculateValues(96573,0.271,40)
yList5 = calculateValues(577011,0.2668947978281542,47)
yList6 = calculateValues(10549586,0.2660853774059309,58)

print("ABC")


totalDayList = np.arange(1, 101, 1)


shortyList4 = [yList4[i] for i in range(40)]
shortyList5 = [yList5[i] for i in range(40)]
shortyList6 = [yList6[i] for i in range(40)]

shortDayList = np.arange(1,29,1)

plt.scatter(shortDayList,germanyCases)
plt.plot(dayList,shortyList4,label = "Inflection on 26.03")
plt.plot(dayList,shortyList5,label = "Inflection on 02.04")
plt.plot(dayList,shortyList6,label = "Inflection on 13.04")
plt.legend()
plt.show()

plt.plot(totalDayList,yList4,label = "Optimistisch")
plt.plot(totalDayList,yList5,label = "Realistisch")
plt.plot(totalDayList,yList6,label = "Pessimistisch")
plt.legend()
plt.show()
"""
shortendDayList = np.arange(1,10,1)
plt.plot(shortendDayList,germanyCases)
plt.show()

L = 20000
k = 0.2
x0 = 15
yList = [logisticFunct(x,L,k,x0) for x in dayList]
plt.plot(dayList,yList)
plt.show()"""


print("ABC")
def expRegress(x,a,b,c):
    return a*np.exp(-b*(x-c))

#germanyRegress = generalRegression(dayList,germanyCases,0,0,'Days','Cases',expRegress,'Exponential Function',(20000*scale,0.1,10),'Logistic Growth')
#germanyRegress = generalRegression(dayList,germanyCases,0,0,'Days','Cases',logisticFunct,'Exponential Function',(20000*scale,0.1,10),'Logistic Growth')
#usaRegress = generalRegression(dayList,usaCases,0,0,'Days','Cases',expRegress,'Exponential Function',(10000*scale,0.1,10),'Logistic Growth')
