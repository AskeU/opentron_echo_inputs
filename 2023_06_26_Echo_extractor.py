# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 09:51:36 2023

@author: askung
"""


from opentrons import protocol_api

metadata = {
    'protocolName': 'After_Echo',
    'author': 'Aske Unger',
    'description': 'This prepares for multiplexed DNA extraction',
    'apiLevel': '2.8'
}

def run(protocol: protocol_api.ProtocolContext):
    #Insert numbers here:
   
    #load labware
    #Tips
    tips10 = protocol.load_labware('opentrons_96_tiprack_10ul', '11')
    # pipettes
    pip20 = protocol.load_instrument("p20_multi_gen2", mount='left',tip_racks=[tips10])





    deep_plate = protocol.load_labware('nest_96_wellplate_2ml_deep',5)
    PCR_384_1 = protocol.load_labware('biorad_384_wellplate_50ul',2)
    PCR_384_2 = protocol.load_labware('biorad_384_wellplate_50ul',8)
    
    
    pip20.pick_up_tip()
    #Start programme
    pip20.flow_rate.dispense = 1000

    for i in range(1,25):
        pip20.aspirate(1,deep_plate['A1'].top(+5))
        pip20.aspirate(9,deep_plate['A1'].bottom(+2))
        pip20.dispense(8,PCR_384_1[f'A{i}'].top(-4))
        pip20.touch_tip(v_offset=-0.1)
        pip20.aspirate(8,deep_plate['A1'].bottom(+2))
        pip20.dispense(8,PCR_384_1[f'B{i}'].top(-4))
        pip20.touch_tip(v_offset=-0.1)
        pip20.dispense(2,deep_plate['A1'])
    pip20.drop_tip()
    pip20.pick_up_tip()
    for i in range(1,25):
        pip20.aspirate(1,deep_plate['A1'].top(+5))
        pip20.aspirate(9,deep_plate['A1'].bottom(+2))
        pip20.dispense(8,PCR_384_2[f'A{i}'].top(-4))
        pip20.touch_tip(v_offset=-0.1)
        pip20.aspirate(8,deep_plate['A1'].bottom(+2))
        pip20.dispense(8,PCR_384_2[f'B{i}'].top(-4))
        pip20.touch_tip(v_offset=-0.1)
        pip20.dispense(2,deep_plate['A1'])
    pip20.drop_tip()
    protocol.pause('Spin down cells weakly and tap on bottom')
    pip20.pick_up_tip()
    for i in range(1,25):
        pip20.aspirate(1,PCR_384_1[f'A{i}'].top(+5))
        pip20.aspirate(9,PCR_384_1[f'A{i}'].bottom(+1))
        pip20.dispense(9,deep_plate['A11'].bottom(+1))
        pip20.touch_tip(v_offset=-1)
        pip20.aspirate(9,PCR_384_1[f'B{i}'].bottom(+1))
        pip20.dispense(9,deep_plate['A11'].bottom(+1))
        pip20.dispense(1,deep_plate['A11'].bottom(+1))
        pip20.touch_tip(v_offset=-1)

    for i in range(1,25):
        pip20.aspirate(1,PCR_384_2[f'A{i}'].top(+5))
        pip20.aspirate(9,PCR_384_2[f'A{i}'].bottom(+1))
        pip20.dispense(9,deep_plate['A11'].bottom(+1))
        pip20.touch_tip(v_offset=-1)
        pip20.aspirate(9,PCR_384_2[f'B{i}'].bottom(+1))
        pip20.dispense(9,deep_plate['A11'].bottom(+1))
        pip20.dispense(1,deep_plate['A11'].bottom(+1))
        pip20.touch_tip(v_offset=-1)
   
    pip20.drop_tip()
        
     