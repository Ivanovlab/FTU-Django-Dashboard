#Python 3.8.5
# Create a virtual environment
python3 -m venv ftu

# Source venv
source ftu/bin/activate

# Clone repo
git clone https://github.com/RohitKochhar/FTU-Django-Dashboard.git

# Enter repo
cd FTU-Django-Dashboard

# Enter app
cd TestGUI/

# Install django
pip3 install django

# Import Needed modules
pip3 install pandas
pip3 install matplotlib

# Perform migrations
python3 manage.py makemigrations DataCollection
python3 manage.py migrate
