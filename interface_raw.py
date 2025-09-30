from abc import ABC, abstractmethod

class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None: pass

# Definir a regra de construção
class EmailNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'📧 EMAIL enviado para: usuario@email.com')
        print(f'   Assunto: Notificação')
        print(f'   Mensagem: {message}')
        print('   Status: Entregue ✅\n')

# Definir a regra de construção
class SMSNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'📱 SMS enviado para: +55 11 99999-9999')
        print(f'   Texto: {message}')
        print(f'   Operadora: Vivo')
        print('   Status: Entregue ✅\n')


class Notificator:
    def __init__(self, notification_sender) -> None:
        self.__notification_sender = notification_sender

    def send(self, massage: str) -> None:
        # Validação de dados
        self.__notification_sender.send_notification(massage)

obj_sms = Notificator(SMSNotificationSender())
obj_email = Notificator(EmailNotificationSender())

print("=== TESTANDO SMS ===")
obj_sms.send('Olá Mundo')

print("=== TESTANDO EMAIL ===")
obj_email.send('Olá Mundo') 