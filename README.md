# ScanMasterX

A GUI application that uses nmap, National Vulnerability Database, and PyQt6 and a custom pen-testing class to check default credentials. 

The source code for this is located under the src file.

A docker-compose orchestration with instructions for a testing environment is under Eric section called Test_Environment.zip

## Usage

Please download the neccesary files with the pipfile folder.

Once everything is successfull installed

Run `sudo python3 main.py` in the src folder.

Please notate this is for mac. If on Windows please run as administrator.

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


