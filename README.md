Work Automation AI
This project is a Python-based Work Automation AI designed to automate the process of sending scheduled emails with attachments, such as monthly reports or documents, based on a defined set of work items.

Getting Started
Prerequisites
You need Python 3.x installed on your system.

Installation
Install the necessary Python packages using pip:

Bash
pip install pyyaml schedule
Configuration
The project relies on two main configuration files: config.yaml and work_items.json.

1. config.yaml
This file stores your email credentials and SMTP server details. Remember to use an App Password instead of your regular email password if you are using a service like Gmail with Two-Factor Authentication enabled.

YAML
email:
  sender: 2k22.csai.2213601@gmail.com # The email address that will send the emails
  username: piyush # The username for logging into the SMTP server (often the same as the sender email)
  password: hfwk yehy tofn xkzx # Your App Password or regular password (use App Password for security)
  smtp_server: smtp.gmail.com
  smtp_port: 587
2. work_items.json
This file defines the tasks to be automated. The provided example shows a "Monthly Report" task.

JSON
[
    {
        "name": "Monthly Report",
        "type": "document",
        "file_path": "C:/Users/piyus/Desktop/Personal/offencial work/self automate ai/monthly_report.pdf",
        "email_recipients": ["recipient@example.com"],
        "schedule": "monthly" # Note: Scheduling logic is simplified; currently, it processes every hour.
    }
]
Work Item Structure:

name: A descriptive name for the task (used as the email subject).

type: Type of content (e.g., "document").

file_path: The absolute path to the file/attachment.

email_recipients: A list of email addresses that will receive the email.

schedule: The intended schedule (currently not fully implemented with the schedule library; the process_work_items function runs hourly).

Usage
To start the automation process, run the main script:

Bash
python self automate.py
The script will:

Initialize the WorkAutomationAI class, loading configurations and existing work items.

Schedule the process_work_items method to run every hour.

Continuously check for pending scheduled tasks.

Note on Scheduling: The current implementation uses schedule.every(1).hour.do(self.process_work_items). The internal _should_process_item logic is currently set to always return True, meaning it will attempt to send all configured work items every hour. You would need to implement more sophisticated date/time comparison within _should_process_item to honor the "schedule": "monthly" setting.

Project Structure
.
├── config.yaml           # Email configuration and credentials
├── work_items.json       # Definitions of scheduled automation tasks
└── self automate.py      # Main Python script containing the automation logic
