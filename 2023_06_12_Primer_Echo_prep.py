# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:27:26 2022

@author: askung
"""

from opentrons import protocol_api

metadata = {
    'protocolName': '384_Primer_Adder_Echo',
    'author': 'Aske Unger',
    'description': 'This adds fw primers to a 384 echo plate',
    'apiLevel': '2.8'
}

def run(protocol: protocol_api.ProtocolContext):
    #Insert numbers here:
   
    #load labware
    #Tips
    tips300_1 = protocol.load_labware('opentrons_96_tiprack_300ul', '10')
    tips300_2 = protocol.load_labware('opentrons_96_tiprack_300ul', '11')
    # pipettes
    pip300 = protocol.load_instrument("p300_multi_gen2", mount='right')


    primer_plate_fw = protocol.load_labware('nest_96_wellplate_2ml_deep',4)
    primer_plate_rev = protocol.load_labware('nest_96_wellplate_2ml_deep',6)
    Echo_plate = protocol.load_labware('biorad_384_wellplate_50ul',5)
    
    
    
    Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
    for i in range(12):  #Forward primers
        for j in range(8):
            pip300.pick_up_tip(tips300_1[f'{Letters[7-j]}{i+1}']) #Picks the lowest position
            
            pip300.aspirate(55,primer_plate_fw[f'{Letters[j]}{i+1}'].bottom())
            
            pip300.dispense(55,Echo_plate[f'{Letters[j]}{i+1}'])
            
            pip300.drop_tip()
     
        
     
    for i in range(4):  #Reverse primers
        for j in range(8):
            pip300.pick_up_tip(tips300_2[f'{Letters[7-j]}{i+1}']) #Picks the lowest position
            
            pip300.aspirate(55,primer_plate_rev[f'{Letters[j]}{i+1}'].bottom())
            
            pip300.dispense(55,Echo_plate[f'{Letters[j]}{i+21}'])
            
            pip300.drop_tip()