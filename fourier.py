import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq, fft
from numpy import array, arange, abs as np_abs
import sys
import psycopg2


def from_file(file):
    f = open(file, "r")
    text = f.read()
    f.close()
    return text.split("\n")


def value_getter(text, position):
    value = str(text[position]).split(" ")[3].replace(",", ".")
    return float(value)


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
    time_step = value_getter(text, 1)
    voltage_step = value_getter(text, 2)
    zero_level = value_getter(text, 3)
    smpl = smpl_finder(text)
    FD = 22050
    LEN = len(smpl)
    spectrum = rfft(smpl)

    conn = psycopg2.connect(database="diplom", user="postgres", password="12Qwer34", host="127.0.0.1", port="5432")
    print('connection on')

    cur = conn.cursor()
    cur.execute("INSERT INTO examples_1 (TIME_STEP, VOLTAGE_STEP, ZERO_LEVEL, FD, LEN, SMPL)  "
                "VALUES (%s, %s, %s, %s, %s, %s) ",
                (time_step, voltage_step, zero_level, FD, LEN, smpl))
    conn.commit()
    conn.close()
    print("Data successfully executed!!")
    if len (sys.argv) > 2:
        plt.plot(arange(LEN) / float(FD), smpl)  # по оси времени секунды!
        plt.xlabel('Время, c')
        plt.ylabel('Напряжение, мВ')
        plt.title('Сигнал')
        plt.grid(True)
        plt.show()

        plt.plot(rfftfreq(LEN, 1. / FD), np_abs(spectrum) / (LEN))
        plt.xlabel('Частота, Гц')
        plt.ylabel('Напряжение, мВ')
        plt.title('Спектр')
        plt.grid(True)
        plt.show()
    else:
        pass

if __name__ == '__main__':
    main()
