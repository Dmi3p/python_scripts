import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq, fft
from numpy import array, arange, abs as np_abs
import sys
def from_file(file):
    f = open(file, "r")
    text = f.read()
    f.close()
    return text.split("\n")


def time_step_finder(text):
    value = text[1].split(" ")[3].replace(",", ".")
    return float(value)


def voltage_step_finder(text):
    value = str(text[2]).split(" ")[3].replace(",", ".")
    return float(value)


def zero_level_finder(text):
    value = str(text[3]).split(" ")[3].replace(",", ".")
    return int(value)


def smpl_finder(text):
    list = []
    list2 = []
    for el in text[7:]:
        list.append(el.split("\t"))
    i = 0
    while i <= len(list) - 2:
        list2.append(int(list[i][1]))
        i += 1
    return list2


def main():

    text = from_file(sys.argv[1])
    time_step = time_step_finder(text)
    voltage_step = voltage_step_finder(text)
    zero_level = zero_level_finder(text)
    smpl = smpl_finder(text)
    FD = 22050
    N = len(smpl)
    spectrum = rfft(smpl)

    plt.plot(arange(N) / float(FD), smpl)  # по оси времени секунды!
    plt.xlabel('Время, c')
    plt.ylabel('Напряжение, мВ')
    plt.title('Сигнал')
    plt.grid(True)
    plt.show()

    plt.plot(rfftfreq(N, 1. / FD), np_abs(spectrum)/(N))
    plt.xlabel('Частота, Гц')
    plt.ylabel('Напряжение, мВ')
    plt.title('Спектр')
    plt.grid(True)
    plt.show()
    #print(time_step, voltage_step, zero_level, type(fourier), fourier)
    print (type(np_abs(spectrum)/(N)))
if __name__ == '__main__':
    main()

