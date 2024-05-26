from ...BaseClasses import Location
from typing import List, NamedTuple

class LocationData(NamedTuple):
    id: int = 0
    region: str = ""
    forkReq: bool = False
    anyShellReq: bool = False
    magnetShellReq: bool = False
    voltaiAdapReq: bool = False
    mantisAdapReq: bool = False
    miscRequired: List[str] = []