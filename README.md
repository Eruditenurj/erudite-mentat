## Erudite
### Mentat
#### Find NSF funded undergraduate research opportunities tailored to your experience

### Setup
1. Clone the repository
`git clone https://github.com/Eruditenurj/mentat.git`
2. Setup virtual environment (install necessary packages)
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Now anytime you work on the project be sure to load up the environment
`source env/bin/activate`
3. Run the server
  1. Go to the mentat directory
  `cd mentat`
  2. Set the Flask variable
  `export FLASK_APP=main`
  3. Run Flask
  `flask run`
4. Go to http://127.0.0.1:5000 in your browser
