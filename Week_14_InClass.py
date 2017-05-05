

def func_room_num ():
    dictionary_room_num = {}
    dictionary_room_num['CS101'] = '3004'
    dictionary_room_num['CS102'] = '4501'
    dictionary_room_num['CS103'] = '6755'
    dictionary_room_num['NT110'] = '1244'
    dictionary_room_num['CM241'] = '1411'
    return dictionary_room_num

def func_instructor ():
    dictionary_instructor = {}
    dictionary_instructor['CS101'] = 'Haynes'
    dictionary_instructor['CS102'] = 'Alvarado'
    dictionary_instructor['CS103'] = 'Rich'
    dictionary_instructor['NT110'] = 'Burke'
    dictionary_instructor['CM241'] = 'Lee'
    return dictionary_instructor

def func_meeting_time ():
    dictionary_meeting_time = {}
    dictionary_meeting_time['CS101'] = '8:00 a.m.'
    dictionary_meeting_time['CS102'] = '9:00 a.m.'
    dictionary_meeting_time['CS103'] = '10:00 a.m.'
    dictionary_meeting_time['NT110'] = '11:00 a.m.'
    dictionary_meeting_time['CM241'] = '1:00 p.m.'
    return dictionary_meeting_time


def main():
    room_num = func_room_num()
    instructor = func_instructor()
    time =func_meeting_time()

    class_num = input('enter class to lookup')
    class_name = room_num[class_num],instructor[class_num],time[class_num]
    print('The Class will be in room:',class_name[0])
    print('The Instructor will be:',class_name[1])
    print('The class will meet at:',class_name[2])



main()




