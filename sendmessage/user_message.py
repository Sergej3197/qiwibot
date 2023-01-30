from marcup.marcup import user_marcup
from bd.bd import Database
import random
from qiwi.qiwi import qiwi_aio

bd = Database()
add_mrkp =user_marcup()
qiwi = qiwi_aio()

class users_typesMessage:
    def __call__(self, user_text, user_id):
        self.message_text = ''
        self.marcup = ''
        self.user_type = ''
        if not bd.user_exists(user_id):
            bd.add_user_id(user_id)
        if not bd.get_block_user(user_id):
            if not user_text==('/start' or '/admin'):
                if bd.get_last_move(user_id)=='add_balans':
                    if ((str(user_text)).isdigit() and int(user_text)) > 0:
                        user_bill_id = random.randint(10000000, 99999999)
                        while bd.user_billId_exists(user_bill_id):
                            user_bill_id = random.randint(10000000, 99999999)
                        bd.add_bill_values(user_id, user_text, user_bill_id)
                        bd.add_last_move('rest', user_id)
                        qiwi.send_bill(user_bill_id, user_text)
                        self.message_text = 'Платёж успешно создан'
                        self.marcup = add_mrkp.addinlineMarkup_Url(2, qiwi.pay_url, '🔗Сылка на оплату', 'check_pay', '✔️Проверка платежа')
                        self.user_type = 'text'
                    else:
                        self.message_text = 'Введите сумму, на которую вы хотите пополнить баланс(целое число)'
                        self.user_type = 'text'
                money_usr_call = bd.get_last_move(user_id)
                if (money_usr_call)[:5]=='money':
                    if ((str(user_text)).isdigit() and int(user_text)) > 0:
                        bd.add_money(user_text, (money_usr_call)[5:])
                        bd.add_last_move('rest', user_id)
                        self.message_text = f'Баланс пользователя {user_id} успешно изменён'
                        self.user_type = 'text'
                    else:
                        self.message_text = 'Введите баланс пользователя(целое число)'
                        self.user_type = 'text'
