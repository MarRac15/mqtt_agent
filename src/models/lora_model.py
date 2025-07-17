
# to validate the incoming messages:
VALID_LABELS = {
    "MD", "ID", "DS", 
    "AT", "H", "I", "WS", "WD", "AP", "P", "P1", "P2", "D", "L",  
    "SM1", "SM2", "SM3", "SM4", "SM5", "SM6",      
    "TD05", "TD1", "TD2", "TD5", "TD10", "TH0", "TH05"  
}

# every message must contain these or it wont be send to kafka:
REQUIRED_LABELS = {
    "MD",
    "O",
    "ID"
}

# for mapping lora labels to field names for kafka:
FIELD_ALIASES = {

    "MD": "measurementDate",
    "O": "owner",
    "ID": "internalId",

    "DS": "dataSourceStoreDate",
    "AT": "airTemperature",
    "H": "relativeHumidity",
    "I": "insolation",
    "WS": "windSpeed",
    "WD": "windDirection",
    "AP": "airPressure",
    "P": "precipitation",
    "P1": "precipitationRaw1",
    "P2": "precipitationRaw2",
    "D": "dewPointTemperature",
    "L": "leafWetness",

    "SM1": "soilMoisture_on_0_1m_depth",
    "SM2": "soilMoisture_on_0_2m_depth",
    "SM3": "soilMoisture_on_0_3m_depth",
    "SM4": "soilMoisture_on_0_4m_depth",
    "SM5": "soilMoisture_on_0_5m_depth",
    "SM6": "soilMoisture_on_0_6m_depth",

    "TD05": "soilTemperature_on_0_05m_depth",
    "TD1": "soilTemperature_on_0_1m_depth",
    "TD2":  "soilTemperature_on_0_2m_depth",
    "TD5": "soilTemperature_on_0_5m_depth",
    "TD10": "soilTemperature_on_1m_depth",
    "TH0": "soilTemperature_on_0m_height",
    "TH05": "soilTemperature_on_0_05m_height"
}
