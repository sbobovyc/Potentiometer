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

plt.figure(1)
array = analyze("Group1B\\1mMinclear_DCPA.dat", 0x3EE)
plt.plot(array[:,0], array[:,1], label="1mM")
array = analyze("Group1B\\5mMinclear_DCPA.dat", 0x3EE)
plt.plot(array[:,0], array[:,1], label="5mM")
array = analyze("Group1B\\10mMinclear_DCPA.dat", 0x3F0)
plt.plot(array[:,0], array[:,1], label="10mM")
plt.xlabel("Time (s)")
plt.ylabel("Current (uA)")
plt.legend()
plt.title("BASi potentiostat with commercial strips")

plt.annotate('', xy=(3.6E7, 0.6), xytext=(3.7E7, 0.7),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, color="r"),
            )
plt.annotate('', xy=(4E7, 0.37), xytext=(4.1E7, 0.47),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, color="g"),
            )
plt.annotate('', xy=(3.9E7, 0.23), xytext=(4.1E7, 0.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, color="b"),
            )
plt.savefig("basi.png")
plt.show()
