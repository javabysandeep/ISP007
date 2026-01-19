class NotificationService:
    def notify_user(self):
        print("notify user using email")


class NotificationServiceImpl(NotificationService):
    def notify_user(self):
        super().notify_user()
        print("notify user using whatsApp")
        print("notify user using push notification")


ref = NotificationServiceImpl()
ref.notify_user()
