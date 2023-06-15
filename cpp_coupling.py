# The content of this file was generated using the Python profile of libCellML 0.4.0.

from enum import Enum
from math import *


__version__ = "0.4.0"
LIBCELLML_VERSION = "0.4.0"

STATE_COUNT = 2
VARIABLE_COUNT = 9


class VariableType(Enum):
    VARIABLE_OF_INTEGRATION = 0
    STATE = 1
    CONSTANT = 2
    COMPUTED_CONSTANT = 3
    ALGEBRAIC = 4


VOI_INFO = {"name": "time", "units": "second", "component": "environment", "type": VariableType.VARIABLE_OF_INTEGRATION}

STATE_INFO = [
    {"name": "v", "units": "m3_per_s", "component": "main_vessel_module", "type": VariableType.STATE},
    {"name": "q_C", "units": "m3", "component": "main_vessel_module", "type": VariableType.STATE}
]

VARIABLE_INFO = [
    {"name": "R_main_vessel", "units": "Js_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "C_main_vessel", "units": "m6_per_J", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_ext_main_vessel", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "I_main_vessel", "units": "Js2_per_m6", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "u_out_main_vessel", "units": "J_per_m3", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "v_in_main_vessel", "units": "m3_per_s", "component": "parameters", "type": VariableType.CONSTANT},
    {"name": "R_v", "units": "Js_per_m6", "component": "main_vessel_module", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u", "units": "J_per_m3", "component": "main_vessel_module", "type": VariableType.ALGEBRAIC},
    {"name": "u_C", "units": "J_per_m3", "component": "main_vessel_module", "type": VariableType.ALGEBRAIC}
]


def create_states_array():
    return [nan]*STATE_COUNT


def create_variables_array():
    return [nan]*VARIABLE_COUNT


def initialise_variables(states, rates, variables):
    variables[0] = 1.0e6
    variables[1] = 1.0e-8
    variables[2] = 0.0
    variables[3] = 1.0e-6
    variables[4] = 10.0
    variables[5] = 1.0e-5
    states[0] = 0.0
    states[1] = 0.0


def compute_computed_constants(variables):
    variables[6] = 0.01/variables[1]


def compute_rates(voi, states, rates, variables):
    variables[8] = states[1]/variables[1]+variables[2]
    variables[7] = variables[8]+variables[6]*(variables[5]-states[0])
    rates[0] = (variables[7]-variables[4]-variables[0]*states[0])/variables[3]
    rates[1] = variables[5]-states[0]


def compute_variables(voi, states, rates, variables):
    variables[8] = states[1]/variables[1]+variables[2]
    variables[7] = variables[8]+variables[6]*(variables[5]-states[0])
