Title:
Create and Apply one or many QGIS Relation Programmatically with Form Update

Description:
These scripte create one or many relations between QGIS layers using a primary key–foreign key pair and ensures that the relation is correctly reflected in the attribute form of the referenced (parent) layer.

Key Features:

Dynamically retrieves layers by name

Defines a QgsRelation between a parent (referenced) and one or many child (referencing) layer(s)

Validates and registers the relation(s) in the QGIS project

Updates the edit form configuration via XML to ensure the relation widget is properly displayed

Triggers a repaint to apply visual updates

Use Case:
Useful for automating the setup of relational forms in QGIS projects, when two or more layers, that are referencing eachother, have to be loaded into QGIS regularly (e.g. when using the QGIS Plugin Map Library).
