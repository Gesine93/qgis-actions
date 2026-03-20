from qgis.core import QgsProject, QgsRelation, QgsEditFormConfig, QgsReadWriteContext
from qgis.PyQt.QtXml import QDomDocument
 
# Variables that need to be changed
referenced_name = "" # Name of the layer in whose form the "referencing" attributes should be displayed
referencing_names = [] # Names of the layers whose attributes should be displayed in the attribute form of the "referenced layer"; comma-separated list
 
pk = [] # Fields in the referenced layer that are linked via the foreign key in the referencing layers; comma-separated list
fk = [] # Foreign key fields in the referencing layers; comma-separated list
 
rel_name = [] # Names must match the already created relations implemented in the referenced layer form; comma-separated list
rel_id =  [] # IDs must match the already created relations implemented in the referenced layer form; comma-separated list
 
def get_layer_by_name(name):
    layers = QgsProject.instance().mapLayersByName(name)
    return layers[0] if layers else None
 
for i in range(0,len(fk)):
	referenced = get_layer_by_name(referenced_name )
	referencing = get_layer_by_name(referencing_names[i] )
 
	if not referenced or not referencing:
		raise Exception("Layer not found")
 
	rel = QgsRelation()
	rel.setReferencingLayer(referencing.id())
	rel.setReferencedLayer(referenced.id())
	rel.addFieldPair(fk[i], pk[i])
	rel.setName(rel_name[i])
	rel.setId(rel_id[i])
 
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
