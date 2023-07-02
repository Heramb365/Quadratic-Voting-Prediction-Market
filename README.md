Quadratic Voting Prediction Market

This Python-based application is a prototype for a democratic prediction market system proposed for the "Democratic Inputs to AI Challenge" by OpenAI. The system is designed to provide a democratic platform where users can flag potential issues in AI behavior, such as misinformation, bias, inappropriate contextualization, or malalignment.

System Overview
The system is organized around a Market class, which includes methods for registering users, posting questions, voting on questions, displaying results of votes, and showing remaining user credits.

Users
Users can register in the system with a unique username. Each user is initially assigned 100 voice credits.

Questions
Registered users can post questions, which serve as the subjects for the prediction markets.

Voting
Users can vote on the posted questions. The cost of voting is quadratic, i.e., it costs the square of the number of votes a user places on a question. This ensures that users strategically use their voice credits and that the influence of a user on the market is kept in check.

Results and Credits
The system includes functionalities to display the results of the voting on the questions and the remaining voice credits of the users.

Quadratic Voting Principle
This system follows the Quadratic Voting principle, which allows users to express not only which direction they lean, but also how strongly they feel about it. It ensures that the enforcement of outcomes remains equitable and just, while preventing undue influence or manipulation.

Enforcement
While the system is designed to allow democratic decision-making, OpenAI holds the veto power on the enforcement of the market's outcome. This serves as a safeguard to prevent potential undue influence or manipulation.

This system encourages active engagement, informed decision-making, and wise use of influence, maintaining the integrity of the project while addressing potential AI biases and misinformation.
