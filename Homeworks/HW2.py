# HW2
# Due Date: 09/24/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
import random

class Course:
    '''
    A simple class that stores the id, name, and number of credits for a class.
    '''
    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self):
        return f'{self.cid}({self.credits}): {self.cname}'

    __repr__ = __str__

    def __eq__(self, other):
        '''
        Checking if courses are equal. Equity check only based on course id.
        '''
        if isinstance(other, Course):
            return self.cid == other.cid
        return False #default case 

class Catalog:
    ''' 
    Stores a collection of Course objectsand their capacityas a dictionary, accessible by their ids.
    '''

    def __init__(self):
        self.courseOfferings = dict() #key: (Course, capacity) <- tuple

    def addCourse(self, cid, cname, credits, capacity):
        '''
        Creates a Course object with the parameters and stores it as a value in courseOfferings.
        '''
        if cid in self.courseOfferings:
            return 'Course already added'
        self.courseOfferings[cid] = (Course(cid, cname, credits), capacity) #initializes next element in courseOfferings
        return 'Course added successfully'

    def removeCourse(self, cid):
        '''
        Removes a course with the given id.
        '''
        if cid not in self.courseOfferings:
            return 'Course not found'
        self.courseOfferings.pop(cid) #removes the element with id in courseOfferings
        return 'Course removed successfully'

class Semester:
    '''
    Stores a collection of Course objects for a semester for a student.
    '''

    def __init__(self, sem_num):
        self.sem_num = sem_num
        self.courses = dict() #[cid], Course -> list of courses in a semester

    def __str__(self):
        if len(self.courses) == 0:
            return 'No courses'
        retString = ''
        for key in self.courses.keys():
            retString += f'{key}, '
        return retString[:-2]

    __repr__ = __str__

    def addCourse(self, course):
        '''
        Adds a Course to the courses dictionary
        '''
        if course.cid in self.courses:
            return 'Course already added'
        self.courses[course.cid] = course

    def dropCourse(self, course):
        '''
        Removes a course from this semester.
        '''
        if course.cid not in self.courses:
            return 'No such course'
        self.courses.pop(course.cid)

    @property
    def totalCredits(self):
        '''
        A property method for the total number of credits in this semester.
        '''
        totCred = 0
        for key in self.courses:
            totCred += self.courses[key].credits #sums all credit values from all courses
        return totCred

    @property
    def isFullTime(self):
        '''
            A property method that checks if a student taking this semester would be 
            considered full-time (taking 12 or more credits) or not.
        '''
        return self.totalCredits >= 12

class Loan:
    '''
    Represents an amount of money, with attributes for id and the loan amount.
    '''
    

    def __init__(self, amount):
        self.loan_id = self.__getloanID
        self.amount = amount


    def __str__(self):
        return f'Balance: ${self.amount}'

    __repr__ = __str__


    @property
    def __getloanID(self):
        '''
        A property method that pseudo-randomly generates loan ids.
        '''
        return random.randrange(10000, 99999)

class Person:
    '''
    Represents a person, with attributes for a name and social security number.
    '''

    def __init__(self, name, ssn):
        self.name = name
        self.__ssn = ssn

    def __str__(self):
        return f'Person({self.name}, ***-**-{self.get_ssn()[-4:]})'

    __repr__ = __str__

    def get_ssn(self):
        '''
        Getter method for accessing the private social security number attribute.
        '''
        return self.__ssn

    def __eq__(self, other):
        '''
        Determines if two objects are equal. -> checks only ssn
        '''
        if isinstance(other, Person):
            return self.get_ssn() == other.get_ssn()
        return False

class Staff(Person):
    '''
    Represents a person who is a staff member and has a supervisor.
    '''
    def __init__(self, name, ssn, supervisor=None):
        super().__init__(name, ssn) #initializes the parent class object
        self.__supervisor = supervisor

    def __str__(self):
        return f'Staff({self.name}, {self.id})'

    __repr__ = __str__

    @property
    def id(self):
        '''
        Property method for generating staff’s id.
        '''
        retStr = '905'
        names = self.name.split(' ')
        for name in names:
            retStr += name[0].lower() #adding the initials to the id
        return retStr + self.get_ssn()[-4:] #concatenating last four ssn digits

    @property   
    def getSupervisor(self):
        '''
        Property method for getting the supervisor.
        '''
        return self.__supervisor

    def setSupervisor(self, new_supervisor):
        '''
        Updates the private supervisor attribute
        '''
        if not isinstance(new_supervisor, Staff):
            return None
        self.__supervisor = new_supervisor #sets the new supervisor
        return 'Completed!'

    def applyHold(self, student):
        '''
        Applies a hold on a student object
        '''
        if not isinstance(student, Student):
            return None
        student.hold = True
        return 'Completed!'
        
    def removeHold(self, student):
        '''
        Removes a hold on a student object
        '''
        if not isinstance(student, Student):
            return None
        student.hold = False
        return 'Completed!'

    def unenrollStudent(self, student):
        '''
        Unenrolls a student object
        '''
        if not isinstance(student, Student):
            return None
        student.active = False
        return 'Completed!'

    def createStudent(self, person):
        '''
        Creates a Student object from a Person object. The new student should have the same 
        information (name, ssn) as the person and always starts out as a freshman (“Freshman”).
        '''
        if not isinstance(person, Person):
            return None
        return Student(person.name, person.get_ssn(), 'Freshman') #creating the new student object

class StudentAccount:
    '''
    Represents the financial status of a student. 
    '''
    CREDIT_PRICE = 1000

    def __init__(self, student):
        self.student = student
        self.balance = 0
        self.loans = dict()

    def __str__(self):
        return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}'

    __repr__ = __str__


    def makePayment(self, amount):
        '''
        Makes a payment by subtracting amount from the balance.
        '''
        self.balance -= amount
        return self.balance

    def chargeAccount(self, amount):
        '''
        Adds amount towards the balance.
        '''
        self.balance += amount
        return self.balance

class Student(Person):
    '''
    Represents a person who is a student that takes courses at the university.
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        super().__init__(name, ssn) #initializes the parent class object
        self.year = year
        self.semesters = dict()
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()


    def __str__(self):
        return f'Student({self.name}, {self.id}, {self.year})'

    __repr__ = __str__

    def __createStudentAccount(self):
        '''
        Creates a StudentAccount object. This should be saved in the account 
        attribute during initialization.
        '''
        if not self.active:
            return None
        return StudentAccount(self)

    @property
    def id(self):
        '''
        Property method for generating student’s id.
        '''
        retStr = ''
        for name in self.name.split(' '):
            retStr += name[0].lower() #getting the initials of student
        return retStr + self.get_ssn()[-4:] #concatenating last four ssn digits

    def registerSemester(self):
        '''
        Creates a Semester object and adds it as a value to the semesters 
        dictionary if the student is active and has no holds. It also
        updates the student’s year attribute according to the number 
        of semesters enrolled.
        '''
        if not self.active or self.hold:
            return 'Unsuccessful operation'
        
        #create new semester object and adds it to the dictionary
        newSem = Semester(len(self.semesters) + 1)
        self.semesters[newSem.sem_num] = newSem

        #checking for change in year
        if newSem.sem_num <= 2:
            self.year = 'Freshman'
        elif newSem.sem_num <= 4:
            self.year = 'Sophomore'
        elif newSem.sem_num <= 6:
            self.year = 'Junior'
        else:
            self.year = 'Senior'


    def enrollCourse(self, cid, catalog, semester):
        '''
        Finds a Course object with the given id from the catalog and adds 
        it to the courses attribute of the Semester object. Charge the 
        student’s account the appropriate amount of money.
        '''
        if not self.active or self.hold:
            return 'Unsuccessful operation'
        if cid not in catalog.courseOfferings: #checking if the course exists in the catalog
            return 'Course not found'
        if cid in self.semesters[semester].courses: #checking if the course has already been enrolled
            return 'Course already enrolled'

        currCourse = catalog.courseOfferings[cid] 
        self.semesters[semester].addCourse(currCourse[0]) #adding course to the semester object
        self.account.chargeAccount(currCourse[0].credits*StudentAccount.CREDIT_PRICE) #charging account for enrollment
        return 'Course added successfully'

    def dropCourse(self, cid):
        '''
        Finds a Course object from the current semester with the given id and 
        removes it. When a course is dropped, only half the course cost is 
        refunded to the student’s account. The current semester is defined 
        as the last added Semester object in the semester dictionary.
        '''
        if not self.active or self.hold:
            return 'Unsuccessful operation'
        currCourses = self.semesters[len(self.semesters)].courses #gets the current list of courses
        if cid not in currCourses:
            return 'Course not found'
        
        self.account.makePayment(currCourses[cid].credits*StudentAccount.CREDIT_PRICE/2) #refund the amt/2
        self.semesters[len(self.semesters)].dropCourse(currCourses[cid]) #drop the course from the current semester
        return 'Course dropped successfully'

    def getLoan(self, amount):
        '''
        If the student is active and currently enrolled full-time (consider 
        the item with the largest key in the semesters dictionary the current 
        enrollment), it creates a Loan object for the student with the given 
        amount, adds it to the student’s account’s loans dictionary, and
        uses the amount to make a payment in the student’s account.
        '''
        if not self.active:
            return 'Unsuccessful operation'
        if not self.semesters[len(self.semesters)].isFullTime: #checking if student is fulltime 
            return 'Not full-time'

        loan = Loan(amount) #creating the loan object
        self.account.loans[loan.loan_id] = loan #adding loan object to loan dictionary
        self.account.makePayment(amount) #'giving the loan'