# Vector Based Image recognition API

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

Go in the `scripts/` and run `create_collection.sh`.
```bash
cd scripts

./create_collection.sh http://localhost:6333 <CollectionName> <Path2JsonPoints> <Distance> <VectorSize>
```
You can take a look at [Qdrant Documentation](https://qdrant.tech/documentation/) to understand how to create a `Collection` and feed it with `Point`.

Before using the above, make sure that your folder `<Path2JsonPoints>` is composed of `.json` file with the following format :
```json
{
  "id": 800,
  "payload": {
    "class": "f"
  },
  "vector": [
    -0.010314688086509705,
    -0.6674487590789795,
    0.0650707483291626,
    -2.838604211807251
  ]
}
```

### Make your first call

```bash
curl \
  -X POST 'http://localhost:8000/service/classifier/predict' \
  --form 'image_file=@"<my-file-path>"'
```

You'll find a postman collection on `docs/postman` with usefull example of API call.
## Test
You can run a test coverage with the following command :
```bash
poetry run test
```
To show the report of the coverage, run
```bash
poetry run report
```
You'll find the tests in `tests/`.

## Contributors
<a href="https://github.com/AgRenaud/Vector-Based-Image-Recognition-API/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AgRenaud/Vector-Based-Image-Recognition-API" />
</a>

Made with [contrib rocks](https://contrib.rocks/).
