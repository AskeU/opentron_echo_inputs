# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:27:26 2022

@author: askung
"""

from opentrons import protocol_api



metadata = {
    'protocolName': 'Add water to primerplates',
    'author': 'Aske Unger',
    'description': 'water',
    'apiLevel': '2.11'
}

def run(protocol: protocol_api.ProtocolContext):
    #Insert numbers here:
   
    #load labware
    #Tips
    tips300_1 = protocol.load_labware('opentrons_96_tiprack_300ul', '10')
    # pipettes
    pip300 = protocol.load_instrument("p300_multi_gen2", mount='right')

    trough = protocol.load_labware('nest_96_wellplate_2ml_deep',5)
    primer_plate_fw = protocol.load_labware('nest_96_wellplate_2ml_deep',4)
    primer_plate_rev = protocol.load_labware('nest_96_wellplate_2ml_deep',6)

    
    

    pip300.pick_up_tip(tips300_1[f'A{1}']) #Picks the lowest position
    for j in range(12):
        pip300.aspirate(20,trough['A1'].top())
        pip300.aspirate(250,trough['A1'])
        pip300.dispense(270,primer_plate_fw[f'A{j+1}'].top())
    for j in range(4):
        pip300.aspirate(20,trough['A1'].top())
        pip300.aspirate(250,trough['A1'])
        pip300.dispense(270,primer_plate_rev[f'A{j+1}'].top())
            
    pip300.drop_tip()
        
     