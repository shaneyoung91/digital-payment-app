# MoneySpread - A Digital Payment Application

- Leveraged Python, Django, and PostgreSQL to build a feature-rich digital payments application, similar to Venmo, CashApp, and Zelle.

- Demonstrated knowledge of Django by creating dynamic views and managing complex data models for seamless application functionality.

- Ensured a seamless user experience by integrating essential banking features, such as account management, fund transfers, and transaction history.

## Link to App :link:
[MoneySpread](https://moneyspread-259abb181ed5.herokuapp.com/)

---

## User Dashboard 
![dashboard](static/images/dashboard.png)

---

## Account Detail 
![account-detail](static/images/account-detail.png)

---

## Credit Card Details 
![dashboard](static/images/cc-detail.png)

---

## Deposits Funds to Card
![dashboard](static/images/deposit-funds.png)

---

## Withdraw Funds from Card
![dashboard](static/images/withdraw-funds.png)

---

## Request Payment from Users
![request-payment](static/images/request-payment.png)

---

## Confirm Payment
![confirm-payment](static/images/confirm-payment.png)

---

## Transactions
![transactions](static/images/transactions.png)

---

## Transaction Detail
![transaction-detail](static/images/transaction-detail.png)

---

## Code Preview
```python
class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_id = ShortUUIDField(unique=True, length=5, max_length=20, prefix="CARD", alphabet="1234567890")
    
    name = models.CharField(max_length=100)
    card_number = models.PositiveBigIntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()
    
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    card_type = models.CharField(choices=CARD_TYPE, max_length=50, default="Mastercard")
    card_status = models.BooleanField(default=True)
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"
```
---
## Technologies Used
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
 ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
 <br>
 ![JavaScript Badge](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
 ![CSS Badge](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
 ![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
 <br>
 ![Heroku Badge](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

---
## Future Enhancements
   - [ ] Search bar feature on dashboard to find user accounts
   - [ ] Notification system when requests/transfers are made and their status updates
   - [ ] Exchange rate feature for other currencies
   - [ ] Updated dashboard featuring recent transactions
---
