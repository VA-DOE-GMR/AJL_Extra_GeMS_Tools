# AJL_Extra_GeMS_Tools
Companion tools to be used for GeMS-related projects to help simplify and/or automate certain tasks.

# Current Tools

## Clear and Reset Identifier Fields:

This tool resets the identifier fields (i.e. fields with names ending in "_ID" excluding DataSources and GeoMaterialDict tables) so that they are numbered according to the OID values and ensures that numbers are not skipped.

## Fill MapUnit Field for Point Feature Classes

This tool automatically fills out all point feature classes fields with a MapUnit field with the corresponding MapUnit value of the polygon of MapUnitPolys that they are located within. Polygons without MapUnit information (i.e. Null values) are skipped and ignored for this process.

## Alphabetize Glossary Table

This tool reorders the items in the Glossary table so that the terms are in alphabetical order.

## Autopopulate DataSources Table

This tool finds all DASID values used in the GeMS geodatabase currently selected and fills out the DataSources table with said information based upon the DataSources.xlsx file that contains all information related to DASIDs. The DataSources.xlsx is replaced with an updated version of the list of DASIDs if one is found.

## Fill Symbol Field for Polygon Feature Classes

This tool automatically fills out all MapUnitPolys and MapUnitOverlayPolys Symbol fields based upon information from DescriptionOfMapUnits table. Polygons without MapUnit information (i.e. Null values) are skipped and ignored for this process.

## Disable Editor Tracking and Delete Related Fields

This tool disables ArcGIS Pro's Editor Tracking for all tables and feature classes with this enabled and then deletes tables related to this information. This information will not affect vital information for GeMS feature classes and tables; however, the removal of Editor Tracking related fields is not reversable. Ergo, a warning is presented that clarifies that this change is permanent. This is done as the other tools currently made for this program do not explicitly alter pre-existing features and/or tables in this manner.

## FaultDecorations
This allows the user to add FaultDecorations point feature classes to the geodatabase's datasets. This tool exists since, as of right now, the GeMS toolbox does not have the ability to generate this feature class and has to be otherwise be created manually. This brings up a dynamic list of datasets currently present in the GeMS geodatabase that the user can choose to add FaultDecorations point feature classes to. However, if FaultDecorations already exists in a dataset, the pre-existing FaultDecorations point feature classes will not be touched and no FaultDecorations point feature class will be generated for that dataset.

# init.txt

## Related to SDE

SDE_SERVER_TYPE: This refers to the type of server being connected to.

SDE_INSTANCE: This refers to the specific identifier for the server desired being connected to.

SDE_AUTHENTICATION: This refers to the account authentication process being used in order for the SDE to be valid.

SDE_DATABASE: This specifies the database that the user wants access to.

# Running Instructions
Right-click on "main.py" and either select "Run with ArcGIS Pro" or "Edit with IDLE (ArcGIS Pro)" and run it within IDLE. Please note the right-click context menu may differ depending on the version of Windows OS that you are using as well as other factor; however, it more or less should be the same.

You will be prompted to select a folder. It is expecting you to select a .gdb folder related to a GeMS project. It will not continue continue until a GeMS-related geodatabase is selected.

Note: It is recommended that you create backups of your geodatabase before using this tool to be safe.

# Requirements
1) ArcGIS Pro 3.1+ (Note: the required Python version and Python modules should be included with the installation of ArcGIS Pro)
2) Windows OS
3) 2 GiB of RAM (Recommended)

# Things to be done
1) Ensure functionality on network drives.
2) Improve UI layout and make it more visually pleasing.
3) Provide more detailed documentation for how code works.


# Known Issues
1) This has been only been tested with Python implimentations available via ArcGIS Pro 3.1+
2) This has not been tested to work within ArcGIS Pro. It is intended to function outside the program only utilizing the arcpy module.
3) Terminal log of processes needs to be more thorough and easier to understand what is doing for users.
4) Program has not been tested to be able to run on non-Windows OSs (i.e., specifically, MacOS and Linux variants). It is expected not to work as it was made with running on a Windows OS in mind. Support for such operating systems may be considered in the future if deemed necessary.
