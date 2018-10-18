#just allows me to copy/paste a column from excel and it outputs it
#formatted as an array for Javascript

#copy/paste column here
data = """
Jaspreet
Karl Stoll
Hazim DyNamik
Tom Allen
Ray Zhong via correspondence from Hong Kong
Martin McArthy, Back from retirement
Based Peter Richards 
Tom Allen's Favorite Shear Flow Section
Nic Smith
Harambe
Zach Huxford's Moustache
Your absentee father
Martin McArthy's Shaft
a door
that guy who never comes to class and you only see at tests
Bryony
Fisher & Paykel Appliances Auditorium 260-115
the thinking emoji
the eggplant emoji
the remains of your Warman report
a lime scooter
your systems group
your truss project
a lecture recording on 0.5x speed
A lifesized cutout of Hazim
Lihua's comprehensive coursenotes
An actual Floating wind turbine
A sunken wind turbine 
More Carbon Fibre
Unenthusiastic Mike Kingan
Very Enthusiastic Mike Kingan 
Nicholas Smith
an Onzo
that guy from ports of auckland who did the Simio guest lecture
Rob Kirkpatrick
a shit project partner 
Harambe
a peice of Carbon fibre 
a life Sized cutout of your friend who chose to go with someone competent instead of you
your Ex 
your soon to be Ex
An Onzo
A lime scooter
a life Sized cutout of your friend who chose to go with your ex instead of you
Stuart Norris 
Brian Mace
BaeVid Wynn
that FSAE guy who never comes to class and you only see at tests
that guy who's on first name basis with all the lecturers 
That guy who says: "can you please move the page up!!!" 
That girl who says: "can you please move the page up!!!" 
Two semesters of pain
Eva Hakansson' Bike 
The Dean 
The Practical Work Commitee 
the person who won't shut up about their F&P internship 
Rocketlab's Rocket sanding intern 
"""
print("["+ data.replace('\n','", "')[3:-3] + "]")
