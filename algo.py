import csv

people = []

shift_counter = {}

def sorting(filename):
    people_shift = {}
    with open(filename,"r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            people_shift[str(row[0])] = []
            
            for shif in range(len(row)):
                if shif != 0:
                    list = people_shift[str(row[0])]
                    list.append(str(row[shif]))
                    people_shift[str(row[0])] = list
            
    return people_shift

def day_sort(filename):
    day_dict = {1:{},2:{},3:{},4:{},5:{}}
    with open(filename,"r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            for shif in range(len(row)):
                if shif != 0 and str(row[shif]) != "not available" and str(row[shif]) != "":
                    
                    time_range = str(row[shif])
                    time_range = time_range.split("-")
                    time_range[0] = int(time_range[0])
                    time_range[1] = int(time_range[1])
                    if time_range[0] < 9:
                        time_range[0] = time_range[0] + 12
                    if time_range[1] < 9:
                        time_range[1] = time_range[1] + 12
                    curr_day_dict = day_dict[shif]
                    for time_avail in range(time_range[0],time_range[1]):
                        if time_avail in curr_day_dict.keys():
                            curr_day_dict[time_avail].append(str(row[0]))
                        else:
                            new_l = [str(row[0])]
                            curr_day_dict[time_avail] = new_l
                    day_dict[shif] = curr_day_dict
    return day_dict

            
    
can = sorting("excel.csv")
c = day_sort("Sunday meeting.csv")
print("the c")
print(c)

def assign_shifts(people):
    people_keys = people.keys()
    small = 100
    small_min = 100
    for key in people_keys:
        val = people[key]

        for time in val:
            ti = time.split(":")
            tim = int(ti[1])
            t = int(ti[0])
            if t < small:
                small = t
                small_min = tim
            elif t == small:
                if tim < small_min:
                    small_min = tim
    first_shift = str(small) + ":" + str(small_min)
    
    shift_counter = {}
    for key in people_keys:
        shift_counter[key] = 0
    
    people_for_the_shift = {}
    for key in people_keys:
        val = people[key]
        for time in val:
            if time not in people_for_the_shift.keys():
                people_for_the_shift[time] = 1
            else:
                curr = people_for_the_shift[time]
                people_for_the_shift[time] = curr + 1
    
    sorted_times = sorted(people_for_the_shift.items(), key=lambda x:x[1])
    
    final_dict = {}
    
    for i in range(len(sorted_times)):
        time_tuple = sorted_times.pop()
        time = time_tuple[0]
        for key in people_keys:
            val = people[key]
            for t in val:
                if t == time:
                    if t not in final_dict.keys():
                        l = []
                        l.append(key)
                        final_dict[time] = l
                        num = shift_counter[key]
                        shift_counter[key] = num + 1
                    else:
                        pe = final_dict[t]
                        
                        if len(pe) < 2:
                            pe.append(key)
                            final_dict[time] = pe
                            num = shift_counter[key]
                            shift_counter[key] = num + 1
                        else:
                            curr_key_shifts = shift_counter[key]
                            ppp = pe
                            
                            for po in pe:                               
                                if po in shift_counter.keys():                              
                                    po_shifts = shift_counter[po]
                                    if po_shifts > curr_key_shifts:
                                        ppp.remove(po)
                                        ppp.append(key)
                                        final_dict[time] = ppp
                                        shift_counter[key] = shift_counter[key] + 1
                                        shift_counter[po] = shift_counter[po] - 1
    print(final_dict)
                                    
                                
                        
                            
                    
                
    
assign_shifts(can)
        