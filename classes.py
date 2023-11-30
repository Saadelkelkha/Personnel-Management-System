from abc import ABCMeta, abstractmethod

# Define an abstract base class 'Personne' with ABCMeta as metaclass.
class Personne(metaclass=ABCMeta):
    count = 0

    # Constructor to initialize a person with default values.
    def __init__(self, code=12, nom="saad", prenom="elkelkha", age=20):
        self._code = code
        self._nom = nom
        self._prenom = prenom
        self._age = age
        Personne.count += 1

    # Class method to get the count of instances created.
    @classmethod
    def Getcount(cls):
        return Personne.count

    # Getter properties for code, name, surname, and age.
    @property
    def Getcode(self):
        return self._code

    @property
    def Getnom(self):
        return self._nom

    @property
    def Getprenom(self):
        return self._prenom

    @property
    def Getage(self):
        return self._age

    # Setter methods for code, name, surname, and age.
    def Setcode(self, code1):
        self._code = code1

    def Setnom(self, nom1):
        self._nom = nom1

    def Setprenom(self, prenom1):
        self._prenom = prenom1

    def Setage(self, age1):
        self._age = age1

    # Abstract method that must be implemented by subclasses.
    @abstractmethod
    def ToString(self):
        pass

    # Method to check if two persons are equal based on their code.
    def Equals(self, per1):
        if per1.Getcode == self.Getcode:
            return True
        else:
            return False

# Subclass 'Employe' inheriting from 'Personne'.
class Employe(Personne):
    count1 = 0

    # Constructor to initialize an employee with default values and a grade.
    def __init__(self, code=12, nom="saad", prenom="elkelkha", age=20, grade=0):
        super().__init__(code, nom, prenom, age)
        self.__grade = grade
        Employe.count1 += 1

    # Class method to get the count of employee instances created.
    @classmethod
    def Getcount1(cls):
        return Employe.count1

    # Getter property for the private attribute 'grade'.
    @property
    def Getgrade(self):
        return self.__grade

    # Setter method for the private attribute 'grade'.
    def Setgrade(self, grade1):
        self.__grade = grade1

    # Method to print employee information.
    def ToString(self):
        print("Last name : ", self.Getnom, "\nFirstname : ", self.Getprenom, "\nAge :", self.Getage, "\ngrade", self.Getgrade)

# Subclass 'Eleve' inheriting from 'Personne'.
class Eleve(Personne):
    count2 = 0

    # Constructor to initialize a student with default values, level, and average.
    def __init__(self, code=12, nom="saad", prenom="elkelkha", age=20, niveau=1, moyenne=10):
        super().__init__(code, nom, prenom, age)
        self.__niveau = niveau
        self.__moyenne = moyenne
        Eleve.count2 += 1

    # Class method to get the count of student instances created.
    @classmethod
    def Getcount2(cls):
        return Eleve.count2

    # Getter properties for the private attributes 'niveau' and 'moyenne'.
    @property
    def Getniveau(self):
        return self.__niveau

    @property
    def Getmoyenne(self):
        return self.__moyenne

    # Setter methods for the private attributes 'niveau' and 'moyenne'.
    def Setniveau(self, niveau1):
        self.__niveau = niveau1

    def Setmoyenne(self, moyenne1):
        self.__moyenne = moyenne1

    # Method to print student information.
    def ToString(self):
        print("Last name : ", self.Getnom, "\nFirstname : ", self.Getprenom, "\nAge : ", self.Getage, "\nLevel", self.Getniveau, "\nAverage", self.Getmoyenne)
