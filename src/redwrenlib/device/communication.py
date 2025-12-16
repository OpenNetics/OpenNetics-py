
# device/communication.py

#- Imports -----------------------------------------------------------------------------------------

from typing import List

from ..typing import numeric_t
from ..utils.debug import alert, AlertLevel


#- Public Calls ------------------------------------------------------------------------------------

def get_data() -> List[numeric_t]:
    Result: List[numeric_t] = []
    return Result


def send_data(data: Any) -> None:
    # if fail
    try:
        pass

    except Exception as e:
        alert(f"failed to send data. {e}", backtrack=3, level=AlertLevel.ERROR)
        # backtrack=3 because:
        #   backtrack=0 is the code in alert() function
        #   backtrack=1 is this call
        #   backtrack=2 is in Devices.write(), where this procedure was called
        #   backtrack=3 is where Devices.write() method was called

