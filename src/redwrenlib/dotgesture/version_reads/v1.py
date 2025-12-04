
# readfile/v1.py

#- Imports -----------------------------------------------------------------------------------------

import h5py
from typing import Tuple

from sklearn.mixture import GaussianMixture

from ...utils.debug import alert
from ...typing import (
    data_dict_t, SensorData
)


#- Read Method -------------------------------------------------------------------------------------

def read_file(f: h5py.File) -> data_dict_t:
    try:
        models_dict: data_dict_t = {}

        threshold=float(f['threshold'][()])
        n_components=int(f['n_components'][()])
        random_state=int(f['random_state'][()])

        for name in f.keys():
            gmm_group = f[name]

            if isinstance(gmm_group, h5py.Group):
                models_dict[name] = SensorData()

                # version 1 had common parameters for all sensor models
                models_dict[name].threshold = threshold
                models_dict[name].n_components = n_components
                models_dict[name].random_state = random_state

                for model_name in gmm_group.keys():
                    model_group = gmm_group[model_name]

                    model_instance = GaussianMixture()
                    model_instance.n_components = model_group['n_components'][()]
                    model_instance.weights_ = model_group['weights'][()]
                    model_instance.means_ = model_group['means'][()]
                    model_instance.covariances_ = model_group['covariances'][()]
                    model_instance.precisions_cholesky_ = model_group['precisions_cholesky'][()]

                    models_dict[name].models.append(model_instance)

    except Exception as e:
        alert(f"Unable to parse file. {e}")

    return models_dict
