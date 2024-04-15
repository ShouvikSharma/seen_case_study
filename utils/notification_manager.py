import sqlite3
def log_notification_to_db(db_connection, channel, recipients, message,account_id,monitor_name):
    # Ensure the channel and message are strings
    channel = str(channel)
    message = str(message)
    monitor_name = str(monitor_name)

    # Convert recipients to a comma-separated string if it's a list
    if isinstance(recipients, list):
        recipients = ', '.join(recipients)
    
    query = """
    INSERT INTO notification_logs (user, communication_channel, message, account_id,monitor_name, sent_at)
    VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP);
    """
    cursor = db_connection.cursor()
    try:
        cursor.execute(query, (recipients, channel, message, account_id,monitor_name))
        db_connection.commit()
    except sqlite3.InterfaceError as e:
        print(f"Failed to insert log into database: {e}")
    finally:
        cursor.close()

class NotificationManager:
    def __init__(self, user,  communication_channel,db_connection,dataframe, monitor_name):
        self.user = user
        self.communication_channel = communication_channel
        self.db_connection = db_connection
        self.dataframe = dataframe
        self.monitor_name = monitor_name

    def send_notification(self, subject, message, channel=None):
        """General method to send notifications based on the communication channel."""
        account_ids = self.dataframe['account_id'].unique()
        messages = []

        # Generate a message for each account ID
        for account_id in account_ids:
            account_specific_data = self.dataframe[self.dataframe['account_id'] == account_id]
            message = f"Alert for account {account_id}: {len(account_specific_data)} events recorded."
            messages.append((account_id, message))
        
        for account_id, message in messages:

            # Log the notification to the database
            log_message = f"{subject} - {message}"
            log_notification_to_db(self.db_connection, self.communication_channel, self.user, log_message, account_id, self.monitor_name)

            # Depending on the communication channel, send the notification
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
