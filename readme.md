# The NCTU Software Engineering project!
### Usage
step1. Install python3.7, pip3.
```bash
sudo apt install python3.7, python3-pip
```
step2. Use pip3 to download pipenv
```bash
pip3 install pipenv
```
step3. Add PATH for pipenv
```bash
# find out where is your pipenv.
# In my case:
export PATH="$PATH:$HOME/.local/bin"
``` 
step4. Cd into your project root
```bash
pipenv update
pipenv shell
```

# To RUN
```bash
# In your project root
pipenv shell # if you are not in the virtual environment 
cd ecommerce
python manage.py runserver
```

# PayPal Sandbox Accounts

Sandbox website: 
https://www.sandbox.paypal.com/signin

Business:
sb-xadzg24911@business.example.com

Personal:
sb-xvzgt12100@personal.example.com

Both passward are:
12345678

If you want to test the PayPal IPN, you need to use [ngrok](https://ngrok.com/). And [change the Business IPN address](https://developer.paypal.com/docs/classic/ipn/integration-guide/IPNSetup/#setting-up-ipn-notifications-on-paypal).
Example Address: http://*.ngrok.io/paypal

---
Paypal Reference:
https://overiq.com/django-paypal-integration-with-django-paypal/
