# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:52:10 2023

@author: askung
"""



from opentrons import protocol_api
 
metadata = {
    'protocolName': 'Exonuclease_1kb_4',
    'author': 'Aske Unger',
    'description': 'ExonucleaseIII_reaction',
    'apiLevel': '2.8'
}

# Noter:
# Sample position modify (til 2 pipettespider)
# 

def run(protocol: protocol_api.ProtocolContext):
 
    # load labware
    #Tips
    tips10 = protocol.load_labware('opentrons_96_tiprack_10ul', '11')
    # pipettes
    p10 = protocol.load_instrument('p20_multi_gen2', mount='left',tip_racks=[tips10])
    #Labware
    Source_plate = protocol.load_labware('corning_96_wellplate_360ul_flat',1)
    temp_mod = protocol.load_module('temperature module', 10)
    dist_plate = temp_mod.load_labware('nest_96_wellplate_2ml_deep')
    #Start programme
    temp_mod.set_temperature(4)
    p10.pick_up_tip(tips10['E1']) # G1, 2 pipettespidser
    pip_amount = 5 #Start amount to be pipetted
    for i in range(70): # (+8 betyder mm op)
        pip_amount=pip_amount-(3/70)
        p10.aspirate(5,Source_plate["A1"].top()) # luft
        p10.aspirate(round(pip_amount,1),Source_plate["A1"].bottom()) # væske
        p10.dispense(8,dist_plate["C3"].bottom(+8)) # Dispense til destination plate
        p10.dispense(2,dist_plate["C3"].top()) # luft (rester af væske)
        p10.aspirate(5,dist_plate["E11"].top()) # washing steps: (beskytter reaktionen mod salt)
        p10.aspirate(5,dist_plate["E11"].bottom(+8))
        p10.dispense(8,dist_plate["E12"].bottom(+8))
        p10.dispense(2,dist_plate["E12"].top())       
        protocol.delay(seconds=20) 




