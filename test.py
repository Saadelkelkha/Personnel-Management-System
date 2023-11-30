# Importing the Personne, Employe, and Eleve classes from the 'classes' module.
from classes import Personne, Employe, Eleve
# Importing the 'copy' module for creating shallow copies of objects.
import copy
# Creating an instance of the Employe class (employee) with specified attributes.
emp1 = Employe(134, "saad", "elkelkha", 18, 15)
# Creating an instance of the Employe class (employee) with default values.
emp2 = Employe()
# Creating a shallow copy of the emp1 instance using the 'copy' module.
emp3 = copy.copy(emp1)

# Printing information about the first employee.
emp1.ToString()
# Printing information about the second employee.
emp2.ToString()
# Printing information about the third employee (shallow copy of emp1).
emp3.ToString()
# Checking if emp1 and emp2 are equal based on their 'code'.
print(emp1.Equals(emp2))

# Creating an instance of the Eleve class (student) with specified attributes.
ele1 = Eleve(564, "badr", "mnsour", 25, 5, 18)
# Creating an instance of the Eleve class (student) with default values.
ele2 = Eleve()
# Creating a shallow copy of the ele1 instance using the 'copy' module.
ele3 = copy.copy(ele1)

# Printing information about the first student.
ele1.ToString()
# Printing information about the second student.
ele2.ToString()
# Printing information about the third student (shallow copy of ele1).
ele3.ToString()
# Checking if ele1 and ele3 are equal based on their 'code'.
print(ele1.Equals(ele3))

# Printing the total number of Personne instances created.
print("number of personne:", Personne.Getcount())
# Printing the total number of Employe instances created.
print("number of employee:", Employe.Getcount1())
# Printing the total number of Eleve instances created.
print("number of pupil:", Eleve.Getcount2())
