# Cyberark
  
Module to connect to Cyberark and manage passwords 

*Read this in other languages: [English](README.md), [Portugues](README.pr.md), [Español](README.es.md).*

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Overview


1. Configure Cyberark credentials  
Configure credentials to connect to the Cyberark API.

2. Get all Safes  
Get all Safes from the CyberArk Vault

3. Get Safe  
Get information about a specific Safe in the Vault.

4. Add Safe  
Adds a new Safe to the Vault. The user must have Add Safes permissions in the Vault.

5. Update Safe  
Update a single Safe in the Vault from CyberArk

6. Delete Safe  
Delete Safe from the Vault

7. Get all Accounts  
Get a list of all the accounts in the Vault

8. Get Account  
Get information about an account identified by its ID

9. Add Account  
Add a new privileged account or SSH key to the Vault

10. Delete Account  
Delete an account from the Vault

11. Generate password  
Generate a new password for an existing account. The password is generated according to the password policy defined in the target system.

12. Get password value  
Retrieve the password or SSH key of an existing account that is identified by its Account ID.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**python-requests**](https://pypi.org/project/python-requests/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)