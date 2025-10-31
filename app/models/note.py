from .. import db
import datetime

class Note(db.Model):
    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "content" : self.content,
            "crated_at" : self.created_at
        }