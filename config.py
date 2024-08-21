config = {
    "MFC_Air": { 
        "type": "mfc",
        "input_device": "23UP", # AnalogInSignal
        "input_channel": 0, 
        "output_device": "ZuC",# AnalogOutSignal
        "output_channel": 0,
        "unit": "ml/min",
        "gradient": 0.2, # Steigung umrechnung Rohdaten mV in mL/min 
        "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
        "x": 50,    # Position in Gui
        "y": 750,     # Position in Gui
    },
    
    "Verdampfer": { 
        "type": "ExtOutput",
        "output_device": "TiX",
        "output_channel": 1,
        "unit": "ml/min",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 940,
    },
    
    "p_1": { 
        "type": "pressure",
        "input_device": "23UK",
        "input_channel": 0,
        "unit": "mbar",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 940,
    },
    
    "p_2": { 
        "type": "pressure",
        "input_device": "23UK",
        "input_channel": 1,
        "unit": "mbar",
        "gradient":1,
        "y-axis":   0,
        "x": 955,
        "y": 890,
    },
    
    "Heater_1": { 
        "type": "easy_PI",
        "input_device": "T_R1",
        "security_input_device": "T_S1",
        "output_type": "PWM",
        "output_device": "Tmw",
        "output_channel": 0,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 800,
        "y": 670,
    },
    
    "Heater_2": { 
        "type": "easy_PI",
        "input_device": "T_R2",
        "output_type": "PWM",
        "output_device": "Tmw",
        "output_channel": 1,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 800,
        "y": 540,
    },
    
    "T_R1": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WPP",
        "input_channel": 0,
        "unit": "°C",
        "x": 650,
        "y": 670,
    },
    
    "T_R2": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WQ3",
        "input_channel": 0,
        "unit": "°C",
        "x": 650,
        "y": 540,
    },
    
    "T_1": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WjR",
        "input_channel": 0,
        "unit": "°C",
        "x": 955,
        "y": 890,
    } ,
    
    "T_S1": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "Wj2",
        "input_channel": 0,
        "unit": "°C",
        "x": 955,
        "y": 890,
    }      
}
