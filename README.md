# ScanMasterX

A GUI application that uses nmap, National Vulnerability Database, and PyQt6 and a custom pen-testing class to check default credentials. 

The source code for this is located under the src file.

A docker-compose orchestration with instructions for a testing environment is under Eric section called Test_Environment.zip

## Usage

Please download the neccesary files with the pipfile folder.

Once everything is successfull installed

Run `sudo python3 main.py` in the src folder.

Please notate this is for mac. If on Windows please run as administrator.

## Testing

We were unable to get the docker orchestration to work and write test to run with this. 

## File Structure

Other than src each file structure holds work for assignments that may or may not be completed. This was used as a file sharing system to colloborate on power points and other deliverable items

## Gui  

Usage of the gui takes you to three windows.

You must first scan a subnet in order to populate the graph.  
Under the IP scan tab type in the ip and the subnet mask and click scan.  

*  This will do a ping sweep of the subnet
*  Next click on port scan and either choose a drop down ip or type in an ip and port ranges
  * If something is typed in the port scan window it will default to that.

Next you can click on the network topology tab.

* Click on any node and it will evaluate the machine
* Refresh the page by clicking on and off to fix the color rating and logo.
  
### Contributors

Eric Leachman   
Will Reese  
Alexa Darrington  
Dennis Vinnikov  
Lewis Thomas

### Environment Setup (Recommended)

1. Ensure python 3.9+ is installed and install pipenv. Ex. py -m pip install pipenv
2. Clone this repository, navigate to the src folder and create a new developer virtual environment. Ex. pipenv install --dev
    1. If the above step fails, ensure that your python binary is set as an environment variable in your PATH, for more info see: https://realpython.com/add-python-to-path/
3. Reload your IDE or text editor and ensure that your virtual environment is set.
    1. For example, in VS Code see: https://code.visualstudio.com/docs/python/environments for more information on how to set your environment.
    2. For help with other IDEs and text editors, look up how to set your virtual environment on your search engine of choice.
    3. Alternatively, run the command "pipenv shell" and then run main.py through terminal as you would regularly. Ex. python ./main.py
4. If any alternative issues are encountered, feel free to reach out at wreese1@ewu.edu for help troubleshooting.
