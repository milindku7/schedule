import csv

shift_counter = {}

def day_sort(filename):
    day_dict = {1:{},2:{},3:{},4:{},5:{}}
    with open(filename,"r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            shift_counter[str(row[0])] = 0
            
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

        
can = day_sort("Sunday meeting.csv")


def assign_shifts(people):
    
    flex = people
    final_list = {}
    people_keys = people.keys()
    for key in people_keys:
        
        cont_hours = {}
        for peeps in shift_counter:
            cont_hours[peeps] = 0
            
        val = people[key]
        this_day_schedule = {}
        time_min = min(val.keys())
        time_max = max(val.keys())
        time = time_min
        
        for i in range(time_max - time_min + 1):
            people_avail = val[time]
            chosen_person = people_avail[0]
            for person in people_avail:
                if cont_hours[person] < 4 and shift_counter[person] < shift_counter[chosen_person]:
                    if (shift_counter[chosen_person] - shift_counter[person] > 2):
                        chosen_person = person
                    elif cont_hours[chosen_person] > 2:
                        chosen_person = person
            if time < 15:       
                lowest = 10
                second_person = ''
                for person2 in people_avail:
                    if cont_hours[person2] < 4 and person2 != chosen_person:
                        diff = shift_counter[person2] - shift_counter[chosen_person]
                        if diff < lowest:
                            lowest = diff
                            second_person = person2
                                        
            this_day_schedule[time] = [chosen_person]
            if time < 15:
                this_day_schedule[time].append(second_person)
            cont_hours[chosen_person] = cont_hours[chosen_person] + 1
            shift_counter[chosen_person] = shift_counter[chosen_person] + 1
            if time < 15:
                cont_hours[person2] = cont_hours[person2] + 1
                shift_counter[person2] = shift_counter[person2] + 1
            time += 1
        print(this_day_schedule)
        #print(shift_counter)
            
print(assign_shifts(can))       
                                
                        
                            
                    
                
    

        