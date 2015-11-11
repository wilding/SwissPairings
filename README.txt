 to create database:
 1. Install Vagrant and Virtualbox if not previously installed
 2. navigate to fullstack/vagrant/ folder in the terminal
 3. type 'vagrant up' and 'vagrant ssh' into terminal to enter VM
 4. navigate to folder /vagrant/tournament/ in the terminal
 5. run psql by typing 'psql'
 6. type '\i tournament.sql' to build and connect to database.

 to run tournament.py and tournament_test.py:
 6. exit psql by typing '\q'
 7. run python scripts by typing 'python tournament.py' or 'python tournament_test.py'