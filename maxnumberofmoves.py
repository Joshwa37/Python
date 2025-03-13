class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        total=0
        for i in range(0,len(students)):
            if(students[i]-seats[i]>0):
                total+=students[i]-seats[i]
            else:
                total+=(students[i]-seats[i])*-1
    
        return total
