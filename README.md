# Instagram Post Like Bot

Like post in threads.net. Work with Python 3.7.2 and Selenium.

## How to install
Install neccessary dependencies by running 
```python
pip install -r requirements.txt
python main.py <your-username> <your-password> <number-of-post-to-like>
```


## How to run
make an exe file by running below code
```python
pyinstaller --onefile main.py 
```

Edit run.bat file with your instagram credentials and the number of posts you want to like.
```python
main.exe <your-username> <your-password> <number-of-post-to-like>    
```
Double-click the run.bat file to like the post
