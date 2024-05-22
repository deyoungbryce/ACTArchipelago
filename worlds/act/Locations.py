from .Types import LocationData
from .Regions import Stages

base_id = 0

actStandardLocations = {
    "The Shallows - Fork": LocationData(base_id + 1, Stages.Shallows)

}

actBossLocations = {
    "The Shallows - Royal Shell Splitter": LocationData(base_id + 1001, Stages.Shallows),
    "The Shallows - Nephro": LocationData(base_id + 1002, Stages.Shallows),
    "The Shallows - Duchess Magista": LocationData(base_id + 1003, Stages.Shallows)
}

location_table = {
    **actStandardLocations,
    **actBossLocations
}