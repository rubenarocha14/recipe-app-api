Overview:
	- Create an advanced RESTAPI project with Python, Django REST framework and Docker using TDD
		○ Set up a local development server with Docker
		○ Build REST API with advanced features such as loading and viewing images
		○ Hands on applying best principles such as PEP-8 and unit tests
		○ Writing a Python project using Test Driven Development
		○ Creating a backend to be used as a base for future projects
		○ Configure Travis-CI to automate code checks
	
	
	
	Technologies Overview
		- Language: Python
		- Web Framework: Django
			§ APIs: Django REST
		- Database: PostgreSQL
		- Containers:Docker
		- API Documentation: Swagger.ui
		- Version Control: Git
		- Automation: Github
		
		
	
	Docker
		- Why?
			§ Establishes a consistent dev and prod environment
			§ Easier Collaboration - Establishes dependencies in the container, not on machine
			§ Captures all dependencies as code
				□ Add all requirements
				□ Add all Op Sys dependencies
			§ Easier cleanup -  Contains all program versions, SDK versions etc in the container and prevents us from having to remove them from our machine and constantly be updating our machine system versions
		- How?
			§ Define a dockerfile
				□ Defines all OS level dependencies for the project
			§ Docker Compose config
				□ Tells docker how to run the images that are created from the Dockerfile
Run all commands via docker compose