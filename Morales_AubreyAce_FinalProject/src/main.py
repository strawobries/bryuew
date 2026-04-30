import json
import os


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
        results = [
            s for s in self.sessions
            if keyword.lower() in s.subject.lower()
        ]

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


def menu():
    print("\n===== Study Time =====")
    print("1. Add Session")
    print("2. View Sessions")
    print("3. Search Session")
    print("4. Delete Session")
    print("5. Update Session")
    print("6. Sort Sessions")
    print("7. Count Sessions")
    print("8. Total Study Time")
    print("9. Save")
    print("10. Load")
    print("11. Exit")


def main():
    manager = SessionManager()

    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                session_id = input("Enter ID: ").strip()
                subject = input("Enter subject: ").strip()
                duration = int(input("Enter duration (minutes): "))
                date = input("Enter date (MM-DD-YYYY): ").strip()
                notes = input("Enter notes: ").strip()

                if not session_id or not subject:
                    print("ID and Subject are required.")
                    continue

                new_session = Session(
                    session_id,
                    subject,
                    duration,
                    date,
                    notes
                )

                manager.add_session(new_session)

            except ValueError:
                print("Duration must be a number.")

        elif choice == "2":
            manager.view_sessions()

        elif choice == "3":
            keyword = input("Search subject: ").strip()
            manager.search_session(keyword)

        elif choice == "4":
            session_id = input("Enter ID to delete: ").strip()
            manager.delete_session(session_id)

        elif choice == "5":
            session_id = input("Enter ID to update: ").strip()
            manager.update_session(session_id)

        elif choice == "6":
            manager.sort_sessions()

        elif choice == "7":
            manager.count_sessions()

        elif choice == "8":
            manager.total_study_time()

        elif choice == "9":
            manager.save_to_file()

        elif choice == "10":
            manager.load_from_file()

        elif choice == "11":
            print("Well Done, Keep it up!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
