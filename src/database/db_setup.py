import sqlite3

def create_database():
    connection = sqlite3.connect("job_screening.db")
    cursor = connection.cursor()
    
    ## Job description table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_descriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            required_skills TEXT NOT NULL,
            experience TEXT,
            responsibilities TEXT,
            qualifications TEXT
        )
    ''')
    
    ## Resume table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            education TEXT,
            experience TEXT,
            skills TEXT NOT NULL,
            certifications TEXT
        )
    ''')
    
    ## Score match table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS match_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER,
            resume_id INTEGER,
            match_score REAL,
            FOREIGN KEY (job_id) REFERENCES job_descriptions(id),
            FOREIGN KEY (resume_id) REFERENCES resumes(id)
        )
    ''')
    ## Candidate related Info for scheduling interviews
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scheduled_interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            candidate_name TEXT NOT NULL,
            candidate_email TEXT NOT NULL,
            job_title TEXT NOT NULL,
            interview_date TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'  -- Status: Pending, Confirmed, Canceled
        )
    ''')
    
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_database()
    print("Database and tables created successfully.")
