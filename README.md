# electricity-analytics


## Development setup

	pip install virtualenv
	virtualenv -p python3.9 env
	source ./env/bin/activate
  
## Install requirements
```
pip install -r requirements.txt
```

## Create .env file in the main project directory
 ```
In root directory create a file **.env** and write in it:

CONSUMER_KEY=' '
CONSUMER_SECRET=' '
ACCESS_TOKEN=' '
ACCESS_TOKEN_SECRET=' '

 ```

## Run Streamlit app
```
To run the Streamlit app:

streamlit run app.py

Running on: localhost:8501/

