"""
Example CLI for {{cookiecutter.project_name}}.
"""
import hydra
import pyprojroot
from omegaconf import DictConfig

default_config_path = str(pyprojroot.here("configs"))
default_config_name = "config"


@hydra.main(config_path=default_config_path, config_name=default_config_name)
def main(cfg: DictConfig):
    """
    Hello world CLI.

    Returns True if function exited successfully.
    """
    print(f"Hello World!\n Default model is {cfg.model_name_default}")
    return True


if __name__ == '__main__':
    main()
