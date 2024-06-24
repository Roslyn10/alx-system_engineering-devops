0x19-postmortem

Postmortem Report: Phishing Email Incident
Date of Incident: March 20, 2024
Date of Postmortem: March 22, 2024
Prepared by: Roslyn Lewis. 

Issue Summary
----------------
Overview: 
On March 20, 2024 at 09:00, an employee  received and opened a phishing email. The employee clicked on one of the links in the email and entered their login credentials on a fake login page, thereby compromising their  login credentials. The attackers then used their details to log into their account on the same day at 06:00 PM and sent malicious emails to other  employees . Lesson learned: phishing emails are like digital mosquitoes – annoying, sneaky and sometimes they bite. 


Timeline
-----------

March 20, 2024, 09:00 AM: Employee receives and opens phishing email. 
March 20,2024, 09:05 AM: Employee enters credentials on a fake login page. (Classic ase of “The Mondays”)
March 20, 2024, 09:05 AM - 17:59 PM: No unusual activity detected; everything appeared normal. 
March 20, 2024, 06:00 PM: Malicious emails sent from the compromised email to other employees
March 21, 2024, 07:00 AM: Two more employees opened the phishing email, thankfully they did not click on the links sent
March 21, 2024, 07:05 AM: IT Security detects unusual activity from the compromised accounts. 
March 21, 2024, 0710 AM: IT Security alerts the IT department about the suspicious activity. 
March 21, 2024, 07:15 AM: IT Security begins monitoring the compromised accounts for further malicious activity. 
March 21, 2024, 08:00 AM: Affected employees are contacted to verify if they noticed any unusual activity. 
March 21, 2024, 08:30 AM: IT Security team prepares to deactivate the compromised accounts and reset passwords. 
March 21, 2024, 09:30 AM: Compromised account is deactivated and passwords are reset.
March 21, 2024, 10:00 AM: IT Security sends a follow-up communication to all employees with guidelines on identifying phishing emails and reporting suspicious activity. 
March 21, 2024, 11:00 AM:  Initial investigation results are reviewed by IT Security to determine the scope of the breach.
March 21, 2024, 02:00 PM: IT Security starts a comprehensive security audit to check for any further compromises. 
March 21-22, 2024: Comprehensive security audit conducted, focusing on email security, network activity, and employee awareness.
March 22, 2024, 09:00 AM: Incident response team begins a detailed investigation to analyse the phishing attack’s root cause and potential improvements to prevent future incidents. 
March 22, 2024, 01:00 PM: IT Security implements immediate improvements to email filtering rules to block similar phishing attempts.
March 22, 2024, 03:00 PM: Follow-up training session scheduled for all employees on recognizing and responding to phishing attempts. 

Root Cause
-----------

Sophisticated Phishing Techniques: The phishing email employed advanced social engineering tactics and spoofed sender details to appear legitimate. It bypassed existing email filters and security measures, making it difficult to detect. (Props to the cybercriminals for their creativity in crafting convincing phishing emails.)
Lack of Phishing Awareness and Training: The employee who initially fell victim to the phishing email was not adequately trained to recognize common phishing red flags, such as suspicious URLs, grammar errors, or unusual sender addresses. Due to this lack of awareness, they inadvertently disclosed their login credentials on a fake login page.
Insufficient Email Security Measures: While the organisation had basic email security protocols in place, they were not robust enough to detect and block sophisticated phishing attempts. This gap allowed the phishing email to reach multiple employees, increasing the risk of further compromise.



Resolution and Recovery
-------------------------

Enhance email security: Review and upgrade email security to detect phishing attempts. (Time to build a stronger firewall) 
Employee training: Implement mandatory phishing awareness training for all employees.
Incident Communication Protocol: Develop a clear protocol for quick communication and response to security incidents. 


Corrective and preventative Measures
--------------------------------------

Proactive security measures: Regularly update and test email security systems to stay ahead of sophisticated phishing techniques. (We’re building a bug zapper for emails) 
Continuous training: Provide ongoing education and training to maintain employee awareness and vigilance against phishing. (How to spot scam: 101)
Improve communication: Ensure effective and timely communication to facilitate prompt incident response. 


Lessons Learned
---------------

Thorough Testing and Monitoring: Regularly update and test security systems to detect advanced threats. 
Importance of Training: Continuous training is crucial for maintaining high levels of employee awareness.
Effective Communication: Prompt and clear communication is essential for efficient incident response and mitigation. 
