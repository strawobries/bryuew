"""
Session Module

This module defines the Session class, which stores
study session information such as ID, subject,
duration, date, and notes.
"""


class Session:
    def __init__(self, session_id, subject, duration, date, notes):
        self.session_id = session_id
        self.subject = subject
        self.duration = duration
        self.date = date
        self.notes = notes

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "subject": self.subject,
            "duration": self.duration,
            "date": self.date,
            "notes": self.notes
        }

    @staticmethod
    def from_dict(data):
        return Session(
            data["session_id"],
            data["subject"],
            data["duration"],
            data["date"],
            data["notes"]
        )