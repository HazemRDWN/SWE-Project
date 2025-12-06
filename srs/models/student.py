from db import get_db

class Student:
    def __init__(self, sID: str, sname: str, password: str):
        self.sID = sID
        self.sname = sname
        self.password = password

    def RegisterCourse(self, course_id):
        
        db = get_db()

        db.execute("""
                INSERT INTO Registered_In VALUES(?, ?, None)
                """, (self.sID, course_id))
        db.commit()

    def get_grades(self):
        db = get_db()

        sql = """SELECT c.cname, r.grade FROM Course c 
                join Registered_In r ON c.cID = r.coID 
                WHERE r.stuID = ?;"""
        cursor = db.execute(sql, (self.sID,))
        rows = cursor.fetchall()
        grades = [{'course': row[0], 'grade': row[1]} for row in rows]
        return grades