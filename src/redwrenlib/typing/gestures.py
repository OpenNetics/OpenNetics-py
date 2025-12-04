
# typing/gesturefile.py

#- Imports -----------------------------------------------------------------------------------------

from typing import List
from dataclasses import dataclass

from sklearn.mixture import GaussianMixture


#- Data Classes ------------------------------------------------------------------------------------

# Mutable container for model configuration and inputs used when creating gestures.
class SensorData:
    models: List[GaussianMixture] = []
    threshold:  float = -10.5
    random_state: int = 2
    n_components: int = 42


# Immutable container for gesture checker
@dataclass(frozen=True)
class GestureMatch:
    value: float
    status: bool


#- Aliases -----------------------------------------------------------------------------------------

data_dict_t = dict[str, SensorData]

