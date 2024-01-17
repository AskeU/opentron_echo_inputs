# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:27:26 2022

@author: askung
"""

from opentrons import protocol_api

metadata = {
    'protocolName': '8 plates, 95 uL_multi',
    'author': 'Aske Unger feat Nikolaj',
    'description': 'Fill a plate with whatever you want',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    #Insert numbers here:
    Number_of_plates = 8
    Amount_of_liquid = 95 #uL up to 300
    #load labware
    #Tips
    tips300 = protocol.load_labware('opentrons_96_tiprack_300ul', '11')
    # pipettes
    p300 = protocol.load_instrument('p300_multi', mount='right',tip_racks=[tips300])
    #Labware
    Source_plate = protocol.load_labware('corning_96_wellplate_360ul_flat',1)
    
    Aliquot=[]


    for i in range(8):
        Aliquot.append(protocol.load_labware('corning_96_wellplate_360ul_flat',i+2))
    
    p300.pick_up_tip()
    for k in range(10):
        #Start programme
        for j in range(Number_of_plates):
            for i in range(1,13):
                p300.aspirate(Amount_of_liquid,Source_plate['A1'])
                p300.dispense(Amount_of_liquid,Aliquot[j][f'A{i}'])
        protocol.pause(f'round {k+1}: If done, click cancel')
     