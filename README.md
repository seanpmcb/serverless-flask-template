# serverless-flask-template

Template for a basic flask app deployed to AWS using the Serverless framework

## Prerequisites
The following need to be installed on your system. Codeblocks are here purely for selfish reasons, given my setup. However, there are some links, so you can install to whatever best fits your setup.

* [Poetry](https://python-poetry.org/docs/#installation) installed
  ```
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
  ```
  
* Python3.8 installed
  ```
  yay -S python38
  ```

* [Node.js](https://nodejs.org/) installed 
  ```
  sudo pacman -S nodejs
  ```
  
* [Serverless](https://www.serverless.com/) installed 
  ```
  npm install -g serverless
  ```
   
## How to stand up and deploy a server
```
poetry env use python3.8
poetry install
serverless plugin install -n serverless-wsgi
serverless plugin install -n serverless-python-requirements
sls login
sls wsgi serve
sls deploy

```