from pyqiwip2p import QiwiP2P

class qiwi_aio:
    def __init__(self):
        self.QIWI_PRIV_KEY = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6ImJxbDBkMS0wMCIsInVzZXJfaWQiOiI3OTc3OTk2NjA0MSIsInNlY3JldCI6ImIxMmZhOTY1MmM3NGVlZTMwZmNiNTgwNjYzMTA3Y2FhYzYyYzRiZDdiM2JhYzNlNTJiNWNmYmY5YjRhMWRjN2UifX0="       
        self.p2p = QiwiP2P(auth_key=self.QIWI_PRIV_KEY)
    def send_bill(self, bill_id, amount):
        new_bill = self.p2p.bill(bill_id=bill_id, amount=amount, lifetime=5)
        self.bill_id = new_bill.bill_id
        self.pay_url = new_bill.pay_url
    def check(self,bill_id):
        return(self.p2p.check(bill_id).status)