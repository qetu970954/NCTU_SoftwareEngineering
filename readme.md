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