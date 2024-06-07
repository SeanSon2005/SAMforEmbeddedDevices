import argparse
from datetime import datetime
from pathlib import Path
from typing import Any, Type

from .tools import read_yaml
from .logger import global_logger_setup


class Config:
    def __init__(self, config: dict):
        self._config = config

        # set experiment name and run id
        exp_name = config["main"]["name"]
        run_id = datetime.now().strftime(r"%Y%m%d_%H%M%S")

        # set and create directory for saving log and model
        model_dir = Path(self.config["trainer"]["model_dir"])
        log_dir = Path(self.config["trainer"]["log_dir"])
        self._save_dir: Path = model_dir
        self._log_dir: Path = log_dir / "logs" / run_id

        exist_ok = run_id == ""
        #self.save_dir.mkdir(parents=True, exist_ok=exist_ok)
        self.log_dir.mkdir(parents=True, exist_ok=exist_ok)

        # setup logging
        global_logger_setup(self.config["logger"], self.log_dir)


    @classmethod
    def load_config(cls, cfg_fname: str) -> "Config":
        config = read_yaml(cfg_fname)
        return cls(config)

    def init_obj(self, cfg_name: str, module: Type[Any], *args, **kwargs) -> Any:
        config = self.config[cfg_name]
        module_name = config["type"]
        module_args = dict(config["args"])
        assert all(
            [k not in module_args for k in kwargs]
        ), "Overwriting kwargs in config file is not allowed"
        module_args.update(kwargs)
        return getattr(module, module_name)(*args, **module_args)

    def __getitem__(self, name: str) -> Any:
        """Access items like ordinary dict."""
        return self.config[name]

    # setting read-only attributes
    @property
    def config(self):
        return self._config

    @property
    def log_dir(self):
        return self._log_dir

    @property
    def save_dir(self):
        return self._save_dir