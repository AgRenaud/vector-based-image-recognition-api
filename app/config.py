import logging
from envyaml import EnvYAML

from os import environ, path
from typing import Tuple

logger = logging.getLogger(__name__)


def set_loggers(config_file) -> None:
    log_file_path = config_file
    logging.config.fileConfig(log_file_path, disable_existing_loggers=True)
    set_env_var("LOGGING_CONFIG_PATH", config_file)


def set_env_var(name, new_value) -> None:
    if name not in environ:
        logger.info(f"set env variable {name}")
        environ[name] = str(new_value)


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
