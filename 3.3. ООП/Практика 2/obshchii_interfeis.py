class EmailNotifier:
    def send(self, message):
        return f'Email: {message}'


class SmsNotifier:
    def send(self, message):
        return f'SMS: {message}'


def notify_all(notifiers, message):
    messages = []
    for notifier in notifiers:
        messages.append(notifier.send(message))
    return messages
