# Weblinter

## Setting up — Dev

Create a virtual environment with `python3 -m venv venv`, then source it with `source venv/bin/activate`.

Run `pip install -r requirements.txt` to install the required dependencies.

Code :wink:

## Running the script

Run `./main.py [urls]` or `python3 main.py [urls]` with at least one URL and let the script run.

Example: 
```sh
$ ./main.py https://nook.sh https://google.com

> 2019-01-21 22:08:26 [https://nook.sh] Response time : 23.51 ms
> 2019-01-21 22:08:26 [https://google.com] Response time : 18.056 ms
```