import sys
import sqlite3


def from_file(file):
    f = open(file, "r")
    text =f.read()
    f.close()
    return text.split("\n")


def time_step_finder(text):
    value = text[1].split(" ")[3].replace(",",".")
    return float(value)


def voltage_step_finder(text):
    value = str(text[2]).split(" ")[3].replace(",",".")
    return float(value)


def zero_level_finder(text):
    value = str(text[3]).split(" ")[3].replace(",",".")
    return int(value)



def smpl_finder(text):
    list = []
    list2 =[]
    for el in text [7:]:
        list.append(el.split("\t"))
    i = 0
    while i <= len(list) - 2:
        list2.append(int(list[i][1]))
        i+=1
    return list2

def main():
    #text = from_file(sys.argv[1])
    text = from_file('generator.txt')
    time_step = time_step_finder(text)
    voltage_step = voltage_step_finder(text)
    zero_level = zero_level_finder(text)
    smpl = smpl_finder(text)
    pack_to_sql = (time_step, voltage_step, zero_level, smpl[0])

   # conn = sqlite3.connect("samples.db")
    #cursor = conn.cursor()
    #cursor.executemany("INSERT INTO samples VALUES (?,?,?,?,?)", pack_to_sql )
    #conn.commit()

    print(time_step, voltage_step, zero_level, type(smpl[0]))

if __name__ == '__main__':
    main()