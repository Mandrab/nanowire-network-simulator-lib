# -*- coding: utf-8 -*-
import logging
import view.plot as plot

from model.analysis.evolution import Evolution
from model.analysis.measures import print_info, inspect
from model.device.datasheet.default import default
from model.device.factory import generate_network, get_graph, generate_graph
from model.device.factory import minimum_viable_network
from model.device.utils import initialize_graph_attributes, largest_component
from model.interface.creation import random_ground, random_sources
from model.interface.evolution import mutate
from model.stimulator import stimulate, voltage_initialization

__all__ = [
    # statistical analysis
    "Evolution",                # network-state collectors for analysis
    "print_info", "inspect",    # supervision utils
    # device utilities & configurations
    "default",
    # network creation
    "generate_network", "get_graph", "generate_graph", "minimum_viable_network",
    # network initialization
    "initialize_graph_attributes", "largest_component",
    # interface / connection definition
    "random_ground", "random_sources", "mutate",
    # stimulation utilities for the network
    "stimulate", "voltage_initialization",
    # logging utilities & setups
    "logging", "debug_mode",
    # plotting utils
    "plot"
]

__LOGGING_FORMAT = '[%(asctime)s %(levelname)s]\t %(message)s'

# define default logging level as INFO and following a standard format
logging.basicConfig(level=logging.INFO, format=__LOGGING_FORMAT)


def debug_mode():
    """Enable the debug mode in the simulator (i.e., log at DEBUG level)"""

    logging.basicConfig(level=logging.DEBUG, format=__LOGGING_FORMAT)
