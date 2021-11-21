# Optical Character Recognition

<p align="middle">
  <img src="./docs/images/tf-logo.png" width="15%" />
  <img src="./docs/images/poetry-logo.svg" width="7%" />
  <img src="./docs/images/fastapi-logo.png" width="18%" />
  <img src="./docs/images/docker-logo.png" width="18%" />
  <img src="./docs/images/qdrant-logo.png" width="18%" />
</p>

Simple implementation of a `Keras` model for optical character recognition (OCR).

The project intends to propose a simple solution to expose through an API a system for One-Shot learning in the field of image recognition (OCR).


## Getting Started
You can start to explore the project by taking a look to the `notebooks/` folder where you'll find several `.ipynb` files containing all you need to train a model for OCR tasks. You'll also find an implementation of  `ArcFace` for `tensorflow`.

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

### Run API with Docker
```
docker-compose up
```
### Feed search engine
Take a look at [Qdrant Documentation](https://qdrant.tech/documentation/) to understand how to create a `Collection` and feed it with `Point`.

Then go in the `scripts/` and run `create_collection.sh`.
```bash
cd scripts

./create_collection.sh http://localhost:6333 <CollectionName> <Path2JsonPoints> <Distance> <VectorSize>

```

### Make your first call

## Train a model
