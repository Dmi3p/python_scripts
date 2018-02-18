def from_file(file):
    f = open(file, "r")
    text =f.read()
    f.close()
    return text.split("\n")

def value_getter(text, position):
    value = str(text[position]).split(" ")[3].replace(",", "." )
    return float(value)


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
    text = from_file('generator.txt')
    time_step = value_getter(text, 1)
    voltage_step = value_getter(text, 2)
    zero_level = value_getter(text, 3)
    smpl = smpl_finder(text)
    print("Временной шаг:", time_step, "nS\nНапряжение:", voltage_step, "mV\nЗемля:", zero_level, "\nМассив:", smpl[3999])

if __name__ == '__main__':
    main()

