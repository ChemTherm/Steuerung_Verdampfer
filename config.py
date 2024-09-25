config = {
    "MFC_Air": { 
        "type": "mfc",
        "input_device": "23UA", # AnalogInSignal
        "input_channel": 0, 
        "output_device": "Zvg",# AnalogOutSignal
        "output_channel": 0,        
        "x": 50,    # Position in Gui
        "y": 750,     # Position in Gui
        "Box": 1,
        "DeviceInfo":{  "Bezeichnung":"Bronkhorst EL-FLOW Prestige",
                        "Seriennummer":"TestNummer123",
                        "ChemTherm-DeviceID": 15,
                        "Information": "10 l/min Air",
                        "unit": "l/min",
                        "gradient": 0.2, # Steigung umrechnung Rohdaten mV in mL/min 
                        "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
                        }
                        
    },
    #"MFC_N2": { 
    #    "type": "mfc",
    #    "input_device": "XXc", # AnalogInSignal
    #    "input_channel": 1, 
    #    "output_device": "XXd",# AnalogOutSignal
    #    "output_channel": 0,        
    #    "x": 50,    # Position in Gui
    #    "y": 750,     # Position in Gui
    #    "Box": 1,
    #    "DeviceInfo":{  "Bezeichnung":"Bronkhorst EL-FLOW Prestige",
    #                    "Seriennummer":"TestNummer456",
    #                    "ChemTherm-DeviceID": 16,
    #                    "Information": "300 ml/min N2",
    #                    "unit": "ml/min",
    #                    "gradient": 0.2, # Steigung umrechnung Rohdaten mV in mL/min 
    #                    "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
    #                    }
    #                    
    #},
    
    "p_1": { 
        "type": "pressure",
        "input_device": "ZZ1",  #Obere Drucksensor
        "input_channel": 0,
        "x": 370,
        "y": 940,
        "DeviceInfo":{  "Bezeichnung":"IFM PT5054",
                        "Seriennummer":"TestNummer789",
                        "ChemTherm-DeviceID": 18,
                        "Information": "10 bar",
                        "unit": "kPa",
                        "gradient": 0.5, # Steigung umrechnung Rohdaten mV in mL/min 
                        "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
                        }
    },
    
    "p_2": { 
        "type": "pressure",
        "input_device": "27DQ",  #Untere Drucksensor
        "input_channel": 1,
        "gradient":1,
        "y-axis":   0,
        "x": 955,
        "y": 890,
        "DeviceInfo":{  "Bezeichnung":"IFM PT5052",
                        "Seriennummer":"TestNummer1111",
                        "ChemTherm-DeviceID": 19,
                        "Information": "5 bar",
                        "unit": "mbar",
                        "gradient": 0.5, # Steigung umrechnung Rohdaten mV in mL/min 
                        "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
                        }
    },
    
    "Verdampfer": { 
        "type": "easy_PI",
        "input_device": "T_R1",
        "security_input_device": "T_S1",
        "output_type": "analog",
        "output_device": "27A7",
        "output_channel": 0,
        "x": 500,
        "y": 470,
        "DeviceInfo":{  "Bezeichnung":"Kombiverdampfer KV.1",
                        "Seriennummer":"TestNummer1122",
                        "ChemTherm-DeviceID": 20,
                        "Information": "TU München",
                        "Power": "500", # Angabe der Leistung in Watt
                        "unit": "W",    
                        "P_Value": 0.018,
                        "I_Value": 0.000013,
                        }
    },
    
    #"Heater_1": { 
    #    "type": "easy_PI",
    #    "input_device": "T_R2",
    #    "security_input_device": "T_S2",
    #    "output_type": "PWM",
    #    "output_device": "XXh",
    #    "output_channel": 1,
    #    "x": 800,
    #    "y": 670,
    #    "DeviceInfo":{  "Bezeichnung":"Begleitheizung",
    #                    "Seriennummer":"TestNummer1122",
    #                    "ChemTherm-DeviceID": 20,
    #                    "Information": "Rohrwendelheizung",
    #                    "Power": "800", # Angabe der Leistung in Watt
    #                    "unit": "W",    
    #                    "P_Value": 0.018,
    #                    "I_Value": 0.000013,
    #                    }
    #},
    
    "T_R1": { 
        "type": "thermocouple",
        "tc_type": "K",
        "input_device": "23hX",
        "x": 650,
        "y": 470,
        "DeviceInfo":{  "Bezeichnung":"Verdampfer Regeltemperatur",
                        "unit": "°C",
                        }
    },
    
    #"T_R2": { 
    #    "type": "thermocouple",
    #    "tc_type": "K",
    #    "input_device": "XXj",
    #    "x": 650,
    #    "y": 540,
    #    "DeviceInfo":{  "Bezeichnung":"Heizung Regelltemperatur",
    #                    "unit": "°C",
    #                    }
    #},
    
    #"T_1": { 
    #    "type": "thermocouple",
    #    "tc_type": "K",
    #    "input_device": "XXk",
    #    "x": 955,
    #    "y": 890,
    #    "DeviceInfo":{  "Bezeichnung":"Temperatur Messstelle 1",
    #                    "unit": "°C",
    #                    }
    #} ,
    
    "T_S1": { 
        "type": "thermocouple",
        "tc_type": "K",
        "input_device": "WQx",
        "input_channel": 0,
        "x": 850,
        "y": 470,
        "DeviceInfo":{  "Bezeichnung":"Sicherheit Verdampfer",
                        "unit": "°C",
                        }
    }, 
    
    #"T_S2": { 
    #    "type": "thermocouple",
    #    "tc_type": "K",
    #    "input_device": "XXm",
    #    "input_channel": 0,
    #    "x": 955,
    #    "y": 890,
    #    "DeviceInfo":{  "Bezeichnung":"Sicherheit Heizung",
    #                    "unit": "°C",
    #                    }
    #}, 
    
    #"HPLC-Pumpe": { 
    #    "type": "ExternInputOutput",
    #    "output_device": "Modbus",
    #    "input_device": "Modbus",
    #    "x": 370,
    #    "y": 940,
    #    "DeviceInfo":{  "Bezeichnung":" HPLC-ChemTherm",
    #                    "Seriennummer":"TestNummer1133",
    #                    "ChemTherm-DeviceID": 21,
    #                    "Information": "Ansteuerung Modbus max 10 ml/min",
    #                    "unit": "ml/min",
    #                    }
    #},     
}
