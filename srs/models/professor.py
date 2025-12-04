from app import db

class Grade(db.Model):
    __tablename__ = 'grades'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    
    student = db.relationship('Student', back_populates='grades')
    course = db.relationship('Course', back_populates='grades')

    def __repr__(self):
        return f"<Grade(student_id={self.student_id}, course_id={self.course_id}, grade='{self.grade}')>"
    