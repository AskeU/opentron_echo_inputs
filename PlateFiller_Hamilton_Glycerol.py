# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:27:26 2022

@author: askung
"""

from opentrons import protocol_api

metadata = {
    'protocolName': 'glycerol_adder_multiplates',
    'author': 'Aske Unger',
    'description': 'This is a test of a PCR prep program',
    'apiLevel': '2.8'
}

def run(protocol: protocol_api.ProtocolContext):
    #Insert numbers here:
    Number_of_plates = 8
    Amount_of_liquid = 50 #uL up to 300
    flow_dispense = 50
    flow_aspirate = 50
    #load labware
    #Tips
    tips300 = protocol.load_labware('opentrons_96_tiprack_300ul', '11')
    # pipettes
    p300 = protocol.load_instrument('p300_multi', mount='right',tip_racks=[tips300])
    #Labware
    Source_plate = protocol.load_labware('nest_96_wellplate_2ml_deep',1)
    
    Aliquot=[]



    for i in range(Number_of_plates):
        Aliquot.append(protocol.load_labware('corning_96_wellplate_360ul_flat',i+2))

    p300.pick_up_tip()
    p300.flow_rate.aspirate = flow_aspirate
    p300.flow_rate.dispense = flow_dispense
    #Start programme
    for k in range(10):
        for j in range(Number_of_plates):
            for i in range(1,13):
                p300.aspirate(Amount_of_liquid,Source_plate['A1'])
                protocol.delay(seconds=1)
                p300.dispense(Amount_of_liquid,Aliquot[j][f'A{i}'].top())
                protocol.delay(seconds=1)
        protocol.pause(f'round {k+1}: If done, click cancel')
            
     