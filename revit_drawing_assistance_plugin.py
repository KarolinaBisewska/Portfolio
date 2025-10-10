# Plugin function:
#   1. Floor Plans
#      a) automaticaly place dimentions on all the walls in active sheet view
#          - retrieve all revit family types for dimentions from the project and present them in a drop down menu -> use selected family to place dimentions
#          - select all the walls available in the current view  
#          -
#      b) door tags
#          - retrieve all revit family types for door tags from the project and present them in a drop down menu -> use selected family to place door tags
#          - detect whether the door in oriented vertically or horizontally - based on that place a tag as per door location
#          - create an offset parameter that would determine the offset of dimension to the door
#
#      c) door setting out:
#          - retrieve all revit family types for dimentions from the project and present them in a drop down menu -> use selected family to place dimentions
#          - checks for the door reference line and the closest nearby wall that is rotated in the opposite direction than the door and then place the dimension from face of that wall to the door reference line
#          - create an offset parameter that would determine the offset of dimension to the door
#      d) 
#
#
#
#
#
#
#
#
#
#
#
# All options should be optional - you activate it by checking in a checkbox next to function (f.e Floor Plan Dimensions (checked/unchecked)).
