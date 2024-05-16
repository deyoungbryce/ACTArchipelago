from .Types import LocationData

base_id = 0

actStandardLocations = {
    "The Shallows - Fork": LocationData(base_id + 1, "The Shallows")

}

actBossLocations = {
    "The Shallows - Royal Shell Splitter": LocationData(base_id + 1001, "The Shallows"),
    "The Shallows - Nephro": LocationData(base_id + 1002, "The Shallows"),
    "The Shallows - Duchess Magista": LocationData(base_id + 1003, "The Shallows")
}

location_table = {
    **actStandardLocations,
    **actBossLocations
}