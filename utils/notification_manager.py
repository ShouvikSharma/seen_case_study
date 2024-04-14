class NotificationManager:
    def __init__(self, user, communication_channel="email"):
        self.user = user
        self.communication_channel = communication_channel

    def send_notification(self, subject, message, channel=None):
        """General method to send notifications based on the communication channel."""
        if self.communication_channel == "email":
            return self.send_email(subject, message)
        elif self.communication_channel == "slack":
            return self.send_slack(channel, message)
        elif self.communication_channel == "jira":
            return self.create_jira_ticket(subject, message)
        else:
            print(f"Communication channel {self.communication_channel} is not supported.")
            return "Unsupported communication channel"

    def send_email(self, subject, message):
        """Stub method to simulate sending an email."""
        print(f"Simulated sending email to {self.user}: Subject='{subject}', Message='{message}'")
        return "Email sent"

    def send_slack(self, channel, message):
        """Stub method to simulate sending a Slack message."""
        print(f"Simulated sending Slack message to channel {channel}: Message='{message}'")
        return "Slack message sent"

    def create_jira_ticket(self, title, description):
        """Stub method to simulate creating a JIRA ticket."""
        print(f"Simulated creating JIRA ticket: Title='{title}', Description='{description}'")
        return "JIRA ticket created"
