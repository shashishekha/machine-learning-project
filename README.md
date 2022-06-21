# machine-learning-project
This is a machine learning project

creating conda environment
```
conda create -p venv python==3.7 -y

```
conda init <shell>

```
conda activate venv
```
pip install -r requirements.txt
```

To check remote url
```
git remote -v
```
To setup CI/CD pipeline in heroku we need 3 information


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

>Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>

```
python setup.py install




