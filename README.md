# Personnel-Management-System
This program, named "Personnel Management System," is designed to manage information about individuals within an organization, specifically employees (Employe) and students (Eleve). The system is implemented using object-oriented principles in Python.

# Main Program:

The main program begins by importing necessary classes from the 'classes' module, which includes the base class 'Personne,' as well as its subclasses 'Employe' and 'Eleve.' Additionally, the 'copy' module is imported for creating shallow copies of objects.

The program then creates instances of the 'Employe' and 'Eleve' classes, demonstrating the flexibility of initializing objects with both specified attributes and default values. Shallow copies of instances are also created using the 'copy' module.

Information about each individual (employee or student) is printed using the ToString method, showcasing details such as last name, first name, age, grade (for employees), level, and average (for students). The program checks if two individuals are equal based on their unique 'code.'

Finally, the program prints the total number of instances created for each class using class methods.

# Classes:

The 'classes' module contains the implementation of the personnel management system. The base class 'Personne' is an abstract class with attributes such as code, last name, first name, and age. Subclasses 'Employe' and 'Eleve' extend 'Personne' and include additional attributes such as grade and level/average, respectively.

Each class provides methods for retrieving and modifying attributes, as well as a ToString method for generating a string representation of the object. The 'Equals' method checks for equality based on the 'code' attribute.

This program serves as a foundation for managing personnel information within an organization, with extensibility for future enhancements and additional functionalities.





