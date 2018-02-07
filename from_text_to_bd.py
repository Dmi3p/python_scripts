import sys


def from_file(file):
    f = open(file, "r")
    text =f.read()
    f.close()
    return text.split("\n")


def time_step_finder(text):
    string = text[1]
    value = string[12:17].replace(",",".")
    return float(value)


def voltage_step_finder(text):
    string = str(text[2])
    value = string[15:20].replace(",",".")
    return float(value)


def zero_level_finder(text):
    string = str(text[3])
    value = string[13:]
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

    print(time_step, voltage_step, zero_level, type(smpl[10]))

if __name__ == '__main__':
    main()