import os
import smtplib
import schedule
import time
import yaml
import json
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class WorkAutomationAI:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
        U0
        self.work_items = []
        self.load_work_items()

    def load_work_items(self):
        """
        Load work items from a JSON file.
        Each work item should have:
        - name: Task name
        - type: Type of work (document, email, report)
        - schedule: When to send/process
        - file_path: Location of the work item
        - email_recipients: List of email recipients
        """
        try:
            with open('work_items.json', 'r') as file:
                self.work_items = json.load(file)
        except FileNotFoundError:
            print("No existing work items found. Please add work items.")

    def add_work_item(self, work_item):
        """
        Add a new work item to the list and save to JSON
        """
        self.work_items.append(work_item)
        with open('work_items.json', 'w') as file:
            json.dump(self.work_items, file, indent=4)

    def send_email(self, subject, body, recipients, attachments=None):
        """
        Send email with optional attachments
        """
        msg = MIMEMultipart()
        msg['From'] = self.config['email']['sender']
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject

        # Attach body
        msg.attach(MIMEText(body, 'plain'))

        # Attach files
        if attachments:
            for attachment in attachments:
                with open(attachment, 'rb') as file:
                    part = MIMEApplication(file.read(), Name=os.path.basename(attachment))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
                    msg.attach(part)

        # Send email
        try:
            with smtplib.SMTP(
                self.config['email']['smtp_server'], 
                self.config['email']['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.config['email']['username'], 
                    self.config['email']['password']
                )
                server.send_message(msg)
            print(f"Email sent: {subject}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def process_work_items(self):
        """
        Process and send scheduled work items
        """
        current_time = datetime.now()
        for item in self.work_items:
            # Check if it's time to process this work item
            # This is a simplified scheduling logic
            if self._should_process_item(item, current_time):
                self.send_email(
                    subject=item.get('name', 'Automated Work Item'),
                    body=f"Automated delivery of work item: {item['name']}",
                    recipients=item.get('email_recipients', []),
                    attachments=[item['file_path']] if 'file_path' in item else None
                )

    def _should_process_item(self, item, current_time):
        """
        Determine if a work item should be processed
        """
        return True

    def start(self):
        """
        Start the work automation process
        """
        schedule.every(1).hour.do(self.process_work_items)

        while True:
            schedule.run_pending()
            time.sleep(1)
"""
email:
  sender: your_email@gmail.com
  username: your_email@gmail.com
  password: your_password
  smtp_server: smtp.gmail.com
  smtp_port: 587
"""
if __name__ == '__main__':
    ai_assistant = WorkAutomationAI()

    ai_assistant.add_work_item({
        'name': 'Monthly Report',
        'type': 'document',
        'file_path': '/path/to/monthly_report.pdf',
        'email_recipients': ['2k22.csai.2213601@gmail.com'],
        'schedule': 'monthly'
    })
    ai_assistant.start() 