# Class Relationships: Association and Multiplicity  
## Previous Work  
[Part I - Classes and Objects](classObjectUML.md)  
[Part II - Class Attributes and Methods](classAttributesMethods.md)  
## Existing Class  
Class: Music  
Description: The Music class represents a song in a music system. It stores information about a song and provides actions that allow the user to interact with it.  
## New Related Class
Class: Artists
Description: The Artists class represents the person/people who created the song or music.
## Association
Relationship: Music HAS-A is created by Artists
Explanation: 
## Multiplicity

Multiplicity: 1 : many
Explanation: The one-to-many multiplicity fits my design because 
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?  
I chose the one-to-many multiplicity because music (or a song) can be made by several artists.
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
