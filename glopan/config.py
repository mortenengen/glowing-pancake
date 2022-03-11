"""Configuration for Glowing Pancake"""
import json
import os

from pathlib import Path

HOMEPATH = Path.home()
CONFIG_FILENAME = 'glowing-pancake.json'


class Config:
    """Glowing Pancake configuration"""

    def __init__(self):
        config_file = HOMEPATH / CONFIG_FILENAME
        self.config_file = config_file

        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as infile:
                config = json.load(infile)
        else:
            config = {}

        self.config = config

        ps2pdf_path = config.get('ps2pdf_path', None)
        if ps2pdf_path is not None:
            os.environ.setdefault(
                'system',
                str(Path(ps2pdf_path).parent.parent / 'bin'),
            )

    def set(self, key, value):
        """Set a key-value pair in the configuration."""
        self.config[key] = value
        with open(self.config_file, 'w', encoding='utf-8') as config_file:
            json.dump(self.config, config_file)

    def reset(self):
        """Reset configuration"""
        self.config = {
            'inkscape_path': None,
            'ps2pdf_path': None,
        }
        with open(self.config_file, 'w', encoding='utf-8') as config_file:
            json.dump(self.config, config_file)
