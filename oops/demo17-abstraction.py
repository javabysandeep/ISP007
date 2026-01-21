from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def notify_user(self):
        pass

class NotificationServiceImpl(NotificationService):
    def notify_user(self):
        print("Notification service - whatsApp email")

ref=NotificationServiceImpl()
ref.notify_user()