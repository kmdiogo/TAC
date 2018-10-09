# TAC
This repository contains all the source code for the TAC tutor management software.

### INSTRUCTIONS FOR PUSHING CHANGES
* First and foremost, please make sure your code is extensively tested and organized as best as possible (see next section for coding standards)
* ***DO NOT PUSH YOUR VIRTUAL PYTHON ENVIRONMENT TO MASTER.*** In your project, your virtual environment is under the folder titled 'venv'. It contains thousands of files and will slow down the repo immensely. When pushing changes, ensure the changelist DOES NOT include the folder 'venv' or any of its files. (See the section titled 'SETTING UP THE PROJECT' on instructions for setting up your own venv)
* Always make sure to add a commit message. This will be extremely helpful later on when tracking the group member contributions

### CODING STANDARDS
These are some general coding standards we should all try to adhere to to maintain consistency across the software.
##### HTML/CSS
* HTML id/class names should be separated with dashes
```HTML
<div class = "example-class-name" id = "example-div"></div>
```
* CSS rules that can be applicable to more than page must be included in the site.css file under the static directory
* CSS rules specific to a page must be placed inline in the header section of the HTML file. This is subject to change as the project scales
```HTML
<head>
  <style>
    body {
      color: green;
    }
  </style>
</head>
```
#### Javascript
* Javascript must be placed at the end of body tag, after all other HTML
* For now, just write the javascript inline with the HTML file, this is also subject to change
* Variable names must be named with lowerCamelCase
```Javascript
let myAge = 5;
let myName = 'John Doe';
```
* Function names must use uppercase camel case
```Javascript
function AddTwoNumbers(a,b){
  return a + b;
}
```

#### Python
The coding style for Python largely adheres to PEP-8 standards, but there are some exceptions. Here are the main things to know:
* Variable names are still lowerCamelCase
```Python
myAge = 5
myName = "John Doe"
```
* Function names are lowercase separated with underscores
```Python
def add_two_numbers(a,b):
  return a+b
```
* Class names are UpperCamelCase
```Python
class MyExampleClass:
  def __init__(self):
    pass
```

### SETTING UP THE PROJECT
0. Download and install Python 3.7 if not installed on your machine already
These next steps apply if you are using PyCharm.
1. Open up PyCharm and ensure you are on the create a new project window. Create a project by pulling from from versional control, and use the repo URL https://github.com/kmdiogo/TAC to download the project files
2. Once the Project is pulled and the project opens, go to File > Settings, then in the pop-up window, find the Python Interpreter tab. In this section, create a new Python Virtual Environment using Python 3.7 as the base interpreter.
3. Let PyCharm finish loading and creating the virtual environment
4. Open the 'requirements.txt' file by double-clicking the file in the folder view. Once it opens, PyCharm should detect you are missing dependencies, click 'Install Requirements' to install all necessary packages.
5. Once that is finished, click on the 'Add Configuration' button near the top right of PyCharm. In this pop-up window, click the plus to add a new configuration, then select Django. For project title, put 'TAC'. Click apply then confirm
6. PyCharm should notify that you are missing packages from requirements.txt, click the install missing packages button and your project should be good to go!


### Resources
As always, refer to documentation first before asking for help. Below are some useful resources.
[Django 2.1 Documenation](https://docs.djangoproject.com/en/2.1/)
[Bootstrap 4.1 Documenation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
[JQuery API Documenation](https://api.jquery.com/)
