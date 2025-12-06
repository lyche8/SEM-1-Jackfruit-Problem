import uuid
import datetime
import csv
import os

def generate_token():
    """Generate a unique appointment token."""
    return "APT-" + uuid.uuid4().hex[:8].upper()

def save_appointment(name, doctor, date, time, filename = os.path.join(os.path.dirname(__file__), "appointments.csv")):
    """Save appointment details + token into a CSV file."""
    
    token = generate_token()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create file if it doesn't exist
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header if file is new
        if not file_exists:
            writer.writerow(["Token", "Patient Name", "Doctor", "Date", "Time", "Timestamp"])

        # Write appointment row
        writer.writerow([token, name, doctor, date, time, timestamp])

    return token


# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    print("=== Healthcare Appointment Token Generator ===")

    name = input("Enter patient name: ")
    doctor = input("Enter doctor name: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM): ")

    token = save_appointment(name, doctor, date, time)

    print(f"\nAppointment token generated: {token}")
    print("Details saved to appointments.csv")