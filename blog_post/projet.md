## The following document was used as a brouillon all along the project.

First: Open CMD
Second: start running commands:
1.	cd regression-model
2.	.\venv\scripts\activate
3.	pip install -r requirements.txt
4.	jupyter notebook
After writing jupyter notebook, chrome is going to open a new tab automatically, I click on:
insurance_charges_model then training then data_exploration.ipynb
Then, I start selecting each cell and clicking RUN to execute the code. 

Dans model_validation il faut remplacer le path du model.joblib par :
model_path = r"C:\Users\ralph\regression-model\insurance_charges_model\model_files\1\model.joblib"
model = joblib.load(model_path)

Then use uvicorn rest_model_service.main:app --reload of uvicorn rest_model_service.main:app \--reload

Then go to http://127.0.0.1:8000/ and the page below will appear in chrome.
 ![Alt Text](proof.jpg.jpg)


Then I need to double click on Docker Desktop
After that I will modify the service_requirements file to the following:
anyio==3.5.0
asgiref==3.5.0
certifi==2021.10.8
charset-normalizer==2.0.12
click==8.0.4
cloudpickle==2.0.0
dask[dataframe]==2022.2.0
deap==1.3.1
distributed==2022.2.0
fastapi==0.74.1
featuretools==0.24.0
fsspec==2022.2.0
h11==0.13.0
heapdict==1.0.1
idna==3.3
jinja2==3.0.3
joblib==1.1.0
markupsafe==2.1.0
ml-base==0.2.0
msgpack==1.0.3
numpy==1.19.4
packaging==21.3
pandas==1.3.3  # Specify a compatible version for Python 3.8
partd==1.2.0
psutil==5.9.0
pydantic==1.9.0
pyparsing==3.0.7
python-dateutil==2.8.2
pytz==2021.3
pyyaml==6.0
requests==2.27.1
rest-model-service==0.2.0
scikit-learn==0.24.2
scipy==1.7.3
six==1.16.0
sniffio==1.2.0
sortedcontainers==2.4.0
starlette==0.17.1
stopit==1.1.2
tblib==1.7.0
threadpoolctl==3.1.0
toolz==0.11.2
tornado==6.1
tpot==0.11.7
tqdm==4.62.3
typing-extensions==4.1.1
update-checker==0.18.0
urllib3==1.26.8
uvicorn==0.17.5
xgboost==1.5.2
zict==2.0.0




Then I run: docker image ls

Then I run: docker run -d -p 80:80 insurance_charges_model:0.1.0

Then I run the following command:
Invoke-RestMethod -Uri 'http://127.0.0.1:8000/api/models/insurance_charges_model/prediction' -Method Post -Headers @{
  'accept' = 'application/json'
  'Content-Type' = 'application/json'
} -Body '{
  "age": 65,
  "sex": "male",
  "bmi": 50,
  "children": 5,
  "smoker": true,
  "region": "southwest"
}'
(proof of the charges, which means project is working)
 


I can run this command to see the logs for docker: docker logs $(docker ps -lq)

I can then run this command to stop the docker container: docker kill $(docker ps -lq)

Then I have to install kubect1 and then I have to install Kind
Then I add the path of Kind to environment variables
Then I go the the directory of kind through powershell
Then I execute the following command to create a new cluster: .\kind.exe create cluster --name my-k8s-cluster

Then I execute the following command: kubectl cluster-info --context kind-my-k8s-cluster 
so I can interact with the new cluster I created.

Then I run kubectl create deployment projetai --image=your-image in vs

I run the following 2 commands:
docker build -t my-fastapi-app .
docker run -p 8000:8000 my-fastapi-app

The app is going to open locally on http://localhost:8000/docs







I can then test the model using this command that will give me the prediction:
Invoke-RestMethod -Uri 'http://127.0.0.1:8000/api/models/insurance_charges_model/prediction' -Method Post -Headers @{
  'accept' = 'application/json'
  'Content-Type' = 'application/json'
} -Body '{
  "age": 65,
  "sex": "male",
  "bmi": 50,
  "children": 5,
  "smoker": true,
  "region": "southwest"
}'
 
![Alt Text](blog_post\proof2.jpg)





