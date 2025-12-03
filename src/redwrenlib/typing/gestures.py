
# typing/gesturefile.py

#- Imports -----------------------------------------------------------------------------------------

from dataclasses import dataclass

from numpy import bool as npbool
from numpy import float64 as npfloat


#- Data Classes ------------------------------------------------------------------------------------

# Immutable container for model configuration and inputs used when creating gestures.
@dataclass(frozen=True)
class ModelParameters:
    random_state: int
    n_components: int
    threshold: float

@dataclass(frozen=True)
class GestureMatch:
    value: npfloat
    status: npbool

