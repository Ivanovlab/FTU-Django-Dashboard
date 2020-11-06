echo "##########################################################################"
echo "#                                                                        #"
echo "#       File Name: installer                                             #"
echo "#       File Description: Installs and configures TestGUI                #"
echo "#                                                                        #"
echo "#       File History: 2020-11-5: Created by Rohit                        #"
echo "#                                                                        #"
echo "##########################################################################"
# ToDo: Check users Python version

# Make a directory called test, this is hidden by the .gitignore
echo "################   Creating directory 'test'  ############################"
mkdir test
echo "################   Created directory 'test'   ############################"

# Create a virtual environment in here
echo "#########     Creating virtual environment 'test/ftu'   ##################"
python3 -m venv test/ftu --clear
echo "#########     Created virtual environment 'test/ftu'    ##################"

# Enter the virtual directory
cd test/ftu

# Source venv
echo "##########      Activating virtual environment 'test/ftu'     ############"
source bin/activate
echo "##########      Activated virtual environment 'test/ftu       ############"

# Clone repo
echo "#############   Downloading code from github                 #############"
git clone https://github.com/RohitKochhar/FTU-Django-Dashboard.git
echo "#############   Code downloaded from github                  #############"

# Enter repo
cd FTU-Django-Dashboard

# Enter app
cd TestGUI/
echo "##############  Installing required Python packages          #############"

# Install django
pip install django

# Import Needed modules
pip install pandas
pip install matplotlib
echo "##############  Python packages installed                    #############"

# Perform migrations
echo "##############  Performing migrations                        #############"

python3 manage.py makemigrations DataCollection
python3 manage.py migrate
alias go='python3 test/ftu/FTU-Django-Dashboard/TestGUI/manage.py runserver'
echo "##########################################################################"
echo "                   Installation Complete!                                 "
echo "                                                                          "
echo "    Now, all you have to do is:                                           "
echo "      - cd test/ftu                                                       "
echo "      - source bin/activate                                               "
echo '      - cd FTU-Django-Dashboard/TestGUI                                   '
echo "      - python3 manage.py runserver                                       "
echo "                                                                          "
echo "##########################################################################"
