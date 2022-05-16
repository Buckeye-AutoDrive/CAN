"""
*********************************************************************
 *  Copyright (c) 2020-2021, The Ohio State UNiversity, ADC II team.
 *  All rights reserved.
 *  Created by:
 *            Shreya Pal, The Ohio State University

 *********************************************************************/
"""
import cantools
import can
from pprint import pprint
from message_other import perception2CAN as pcan

db = cantools.database.load_file('/home/shreya0407/Documents/Auto_Drive_Challenge_II/Scoring_Year1.dbc')
can_bus = can.interface.Bus('can0', bustype='socketcan')

i = pcan()
msg = i.GetMsg()
msg_names = msg.keys()
detected_objects = msg['Objects']['Number_Of_Detected_Objects']
detected_signals = msg['TrafficSignalHeads']['Number_Of_Detected_Signals']
detected_signs = msg['TrafficSigns']['Number_Of_Detected_Signs']
detected_markings = msg['LaneMarkings']['Number_Of_Detected_Markings']
detected_lines = msg['LimitLines']['Number_Of_Detected_Lines']
dict_light = {0: {'IllumLtNone': 1, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               1: {'IllumLtNone': 0, 'IllumLtRedBall': 1, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               2: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 1, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               3: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 1,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               4: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 1, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               5: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 1, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               6: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 1,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               7: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 1, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               8: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 1, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               9: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 1,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               10: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 1, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               11: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 1, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               12: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 1,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               13: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 1, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                   },
               14: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 1, 'IllumLtFlshngYellowRightArrow': 0
                   },
               15: {'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                   'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                   'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                   'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                   'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 1
                   }
               }
data0 = db.encode_message(msg_names[0], msg[msg_names[0]])                                          #Current_Observed_Speed_Limit, Active_Lane_Number           
data1 = db.encode_message(msg_names[1], {'Rolling_Count': msg['Objects']['Rolling_Count'], 'Current_Object_Count': detected_objects})
if detected_objects > 0:
    for i in range(detected_objects):
        data2[i] = db.encode_message(msg_names[2], {'Rolling_Count': msg['Object_TrackA']['Rolling_Count'][i],
                                                    'ObjObjectId': msg['Object_TrackA']['ObjObjectId'][i],
                                                    'ObjObjectType': msg['Object_TrackA']['ObjObjectType'][i],
                                                    'LongPos': msg['Object_TrackA']['LongPos'][i],
                                                    'LatPos': msg['Object_TrackA']['LatPos'][i],
                                                    'RelLongVel': msg['Object_TrackA']['RelLongVel'][i],
                                                    'RelLatVel': msg['Object_TrackA']['RelLatVel'][i],
                                                    'Relative_Lane': msg['Object_TrackA']['Relative_Lane'][i],
                                                    })                                                                                    #Confidence
        data3[i] = db.encode_message(msg_names[3], {'Rolling_Count': msg['Object_TrackB']['Rolling_Count'][i],
                                                    'ObjObjectId': msg['Object_TrackB']['ObjObjectId'][i],
                                                    'Width': msg['Object_TrackB']['Width'][i],
                                                    'Height': msg['Object_TrackB']['Height'][i],
                                                    'Object_Source_Camera': msg['Object_TrackB']['Object_Source_[Source]'][i][0],
                                                    'Object_Source_Radar': msg['Object_TrackB']['Object_Source_[Source]'][i][1],
                                                    'Object_Source_Ultrasonic': msg['Object_TrackB']['Object_Source_[Source]'][i][2],
                                                    'Object_Source_V2X': msg['Object_TrackB']['Object_Source_[Source]'][i][3],
                                                    'Object_Source_Lidar': msg['Object_TrackB']['Object_Source_[Source]'][i][4],
                                                    'Object_Source_Other': msg['Object_TrackB']['Object_Source_[Source]'][i][5]
                                                    })                                                    #Object_Relative_Orientation, RelLnPosition
        data4[i] = db.encode_message(msg_names[4], {'Rolling_Count': msg['Object_TrackC']['Rolling_Count'][i],
                                                    'ObjObjectId': msg['Object_TrackC']['ObjObjectId'][i],
                                                    'Object_Absolute_Velocity': msg['Object_TrackC']['Object_Absolute_Velocity'][i],
                                                    'Object_Course': msg['Object_TrackC']['Object_Course'][i],
                                                    'DynProp': msg['Object_TrackC']['DynProp'][i]
                                                    })                                                                               #Object_Latitude
        data5[i] = db.encode_message(msg_names[5], {'Rolling_Count': msg['Object_TrackD']['Rolling_Count'][i],
                                                    'ObjObjectId': msg['Object_TrackD']['ObjObjectId'][i]
                                                    })                                                                              #Object_Longitude
else:
    data2 = db.encode_message(msg_names[2], {'Rolling_Count': 0,
                                            'ObjObjectId': 0,
                                            'ObjObjectType': 0,
                                            'LongPos': 0,
                                            'LatPos': 0,
                                            'RelLongVel': 0,
                                            'RelLatVel': 0,
                                            'Relative_Lane': 0,
                                            })                                                                                            #Confidence
    data3 = db.encode_message(msg_names[3], {'Rolling_Count': 0,
                                            'ObjObjectId': 0,
                                            'Width': 0,
                                            'Height': 0,
                                            'Object_Source_Camera': 0,
                                            'Object_Source_Radar': 0,
                                            'Object_Source_Ultrasonic': 0,
                                            'Object_Source_V2X': 0,
                                            'Object_Source_Lidar': 0,
                                            'Object_Source_Other': 0
                                            })                                                            #Object_Relative_Orientation, RelLnPosition
    data4 = db.encode_message(msg_names[4], {'Rolling_Count': 0,
                                            'ObjObjectId': 0,
                                            'Object_Absolute_Velocity': 0,
                                            'Object_Course': 0,
                                            'DynProp': 0
                                            })                                                                                       #Object_Latitude
    data5 = db.encode_message(msg_names[5], {'Rolling_Count': 0,
                                            'ObjObjectId': 0
                                            })                                                                                      #Object_Longitude
data6 = db.encode_message(msg_names[6], {'Rolling_Count': msg['TrafficSignalHeads']['Rolling_Count'], 'Current_Signal_Head_Count': detected_signals})
                                                                                                                            #Observation_Time_of_Hour
if detected_signals > 0:
    for i in range(detected_signals):
        dict_temp = {'Rolling_Count': msg['TrafficSignalHead_TrackA']['Rolling_Count'][i],
                    'SignalObjectId': msg['TrafficSignalHead_TrackA']['SignalObjectId'][i],
                    'Height_Above_Ground': msg['TrafficSignalHead_TrackA']['Height_Above_Ground'][i],
                    'LongPos': msg['TrafficSignalHead_TrackA']['LongPos'][i],
                    'LatPos': msg['TrafficSignalHead_TrackA']['LatPos'][i],
                    }                                                                                                   #Confidence, Signal_Head_Type
        dict_temp.update(dict_light[msg['TrafficSignalHead_TrackA']['IllumLt'][i]])
        data7[i] = db.encode_message(msg_names[7], dict_temp)
else:
    dict_temp = {'Rolling_Count': 0,
                'SignalObjectId': 0,
                'Height_Above_Ground': 0,
                'LongPos': 0,
                'LatPos': 0,
                'IllumLtNone': 0, 'IllumLtRedBall': 0, 'IllumLtYellowBall': 0, 'IllumLtGreenBall': 0,
                'IllumLtFlshngRedBall': 0, 'IllumLtFlshngYellowBall': 0, 'IllumLtRedLeftArrow': 0,
                'IllumLtYellowLeftArrow': 0, 'IllumLtGreenLeftArrow': 0, 'IllumLtFlshngRedLeftArrow': 0,
                'IllumLtFlshngYellowLeftArrow': 0, 'IllumLtRedRightArrow': 0, 'IllumLtYellowRightArrow': 0,
                'IllumLtGreenRightArrow': 0, 'IllumLtFlshngRedRightArrow': 0, 'IllumLtFlshngYellowRightArrow': 0
                }                                                                                                       #Confidence, Signal_Head_Type
    data7 = db.encode_message(msg_names[7], dict_temp)
data8 = db.encode_message(msg_names[8], {'Rolling_Count': msg['TrafficSigns']['Rolling_Count'], 'Current_Sign_Count': detected_signs})
                                                                                                                            #Observation_Time_of_Hour
if detected_signs > 0:
    for i in range(detected_signals):
        data9[i] = db.encode_message(msg_names[9], {'Rolling_Count': msg['TrafficSign_TrackA']['Rolling_Count'][i],
                                                    'SignObjectId': msg['TrafficSign_TrackA']['SignObjectId'][i],
                                                    'LongPos': msg['TrafficSign_TrackA']['LongPos'][i],
                                                    'LatPos': msg['TrafficSign_TrackA']['LatPos'][i],
                                                    'Sign_Type': msg['TrafficSign_TrackA']['SignType'][i],
                                                    'Sign_Value': msg['TrafficSign_TrackA']['SignValue'][i]          
                                                    })                                                               #Confidence, Height_Above_Ground
else:
    data9 = db.encode_message(msg_names[9], {'Rolling_Count': 0,
                                            'SignObjectId': 0,
                                            'LongPos': 0,
                                            'LatPos': 0,
                                            'Sign_Type': 0,
                                            'Sign_Value': 0          
                                            }) 
data10 = db.encode_message(msg_names[10], {'Rolling_Count': msg['LaneMarkings']['Rolling_Count'], 'CurrentLaneMarkingCount': detected_markings})
                                                                                                                            #Observation_Time_of_Hour
if detected_markings > 0:
    for i in range(detected_markings):
        data11[i] = db.encode_message(msg_names[11], {'Rolling_Count': msg['LaneMarking_TrackA']['Rolling_Count'][i],
                                                    'LaneMarkingId': msg['LaneMarking_TrackA']['LaneMarkingId'][i],
                                                    'LaneMarkingLnDstV': msg['LaneMarking_TrackA']['LaneMarkingLnDstV'][i],
                                                    'LaneMarkingLnDst': msg['LaneMarking_TrackA']['LaneMarkingLnDst'][i],
                                                    'LaneMarkingLnMrkrTyp': msg['LaneMarking_TrackA']['LaneMarkingType'][i],
                                                    'LaneMarkingColor': msg['LaneMarking_TrackA']['LaneMarkingColor'][i],
                                                    }) '''LaneMarkingLnHdngTngtV, LaneMarkingLnHdngTngt, LaneMarkingLnCrvtV, LaneMarkingLnCrvtGradV, 
                                                                                LaneMarkingLnCrvtGrad, LaneMarkingLnCrvt, LaneMarkingLnQltyConfLvl'''
else:
    data11 = db.encode_message(msg_names[11], {'Rolling_Count': 0,
                                               'LaneMarkingId': 0,
                                               'LaneMarkingLnDstV': 0,
                                               'LaneMarkingLnDst': 0,
                                               'LaneMarkingLnMrkrTyp': 0,
                                               'LaneMarkingColor': 0,
                                              })        '''LaneMarkingLnHdngTngtV, LaneMarkingLnHdngTngt, LaneMarkingLnCrvtV, LaneMarkingLnCrvtGradV, 
                                                                                LaneMarkingLnCrvtGrad, LaneMarkingLnCrvt, LaneMarkingLnQltyConfLvl'''
data12 = db.encode_message(msg_names[12], {'Rolling_Count': msg['LimitLines']['Rolling_Count'], 'Current_Limit_Line_Count': detected_lines})
                                                                                                                            #Observation_Time_of_Hour
if detected_lines > 0:
    for i in range(detected_lines):
        data13[i] = db.encode_message(msg_names[13], {'Rolling_Count': msg['LimitLine_TrackA']['Rolling_Count'][i],
                                                    'LineObjectId': msg['LimitLine_TrackA']['LineObjectId'][i],
                                                    'LongPos': msg['LimitLine_TrackA']['LongPos'][i],
                                                    'LatPos': msg['LimitLine_TrackA']['LatPos'][i],
                                                    'Relative_Lane': msg['LimitLine_TrackA']['Relative_Lane'][i],
                                                    })                                                        #Confidence, Longitudinal_Length, Width
else:
    data13 = db.encode_message(msg_names[13], {'Rolling_Count': 0,
                                               'LineObjectId': 0,
                                               'LongPos': 0,
                                               'LatPos': 0,
                                               'Relative_Lane': 0,
                                              })                                                              #Confidence, Longitudinal_Length, Width

# data1=db.encode_message('AVState',{'UNUSED_MSG_PLACEHOLDER':0})
# data2=db.encode_message('Roadstate',{'Rolling_Count':0, 'Active_Traffic_Signal_Head_ID':0, 'Current_Observed_Speed_Limit':45, 'Next_Observed_Speed_Limit':0, 'Next_Observed_Speed_Limit_Longit':27.8, 'Active_Lane_Number':0, 'Left_Lane_Marking_ID':0, 'Right_Lane_Marking_ID':0, 'LLnDistanceValid':0, 'DistToLLnEdge':3, 'RLnDistanceValid':0, 'DistToRLnEdge':3})
# data3=db.encode_message('VehicleLocation',{'VehicleLatitude':90.00, 'VehicleLongitude':50.00})

# message1 = can.Message(arbitration_id=db.get_message_by_name('AVState').frame_id, data=data1)
# message3 = can.Message(arbitration_id=db.get_message_by_name('VehicleLocation').frame_id, data=data3)

message0 = can.Message(arbitration_id=db.get_message_by_name('RoadState').frame_id, data=data0)
message1 = can.Message(arbitration_id=db.get_message_by_name('Objects').frame_id, data=data1)
if detected_objects > 0:
    for i in range(detected_objects):
        message2[i] = can.Message(arbitration_id=db.get_message_by_name('Object_TrackA').frame_id, data=data2[i])
        message3[i] = can.Message(arbitration_id=db.get_message_by_name('Object_TrackB').frame_id, data=data3[i])
        message4[i] = can.Message(arbitration_id=db.get_message_by_name('Object_TrackC').frame_id, data=data4[i])
        message5[i] = can.Message(arbitration_id=db.get_message_by_name('Object_TrackD').frame_id, data=data5[i])
else:
    message2 = can.Message(arbitration_id=db.get_message_by_name('Object_TrackA').frame_id, data=data2)
    message3 = can.Message(arbitration_id=db.get_message_by_name('Object_TrackB').frame_id, data=data3)
    message4 = can.Message(arbitration_id=db.get_message_by_name('Object_TrackC').frame_id, data=data4)
    message5 = can.Message(arbitration_id=db.get_message_by_name('Object_TrackD').frame_id, data=data5)
message6 = can.Message(arbitration_id=db.get_message_by_name('TrafficSignalHeads').frame_id, data=data6)
if detected_signals > 0:
    for i in range(detected_signals):
        message7[i] = can.Message(arbitration_id=db.get_message_by_name('TrafficSignalHead_TrackA').frame_id, data=data7[i])
else:
    message7 = can.Message(arbitration_id=db.get_message_by_name('TrafficSignalHead_TrackA').frame_id, data=data7)
message8 = can.Message(arbitration_id=db.get_message_by_name('TrafficSigns').frame_id, data=data8)
if detected_signs > 0:
    for i in range(detected_signs):
        message9[i] = can.Message(arbitration_id=db.get_message_by_name('TrafficSign_TrackA').frame_id, data=data9[i])
else:
    message9 = can.Message(arbitration_id=db.get_message_by_name('TrafficSign_TrackA').frame_id, data=data9)
message10 = can.Message(arbitration_id=db.get_message_by_name('LaneMarkings').frame_id, data=data10)
if detected_markings > 0:
    for i in range(detected_markings):
        message11[i] = can.Message(arbitration_id=db.get_message_by_name('LaneMarking_TrackA').frame_id, data=data11[i])
else:
    message11 = can.Message(arbitration_id=db.get_message_by_name('LaneMarking_TrackA').frame_id, data=data11)
message12 = can.Message(arbitration_id=db.get_message_by_name('LimitLines').frame_id, data=data12)
if detected_lines > 0:
    for i in range(detected_lines):
        message13[i] = can.Message(arbitration_id=db.get_message_by_name('LimitLine_TrackA').frame_id, data=data13[i])
else:
    message13 = can.Message(arbitration_id=db.get_message_by_name('LaneMarking_TrackA').frame_id, data=data13)

while True:
    try:
        can_bus.send(message0)
        can_bus.send(message1)
        if detected_objects > 0:
            for i in range(detected_objects):
                can_bus.send(message2[i])
                can_bus.send(message3[i])
                can_bus.send(message4[i])
                can_bus.send(message5[i])
        else:
            can_bus.send(message2)
            can_bus.send(message3)
            can_bus.send(message4)
            can_bus.send(message5)
        can_bus.send(message6)
        if detected_signals > 0:
            for i in range(detected_signals):
                can_bus.send(message7[i])
        else:
            can_bus.send(message7)
        can_bus.send(message8)
        if detected_signs > 0:
            for i in range(detected_signs):
                can_bus.send(message9[i])
        else:
            can_bus.send(message9)
        can_bus.send(message10)
        if detected_markings > 0:
            for i in range(detected_markings):
                can_bus.send(message11[i])
        else:
            can_bus.send(message11)
        can_bus.send(message12)
        if detected_lines > 0:
            for i in range(detected_lines):
                can_bus.send(message13[i])
        else:
            can_bus.send(message13)
    except:
        continue
        

