#Python 3.8.5
# Create a virtual environment
echo "##########################################################################"
echo "#       File Name: installer                                             #"
echo "#       File Description: Installs and configures TestGUI                #"
echo "#                                                                        #"
echo "#       File History: 2020-11-5: Created by Rohit                        #"
echo "#                                                                        #"
echo "##########################################################################"
python3 -m venv ftu
cd ftu

# Source venv
source bin/activate

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
