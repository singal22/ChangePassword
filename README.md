# Change Password
It is simple Python project to validate new password based on requirements

## Build project
### Clone Project
```bash
git clone https://github.com/singal22/ChangePassword.git
```

### Build docker image

```bash
cd ChangePassword
docker build -t <<username>>/changepassword .
```
Provide docker username

## OR
## Download docker image
```bash
docker pull singal22/changepassword
```

## Run ChangePassword project
Bind localhost:80 to the docker container 0.0.0.0/5000
```bash
docker run -p 80:5000 singal22/changepassword
```
Update username if build dockor image from your account

## Access GET API: 
URL: http://localhost:80/api/changepassword?old_password=<<value>>&new_password=<<value>>
#### It has two parameters:
  * old_password: Provide the old password of the system
  * new_password: Provide the new password
#### Example
  ```url
  http://localhost:80/api/changepassword?old_password=HomeAssignment123$&new_password=CricketAssignment123$
  ```
  
  
## Access POST API: 
URL: http://localhost:80/api/changepassword
#### JSON body request:
  * old_password: Provide the old password of the system
  * new_password: Provide the new password
#### Example:
  ```json
  {
	"old_password":"HomeAssignment123$",
	"new_password":"CricketAssignment123&"
  }
  ```
 ## Old password:
 ```
 HomeAssignment12345$
 ```
 ## Run Test Cases
 ### Mac OS Terminal
 To execute all test cases, execute below command:
 ```
 docker run  singal22/changepassword  /bin/sh -c  "pytest -v TestPassword.py"
 ```
 Update username if build dockor image from your account
