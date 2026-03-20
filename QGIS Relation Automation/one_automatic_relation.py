from qgis.core import QgsProject, QgsRelation, QgsEditFormConfig, QgsReadWriteContext
from qgis.PyQt.QtXml import QDomDocument
 
# Variables that need to be changed
referenced_name = "" # Name of the layer in whose form the "referencing" attributes should be displayed
referencing_name = "" # Name of the layer whose attributes should be displayed in the attribute form of the "referenced" layer
 
pk = "" # Field in the referenced layer that is linked via the foreign key in the referencing layer
fk = "" # Foreign key field in the referencing layer
 
rel_name = "" # Must match the name of the already created relation implemented in the referenced layer form
rel_id =  "" # Must match the ID of the already created relation implemented in the referenced layer form
 
def get_layer_by_name(name):
    layers = QgsProject.instance().mapLayersByName(name)
    return layers[0] if layers else None
 
referenced = get_layer_by_name(referenced_name )
referencing = get_layer_by_name(referencing_name )
 
if not referenced or not referencing:
    raise Exception("Layer not found")
 
rel = QgsRelation()
rel.setReferencingLayer(referencing.id())
rel.setReferencedLayer(referenced.id())
rel.addFieldPair(fk, pk)
rel.setName(rel_name)
rel.setId(rel_id)
 
if rel.isValid():
    QgsProject.instance().relationManager().addRelation(rel)
 
else:
    raise Exception("Relation is invalid")
 
# Update form config
form_config = referenced.editFormConfig()
cfg = referenced.editFormConfig()
doc = QDomDocument()
context = QgsReadWriteContext()     
cfg.writeXml(doc, context)           
new_cfg = QgsEditFormConfig()
new_cfg.readXml(doc, context)        
 
referenced.setEditFormConfig(new_cfg)
referenced.setEditFormConfig(form_config)
referenced.triggerRepaint()
