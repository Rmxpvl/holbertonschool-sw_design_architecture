#!/usr/bin/env python3
"""Observer pattern example with topic filtering."""


class NewsSubject:
    """Subject that notifies observers about news topics."""

    def __init__(self):
        self._observers = []

    def subscribe(self, observer, topics=None):
        """Subscribe an observer, optionally limiting the topics it receives."""
        topic_set = None if topics is None else set(topics)
        self._observers.append((observer, topic_set))

    def unsubscribe(self, observer):
        """Remove an observer from the subscription list."""
        self._observers = [
            (current_observer, topics)
            for current_observer, topics in self._observers
            if current_observer is not observer
        ]

    def notify(self, topic, data):
        """Notify observers interested in the given topic."""
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Observer that logs sports and breaking news."""

    def update(self, topic, data):
        print(f"log:{topic}={data}")


class EmailObserver:
    """Observer that receives every topic."""

    def update(self, topic, data):
        print(f"email:{topic}={data}")


class SmsObserver:
    """Observer that receives only breaking news."""

    def update(self, topic, data):
        print(f"sms:{topic}={data}")


def main():
    """Run a small demo of the notification flow."""
    subject = NewsSubject()

    log_observer = LogObserver()
    email_observer = EmailObserver()
    sms_observer = SmsObserver()

    subject.subscribe(log_observer, topics={"sports", "breaking"})
    subject.subscribe(email_observer)
    subject.subscribe(sms_observer, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
