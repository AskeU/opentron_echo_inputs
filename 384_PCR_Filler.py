# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:27:26 2022

@author: askung
"""

from opentrons import protocol_api

metadata = {
    'protocolName': '384_PCR_Prep',
    'author': 'Aske Unger',
    'description': 'This is a test of a PCR prep program',
    'apiLevel': '2.8'
}

def run(protocol: protocol_api.ProtocolContext):
    #Insert numbers here:
   
    #load labware
    #Tips
    tips10 = protocol.load_labware('opentrons_96_tiprack_10ul', '11')
    # pipettes
    pip20 = protocol.load_instrument("p20_multi_gen2", mount='left',tip_racks=[tips10])




    plate1 = protocol.load_labware('corning_96_wellplate_360ul_flat',1)
    plate2 = protocol.load_labware('corning_96_wellplate_360ul_flat',2)
    plate3 = protocol.load_labware('corning_96_wellplate_360ul_flat',3)
    plate4 = protocol.load_labware('corning_96_wellplate_360ul_flat',4)
    platelist = [plate1,plate2,plate3,plate4]

    source = protocol.load_labware('corning_96_wellplate_360ul_flat',8)
    wash = protocol.load_labware('nest_96_wellplate_2ml_deep',6)
    
    PCR_384 = protocol.load_labware('biorad_384_wellplate_50ul',5)
    
    
    pip20.pick_up_tip()
    #Start programme

    for i in range(1,25):
        pip20.aspirate(1,source['A1'].top(+5))
        pip20.aspirate(9,source['A1'].bottom(+2))
        pip20.dispense(4,PCR_384[f'A{i}'])
        pip20.dispense(4,PCR_384[f'B{i}'])
        pip20.dispense(2,source['A1'])
    pip20.drop_tip()
    
    for plates in range(1,5):
        pip20.pick_up_tip()

        for i in range(1,13):
            pip20.aspirate(5,platelist[plates-1][f'A{i}'].top())
            pip20.mix(4, 2, platelist[plates-1][f'A{i}'])
            pip20.aspirate(0.1,platelist[plates-1][f'A{i}'])
            
            if plates == 1:
                pos = (i-1)*2+1 #Sets the positions for plate1
                pos = f'A{pos}'
            if plates == 2:
                pos = (i-1)*2+1 #Sets the positions for plate1
                pos = f'B{pos}'
            if plates == 3:
                pos = i*2 #Sets the positions for plate1
                pos = f'A{pos}'
            if plates == 4:
                pos = i*2 #Sets the positions for plate1
                pos = f'B{pos}'
            
                
            pip20.dispense(0.1,PCR_384[pos])
            pip20.mix(3, 2, PCR_384[pos].bottom())
            pip20.dispense(5, wash[f'A{(plates-1)*3+1}'].top())
            pip20.mix(3, 6, wash[f'A{(plates-1)*3+1}'])
            pip20.mix(3, 6, wash[f'A{(plates-1)*3+2}'])
            pip20.mix(3, 6, wash[f'A{(plates-1)*3+3}'])
        
        pip20.drop_tip()
        
     