# RANDOM QUIZ QUESTIONS API

# Used tech stack
Python, Flask-API, SQLAlchemy, PostgreSQL

# General description
API is designed to recieve post requests with a JSON in the following form:
{"questions_num": integer}

As a result, new questions are added into a database and a response is returned to the user (the last added question is returned).
Questions are taken randomly from a public QUIZ-API.

# Example of a post-request
request - {"questions_num": 2}
new quiz questions added to a database :
{
        "id": 31023,
        "request": "Some small wedding receptions eliminate this greeting line that was once de rigeueur",
        "response": "the receiving line (the reception line accepted)",
        "datetime": "2022-12-30 18:50:22"
    },
    {
        "id": 189006,
        "request": "Mei Xiang to Bao Bao (born 2013)",
        "response": "mother",
        "datetime": "2022-12-30 21:30:15"
    }
response: [] (if database was empty before the request)
          {
        "id": 63337,
        "request": "11 years after his last Top 20 solo hit, this \"Sweet Caroline\" singer had the third top-grossing tour of 1993",
        "response": "Neil Diamond",
        "datetime": "2022-12-30 19:05:03"
    }
    (the last previous added item if database was not empty before the request)


# Database description
The database contains the following data: 
id of the quizquestion, 
text of a question (request field)
text of an answer (response field)
creation date (datetime field)
date, when question was added to a database (date field, not returned to a user)


# Build instructions
To run project on your machine you need to have docker installed.
1) Clone the repository (git clone)
2) In the project directory run docker containers (docker-compose up --build)
3) Your localhost now can recieve post requests
