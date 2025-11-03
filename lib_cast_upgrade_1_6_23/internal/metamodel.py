import functools


class Attribute:
    """
    @deprecated: unused
    """
    def __init__(self):
        self.name = None
        self.value = None

    def get_value(self):
        return self.value

    def __repr__(self):
        return "Attribute(" + self.name + "," + str(self.value) + ")"


class Attributed:

    def __init__(self):
        self.id = None
        self.name = None
        self.description = None
        self.attributes = {}

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def get_attributes(self):
        """
        A map attribute name -> str or int
        """
        return self.attributes


class Property(Attributed):

    def __init__(self):
        Attributed.__init__(self)
        # type of the property
        self.type = None
        # name of the type of the property
        self.type_name = None
        self.minimal_cardinality = 0
        self.maximal_cardinality = 1
        # category containing the property
        self.category = None

    def get_type(self):
        return self.type

    def get_minimal_cardinality(self):
        return self.minimal_cardinality

    def get_maximal_cardinality(self):
        return self.maximal_cardinality

    def __repr__(self):
        return "Property(" + self.name + "," + str(self.id) + ")"


class Category(Attributed):

    def __init__(self):
        Attributed.__init__(self)
        self.metamodel = None
        self.properties = set()
        self.inherited_categories = set()
        # useless
        self.sub_categories = set()
        # all types that inherit (transitivelly) from this category
        self.sub_types = set()
        self.all_inherited_categories = set()
        self.inherited_names = set()
        
        # for xml only
        self.xml_fragments = []
        
    def get_properties(self):
        return self.properties

    def get_direct_parents(self):
        return self.inherited_categories

    def is_language(self):
        """
        True when the category is a quality rule language.
        """
        return self.metamodel.get_category(name='CsvLanguage') in self.get_direct_parents()

    def inherit_from(self, category):
        """
        True if self inherit from category.

        @param category: can be a Category object or a name or an id
        """

        _type = type(category)

        if _type is str:
            category = self.metamodel.get_category(name=category)
        elif _type is int:
            category = self.metamodel.get_category(id=category)

        if self == category:
            return True
        
        if self.all_inherited_categories:

            return category in self.all_inherited_categories

        if category in self.inherited_categories:
            return True

        for parent in self.inherited_categories:
            if parent.inherit_from(category):
                return True

        return False

    def inherit_from_one_of(self, categories):
        """
        True if category inherit from one of categories.
        """

        if not categories:
            return True

        for category in categories:
            if self.inherit_from(category):
                return True

        return False

    def get_sub_types(self):
        """
        Return all sub types
        """
        return self.sub_types

    def is_type(self):
        return False

    def __repr__(self):

        if self.is_type():
            result = "Type("
        else:
            result = "Category("

        result = result + self.name + "," + str(self.id)

        for _property in self.properties:
            result = result + " " + str(_property)

        for category in self.inherited_categories:
            result = result + " " + str(category)

        return result + ')'


class Type(Category):

    def is_type(self):
        return True
    
    @functools.lru_cache(maxsize=None)
    def get_language(self):
        """
        Returns the quality rule language or None.
        """
        for cat in self.all_inherited_categories:
            if cat.is_language():
                return cat
    

class MetaModel:

    def __init__(self):
        self.categories = set()
        self.types = set()
        self.properties = set()

        self.categories_by_name = {}
        self.categories_by_id = {}
        self.properties_by_name = {}
        self.properties_by_id = {}

        self.delta = 0

    def get_categories(self):
        return self.categories

    def get_properties(self):
        return self.properties

    def get_types(self):
        return self.types

    def get_category(self, name=None, id=None):

        if name:
            return self.categories_by_name[name]

        if id:
            return self.categories_by_id[id]

        return None

    def get_property(self, name=None, id=None):
        if name:
            return self.properties_by_name[name]

        if id:
            return self.properties_by_id[id]

        return None
        
    def _add_category(self, category):

        self.categories.add(category)
        if category.get_id():
            self.categories_by_id[category.get_id()] = category
        if category.get_name():
            self.categories_by_name[category.get_name()] = category
        category.metamodel = self

    def _add_type(self, _type):

        self._add_category(_type)
        self.types.add(_type)
        _type.sub_types.add(_type)

    def _add_property(self, _property):

        if _property.get_id() in self.properties_by_id:
            raise RuntimeError("property already present")

        self.properties.add(_property)
        if _property.get_id():
            self.properties_by_id[_property.get_id()] = _property
        if _property.get_name():
            self.properties_by_name[_property.get_name()] = _property

    def _finalize(self, allow_partial=False):

        for _property in self.properties:

            if _property.type:
                continue
            category = self.get_category(name=_property.type_name)
            _property.type = category

        for category in self.categories:

            for name in category.inherited_names:
                try:
                    parent = self.get_category(name=name)
                    category.inherited_categories.add(parent)
                    parent.sub_categories.add(category)
                    if category.is_type():
                        parent.sub_types.add(category)
                except KeyError:
                    if not allow_partial:
                        raise

        # recursive inheritance
        def saturate_category(category):
            
            category.all_inherited_categories |= category.inherited_categories
            for parent in category.inherited_categories:
                saturate_category(parent)
                category.all_inherited_categories |= parent.all_inherited_categories

        # all_inherited_categories
        for category in self.categories:
            saturate_category(category)

        # sub_types and sub_categories
        for category in self.categories:
            if category.is_type():
                for parent in category.all_inherited_categories:
                    parent.sub_types.add(category)
            for parent in category.all_inherited_categories:
                parent.sub_categories.add(category)
                
                    
class MetaModelConcepts:
    """
    Because upgrade is played after loading, the metamodel is already loaded and constructed.
    So we cannot really add methods to MetaModel class.
    
    This wrapper handle this situation.
    """
    def __init__(self, metamodel):
        self.metamodel = metamodel


    def _get_by_name_end(self, name):
        result = list()
        for t in self.metamodel.categories:
            if t.name.endswith(name):
                result.append(t)
    
        return result
        
    @functools.lru_cache(maxsize=None)
    def get_web_service_operation(self):

        return [self.metamodel.get_category('operation')]

    @functools.lru_cache(maxsize=None)
    def get_web_service_call(self):
        """
        Gives the list of categories representing web services calls.
        
        CAST_ResourceService
        CAST_WebServiceLinker_Resource
        CAST_SOAP_OperationCall
        """
        result = []
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.append(name)
            except KeyError:
                pass

        add_if_exist('CAST_ResourceService', result)
        add_if_exist('CAST_WebServiceLinker_Resource', result)
        add_if_exist('CAST_SOAP_OperationCall', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_rest_web_service_call(self):
        """
        Gives the list of categories representing REST calls.

        CAST_ResourceService
        CAST_WebServiceLinker_Resource
        """
        result = []

        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.append(name)
            except KeyError:
                pass

        add_if_exist('CAST_ResourceService', result)
        add_if_exist('CAST_WebServiceLinker_Resource', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_rest_web_service_receive(self):
        """
        Gives the list of categories representing REST receives.

        CAST_WebService_Operation
        CAST_WebServiceLinker_Operation
        """
        result = []

        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.append(name)
            except KeyError:
                pass

        add_if_exist('CAST_WebService_Operation', result)
        add_if_exist('CAST_WebServiceLinker_Operation', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_soap_web_service_call(self):
        """
        Gives the list of categories representing SOAP calls.

        CAST_SOAP_OperationCall
        """
        result = []

        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.append(name)
            except KeyError:
                pass

        add_if_exist('CAST_SOAP_OperationCall', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_soap_web_service_receive(self):
        """
        Gives the list of categories representing SOAP receive.

        CAST_SOAP_Operation
        """
        result = []

        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.append(name)
            except KeyError:
                pass

        add_if_exist('CAST_SOAP_Operation', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_nosql_collection(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_Java_NoSQL_Collection', result)
        add_if_exist('CAST_DotNet_NoSQL_Collection', result)
        add_if_exist('CAST_NodeJS_NoSQL_Collection', result)
        add_if_exist('CAST_AWS_Bucket', result)
        add_if_exist('CAST_AWS_DynamodbTable', result)
        add_if_exist('CAST_SHELL_AWS_DynamoDB_Table', result)
        add_if_exist('CAST_SHELL_AWS_Unknown_DynamoDB_Table', result)
        add_if_exist('CAST_Azure_Blob_Container', result)
        add_if_exist('CAST_GCP_Bigtable_Table', result)
        add_if_exist('CAST_CosmosDB_Collection', result)
        add_if_exist('CAST_NodeJS_CosmosDB_Unknown_Collection', result)
        add_if_exist('CAST_SHELL_AWS_Unknown_S3_Bucket', result)
        add_if_exist('CAST_Cassandra_Table', result)
        
        result.update(self._get_by_name_end('_Collection'))
        result.update(self._get_by_name_end('_S3_Bucket'))
        result.update(self._get_by_name_end('_DynamoDB_Table'))
        result.update(self._get_by_name_end('_Couchbase_Bucket'))

        # for older versions
        for t in self.metamodel.types:
            if (t.name.startswith('CAST_Java_') or t.name.startswith('CAST_DotNet_')) and t.name.endswith('_Collection'):
                result.add(t)

        return result

    @functools.lru_cache(maxsize=None)
    def get_program_call(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_CallToProgram', result)
        add_if_exist('CAST_CallToJavaProgram', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_bean(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_Web_AllBeans', result)
        add_if_exist('CAST_Spring_AllBeans', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_cloud_function(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_AWS_Lambda', result)
        add_if_exist('CAST_Azure_Function', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_cloud_function_call(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_CallTo_AWS_Lambda', result)
        add_if_exist('CAST_CallTo_Azure_Function', result)

        result.update(self._get_by_name_end('_Lambda_Call'))

        return result

    @functools.lru_cache(maxsize=None)
    def get_rpc_receive(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_gRPC_Method', result)
        add_if_exist('CAST_GenericRPC_Method', result)
        
        return result

    @functools.lru_cache(maxsize=None)
    def get_rpc_call(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_CallTo_gRPC_Method', result)
        add_if_exist('CAST_GenericRPC_CallTo_Method', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_message_receive(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_MQE_QueueReceive', result)
        add_if_exist('CAST_AWS_SQS_Receiver', result)
        add_if_exist('CAST_AWS_SNS_Subscriber', result)
        add_if_exist('CAST_Azure_ServiceBus_Receiver', result)
        add_if_exist('CAST_Azure_Unknown_ServiceBus_Receiver', result)
        add_if_exist('CAST_RabbitMQ_Queue', result)
        add_if_exist('CAST_RabbitMQ_Queue', result)
        add_if_exist('CAST_ActiveMQ_QueueReceive', result)
        add_if_exist('CAST_RabbitMQ_Consumer', result)
        add_if_exist('CAST_GCP_PubSub_Receiver', result)
        add_if_exist('CAST_Azure_EventHub_Receiver', result)
        add_if_exist('CAST_IBM_MQ_Subscriber', result)
        add_if_exist('RPG300DataUnknownQueueReceive', result)

        result.update(self._get_by_name_end('_Unknown_Receiver'))
        result.update(self._get_by_name_end('_QueueReceive'))
        result.update(self._get_by_name_end('_TopicReceive'))
        result.update(self._get_by_name_end('_EventHub_Receiver'))
        result.update(self._get_by_name_end('_Unknown_Subscriber'))

        result.update(self._get_by_name_end('_ActiveMQ_QueueReceive'))
        result.update(self._get_by_name_end('_IBM_QueueReceive'))
        result.update(self._get_by_name_end('_JMS_QueueReceive'))
        result.update(self._get_by_name_end('_Kafka_TopicReceive'))
        result.update(self._get_by_name_end('_RabbitMQ_TopicReceive'))
        result.update(self._get_by_name_end('_RabbitMQ_Unknown_Receiver'))
        
        return result

    @functools.lru_cache(maxsize=None)
    def get_message_send(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_MQE_QueueCall', result)
        add_if_exist('CAST_AWS_SQS_Sender', result)
        add_if_exist('CAST_AWS_SNS_Publisher', result)
        add_if_exist('CAST_Azure_ServiceBus_Publisher', result)
        add_if_exist('CAST_Azure_Unknown_ServiceBus_Publisher', result)
        add_if_exist('CAST_RabbitMQ_Exchange', result)
        add_if_exist('CAST_RabbitMQ_Exchange', result)
        add_if_exist('CAST_RabbitMQ_Publisher', result)
        add_if_exist('CAST_GCP_PubSub_Publisher', result)
        add_if_exist('CAST_Azure_EventHub_Publisher', result)
        add_if_exist('CAST_IBM_MQ_Publisher', result)
        add_if_exist('RPG300DataUnknownQueueCall', result)
         
        result.update(self._get_by_name_end('_Unknown_Publisher'))
        result.update(self._get_by_name_end('_QueueCall'))
        result.update(self._get_by_name_end('_TopicCall'))
        result.update(self._get_by_name_end('_EventHub_Publisher'))

        result.update(self._get_by_name_end('_ActiveMQ_QueueCall'))
        result.update(self._get_by_name_end('_IBM_QueueCall'))
        result.update(self._get_by_name_end('_JMS_QueueCall'))
        result.update(self._get_by_name_end('_Kafka_TopicCall'))
        result.update(self._get_by_name_end('_RabbitMQ_TopicCall'))
        result.update(self._get_by_name_end('_RabbitMQ_Unknown_Publisher'))

        return result

    @functools.lru_cache(maxsize=None)
    def get_query(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_SQL_MetricableQuery', result)
        add_if_exist('CAST_Unknown_SQLQuery', result)
        add_if_exist('CAST_Java_JPQLQuery', result)
        add_if_exist('CAST_IMS_SQLQuery', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_entity(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_Entity', result)
        add_if_exist('CAST_Unknown_Entity', result)

        return result
        
    @functools.lru_cache(maxsize=None)
    def get_entity_operation(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_Entity_Operation', result)
        add_if_exist('CAST_Unknown_Entity_Operation', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_executable(self):

        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_Java_Method', result)
        add_if_exist('CAST_Python_Method', result)
        add_if_exist('APM Methods', result)
        add_if_exist('templateInstanceMethod', result)
        add_if_exist('method', result)
        add_if_exist('APM Inventory Functions', result)
        add_if_exist('Database Function', result)
        add_if_exist('templateInstanceFunction', result)
        add_if_exist('CAST_COBOL_Procedure', result)
        add_if_exist('Database Procedure', result)
        add_if_exist('APM Inventory Triggers', result)
        add_if_exist('CAST_ANSISQL_Trigger', result)
        add_if_exist('CAST_SQL_UnresolvedFunction', result)
        add_if_exist('CAST_SQL_UnresolvedProcedure', result)

        result.update(self._get_by_name_end('_MissingTable_Procedure'))
        
        return result
        
    @functools.lru_cache(maxsize=None)
    def get_table(self):
        
        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('Database Table', result)
        add_if_exist('Database View', result)

        result.update(self._get_by_name_end('_MissingTable_Table'))
        return result
        
    @functools.lru_cache(maxsize=None)
    def get_dbms(self):
        
        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('ServerObject', result)
        add_if_exist('APM Server objects', result)
        add_if_exist('ANSISQL', result)
        add_if_exist('SERVER_DATABASE', result)

        return result
    
    @functools.lru_cache(maxsize=None)
    def get_directory(self):
        return [self.metamodel.get_category('Directory')]

    @functools.lru_cache(maxsize=None)
    def get_program(self):
        return [self.metamodel.get_category('APM Inventory Programs')]

    @functools.lru_cache(maxsize=None)
    def get_class(self):
        
        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('APM Classes', result)
        add_if_exist('templateInstanceClass', result)
        add_if_exist('CAST_ABAP_ClassOrInterface', result)
        add_if_exist('CAST_DotNet_Type', result)
        add_if_exist('APM Interfaces', result)
        add_if_exist('templateInstanceInterface', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_package(self):
        
        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # debatable...
        add_if_exist('APM_Namespaces', result)
        add_if_exist('APM Inventory Packages', result)
        add_if_exist('APM Inventory Modules', result)
        add_if_exist('APM Client Modules', result) # not sure
        add_if_exist('SERVER_DATABASE', result)
        add_if_exist('CAST_SQL_InstanceContainer', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_variable(self):
        
        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('APM Data Members', result)
        add_if_exist('field', result)
        add_if_exist('CAST_DotNet_Fields', result)
        add_if_exist('CAST_DotNet_Property', result)
        add_if_exist('CAST_DotNet_Event', result)
        add_if_exist('CAST_DotNet_EnumerationItem', result)
        add_if_exist('CAST_COBOL_Data', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_index(self):
        
        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('Database Index', result)
        add_if_exist('CAST_ANSISQL_PrimaryKeyConstraint', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_foreignkey(self):
        
        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('CAST_ANSISQL_ForeignKeyConstraint', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_form(self):
        
        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('APM Forms', result)
        add_if_exist('APM Controls and events', result)
        add_if_exist('APM Inventory Events', result)

        return result

    @functools.lru_cache(maxsize=None)
    def get_default_transaction_entry(self):
        
        result = set()
        def add_if_exist(name, result):
            try:
                if self.metamodel.get_category(name):
                    result.add(name)
            except KeyError:
                pass

        # common categories
        add_if_exist('APM Forms', result)
        add_if_exist('APM IFPUG Transaction', result)
        add_if_exist('CAST_Web_File', result)

        return result


def find_metamodel_files(folders, allow_test_metamodel=False):
    """
    Find metamodel files in given folders
    """

    import fnmatch
    import os

    result = set()

    for folder in folders:
        for root, _, filenames in os.walk(folder):
            for filename in fnmatch.filter(filenames, '*MetaModel.xml'):
                result.add(os.path.join(root, filename))
            
            if allow_test_metamodel:
                
                for filename in fnmatch.filter(filenames, '*MetaModelTest.xml'):
                    result.add(os.path.join(root, filename))
            
            
    return result


def read_metamodel(folders, allow_partial=False, allow_test_metamodel=False):
    """
    Read a metamodel from some folders
    
    :param folders: list of pathes
    :param allow_partial: if True allow reading partial metamodels
    :param allow_test_metamodel: if True allow reading of files named xxxMetamodelTest.xml
    """
    files = find_metamodel_files(folders, allow_test_metamodel)
    result = MetaModel()

    import xml.etree.ElementTree as ET

    for file in files:
        tree = ET.parse(file)
        parse(tree.getroot(), result, file)

    result._finalize(allow_partial)

    return result


def parse(metamodel_node, metamodel, file_path=None):

    mapping = {'core': 0,
               'builtin': 1000000,
               'prepackaged': 1500000,
               'client': 2000000}
    
    if 'file_level' in metamodel_node.attrib:
        level = metamodel_node.attrib['file_level']
    else:
        level = 'core'
    if 'file_no' in metamodel_node.attrib:
        number = metamodel_node.attrib['file_no']
    else:
        number = 0
    if not number:
        number = 0

    metamodel.delta = mapping[level] + 1000 * int(number)

    for child in metamodel_node:
        if child.tag in ['type', 'partialType', 'partial_type']:
            parse_type(child, metamodel, file_path)
        elif child.tag in ['category', 'partialCategory']:
            parse_category(child, metamodel, file_path)


def is_valid(node):

    if 'status' in node.attrib:
        if node.attrib['status'] == "obsolete":
            return False

    return True


def internal_parse_attributed(node, metamodel, result):
    result.name = node.attrib['name']

    if 'id' in node.attrib:
        result.id = int(node.attrib['id'])
    if 'rid' in node.attrib:
        result.id = metamodel.delta + int(node.attrib['rid'])


def internal_parse_attribute(node, result):
    value = None
    name = node.attrib['name']
    if 'intValue' in node.attrib:
        if node.attrib['intValue']:
            value = int(node.attrib['intValue'], 0)
    else:
        value = node.attrib['stringValue']

    result.attributes[name] = value


def internal_parse_type_or_category(node, metamodel, result, file_path=None):
    internal_parse_attributed(node, metamodel, result)

    for child in node:
        if child.tag == 'description':
            result.description = child.text if child.text else '' 
        elif child.tag == 'property' and is_valid(child):
            parse_property(child, metamodel, result)
        elif child.tag == 'inheritedCategory' and is_valid(child):
            result.inherited_names.add(child.attrib['name'])
        elif child.tag == 'attribute' and is_valid(child):
            internal_parse_attribute(child, result)
    
    import xml.etree.ElementTree as ET
    
    result.xml_fragments.append((ET.tostring(node, encoding='utf-8').decode(), file_path))

def parse_type(type_node, metamodel, file_path=None):

    try:
        result = metamodel.get_category(name=type_node.attrib['name'])
    except KeyError:
        result = Type()
    internal_parse_type_or_category(type_node, metamodel, result, file_path)
    metamodel._add_type(result)


def parse_category(category_node, metamodel, file_path=None):
    try:
        result = metamodel.get_category(name=category_node.attrib['name'])
    except KeyError:
        result = Category()
    internal_parse_type_or_category(category_node, metamodel, result, file_path)
    metamodel._add_category(result)


def parse_property(node, metamodel, category):
    result = Property()
    internal_parse_attributed(node, metamodel, result)
    name = result.name
    result.name = category.name + '.' + result.name
    result.type_name = node.attrib['type']
    result.category = category

    if 'minimalCardinality' in node.attrib:
        result.minimal_cardinality = int(node.attrib['minimalCardinality'])

    if 'maximalCardinality' in node.attrib:
        cardinality = node.attrib['maximalCardinality']
        if cardinality != "*":
            result.maximal_cardinality = int(cardinality)
        else:
            result.maximal_cardinality = None

    simple_types = set(['integer',
                        'string',
                        'bookmark',
                        'reference',
                        'dateTime'])

    if result.type_name in simple_types:
        result.type = result.type_name

    list_types = set(['integerList',
                      'stringList',
                      'bookmarkList',
                      'referenceList',
                      'dateTimeList'])
    
    if result.type_name in list_types:
        result.maximal_cardinality = None

        result.type = result.type_name[:-4]

    for child in node:
        if child.tag == 'description':
            result.description = child.text if child.text else ''
        elif child.tag == 'attribute' and is_valid(child):
            internal_parse_attribute(child, result)

    category.properties.add(result)
    metamodel._add_property(result)
    result.name = name


if __name__ == "__main__":

    mm = read_metamodel(['configuration'])
    print(len(mm.get_types()))
    print(len(mm.get_categories()))
    print(mm.get_category(name="CAST_COBOL_Select"))
