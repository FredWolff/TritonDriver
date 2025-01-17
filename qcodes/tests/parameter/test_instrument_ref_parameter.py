from collections.abc import Generator

import pytest

from qcodes.parameters import InstrumentRefParameter
from qcodes.tests.instrument_mocks import DummyInstrument


@pytest.fixture(name="instrument_a")
def _make_instrument_a() -> Generator[DummyInstrument, None, None]:
    a = DummyInstrument('dummy_holder')
    try:
        yield a
    finally:
        a.close()


@pytest.fixture(name="instrument_d")
def _make_instrument_d() -> Generator[DummyInstrument, None, None]:
    d = DummyInstrument('dummy')
    try:
        yield d
    finally:
        d.close()


def test_get_instr(
    instrument_a: DummyInstrument, instrument_d: DummyInstrument
) -> None:
    instrument_a.add_parameter("test", parameter_class=InstrumentRefParameter)

    instrument_a.test.set(instrument_d.name)

    assert instrument_a.test.get() == instrument_d.name
    assert instrument_a.test.get_instr() == instrument_d
