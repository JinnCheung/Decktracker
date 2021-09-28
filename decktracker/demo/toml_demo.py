#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""A simple introdution

more description

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/27 20:00 
"""
import os
import toml

# script_folder = os.path.abspath(os.path.dirname(__file__))
# package_folder = os.path.abspath(os.path.dirname(script_folder))
# project_folder = os.path.abspath(os.path.dirname(package_folder)) if config.get('base').get('root_folder') == '.'
#
# config_file =
#
# os.path.join(project_folder, 'config.toml')
#
#
if __name__ == "__main__":
    custom_config_file = ""
    default_config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.toml'))
    if os.path.exists(custom_config_file):
        config_file = custom_config_file
    elif os.path.exists(default_config_file):
        config_file = default_config_file
    else:
        raise FileNotFoundError("config.toml not found. there is a sample of config.toml in /docs.")

    config = toml.load(config_file)

    if os.path.exists(config.get('folders').get('root_folder')):
        data_folder = os.path.abspath(os.path.join(config.get('folders').get('root_folder'),
                                                   config.get('folders').get('data_folder')))
    else:
        data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                   config.get('folders').get('data_folder')))

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

