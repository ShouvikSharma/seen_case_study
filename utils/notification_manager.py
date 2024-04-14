class NotificationManager:
    def __init__(self, user):
        self.user = user

    def send_email(self, subject, message):
        """Stub method to simulate sending an email."""
        print(f"Simulated sending email to {self.user}: Subject='{subject}', Message='{message}'")

    def send_slack(self, channel, message):
        """Stub method to simulate sending a Slack message."""
        print(f"Simulated sending Slack message to channel {channel}: Message='{message}'")

    def create_jira_ticket(self, title, description):
        """Stub method to simulate creating a JIRA ticket."""
        print(f"Simulated creating JIRA ticket: Title='{title}', Description='{description}'")
