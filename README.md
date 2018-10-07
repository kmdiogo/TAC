# TAC
This repository contains all the source code for the TAC tutor management software.

### INSTRUCTIONS FOR PUSHING CHANGES
* First and foremost, please make sure your code is extensively tested and organized as best as possible (see next section for coding standards)
* DO NOT PUSH YOUR VIRTUAL PYTHON ENVIRONMENT TO MASTER. In your project, your virtual environment is under the folder titled 'venv'. It contains thousands of files and will slow down the repo immensely. When pushing changes, ensure the changelist DOES NOT include the folder 'venv' or any of its files. (See the section titled 'setting up the project' on instructions for setting up your own venv)
* Always make sure to add a commit message. This will be extremely helpful later on when tracking the group member contributions

### CODING STANDARDS
These are some general coding standards we should all try to adhere to to maintain consistency across the software.
1. HTML id/class names should be separated with dashes. Example:
```HTML
<div class = 'example-class-name' id = 'example-div'></div>
```
