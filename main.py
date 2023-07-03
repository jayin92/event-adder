import ics

c = ics.Calendar()

cur_date = None

with open("camp.txt", "r") as f:
    for line in f:
        if line.startswith("Date:"):
            cur_date = line[5:].strip()
        else:
            line = line.split(" ")
            begin = line[0].split("-")[0]
            end = line[0].split("-")[1]
            # use taipei timezone
            begin = begin + "+08:00"
            end = end + "+08:00"
            name = " ".join(line[1:]).strip()
            c.events.add(ics.Event(name=name, begin=cur_date + " " + begin, end=cur_date + " " + end))

with open('camp.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())