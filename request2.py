def overlap(m1, m2):
    if ((m1[1] <= m2[0]) or (m1[0] >= m2[1])):
        return False
    return True

def answer(meetings):
    # your code here
    count = 1;
    meetings_sorted = sorted(meetings, key=lambda meeting: meeting[1])

    print meetings_sorted
    
    current_meeting = meetings_sorted[0]
    
    for meeting in meetings_sorted:
        if (overlap(current_meeting, meeting)):
            print "overlapping " + str(current_meeting) + " and " + str(meeting)
            continue
        else:
            current_meeting = meeting
            count = count + 1
    return count

me = [[1,3], [2,3], [3,4], [1,2]]
print answer(me)
