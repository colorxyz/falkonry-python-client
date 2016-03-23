"""
Falkonry Client

Client to access Condition Prediction APIs

:copyright: (c) 2016 by Falkonry Inc.
:license: MIT, see LICENSE for more details.

"""

from falkonryclient.helper.models import *

Models = {
 "Assessment": Assessment,
 "Pipeline": Pipeline,
 "Signal": Signal
}

__all__ = [
    'Models'
]
