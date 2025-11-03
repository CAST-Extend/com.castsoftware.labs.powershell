"""
API for testing

- use sqllite as a server
- a 'small' schema is built

"""
import lxml.etree as ET
import os
from datetime import date
from .metamodel import read_metamodel
from sqlalchemy import Table, MetaData, select, func


def create_schema(engine):
    """
    Create the minimal schema for object access.
    
    Usefull for testing in an in memory database
    
    """
    conn = engine.raw_connection()
    
    conn.executescript(script_create)

def clean_data(engine):
    """
    reset all tables except mm
    """
    conn = engine.raw_connection()
    
    conn.executescript(delete_script)

def load_metamodel_from_disk(engine, auto=True, dependency_to_load=[]):
    """
    load the metamodel from disk
    
    if auto is True then the dependencies will be calculated automatically
    if dependency_to_load is provided, this will be the list of dependencies extension to load
    assuming them to be 'local' side by side with current plugin
    """
    
    metamodel = read_metamodel(_collect_metamodel_folders(dependency_to_load), 
                               allow_partial=True,
                               allow_test_metamodel=True)
    
    if engine:
        
        metadata = MetaData(bind=engine)
        Typ = Table("typ", metadata, autoload=True, autoload_with=engine)
        Cat = Table("cat", metadata, autoload=True, autoload_with=engine)
        TypCat = Table("typcat", metadata, autoload=True, autoload_with=engine)
        CatCat = Table("catcat", metadata, autoload=True, autoload_with=engine)
        Prop = Table("prop", metadata, autoload=True, autoload_with=engine)
        PropCat = Table("propcat", metadata, autoload=True, autoload_with=engine)
        TypProp = Table("typprop", metadata, autoload=True, autoload_with=engine)
        PropAttr = Table("propattr", metadata, autoload=True, autoload_with=engine)
        
        typ_values = []
        typcat_values = []
        typprop_values = []
        propattr_values = []

        prop_values = []
        
        cat_values = []
        catcat_values = []
        propcat_values = []
        
        for category in metamodel.get_categories():

            if not category.id:
                continue

            if category.is_type():
                
                typ_values.append({'idtyp':category.id,
                                   'typnam':category.name,
                                   'typdsc':category.description if category.description else '',
                                   'status':'ACTIVE'})
                
                for parent in category.all_inherited_categories:
                    
                    typcat_values.append({'idtyp':category.id,
                                          'idcatparent':parent.id,
                                          'iscatprop':1 if parent in category.inherited_categories else 0,
                                          'status':'ACTIVE'})
                
                for prop in category.properties:
                    
                    typprop_values.append({'idtyp':category.id,
                                           'idprop':prop.id,
                                           'status':'ACTIVE'})      
                
            else:

                cat_values.append({'idcat':category.id,
                                   'catnam':category.name,
                                   'catdsc':category.description if category.description else '',
                                   'status':'ACTIVE'})
                for parent in category.inherited_categories:
                    
                    catcat_values.append({'idcat':category.id,
                                          'idcatparent':parent.id,
                                          'status':'ACTIVE'})
                
                for prop in category.properties:
                    
                    propcat_values.append({'idcat':category.id,
                                           'idprop':prop.id,
                                           'status':'ACTIVE'})
 
                
        for prop in metamodel.get_properties():
            
            m = {'integer':137475, 'string':137476, 'bookmark':137477, 'dateTime':137478, 'reference':1028}
            
            property_type = 1028
            try:
                property_type = m[prop.type]
            except:
                pass
            
            prop_values.append({'idprop':prop.id,
                                'propnam':prop.name,
                                'propdsc':prop.description if prop.description else '',
                                'proptyp':property_type,
                                'propmrg':"NON",
                                'cardmin':prop.minimal_cardinality,
                                'cardmax':prop.maximal_cardinality,
                                'status':'ACTIVE'})

            for attribute_name, attribute_val in prop.attributes.items():
                intval = None
                strval = None
                if isinstance(attribute_val, int):
                    attrtyp = 137475
                    intval = attribute_val
                    
                else:
                    attrtyp = 137476
                    strval = attribute_val
                    
                propattr_values.append({'idprop':prop.id,
                                        'attrnam':attribute_name,
                                        'attrtyp':attrtyp,
                                        'intval':intval,
                                        'strval':strval,
                                        'status':'ACTIVE'})


        engine.execute(Typ.insert(), typ_values)
        engine.execute(TypCat.insert(), typcat_values)
        engine.execute(TypProp.insert(), typprop_values)
        
        engine.execute(Cat.insert(), cat_values)
        engine.execute(CatCat.insert(), catcat_values)
        engine.execute(PropCat.insert(), propcat_values)
        
        engine.execute(Prop.insert(), prop_values)
        engine.execute(PropAttr.insert(), propattr_values)
             
    return metamodel


def generate_keys_acc_id(engine):

    metadata = MetaData(bind=engine)
    KEYACCSequence = Table("KEYACCSequence", metadata, autoload=True, autoload_with=engine)
    
    ins = KEYACCSequence.insert()
    result = engine.execute(ins)
    return result.inserted_primary_key[0]
    
    
def create_application(engine, application_name):
    """
    Create an application of a given name.
    
    @todo : check that application name is unique ?
    """
    metadata = MetaData(bind=engine)
    UsrPro = Table("usrpro", metadata, autoload=True, autoload_with=engine)
    Keys = Table("keys", metadata, autoload=True, autoload_with=engine)
    USERPROJECT = 669
    # insert in keys
    application_id = generate_keys_acc_id(engine)
    ins = Keys.insert().values(idkey=application_id,
                               keynam=application_name,
                               objtyp=USERPROJECT,
                               keytyp='XXXXXX',
                               keysubtyp=-1,
                               keyclass=20150,
                               keyprop=0,
                               idusrdevpro='???',
                               keydevdat=date.today())
    result = engine.execute(ins)
    
    # insert in usrpro
    ins = UsrPro.insert().values(idusrpro=application_id,
                                 usrpronam=application_name,
                                 ordnum=1)
    
    engine.execute(ins)
    
    return application_id


def create_project(engine, application_id, project_name, project_type = None):
    """
    Create a result project.
    """
    metadata = MetaData(bind=engine)
    UsrProRoot = Table("usrproroot", metadata, autoload=True, autoload_with=engine)
    ProDep = Table("prodep", metadata, autoload=True, autoload_with=engine)
    Keys = Table("keys", metadata, autoload=True, autoload_with=engine)
    ObjPro = Table("objpro", metadata, autoload=True, autoload_with=engine)
    CAST_DotNet_Project = 137017
    
    # insert in keys
    ptype = project_type
    if not ptype:
        ptype = CAST_DotNet_Project
    
    project_id = generate_keys_acc_id(engine)
    ins  = Keys.insert().values(idkey = project_id,
                                keynam=project_name,
                                objtyp=ptype,
                                keytyp='XXXXXX',
                                keysubtyp=-1,
                                keyclass=0, # keyclass is obsolete 
                                keyprop=0,
                                idusrdevpro='???',
                                keydevdat=date.today())
    result = engine.execute(ins)
    
    # insert in usrproroot
    ins = UsrProRoot.insert().values(idusrpro=application_id,
                                     idroot=project_id,
                                     prop=0)
    
    engine.execute(ins)
    
    ins = ProDep.insert().values(idpromain=project_id,
                                 idpro=project_id,
                                 prop=0)
    
    engine.execute(ins)
    
    # insert in objpro
    ins = ObjPro.insert().values(idobj=project_id,
                                 idpro=project_id,
                                 prop=0)
    
    engine.execute(ins)
    
    return project_id

def create_object(engine, project_id, name, objtyp, internal=True, fullname=None, keyprop=0):
    """
    Create an object in a project
    """
    metadata = MetaData(bind=engine)
    Keys = Table("keys", metadata, autoload=True, autoload_with=engine)
    ObjPro = Table("objpro", metadata, autoload=True, autoload_with=engine)

    # insert in keys
    object_id = generate_keys_acc_id(engine)
    ins = Keys.insert().values(idkey = object_id, 
                               keynam = name, 
                               objtyp = objtyp,
                               keytyp = 'XXXXXX', 
                               keysubtyp = -1, 
                               keyclass = 0, # keyclass is obsolete
                               keyprop = keyprop, 
                               idusrdevpro = '???',
                               keydevdat = date.today())
    result = engine.execute(ins)
    
    # insert in objpro
    ins = ObjPro.insert().values(idobj = object_id,
                                 idpro = project_id,
                                 prop = 0 if internal else 1)
    
    engine.execute(ins)
    
    if fullname:
        ObjFulNam = Table("objfulnam", metadata, autoload=True, autoload_with=engine)

        ins = ObjFulNam.insert().values(idobj = object_id,
                                        fullname = fullname)
        engine.execute(ins)
    
    return object_id


def add_object_to_project(engine, object_id, project_id, internal):
    
    metadata = MetaData(bind=engine)
    ObjPro = Table("objpro", metadata, autoload=True, autoload_with=engine)
    
    # insert in objpro
    ins = ObjPro.insert().values(idobj = object_id,
                                 idpro = project_id,
                                 prop = 0 if internal else 1)
    
    engine.execute(ins)
    

def create_object_with_parent(engine, project_id, name, objtyp, parent_id, internal = True, keyprop=0, fullname=None):
    """
    Create an object in a project under a parent
    """
    object_id = create_object(engine, project_id, name, objtyp, internal, fullname, keyprop)
    # insert in keypar
    metadata = MetaData(bind=engine)
    KeyPar = Table("keypar", metadata, autoload=True, autoload_with=engine)

    ins = KeyPar.insert().values(idkey = object_id,
                                 idparent = parent_id)
    
    engine.execute(ins)
    
    return object_id

def create_file(engine, project_id, name, objtyp, path, internal=True):

    metadata = MetaData(bind=engine)
    RefPath = Table("refpath", metadata, autoload=True, autoload_with=engine,)
    ObjFilRef = Table("objfilref", metadata, autoload=True, autoload_with=engine)
    
    object_id = create_object(engine, project_id, name, objtyp, internal)
    
    ins = RefPath.insert().values(path=path)
    result = engine.execute(ins)
    idfilref = result.inserted_primary_key[0]

    ins = ObjFilRef.insert().values(idobj=object_id,
                                    idfilref=idfilref,
                                    idfil=object_id)
    engine.execute(ins)
    
    return object_id

def create_file_with_parent(engine, project_id, name, objtyp, path, parent_id, internal=True):

    metadata = MetaData(bind=engine)
    RefPath = Table("refpath", metadata, autoload=True, autoload_with=engine,)
    ObjFilRef = Table("objfilref", metadata, autoload=True, autoload_with=engine)
    
    object_id = create_object_with_parent(engine, project_id, name, objtyp, parent_id, internal)
    
    ins = RefPath.insert().values(path=path)
    result = engine.execute(ins)
    idfilref = result.inserted_primary_key[0]

    ins = ObjFilRef.insert().values(idobj=object_id,
                                    idfilref=idfilref,
                                    idfil=object_id)
    engine.execute(ins)
    
    return object_id


def create_link(engine, project_id, caller, callee, link_type, prop=0):
    """
    return Acc link id
    """
    metadata = MetaData(bind=engine)
    Acc = Table("acc", metadata, autoload=True, autoload_with=engine)
    FusAcc = Table("fusacc", metadata, autoload=True, autoload_with=engine)

    link_id = generate_keys_acc_id(engine)
    ins = Acc.insert().values(idacc=link_id,
                              idclr=caller,
                              idcle=callee,
                              acctyplo=link_type[0],
                              acctyphi=link_type[1],
                              acctyplo2 = 0, # do not care
                              acctyphi2 = 0, # do not care
                              accknd = 0, # do not care for now
                              idpro = project_id,
                              prop = prop 
                              )
    
    result = engine.execute(ins)

    # search in fusacc if we already have a idfus
    query_acc = select([Acc.c.idacc]).where(Acc.c.idclr==caller).where(Acc.c.idcle==callee)
    query_exist = select([FusAcc.c.idfus]).where(FusAcc.c.idacc.in_(query_acc))
    
    idfus = None
    for line in engine.execute(query_exist):
        idfus = line[0]
        
    if idfus is None:
        # new link, generate an id
        idfus = generate_keys_acc_id(engine)
    
    ins = FusAcc.insert().values(idfus=idfus,
                                 idacc=link_id)
    
    engine.execute(ins)
    
    return link_id
    
    
def add_position(engine, object_id, file_id, begin_line, begin_column, end_line, end_column):
    """
    Add position on an object
    """
    metadata = MetaData(bind=engine)
    ObjPos = Table("objpos", metadata, autoload=True, autoload_with=engine)

    ins = ObjPos.insert().values(idobj=object_id,
                                 idobjref=file_id,
                                 posmode=2,
                                 info1=begin_line,
                                 info2=begin_column,
                                 info3=end_line,
                                 info4=end_column,
                                 prop=0,
                                 blkno=file_id)
    
    engine.execute(ins)

def add_link_position(engine, link_id, file_id, begin_line, begin_column, end_line, end_column):
    """
    Add position on a link
    @todo
    """
    metadata = MetaData(bind=engine)
    AccBook = Table("accbook", metadata, autoload=True, autoload_with=engine)

    ins = AccBook.insert().values(idacc=link_id,
                                  bookmode=2,
                                  info1=begin_line,
                                  info2=begin_column,
                                  info3=end_line,
                                  info4=end_column,
                                  prop=0,
                                  blkno=file_id)
    
    engine.execute(ins)

def add_property(engine, object_id, inftyp, infsubtyp, value):
    """
    Add a property on an object
    """
    metadata = MetaData(bind=engine)
    
    if type(value) is int:
        
        ObjInf = Table("objinf", metadata, autoload=True, autoload_with=engine)
        
        ins = ObjInf.insert().values(idobj=object_id,
                                     inftyp=inftyp,
                                     infsubtyp=infsubtyp,
                                     blkno=0,
                                     infval=value)
        engine.execute(ins)
        
    elif type(value) is str:
        
        ObjDsc = Table("objdsc", metadata, autoload=True, autoload_with=engine)

        values = [value]

        if len(value) > 255:
            values =[value[i:i+255] for i in range(0, len(value), 255)]
        ordnum = 0    
        
        for val in values:
            ins = ObjDsc.insert().values(idobj=object_id,
                                         inftyp=inftyp,
                                         infsubtyp=infsubtyp,
                                         blkno=0,
                                         ordnum=ordnum,
                                         prop=0,
                                         infval=val)
            engine.execute(ins)
            ordnum += 1


    elif type(value) is list and value:
        
        first_value = value[0]
        
        if type(first_value) is int:
            
            ObjInf = Table("objinf", metadata, autoload=True, autoload_with=engine)
            blkno = 0
            for v in value:
                
                
                ins = ObjInf.insert().values(idobj=object_id,
                                             inftyp=inftyp,
                                             infsubtyp=infsubtyp,
                                             blkno=blkno,
                                             infval=v)
                engine.execute(ins)
                blkno += 1
            
        elif type(first_value) is str:
            
            ObjDsc = Table("objdsc", metadata, autoload=True, autoload_with=engine)
    
            blkno = 0
            for v in value:
                
                values = [v]
        
                if len(v) > 255:
                    values = [v[i:i+255] for i in range(0, len(v), 255)]
                ordnum = 0    
                
#                 print('values=', values)
                
                for val in values:
                
                    ins = ObjDsc.insert().values(idobj=object_id,
                                                 inftyp=inftyp,
                                                 infsubtyp=infsubtyp,
                                                 blkno=blkno,
                                                 ordnum=ordnum,
                                                 prop=0,
                                                 infval=val)
                    engine.execute(ins)
                    ordnum += 1
                    
                blkno += 1


def add_link_property(engine, link_id, inftyp, infsubtyp, value):
    """
    
    """
    metadata = MetaData(bind=engine)
    FusAcc = Table("fusacc", metadata, autoload=True, autoload_with=engine)
    
    query_exist = select([FusAcc.c.idfus]).where(FusAcc.c.idacc==link_id)
    
    idfus = None
    for line in engine.execute(query_exist):
        idfus = line[0]
        
    if idfus is None:
        raise RuntimeError("Could not find FuAcc for link %s in add_link_property" % str(link_id))
    add_property(engine, idfus, inftyp, infsubtyp, value)



script_create = """

/* Fake table to generate ids for Keys, Acc and FusAcc which share the same ids */
CREATE TABLE KEYACCSequence(objectid integer primary key autoincrement);

    
CREATE TABLE anaattr
(
  session_id integer NOT NULL,
  attrnam VARCHAR(255) NOT NULL,
  intval integer
);
    
CREATE TABLE sys_package_version
(
  package_name VARCHAR(100) NOT NULL,
  version VARCHAR(30) NOT NULL
);
    
CREATE TABLE usrpro (
    idusrpro INTEGER NOT NULL, 
    usrpronam VARCHAR(255) NOT NULL, 
    ordnum INTEGER
);

CREATE TABLE proroot
(
  idpro integer NOT NULL,
  idroot integer NOT NULL
);

CREATE UNIQUE INDEX pk_usrpro ON usrpro (idusrpro);


CREATE TABLE usrprojob (
    idusrpro INTEGER NOT NULL, 
    idjob INTEGER NOT NULL, 
    ordnum INTEGER NOT NULL, 
    prop INTEGER NOT NULL
)

;
CREATE INDEX idx_usrprojob ON usrprojob (idusrpro, idjob);

CREATE TABLE dss_positions
(
  metricpositionid integer NOT NULL,
  objectid integer NOT NULL,
  propertyid integer,
  sourceid integer NOT NULL,
  positionid integer NOT NULL,
  positionindex integer,
  linestart integer NOT NULL,
  colstart integer NOT NULL,
  lineend integer NOT NULL,
  colend integer NOT NULL
);


CREATE TABLE anajob (
    idjob INTEGER NOT NULL, 
    jobnam VARCHAR(255) NOT NULL, 
    jobtyp INTEGER NOT NULL, 
    jobver INTEGER NOT NULL, 
    idcnx INTEGER, 
    jobbegindate TIMESTAMP, 
    jobenddate TIMESTAMP
)

;
CREATE UNIQUE INDEX pk_anajob ON anajob (idjob);

CREATE TABLE acc
(
  idacc integer NOT NULL,
  idclr integer NOT NULL,
  idcle integer NOT NULL,
  acctyplo integer NOT NULL,
  acctyphi integer NOT NULL,
  acctyplo2 integer NOT NULL,
  acctyphi2 integer NOT NULL,
  accknd integer NOT NULL,
  idpro integer NOT NULL,
  prop integer NOT NULL DEFAULT 0,
  CONSTRAINT pk_accidacc PRIMARY KEY (idacc)
);

CREATE TABLE fusacc
(
  idfus integer NOT NULL,
  idacc integer NOT NULL
);

CREATE TABLE prodep (
    idpromain INTEGER NOT NULL, 
    idpro INTEGER NOT NULL, 
    prop INTEGER NOT NULL
)

;
CREATE INDEX idx2_prodep ON prodep (idpro);
CREATE INDEX idx1_prodep ON prodep (idpromain);

CREATE TABLE refpath (
    idfilref INTEGER NOT NULL, 
    path VARCHAR(600) NOT NULL,
    CONSTRAINT pk_refpathidfilref PRIMARY KEY (idfilref)
);
CREATE UNIQUE INDEX pk_refpath ON refpath (idfilref);
CREATE UNIQUE INDEX refpath_path ON refpath (path);
CREATE TABLE objpro (
    idobj INTEGER NOT NULL, 
    idpro INTEGER NOT NULL, 
    prop INTEGER NOT NULL
);


CREATE INDEX objpro_obj ON objpro (idobj);
CREATE UNIQUE INDEX objpro_proobj ON objpro (idpro, idobj);

CREATE TABLE objfilref (
    idobj INTEGER NOT NULL, 
    idfilref INTEGER NOT NULL, 
    idfil INTEGER
);


CREATE INDEX objfilref_idfil ON objfilref (idfil);
CREATE INDEX objfilref_idobj ON objfilref (idobj);

CREATE TABLE usrproroot (
    idusrpro INTEGER NOT NULL, 
    idroot INTEGER NOT NULL, 
    prop INTEGER NOT NULL
);


CREATE INDEX idx_usrproroot ON usrproroot (idusrpro);

CREATE TABLE keys (
    idkey INTEGER NOT NULL, 
    keynam VARCHAR(255), 
    keylib VARCHAR(255), 
    keytyp CHAR(6) NOT NULL, 
    keysubtyp INTEGER NOT NULL, 
    keyclass INTEGER NOT NULL, 
    keyprop INTEGER NOT NULL, 
    objtyp INTEGER NOT NULL, 
    idusrdevpro CHAR(3) NOT NULL, 
    keydevdat TIMESTAMP NOT NULL, 
    keydevvlddat TIMESTAMP, 
    status INTEGER DEFAULT 0, 
    sqlowner VARCHAR(128), 
    CONSTRAINT pk_keysidkey PRIMARY KEY (idkey)
);


CREATE INDEX keys_classidproptyp ON keys (keyclass, idkey, keyprop, objtyp);
CREATE INDEX keys_keynam ON keys (keynam, objtyp);


CREATE TABLE objects
(
  idkey integer NOT NULL,
  idnam character varying(1015) NOT NULL,
  idshortnam character varying(600) NOT NULL,
  objtyp integer NOT NULL
);

CREATE INDEX idx2_objects ON objects (idkey);

CREATE TABLE objfulnam (
    idobj INTEGER NOT NULL, 
    fullname VARCHAR(255)
);

CREATE INDEX objfulnam_idobj ON objfulnam (idobj);


CREATE TABLE objinf
(
  idobj integer NOT NULL,
  inftyp integer NOT NULL,
  infsubtyp integer NOT NULL,
  blkno integer NOT NULL,
  infval integer NOT NULL
);

CREATE INDEX pk_objinf ON objinf (idobj, inftyp, infsubtyp, blkno);

CREATE TABLE objdsc
(
  idobj integer NOT NULL,
  inftyp integer NOT NULL,
  infsubtyp integer NOT NULL,
  blkno integer NOT NULL,
  ordnum integer NOT NULL,
  prop integer NOT NULL,
  infval VARCHAR(255),
  CONSTRAINT pk_objdsc PRIMARY KEY (idobj, inftyp, infsubtyp, blkno, ordnum)
);

   
CREATE TABLE typcat (
    idtyp INTEGER NOT NULL, 
    idcatparent INTEGER NOT NULL, 
    iscatprop INTEGER NOT NULL, 
    status CHAR(10) NOT NULL
);


CREATE INDEX typcat_335 ON typcat (idtyp);
CREATE INDEX idx_typcat ON typcat (idcatparent, idtyp);

CREATE TABLE typ (
    idtyp INTEGER NOT NULL, 
    typnam VARCHAR(255) NOT NULL, 
    typdsc VARCHAR(255) NOT NULL, 
    status CHAR(10) NOT NULL
);
CREATE UNIQUE INDEX idx_typ ON typ (idtyp);

CREATE TABLE cat (
    idcat INTEGER NOT NULL, 
    catnam VARCHAR(255) NOT NULL, 
    catdsc VARCHAR(255) NOT NULL, 
    status CHAR(10) NOT NULL
);
CREATE UNIQUE INDEX idx_cat ON cat (idcat);

CREATE TABLE catcat (
    idcat INTEGER NOT NULL, 
    idcatparent INTEGER NOT NULL, 
    status CHAR(10) NOT NULL
);
CREATE INDEX idx_catcat ON catcat (idcatparent);

CREATE TABLE prop (
    idprop INTEGER NOT NULL, 
    propnam VARCHAR(255) NOT NULL, 
    propdsc VARCHAR(255) NOT NULL, 
    proptyp INTEGER NOT NULL, 
    propmrg CHAR(3) NOT NULL, 
    cardmin INTEGER, 
    cardmax INTEGER, 
    status CHAR(10) NOT NULL
)

;
CREATE INDEX idx_prop ON prop (idprop);

CREATE TABLE propcat (
    idprop INTEGER NOT NULL, 
    idcat INTEGER NOT NULL, 
    status CHAR(10) NOT NULL
)

;
CREATE INDEX idx_propcat ON propcat (idcat);

CREATE TABLE typprop (
    idtyp INTEGER NOT NULL, 
    idprop INTEGER NOT NULL, 
    status CHAR(10) NOT NULL
)

;
CREATE INDEX idx_typprop ON typprop (idtyp);

CREATE TABLE propattr
(
  idprop integer NOT NULL,
  attrnam VARCHAR(255),
  attrtyp integer NOT NULL,
  intval integer,
  strval VARCHAR(255),
  status CHAR(10) NOT NULL
);

CREATE TABLE catattr
(
  idcat integer NOT NULL,
  attrnam character varying(255),
  attrtyp integer NOT NULL,
  intval integer,
  strval character varying(255),
  status character(10) NOT NULL
);

CREATE TABLE typattr
(
  idtyp integer NOT NULL,
  attrnam character varying(255),
  attrtyp integer NOT NULL,
  intval integer,
  strval character varying(255),
  status character(10) NOT NULL
);

CREATE TABLE objpos (
    idobj INTEGER NOT NULL, 
    idobjref INTEGER NOT NULL, 
    posmode INTEGER NOT NULL, 
    info1 INTEGER NOT NULL, 
    info2 INTEGER, 
    info3 INTEGER, 
    info4 INTEGER, 
    prop INTEGER, 
    blkno INTEGER
)

;
CREATE INDEX objpos_idobjref ON objpos (idobjref);
CREATE INDEX objpos_idobj ON objpos (idobj);
    
CREATE TABLE in_objects (
    session_id INTEGER NOT NULL, 
    object_id INTEGER NOT NULL, 
    name_id VARCHAR(1015) NOT NULL, 
    short_name_id VARCHAR(600) NOT NULL, 
    object_type_id INTEGER NOT NULL
)

;
CREATE INDEX idx_inobjects ON in_objects (object_id);

CREATE TABLE in_links (
    session_id INTEGER NOT NULL, 
    link_id INTEGER NOT NULL, 
    source_id INTEGER NOT NULL, 
    target_id INTEGER NOT NULL, 
    project_id INTEGER NOT NULL, 
    source_kind CHAR(1) NOT NULL, 
    target_kind CHAR(1) NOT NULL, 
    project_kind CHAR(1) NOT NULL, 
    link_type_id INTEGER NOT NULL
)

;
CREATE INDEX idxs_link ON in_links (source_id);
CREATE UNIQUE INDEX idxl_link ON in_links (link_id, session_id);
CREATE INDEX idxt_link ON in_links (target_id);

CREATE TABLE in_char_properties (
    session_id INTEGER NOT NULL, 
    object_id INTEGER NOT NULL, 
    property_type_id INTEGER NOT NULL, 
    property_offset INTEGER NOT NULL, 
    char_block INTEGER NOT NULL, 
    property_char VARCHAR(255)
)

;
CREATE INDEX idx_incharprop ON in_char_properties (object_id, property_type_id, session_id);

CREATE TABLE keypar (
  idkey integer NOT NULL,
  idparent integer NOT NULL);

CREATE INDEX idx_keyparkey ON keypar (idkey);
CREATE INDEX idx_keyparparent ON keypar (idparent);

CREATE TABLE pmc_subsets
(
  subset_id integer NOT NULL,
  subset_name character varying(255) NOT NULL
);
CREATE TABLE pmc_subset_objects
(
  subset_id integer NOT NULL,
  object_id integer NOT NULL
);

CREATE TABLE appset
(
  idset integer NOT NULL,
  idsetnam character varying(600) NOT NULL,
  idjob integer
);

CREATE TABLE objset
(
  idset integer NOT NULL,
  idobj integer NOT NULL
);

CREATE TABLE setroot
(
  idset integer NOT NULL,
  idroot integer NOT NULL
);

CREATE TABLE ctt_object_applications
(
  object_id integer NOT NULL,
  application_id integer NOT NULL,
  object_type integer NOT NULL,
  application_type integer NOT NULL,
  properties integer NOT NULL DEFAULT 0
);

CREATE TABLE accbook
(
  idacc integer NOT NULL,
  bookmode integer NOT NULL,
  info1 integer NOT NULL,
  info2 integer,
  info3 integer,
  info4 integer,
  prop integer,
  blkno integer
);

CREATE TABLE dss_history
(
  description character varying(500) NOT NULL,
  action_date timestamp NOT NULL,
  history_id serial NOT NULL
);

CREATE TABLE sys_site_options
(
  option_name character varying(255) NOT NULL,
  option_value character varying(255)
);

CREATE TABLE sys_package_history
(
  package_name character varying(100) NOT NULL,
  revision character varying(30) NOT NULL,
  revision_type integer NOT NULL,
  revision_date timestamp without time zone NOT NULL,
  installer character varying(100)
);

CREATE TABLE mod
(
  idmod integer NOT NULL,
  modnam character varying(255) NOT NULL,
  modlib character varying(255),
  modtyp integer NOT NULL,
  idfld integer NOT NULL,
  path character varying(600),
  idusr character(3),
  CONSTRAINT pk_mod PRIMARY KEY (idmod)
);

CREATE TABLE modcom
(
  idmod integer NOT NULL,
  idxmodcom integer NOT NULL,
  typ integer NOT NULL,
  subtyp integer NOT NULL,
  grid integer NOT NULL,
  grp integer NOT NULL
);

CREATE TABLE moddfc
(
  idmod integer NOT NULL,
  idxmodcom integer NOT NULL,
  iddfc integer NOT NULL
);

CREATE TABLE modkey
(
  idmod integer NOT NULL,
  idxmodcom integer NOT NULL,
  idkey integer NOT NULL,
  keynum integer NOT NULL,
  x integer NOT NULL,
  y integer NOT NULL,
  wdt integer NOT NULL,
  hgt integer NOT NULL,
  idlay integer NOT NULL
);

CREATE TABLE modlay
(
  idlay integer NOT NULL,
  laynam character varying(30) NOT NULL,
  layvis integer NOT NULL,
  idmod integer NOT NULL,
  idxmodcom integer NOT NULL
);

CREATE TABLE modlnk
(
  idmod integer NOT NULL,
  idxmodcom integer NOT NULL,
  idacc integer NOT NULL,
  accnum integer NOT NULL,
  lnkarw integer NOT NULL,
  lnk bytea NOT NULL,
  firstnum integer NOT NULL,
  secondnum integer NOT NULL,
  idlay integer NOT NULL,
  lnkvis integer NOT NULL DEFAULT 0,
  acctyplo integer NOT NULL DEFAULT 0,
  acctyphi integer NOT NULL DEFAULT 0,
  dist integer
);

CREATE TABLE modroot
(
  idmod integer NOT NULL,
  idxmodcom integer NOT NULL,
  idkey integer NOT NULL,
  typ integer NOT NULL,
  subtyp integer NOT NULL
);

CREATE TABLE modvew
(
  idmod integer NOT NULL,
  idxmodcom integer NOT NULL,
  num integer NOT NULL,
  startcol integer NOT NULL,
  startrow integer NOT NULL,
  width integer NOT NULL,
  height integer NOT NULL,
  zoomfactor integer NOT NULL
);



    """
    
    
delete_script = """
delete from anaattr ;
delete from sys_package_version ;
delete from usrpro ;
delete from proroot ;
delete from usrprojob ;
delete from dss_positions ;
delete from anajob ;
delete from acc ;
delete from fusacc ;
delete from prodep ;
delete from refpath ;
delete from objpro ;
delete from objfilref ;
delete from usrproroot ;
delete from keys ;
delete from objects ;
delete from objfulnam ;
delete from objinf ;
delete from objdsc ;
delete from objpos ;
delete from in_objects ;
delete from in_links ;
delete from in_char_properties ;
delete from keypar ;
delete from pmc_subsets ;
delete from pmc_subset_objects ;
delete from appset ;
delete from objset ;
delete from setroot ;
delete from ctt_object_applications ;
delete from accbook ;
delete from dss_history ;
delete from sys_site_options ;
delete from sys_package_history ;
"""

def _generate_delete_script():
    # generates the delete script for all tables except metamodel
    for line in script_create.splitlines():
        if line.startswith('CREATE TABLE'):
            table_name = line.split()[2]
            if table_name not in ['typcat', 'typ', 'cat', 'catcat', 'prop', 'propcat', 'typprop', 'propattr']:
                print('delete', table_name, ';')


def _get_nuspec_dependencies(plugin_path):
    
    # 1. search the file
    file_path = os.path.join(plugin_path, 'plugin.template.nuspec')
    if not os.path.isfile(file_path):
        file_path = os.path.join(plugin_path, 'plugin.nuspec')
        if not os.path.isfile(file_path):
            return []
        
    try:
        root = ET.parse(file_path)
        result = []
        for dependencies in root.xpath(".//*[local-name()='dependencies']"):
            
            for dependency in dependencies:
                
                _id = dependency.attrib['id']
                
                version = None
                try:
                    version = dependency.attrib['version']
                except:
                    pass
                
                result.append((_id, version))
            
        return result
        
    except:
        return []


def _get_forced_install(flat_path):
    """
    Read forced install...
    """
    file_path = os.path.join(flat_path, 'shipped_extensions', 'force_install.xml')
    if not os.path.isfile(file_path):
        return []
    
    try:
        root = ET.parse(file_path)
        result = []
        for command in root.getroot():
            
            try:
                _id = command.attrib['id']
                
                version = None
                try:
                    version = command.attrib['version']
                except:
                    pass
                
                result.append((_id, version))
            except:
                pass
            
        return result
        
    except:
        return []
    

def _get_plugin_path():

    test_class_file_path = ''
    is_test_class = False
    import traceback
    stack = traceback.extract_stack()
    for element in stack:
        if is_test_class:
            test_class_file_path = element[0]
            break
        if element[2] == 'run' and element[3] == 'testMethod()':
            # next element is the unit test file
            is_test_class = True

    pathname = os.path.dirname(test_class_file_path)
    plugin_path = os.path.abspath(os.path.join(pathname, '..'))
    return plugin_path


def _find_plugin(_id, version, folder):
    """
    Find a plugin with given id and version inside a folder
    """
    # we have it ...
    fullname = _id + '.' + version
    path = os.path.join(folder, fullname)
    if os.path.isdir(path):
        return path
        
    # either the extension exists without version on it:
    path = os.path.join(folder, _id)
    if os.path.isdir(path):
        return path


def _collect_metamodel_folders(dependency_to_load=[]):
    """
    """
    folders = []
    from ..setup import CASTAIP
    # 1. collect the MM folders : 
    # AIP Core,
    aip_folder = CASTAIP.get_running_caip().get_path()
    folders.append(os.path.join(aip_folder, 'configuration'))
    
    # 2. tested plugin
    plugin_path = _get_plugin_path()
    folders.append(plugin_path)

    contener_folder = os.path.join(plugin_path, '..')
    for dependency in dependency_to_load:
        folders.append(os.path.join(contener_folder, dependency))

    # for 8.3 force install ?
#     print(folders)
    return folders
