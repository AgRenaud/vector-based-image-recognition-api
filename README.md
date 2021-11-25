# Vector Based Image recognition API
[![test](https://github.com/AgRenaud/vector-based-image-recognition-api/actions/workflows/run-tests.yaml/badge.svg?branch=master)](https://github.com/AgRenaud/vector-based-image-recognition-api/actions/workflows/run-tests.yaml)
<p align="middle">
  <img src="./docs/images/tf-logo.png" width="15%" />
  <img src="./docs/images/poetry-logo.svg" width="6%" />
  <img src="./docs/images/fastapi-logo.png" width="18%" />
  <img src="./docs/images/docker-logo.png" width="18%" />
  <img src="./docs/images/qdrant-logo.png" width="18%" />
</p>

The project show a simple solution to expose through an API a system for image recognition using a features extractor (tensorflow neural network deployed with `tensorflow-serving`) and a vector similarity search engine `qdrant`.

## Getting Started
You can start to explore the project by taking a look to the `notebooks/` folder where you'll find several `.ipynb` files containing all you need to train a model for image recognition tasks. You'll also find an implementation of  `ArcFace` for `tensorflow`.

The project is divided into three main parts: services, scripts and notebooks.

The services are composed of :
- api : main app.
- qdrant : Vector based search engine.
- tensorflow-serving : api which expose tensorflow model.

The notebooks are composed of:
- A notebook to create a model `train_model_arcface.ipynb`

The scripts allows the following actions:
- Initialize the qdrant search engine
- Clean the qdrant search engine


## Start the application

### Run the application with Docker
```
docker-compose up
```

The configuration file for the application are describe in `app/default_config.yaml`.


### Feed search engine
Run jupyter and train a model with `notebooks/train_model.ipynb`. The notebook will train a model, save it in  `storage/models` and create points to feed the search engine and save them in `storage/collections_resources`.

Then go in the `scripts/` and run `create_collection.sh`. (Make sure the apis are up `docker-compose up`)
```bash
cd scripts

./create_collection.sh http://localhost:6333 CharactersVectors <path-to-project>/collections_resources Cosine 256

# ./create_collection.sh <qdrant-url> <collection-name> <path-to-points-folder> <distance> <vector-size>
```
You can take a look at [Qdrant Documentation](https://qdrant.tech/documentation/) to understand how to create a `Collection` and feed it with `Point`.


### Make your first call

```bash
curl \
  -X POST 'http://localhost:8000/service/classifier/predict' \
  --form 'image_file=@"<my-file-path>"'
```
## Use poetry
### Installation
Install Poetry using `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

The project is running under `python 3.8.10`. Thus you need to link poetry to your interpreter to allow poetry to create a virtual environment.
```
poetry env use <path-to-python-3.8.10-interpreter>
```

Check [Poetry Documentation](https://python-poetry.org/docs/) for further informations about poetry's command.

### Tests and linter
You can run a test coverage with the following command :
```bash
poetry run test
```
To show the report of the coverage, run
```bash
poetry run report
```
You'll find the tests in `tests/`.

To check if the code follow python dev recommendations you can audit the code with
```bash
poetry run audit
cat .audit
```
## Workflows
### Run test on PR
From [install poetry action](https://github.com/marketplace/actions/install-poetry-action)

## Contributors
<a href="https://github.com/AgRenaud/Vector-Based-Image-Recognition-API/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AgRenaud/Vector-Based-Image-Recognition-API" />
</a>

Made with [contrib rocks](https://contrib.rocks/).
