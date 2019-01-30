# Weblinter

## Setting up — Dev

Create a virtual environment with `python3 -m venv venv`, then source it with `source venv/bin/activate`.

Run `pip install -r requirements.txt` to install the required dependencies.

Code :wink:

## Running the script

Install the required dependencies with `pip install -r requirements.txt` or get into the venv, then run the script as follows.

Run `./main.py [urls]` or `python3 main.py [urls]` with at least one URL and let the script run.

Example: 
```sh
$ ./main.py https://nook.sh https://google.com

> 2019-01-21 22:08:26 [https://nook.sh] Response time : 23.51 ms
> 2019-01-21 22:08:26 [https://google.com] Response time : 18.056 ms
```

When running the script with no flag, all the tests will be run. If you want to run only a bunch of specific tests, add the flags when you run the script.
You can have the list of available tests by running the script with the `-h` or `--help` flag.

```sh
$ ./main.py https://google.com https://leetchi.com --img-alt --response-time
> 2019-01-30 17:41:19 [https://google.com] Response time : 43.71 ms
> 2019-01-30 17:41:19 [https://leetchi.com] Response time : 34.98 ms
> 2019-01-30 17:41:23 [https://leetchi.com] "alt" cannot be empty <img alt="" class="trustpilot-map map" src="https://asset.leetchi.com/Content/Longane/dist/img/view/homepage/trustpilot/trustpilot-map.png?v=cb13165b51b843bebde585f3d57d3a12"/>
```