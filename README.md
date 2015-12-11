# CS 458 Automated Decision Systems Final Project
A Course Recommendation System for the Confused Student

The original proposal for the project is below:

We propose a Yale Bluebook Recommendation System for our final project. This will take in a number of inputs for the user, including past course history (and how the user rated those courses), topic preferences, and workload preferences. Using this data, it will create a weighted "preference" score for each class offered, which the user can utilize when considering courses to select. We will use existing ratings on the Coursetable website (formerly Yale Bluebook Plus, created by Yale alum) for numerical ratings of a class's workload and quality. To match subject matter preferences, the program will compare keywords that the user enters to the course's name and description (and possibly syllabus if available). The user's ratings of old courses will be used when evaluating similar courses. Finally, the user will also be able to adjust how each factor is weighed; for example, the user can choose to weigh workload over quality, and the program will take this into account when calculating the preference score. This project will be written in Python. 

Given that this problem has several real-world variables each with various attributes, we will approach the problem from an object-oriented perspective. Our primary objects will be Students and Recommendations. Within the Student object, we will incorporate elements that include but are not limited to the following:
	Major
	Class Year
	Past Course History (and the person's ratings of those courses)
	Topic Preferences
	Workload Preferences (4 or 5 classes, # of hours/week working)
	Extracurriculars (and the related time commitments)
	Other Interests
	Related Restrictions (i.e. attempting to double major, time constraints during the day)
This information will be retrieved by asking the student questions about their history and recording their input in the object.

Within the Recommendation object, we will include the following attributes:
	Recommended Class List (4 or 5 depending on preference)
	Backup List of Classes (another 5 or 6 to give the user flexibility and something to do during Shopping Period)
	Explanation (per class)

We will get course data from the Yale Courses API and store it in a database. Then, we will cross-reference this information with a student's provided preferences to recommend an optimal class list. At first, the recommendation system will be rule-based, hinging on the limitations of a student's time and their preferences. However, the system could easily become case-based as well once users are able to provide input as to whether the recommendations were effective if they choose to follow any of them. That is, if a new student with a profile similar to a previous student asks for recommendations, the system could use the old student's results to guide its decision for the new student. For example, if a sophomore Computer Science major asks for a recommendation, the system can look at all past Computer Science majors (and their classes when they were sophomores) to see if they had any classes that were high quality, interesting, or helpful to their personal development.

In short, this system will act like an automated adviser who provides tailored solutions to students after brief consultations. It has the potential to solve many of the problems that students face during Shopping Period while increasing efficiency of the entire process. For athletes, it would automatically factor in their busy schedules and remove the clutter of classes that are incompatible with their schedules. For students beginning a semester full of job interviews, the system will naturally reduce the prospective workload of the student's schedule while still considering all of the other constraints in their life, like graduation requirements. Ultimately, our system would be able to serve as a useful supplement to the resources already provided by the University.

Primarily, this project will be written in Python. Ideally, we will implement a web-based, user-friendly interface that anyone can use. Most likely, we will build this using Flask or Django, which are MVC web frameworks both built with Python. If fully implemented, we would probably use a SQL database to store all of the information.
