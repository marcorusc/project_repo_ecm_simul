### Run in Binder : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcorusc/project_repo_ecm_simul/master?filepath=project_repo_ecm_simul.ipynb)

### Run locally with Docker and Docker-compose
```
docker-compose up -d
```
	
And then open your browser to this url : http://localhost:8888/notebooks/project_repo_ecm_simul.ipynb

### Run locally with Docker
```
docker build -t ecm_simul .
docker run -p 8888:8888 -d ecm_simul
```	

And then open your browser to this url : http://localhost:8888/notebooks/project_repo_ecm_simul.ipynb