"""
Session Manager Module

This module handles study session management,
including adding, viewing, searching, updating,
deleting, sorting, saving, and loading sessions.
"""

import json
import os
from session import Session


class SessionManager:
    def __init__(self):
        self.sessions = []
        self.file_path = os.path.join("data", "sessions.json")

    def add_session(self, session):
        if any(s.session_id == session.session_id for s in self.sessions):
            print("Session ID already exists.")
            return

        self.sessions.append(session)
        print("Session added successfully.")

    def view_sessions(self):
        if not self.sessions:
            print("No sessions found.")
            return

        print("\n--- Study Sessions ---")
        for s in self.sessions:
            print(f"ID: {s.session_id}")
            print(f"Subject: {s.subject}")
            print(f"Duration: {s.duration} minutes")
            print(f"Date: {s.date}")
            print(f"Notes: {s.notes}")
            print("-" * 30)

    def search_session(self, keyword):
        results = [s for s in self.sessions if keyword.lower() in s.subject.lower()]

        if results:
            print("\n--- Search Results ---")
            for s in results:
                print(f"{s.session_id} | {s.subject} | {s.duration} mins")
        else:
            print("No session found.")

    def delete_session(self, session_id):
        for s in self.sessions:
            if s.session_id == session_id:
                self.sessions.remove(s)
                print("Session deleted successfully.")
                return
        print("Session not found.")

    def update_session(self, session_id):
        for s in self.sessions:
            if s.session_id == session_id:
                print("Leave blank to keep current value.")

                subject = input(f"New subject ({s.subject}): ")
                duration = input(f"New duration ({s.duration}): ")
                date = input(f"New date ({s.date}) (MM-DD-YYYY): ")
                notes = input(f"New notes ({s.notes}): ")

                if subject:
                    s.subject = subject
                if duration:
                    try:
                        s.duration = int(duration)
                    except ValueError:
                        print("Invalid duration. Old value kept.")
                if date:
                    s.date = date
                if notes:
                    s.notes = notes

                print("Session updated successfully.")
                return

        print("Session not found.")

    def sort_sessions(self):
        self.sessions.sort(key=lambda s: s.subject.lower())
        print("Sessions sorted successfully.")

    def count_sessions(self):
        print(f"Total sessions: {len(self.sessions)}")

    def total_study_time(self):
        total = sum(s.duration for s in self.sessions)
        print(f"Total study time: {total} minutes")

    def save_to_file(self):
        os.makedirs("data", exist_ok=True)
        with open(self.file_path, "w") as file:
            json.dump([s.to_dict() for s in self.sessions], file, indent=4)
        print("Data saved successfully.")

    def load_from_file(self):
        if not os.path.exists(self.file_path):
            print("No saved file found.")
            return

        with open(self.file_path, "r") as file:
            data = json.load(file)

        self.sessions = [Session.from_dict(item) for item in data]
        print("Data loaded successfully.")
