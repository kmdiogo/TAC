# TAC
This repository contains all the source code for the TAC tutor management software.

### Table of Contents
[Pushing Changes](#INSTRUCTIONS_FOR_PUSHING_CHANGES)  
[Coding Standards](#heading-1)  
[Setting Up the Project](#heading-2)  
[Resources](#heading-3)  

## Heading
## INSTRUCTIONS FOR PUSHING CHANGES
* First and foremost, please make sure your code is extensively tested and organized as best as possible (see next section for coding standards)
* ***DO NOT PUSH YOUR VIRTUAL PYTHON ENVIRONMENT TO MASTER.*** In your project, your virtual environment is under the folder titled 'venv'. It contains thousands of files and will clutter the repo immensely. When pushing changes, ensure the changelist DOES NOT include the folder 'venv' or any of its files. (See the section titled 'SETTING UP THE PROJECT' on instructions for setting up your own venv)
* Always make sure to add a commit message. This will be extremely helpful later on when tracking the group member contributions
## Heading
## CODING STANDARDS
These are some general coding standards we should all try to adhere to to maintain consistency across the software.
### HTML/CSS
* HTML class names should be lowercase and separated with dashes
```HTML
<div class = "example-class-name"></div>
```
* When giving HTML elements id's, refer to the following sequence of rules. For each rule, separate the id with a dash
  - if the element tag is one of the following: 
    {\<h1\> - \<h6\>, \<p\>, \<button\>, \<input\>}
    start the id with the respective tag name
  - if the element belongs to a specific sub-html section, add it. The section must use upper camel case (ex. StudentSection)
  - provide a descriptive and appropriate lengthed name for what the element does. This must use lower camel case (ex. errorMessage)
  Consider the following examples:
  
  #### Example 1:
  ```HTML
    <div id="StudentSection-errorMessage">
      <h1>AN ERROR OCCURED</h1>
      <p>Please contact an administrator</p>
    </div>
  ```
  The id 'StudentSection-errorMessage' lets us know that the element tag is not a header, \<p\>, \<button\>, or \<input\> (usually this means the   id belongs to a div or container element) and that it belongs to the StudentSection sub-html file.
  
  #### Example 2:
  ```HTML
    <button id="button-EmployeeSection-submitClockIn">Submit</button>
  ```
  The id 'button-EmployeeSection-submitClockIn' id tells us the element is a button in the EmployeeSection sub-html file that is used     to submit something relating to ClockingIn (more specifically, since it is located in the EmployeeSection, it is probably used to       submit employee clock-in requests)
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
### Javascript
* Javascript must be placed at the end of body tag, after all other HTML
```HTML
<body>
  <p>This</p>
  <p>Is</p>
  <p>My HTML</p>
  ...
  ...
  ...
  <script id='example-javascript'>
    console.log("Hello World");
  </script>
</body>
```
* For now, just write the javascript inline with the HTML file, this is also subject to change
* Variable names must be named with lowerCamelCase
```Javascript
let myAge = 5;
let myName = 'John Doe';
```
* Function names must use UpperCamelCase
```Javascript
function AddTwoNumbers(a,b){
  return a + b;
}
```

### Python
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
## Heading
## SETTING UP THE PROJECT
0. Download and install Python 3.7 (3.6 is also fine if on Linux) if not installed on your machine already. These next steps apply only if you are using PyCharm.
1. Open up PyCharm and ensure you are on the create a new project window. Create a project by pulling from versional control, and use the repo URL https://github.com/kmdiogo/TAC to download the project files
2. Once the Project is pulled and the project opens, go to File > Settings; then in the pop-up window, find the Python Interpreter tab. In this section, create a new Python Virtual Environment using Python 3.7 as the base interpreter.
3. Let PyCharm finish loading and creating the virtual environment
4. Open the 'requirements.txt' file by double-clicking the file in the folder view. Once it opens, PyCharm should detect you are missing dependencies, click 'Install Requirements' to install all necessary packages.
5. Once that is finished, click on the 'Add Configuration' button near the top right of PyCharm. In this pop-up window, click the plus to add a new configuration, then select Django. For project title, put 'TAC'. Leave the rest of the fields. Click apply then confirm.
6. You are now ready to start developing. Happy Coding!

## Heading
## Resources
As always, refer to documentation first before asking for help. Below are some useful resources.
* [Django 2.1 Documenation](https://docs.djangoproject.com/en/2.1/)
* [Bootstrap 4.1 Documenation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
* [JQuery API Documenation](https://api.jquery.com/)
