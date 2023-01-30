from marcup.marcup import user_marcup
from bd.bd import Database
from qiwi.qiwi import qiwi_aio

bd = Database()
add_mrkp =user_marcup()
qiwi = qiwi_aio()

class user_callback:
    def __call__(self,user_text, user_id):
        self.message_text  = ''
        self.marcup = ''
        self.user_type = ''
        if not bd.user_exists(user_id):
            bd.add_user_id(user_id)
        if not bd.get_block_user(user_id):
            if user_text == 'add_balans':
                bd.add_last_move(user_text, user_id)
                self.message_text = 'Введите сумму, на которую вы хотите пополнить баланс'
                self.user_type = 'text'
            elif user_text == 'check_pay':
                bill_id = bd.get_user_bill_id(user_id)
                pay_sastus = qiwi.check(bill_id)
                if pay_sastus == 'PAID':
                    bill_status = bd.get_bill_status(bill_id)
                    if bill_status == 'rest':
                        amount = bd.get_bill_money(bill_id)
                        money = bd.get_money(user_id)
                        money = int(money) + int(amount)
                        bd.add_money(money, user_id)
                        bd.add_bill_status(pay_sastus, bill_id)
                        self.message_text = 'Платёж прошёл👍'
                        self.user_type = 'text'
                    elif bill_status == 'PAID':
                        self.message_text = 'Платёж уже проведён и добавлен вам на баланс'
                        self.user_type = 'text'           
                else:
                    self.message_text = 'Платёж не прошёл👎'
                    self.user_type = 'text'
            elif user_text == 'uploading_users':
                self.admin_users = bd.get_users_and_money()
                self.user_type = 'uploading_users'
            elif user_text[:5] == "money":
                bd.add_last_move(user_text, user_id)
                self.message_text = 'Введите баланс пользователя'
                self.user_type = 'text'
            elif user_text[:5] == "block":
                block_id = user_text[5:]
                bd.add_block_list(block_id)
                self.message_text = f'Пользователь {block_id} заблокирован'
                self.user_type = 'text'
            elif user_text == "uploading_log":
                with open("/home/vas/Документы/testQiwi/error.log", 'r') as file:
                    self.message_text = file.read()
                self.user_type = 'text'