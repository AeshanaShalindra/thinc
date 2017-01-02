import pytest
from flexmock import flexmock
from hypothesis import given, strategies
import abc

from .... import base


@pytest.fixture
def model_with_no_args():
    flexmock(base.Model)
    base.Model.should_receive('_args2kwargs').and_return({})
    base.Model.should_receive('_update_defaults').and_return({})
    base.Model.should_receive('setup').and_return(None)
    flexmock(base.util)
    base.util.should_receive('get_ops').with_args('cpu').and_return('cpu-ops')
    model = base.Model()
    return model


def test_Model_defaults_to_name_model(model_with_no_args):
    assert model_with_no_args.name == 'model'


def test_Model_defaults_to_cpu(model_with_no_args):
    assert model_with_no_args.ops == 'cpu-ops'


def test_Model_defaults_to_no_layers(model_with_no_args):
    assert model_with_no_args.layers == []


def test_Model_defaults_to_no_param_descripions(model_with_no_args):
    assert list(model_with_no_args.describe_params) == []


def test_Model_defaults_to_no_output_shape(model_with_no_args):
    assert model_with_no_args.output_shape == None
 

def test_Model_defaults_to_no_input_shape(model_with_no_args):
    assert model_with_no_args.input_shape == None


def test_Model_defaults_to_0_size(model_with_no_args):
    assert model_with_no_args.size == 0


def test_Model_defaults_to_no_params(model_with_no_args):
    assert model_with_no_args.params is None


@given(strategies.integers(min_value=0))
def test_model_with_unk_input_shape_scalar_output_shape(scalar_output_shape):
    '''This jointly tests init, _update_defaults, and _args2kwargs.'''
    flexmock(base.Model)
    base.Model.should_receive('setup').with_args().and_return(None)
    flexmock(base.util)
    base.util.should_receive('get_ops').with_args('cpu').and_return('cpu-ops')
    model = base.Model(scalar_output_shape)

    assert model.output_shape == scalar_output_shape
    assert model.input_shape is None
