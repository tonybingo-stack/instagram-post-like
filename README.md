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
pip install pyinstaller
pyinstaller --onefile main.py 
```

Edit run.bat file with your instagram credentials and the number of posts you want to like.
```python
main.exe <your-username> <your-password> <number-of-post-to-like>    
```
Double-click the run.bat file to like the post

## On Mac
you should using python3, pip3 instead of python, pip in every command

```python
pip3 install -r requirements.txt
python3 main.py <your-username> <your-password> <number-of-post-to-like>  
pip3 install pyinstaller
python3 -m PyInstaller main.py
```

make run.command file with following content

```python
cd "$(dirname "$0")"
./main username password 10
```
Double-click the run.command file to like the post
