import csv
import numpy
import matplotlib.pyplot as plt

def analyze(filename, offset):
    f = open(filename, "r")
    f.seek(offset)

    csv_reader = csv.reader(f, delimiter=",")
    data = list(csv_reader)
    entries = len(data)
    array = numpy.zeros((entries, 2))

    i = 0
    for row in data:
        converted_row = map(lambda x: float(x)* 10**6, row)
        array[i][:] = converted_row
        i += 1

    min_current = numpy.min(array[:,1])
    max_current = numpy.max(array[:,1])
    print "Min: %f uA, Max: %f uA" % (min_current, max_current )
    #print array[:,0]
    return array

array = analyze("Group1B\\1mMinclear_DCPA.dat", 0x3EE)
one_m_current = numpy.average(array[35:,1])
print one_m_current

array = analyze("Group1B\\5mMinclear_DCPA.dat", 0x3EE)
five_m_current = numpy.average(array[37:,1])
print five_m_current

array = analyze("Group1B\\10mMinclear_DCPA.dat", 0x3F0)
ten_m_current = numpy.average(array[37:,1])
print ten_m_current

x = numpy.array([1, 5, 10])
A = numpy.array([x, numpy.ones(3)])
y = numpy.array([one_m_current, five_m_current, ten_m_current])
w = numpy.linalg.lstsq(A.T,y)[0]

line = w[0]*x+w[1] # regression line

plt.figure(1)
array = analyze("Group1B\\1mMinclear_DCPA.dat", 0x3EE)
plt.scatter(x, y, marker="o")
plt.plot(x, line, "r-")

plt.xlim((0,11))
plt.xlabel("Concentration (mM)")
plt.ylabel("Current (uA)")
plt.title("Concentration vs. current")

"""
plt.annotate('', xy=(3.6E7, 0.6), xytext=(3.7E7, 0.7),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, color="r"),
            )
plt.annotate('', xy=(4E7, 0.37), xytext=(4.1E7, 0.47),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, color="g"),
            )
plt.annotate('', xy=(3.9E7, 0.23), xytext=(4.1E7, 0.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, color="b"),
            )
"""

plt.savefig("CI.png")
plt.show()


