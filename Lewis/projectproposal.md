The core of our solution lies in a GUI (Graphical User Interface) designed to abstract the intricacies of network testing and computer security. This interface serves as the gateway for users to interact with the program seamlessly. By incorporating user-friendly elements such as dropdown menus and comprehensive prompts, we aim to make the testing process intuitive and accessible.  

The initial phase of the flow involves utilizing established frameworks like nmap to map out the network topology. This step is crucial in understanding the network structure and identifying potential entry points for attackers. The GUI facilitates this mapping process, providing visual representations of the network layout in a graph format for easier comprehension.  

Once the network topology is established, our solution delves into comprehensive network assessment. We will employ techniques to identify open ports and conduct fingerprinting to gather detailed information about these ports. Leveraging the National Institute of Standards and Technology (NIST) database, we will correlate port vulnerabilities and overlay heat maps on the network topology. This visualization aids in highlighting vulnerable areas and prioritizing security measures.


Furthermore, our plan is to integrate the data with the MITRE framework to contextualize vulnerabilities and map them to potential stages in an attack. This analysis should provide actionable insights into the likelihood and severity of potential breaches, allowing organization and developers to harden their systems and proactively prevent cyber threats.   

Moving beyond assessment, our plan is to to use exploitation frameworks such as Metasploit to actively test the system. We will use the previous reconnaissance methodologies to identify pre-defined vulnerabilities and match them based on a curated list. This last step will emphasize how vulnerable their system is.   

In addition, our plan is to include robust password cracking capabilities. We will offer interfaces for dictionary attacks and hybrid attacks, enabling organizations to test the strength of their passwords. By measuring the cracking speeds we can provid detailed reports. These reports will spotlight weaknesses caused by developers and users accessing their systems.    

The nature of our solution is that of a standalone program, designed to be run locally for efficient network access and testing. The software components encompass various virtual machines to create proof-of-concept topologies and possibly a database for storing critical information. While the database plays a supporting role, the primary focus remains on the functionality and features that enhance security assessment and testing capabilities.

On the hardware front, each team member requires a laptop equipped with an x86 chip to run virtual machines effectively. Alternatively, cloud-based virtual machines can be leveraged, with interaction facilitated through Command Line Interface (CLI) for seamless integration and testing. As alot of the software and vulnerable machines we will be testing are only able to be ran on an x86 chip.   
