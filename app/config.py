import logging

import logging.config
from envyaml import EnvYAML

from os import environ, path
from typing import Tuple

logger = logging.getLogger(__name__)


def set_loggers() -> None:
    configuration = get_config()
    log_file_path = configuration['logging']['config']['path']
    logging.config.fileConfig(log_file_path, disable_existing_loggers=True)


def get_config() -> EnvYAML:
    try:
        configuration = EnvYAML(environ["CONFIG_PATH"])
        return configuration
    except Exception as exc:
        logger.error(exc)
        raise exc


def get_tf_serving_credentials() -> str:
    configuration = get_config()

    url = configuration["tensorflow_serving"]["url"]
    port = configuration["tensorflow_serving"]["port"]
    model_path = configuration["tensorflow_serving"]["model"]["path"]
    model_name = configuration["tensorflow_serving"]["model"]["name"]

    return f"{url}:{port}/{model_path}/{model_name}"


def get_qdrant_credentials() -> Tuple[str, str]:
    configuration = get_config()

    url = configuration["qdrant"]["url"]
    port = configuration["qdrant"]["port"]

    return url, port
