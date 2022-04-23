import logging
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

    url = configuration["serving"]["url"]
    port = configuration["serving"]["port"]
    model_path = configuration["serving"]["model_path"]

    return f"{url}:{port}/{model_path}"


def get_qdrant_credentials() -> Tuple[str, str]:
    configuration = get_config()

    url = configuration["qdrant"]["url"]
    port = configuration["qdrant"]["port"]

    return url, port
