import logging
import yaml

from os import environ


logger = logging.getLogger(__name__)


def set_loggers(config_file):
    log_file_path = config_file
    logging.config.fileConfig(log_file_path, disable_existing_loggers=True)
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    set_env_var('LOGGING_CONFIG_PATH', config_file)

def set_env_var(name, new_value):
    if name not in environ:
        environ[name] = new_value
        logger.info(f'set env variable {name}')

def get_app_config():
    # Load configuration file
    with open("config.yaml", "r") as stream:
        try:
            configuration=yaml.safe_load(stream)
            logger.info(f'Configuration file is loaded')
        except yaml.YAMLError as exc:
            logger.error(exc)
            raise exc

    if configuration:
        set_loggers(configuration['logging']['config']['path'])
        set_env_var('TF_SERVING_URL', configuration['tensorflow_serving']['url'])
        set_env_var('TF_SERVING_MODEL_NAME', configuration['tensorflow_serving']['model']['name'])
        set_env_var('TF_SERVING_MODEL_PATH', configuration['tensorflow_serving']['model']['path'])
