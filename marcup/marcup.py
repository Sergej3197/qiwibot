from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class user_marcup:
    def addinlineMarkup(self, row, **add_btn):
        inline_menu = InlineKeyboardMarkup(row_width=row)
        for callback_data, text_data in add_btn.items():
            callback = InlineKeyboardButton(text_data, callback_data = callback_data)
            self.add_mrkp = inline_menu.insert(callback)
        return(self.add_mrkp)
    def addinlineMarkup_Url(self, row, url, first_button, callback_data, second_button):
        inline_url = InlineKeyboardMarkup(row_width=row)
        callback_url = InlineKeyboardButton(first_button, url = url)
        callback_button  = InlineKeyboardButton(second_button, callback_data = callback_data)
        self.add_mrkp_url = inline_url.add(callback_url, callback_button)
        return(self.add_mrkp_url)
    def addinlineMarkup_usr(self, callback_data):
        inline_url = InlineKeyboardMarkup(row_width=2)
        callback_money_usr  = InlineKeyboardButton('Изменить баланс', callback_data = f"money{callback_data}")
        callback_block_usr = InlineKeyboardButton('Заблокировать', callback_data = f"block{callback_data}")
        self.add_mrkp_callback = inline_url.add(callback_money_usr, callback_block_usr)
        return(self.add_mrkp_callback)