As an Information Security Lead  
I need to test the orgnaization's passwords    
So that I can identify Attack Vectors  

Assumptions and Details  

* We have access to everyone password hash  
* We are testing again common word list  

Acceptance Critieria:   
Given there are 100 employees in Active Directory  
And Security Operations have agreed to give us access    
When I request passwords  
Then I should receive a 100 hashes  


As an Information Security Analyst  
I need to identify an hash  
So that I can send it to the password cracking team    

Assumptions and Details    

* The hashes will be commonly identifiable hashes  

Acceptance Criteria:
Given a password hash   
And password is hashed with a approved hash    
When I receive the password  
Then I should output the type 

As a developer  
I need to identify my vulnerable machines  
So that I can prevent remote access  

Assumptions and Details  
* I will only be able to exploit known exploits  
* It will either pass or fail  

Acceptance Criteria:  
Given a virtual machine  
And virtual machine is on the same network  
When I test the machine  
Then I should either be given access or fail  


