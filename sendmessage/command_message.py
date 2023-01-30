from marcup.marcup import user_marcup
from bd.bd import Database

bd = Database()
add_mrkp =user_marcup()

class user_command():
    def __call__(self, user_name, user_text, user_id):
        self.message_text = ''
        self.marcup = ''
        self.user_type = ''
        if not bd.user_exists(user_id):
            bd.add_user_id(user_id)
        if not bd.get_block_user(user_id):
            if user_text == '/start':
                self.message_text = f'Привет {user_name}\nЯ - бот для пополнения баланса.\nНажмите на кнопку, чтобы пополнить баланс'
                self.marcup = add_mrkp.addinlineMarkup(2, add_balans= '💰Пополнить баланс')
                self.user_type = 'text'
            elif user_text == '/admin':
                self.marcup = add_mrkp.addinlineMarkup(2, uploading_users= 'Пользователи', uploading_log= 'Логи')
                self.message_text = 'Смотрите и редактируйте пользователей или Смотрите логи'
                self.user_type = 'text'