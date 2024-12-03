class Course:
    def __init__(self, code, name, cost):
        self.__code = code 
        self.__course_name = name 
        self.__course_cost = cost

    @property
    def code(self):
        return self.__code
    
    @property
    def cost(self):
        return self.__course_cost
    
    def __str__(self):
        return "Course:{}       Name:{}".format(self.__code, self.__course_name)
        
class TeachingStaff:
    def __init__(self, staff_id, name, rate):
        self.__staff_id = staff_id 
        self.__name = name
        self.__rate_per_day = rate

    @property
    def rate_per_day(self):
        return self.__rate_per_day
    
    @rate_per_day.setter
    def rate_per_day(self, new_rate):
        self.__rate_per_day = new_rate

    def __str__(self):
        return "Staff ID:{}     Name:{}".format(self.__staff_id, self.__name)
    
class CourseOffering:
    __sch_id = 1
    def __init__(self, course, instructors, start_date, days):
        self.__schedule_id = course.code + "_" + CourseOffering.__sch_id
        CourseOffering.__sch_id +=1
        self.__course = course
        self.__instructors = instructors 
        self.__start_date = start_date
        self.__days = days

    @classmethod
    def change_sch_id(cls, new_id):
        cls.__sch_id = new_id 

    @property
    def schedule_id(self):
        return self.__schedule_id
    
    @property
    def start_date(self):
        return self.__start_date
    
    @start_date.setter 
    def start_date(self, newDate):
        self.__start_date = newDate

    def get_course_fee(self):
        instructors_fee = 0
        for inst in self.__instructors:
            instructors_fee = inst.rate_per_day * self.__days

        return self.__course.cost + instructors_fee 
    
    def __str__(self):
        instructors = ""
        for inst in self.__instructors:
            pass
