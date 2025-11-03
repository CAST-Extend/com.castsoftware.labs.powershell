tables = {
    "fp_lookup_tables": {
        "name": "FP_Lookup_Tables",
        "columns": [
            {
                "type": "Integer",
                "name": "Appli_ID"
            },
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "Lkp_Type"
            }
        ]
    },
    "cms_cobol_project": {
        "name": "CMS_COBOL_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "Integer",
                "name": "IBM_Environment"
            },
            {
                "type": "Integer",
                "name": "Cobol_StartingColumn"
            },
            {
                "type": "Integer",
                "name": "Cobol_ReadTermFormat"
            },
            {
                "type": "Integer",
                "name": "Tab_Length"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cobol_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JCL_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "IMS_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CICS_FileExtensions"
            },
            {
                "type": "Integer",
                "name": "Cobol_UseComponentName"
            },
            {
                "type": "Integer",
                "name": "cobol_CodeBeyondRightCol"
            },
            {
                "type": "Integer",
                "name": "IMS_IndcatorArea"
            }
        ]
    },
    "viewer_frames": {
        "name": "VIEWER_FRAMES",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PARENT_SECTION_ID"
            },
            {
                "type": "Integer",
                "name": "CHILD_OFFSET"
            }
        ]
    },
    "wk_dia_cobjclpgm": {
        "name": "WK_DIA_COBJCLPGM",
        "columns": [
            {
                "type": "Integer",
                "name": "jcl"
            },
            {
                "type": "Integer",
                "name": "pgm"
            }
        ]
    },
    "cms_net_pathmantgtdfm": {
        "name": "CMS_NET_PathManTgtDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "dss_locks": {
        "name": "DSS_LOCKS",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "LOCK_NAME"
            },
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "SESSION_ID_2"
            },
            {
                "type": "String",
                "length": 255,
                "name": "USER_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "HOST_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROGRAM_NAME"
            },
            {
                "type": "TIMESTAMP",
                "name": "LOCK_TIME"
            }
        ]
    },
    "cms_ora_anaoptions": {
        "name": "CMS_ORA_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "cms_pb_prodoptions": {
        "name": "CMS_PB_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "UseInferenceEngine"
            }
        ]
    },
    "appmarq_featpercenttimemodel": {
        "name": "AppMarq_FeatPercentTimeModel",
        "columns": [
            {
                "type": "Integer",
                "name": "FeaturePercentTimeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "FeaturePercentTimeName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "FeaturePercentTimeDescription"
            }
        ]
    },
    "efp_obj_cpt_statuses_app": {
        "name": "EFP_OBJ_CPT_STATUSES_APP",
        "columns": [
            {
                "length": 30,
                "type": "String",
                "name": "DATE_END"
            },
            {
                "length": 30,
                "type": "String",
                "name": "DATE_START"
            },
            {
                "type": "Integer",
                "name": "APP_ID"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Integer",
                "name": "IS_ART"
            },
            {
                "type": "Numeric",
                "name": "RESULT_COUNT"
            }
        ]
    },
    "diag_ctv_links": {
        "name": "DIAG_CTV_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_LO"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_HI"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "cms_am_parm_floats": {
        "name": "CMS_AM_PARM_Floats",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Numeric",
                "name": "FloatValue"
            }
        ]
    },
    "wk_dia_frminherit": {
        "name": "WK_DIA_FRMINHERIT",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "adg_func_module_modules": {
        "name": "ADG_FUNC_MODULE_MODULES",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "FUNC_MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "wk_dia_cpp_include": {
        "name": "WK_DIA_CPP_INCLUDE",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            }
        ]
    },
    "tmp_dia_inc_curr": {
        "name": "TMP_DIA_INC_CURR",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            }
        ]
    },
    "amt_del_objpro": {
        "name": "AMT_DEL_OBJPRO",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            }
        ]
    },
    "tmp_dia_netmethod": {
        "name": "TMP_DIA_NETMETHOD",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "all_positions": {
        "name": "ALL_POSITIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_SOURCE_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_SOURCE_KIND"
            },
            {
                "type": "Integer",
                "name": "SEQ_NUM"
            },
            {
                "type": "Integer",
                "name": "POSITION_MODE"
            },
            {
                "type": "Integer",
                "name": "POSITION1"
            },
            {
                "type": "Integer",
                "name": "POSITION2"
            },
            {
                "type": "Integer",
                "name": "POSITION3"
            },
            {
                "type": "Integer",
                "name": "POSITION4"
            },
            {
                "type": "Integer",
                "name": "GROUP_NUM"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_SOURCE_ID"
            }
        ]
    },
    "viewer_parameters": {
        "name": "VIEWER_PARAMETERS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "COMPONENT_ID"
            },
            {
                "type": "Integer",
                "name": "PARAMETER_INDEX"
            },
            {
                "length": 3500,
                "type": "String",
                "name": "VALUE"
            }
        ]
    },
    "cms_am_parm_txtlstoverrides": {
        "name": "CMS_AM_PARM_TxtLstOverrides",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            },
            {
                "type": "Integer",
                "name": "ContextParam"
            }
        ]
    },
    "accessbit": {
        "name": "ACCESSBIT",
        "columns": [
            {
                "type": "Integer",
                "name": "ACCTYPVAL"
            }
        ]
    },
    "tmp_dia_cob_statmc": {
        "name": "TMP_DIA_COB_STATMC",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "fp_wk_apptransaction": {
        "name": "FP_WK_AppTransaction",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            }
        ]
    },
    "dss_source_texts": {
        "name": "DSS_SOURCE_TEXTS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "LOCAL_SITE_ID"
            },
            {
                "type": "Integer",
                "name": "LOCAL_SOURCE_ID"
            },
            {
                "type": "Text",
                "name": "SOURCE_TEXT"
            },
            {
                "length": 600,
                "type": "String",
                "name": "SOURCE_PATH"
            }
        ]
    },
    "dssext_cumulated_counts": {
        "name": "DSSEXT_CUMULATED_COUNTS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "DEF_COUNT"
            }
        ]
    },
    "apm_cross_lang": {
        "name": "APM_CROSS_LANG",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NODE"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_TYPE"
            }
        ]
    },
    "catcat": {
        "name": "CatCat",
        "columns": [
            {
                "type": "Integer",
                "name": "IdCat"
            },
            {
                "type": "Integer",
                "name": "IdCatParent"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "objfulnam": {
        "name": "ObjFulNam",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            }
        ]
    },
    "cms_sqlsrv_prodoptions": {
        "name": "CMS_SQLSRV_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "apm_parent_list": {
        "name": "APM_PARENT_LIST",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            }
        ]
    },
    "cms_cpp_apptechno": {
        "name": "CMS_CPP_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "usrproroot": {
        "name": "UsrProRoot",
        "columns": [
            {
                "type": "Integer",
                "name": "IdUsrPro"
            },
            {
                "type": "Integer",
                "name": "IdRoot"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "cms_dep_default": {
        "name": "CMS_DEP_Default",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Source"
            },
            {
                "type": "Integer",
                "name": "Target"
            }
        ]
    },
    "frmitm": {
        "name": "FrmItm",
        "columns": [
            {
                "type": "Integer",
                "name": "IdItm"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ItmNam"
            },
            {
                "type": "Integer",
                "name": "ItmClass"
            },
            {
                "type": "Integer",
                "name": "ItmProp"
            }
        ]
    },
    "cms_am_qual_measures": {
        "name": "CMS_AM_QUAL_Measures",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "TranslationItem"
            },
            {
                "type": "Integer",
                "name": "PatternDescItem"
            },
            {
                "type": "Integer",
                "name": "RationaleDescItem"
            },
            {
                "type": "Integer",
                "name": "ScopeDescItem"
            },
            {
                "type": "Integer",
                "name": "OutputDescItem"
            },
            {
                "type": "Integer",
                "name": "ShortNameItem"
            },
            {
                "type": "Numeric",
                "name": "Threshold4"
            },
            {
                "type": "Numeric",
                "name": "Threshold3"
            },
            {
                "type": "Numeric",
                "name": "Threshold2"
            },
            {
                "type": "Numeric",
                "name": "Threshold1"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SQLProcedure"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            }
        ]
    },
    "inkb_dia_expensivepath": {
        "name": "InKB_DIA_ExpensivePath",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPath"
            },
            {
                "type": "Integer",
                "name": "IdTyp"
            },
            {
                "type": "Integer",
                "name": "Ord"
            },
            {
                "type": "Integer",
                "name": "IdAcc"
            }
        ]
    },
    "tmp_allfileproject": {
        "name": "TMP_ALLFILEPROJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDPRO"
            },
            {
                "type": "Integer",
                "name": "FILETYPE"
            },
            {
                "type": "Integer",
                "name": "IDFILE"
            },
            {
                "type": "String",
                "length": 600,
                "name": "FILEPATH"
            },
            {
                "type": "Integer",
                "name": "FILECRC"
            }
        ]
    },
    "dss_codegroup": {
        "name": "DSS_CodeGroup",
        "columns": [
            {
                "type": "Integer",
                "name": "IdUsrPro"
            },
            {
                "type": "Integer",
                "name": "GroupId"
            },
            {
                "type": "Integer",
                "name": "MetricId"
            },
            {
                "type": "Integer",
                "name": "MainObjectId"
            },
            {
                "type": "Integer",
                "name": "ObjectId"
            }
        ]
    },
    "in_typprop": {
        "name": "IN_TYPPROP",
        "columns": [
            {
                "type": "Integer",
                "name": "IDTYP"
            },
            {
                "type": "Integer",
                "name": "IDPROP"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "viewer_roles": {
        "name": "VIEWER_ROLES",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            }
        ]
    },
    "msg": {
        "name": "Msg",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMsg"
            },
            {
                "type": "String",
                "length": 255,
                "name": "MsgLib"
            },
            {
                "type": "Integer",
                "name": "MsgNo"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            }
        ]
    },
    "frmmod": {
        "name": "FrmMod",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdApp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ModNam"
            },
            {
                "type": "Integer",
                "name": "ModClass"
            },
            {
                "type": "Integer",
                "name": "ModProp"
            }
        ]
    },
    "enmod": {
        "name": "ENMod",
        "columns": [
            {
                "type": "Integer",
                "name": "IdENMod"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ModNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ModLib"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ModPath"
            },
            {
                "type": "Integer",
                "name": "ArrangeMode"
            }
        ]
    },
    "pmc_archi_checker_def": {
        "name": "PMC_ARCHI_CHECKER_DEF",
        "columns": [
            {
                "type": "Integer",
                "name": "MODEL_ID"
            },
            {
                "type": "Integer",
                "name": "RULE_ID"
            },
            {
                "type": "Integer",
                "name": "RULE_TYPE"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_LOW"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_HIGH"
            },
            {
                "type": "Integer",
                "name": "CALLER_SUBSET_ID"
            },
            {
                "type": "Integer",
                "name": "CALLEE_SUBSET_ID"
            }
        ]
    },
    "adg_work_grade_min": {
        "name": "ADG_WORK_GRADE_MIN",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Numeric",
                "name": "GRADE_MIN"
            }
        ]
    },
    "cms_am_desc_sample": {
        "name": "CMS_AM_DESC_Sample",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            }
        ]
    },
    "dss_wk_snapshots": {
        "name": "DSS_WK_SNAPSHOTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "cwobjtyp": {
        "name": "CWObjTyp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObjTyp"
            },
            {
                "type": "Integer",
                "name": "ObjTyp"
            },
            {
                "type": "Integer",
                "name": "KeyClass"
            },
            {
                "type": "Integer",
                "name": "KeyProp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjTypNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjTypDsc"
            },
            {
                "type": "String",
                "length": 600,
                "name": "IconPath"
            }
        ]
    },
    "apm_work_mod_std_results": {
        "name": "APM_WORK_MOD_STD_RESULTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Numeric",
                "name": "RESULT_COUNT"
            },
            {
                "type": "Numeric",
                "name": "RESULT_SUM"
            }
        ]
    },
    "dssapp_modtyp_worktable": {
        "name": "DSSAPP_MODTYP_WORKTABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            }
        ]
    },
    "cms_am_desc_pattern": {
        "name": "CMS_AM_DESC_Pattern",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            }
        ]
    },
    "syn": {
        "name": "Syn",
        "columns": [
            {
                "type": "Integer",
                "name": "IdSyn"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 30,
                "name": "SynNam"
            },
            {
                "type": "String",
                "length": 6,
                "name": "ObjTyp"
            },
            {
                "type": "String",
                "length": 30,
                "name": "ObjNam"
            },
            {
                "type": "String",
                "length": 30,
                "name": "ObjDbeNam"
            },
            {
                "type": "String",
                "length": 128,
                "name": "DbLnk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Host"
            },
            {
                "type": "Integer",
                "name": "SynClass"
            },
            {
                "type": "Integer",
                "name": "SynProp"
            }
        ]
    },
    "classproptyp": {
        "name": "ClassPropTyp",
        "columns": [
            {
                "type": "Integer",
                "name": "Class"
            },
            {
                "type": "Integer",
                "name": "Prop"
            },
            {
                "type": "Integer",
                "name": "ObjTyp"
            }
        ]
    },
    "cms_net_deftechno": {
        "name": "CMS_NET_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            },
            {
                "type": "Integer",
                "name": "DynamicAnalysisOptions"
            },
            {
                "type": "Integer",
                "name": "AllowExtensions"
            },
            {
                "type": "Integer",
                "name": "CallLightImport"
            },
            {
                "type": "Integer",
                "name": "IncludeLightImport"
            },
            {
                "type": "Integer",
                "name": "MaxComplexity"
            }
        ]
    },
    "cms_sync_translation": {
        "name": "CMS_SYNC_Translation",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "EntryObjPmc"
            },
            {
                "type": "String",
                "length": 255,
                "name": "EntryService"
            },
            {
                "type": "Integer",
                "name": "IdObjService"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "AdapterClass"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjTyp"
            }
        ]
    },
    "cms_am_desc_shortitems": {
        "name": "CMS_AM_DESC_ShortItems",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            }
        ]
    },
    "amt_objprodat": {
        "name": "AMT_OBJPRODAT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "PROPERTY_DATE"
            }
        ]
    },
    "fp_wk_subsets": {
        "name": "FP_WK_Subsets",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "SUBSET_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SUBSET_NAME"
            }
        ]
    },
    "viewer_data_types": {
        "name": "VIEWER_DATA_TYPES",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "DATA_MANAGER_CLASS_PATH"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "DATA_CLASS_PATH"
            },
            {
                "length": 200,
                "type": "String",
                "name": "SQL_MAPPING_NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "XML_MAPPING_NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "DATA_MANAGEMENT_MODE"
            }
        ]
    },
    "tmp_dia_pathdepth": {
        "name": "TMP_DIA_PATHDEPTH",
        "columns": [
            {
                "type": "Integer",
                "name": "PATHID"
            },
            {
                "type": "Integer",
                "name": "POS"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "DEPTH"
            }
        ]
    },
    "appmarq_applicationviolations": {
        "name": "AppMarq_ApplicationViolations",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "SnapshotId"
            },
            {
                "type": "Integer",
                "name": "RuleId"
            },
            {
                "type": "Integer",
                "name": "TotalNumber"
            },
            {
                "type": "Integer",
                "name": "ViolationNumber"
            },
            {
                "type": "Numeric",
                "name": "RuleGrade"
            }
        ]
    },
    "keyparana": {
        "name": "KeyParAna",
        "columns": [
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "IdParent"
            }
        ]
    },
    "diag_object_metrics": {
        "name": "DIAG_OBJECT_METRICS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_TYPE"
            },
            {
                "type": "Integer",
                "name": "METRIC_VALUE"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "dssapp_cls_fields_simple": {
        "name": "DSSAPP_CLS_FIELDS_SIMPLE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            }
        ]
    },
    "tmp_filedepproject": {
        "name": "TMP_FILEDEPPROJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDPRO"
            },
            {
                "type": "Integer",
                "name": "FILETYPE"
            },
            {
                "type": "Integer",
                "name": "IDFILE"
            },
            {
                "type": "String",
                "length": 600,
                "name": "FILEPATH"
            },
            {
                "type": "Integer",
                "name": "IDINCLUDEFILE"
            },
            {
                "type": "String",
                "length": 600,
                "name": "INCLUDEPATH"
            },
            {
                "type": "Integer",
                "name": "INCLUDECRC"
            },
            {
                "type": "Integer",
                "name": "DEPLEVEL"
            }
        ]
    },
    "defana_entity": {
        "name": "DEFANA_ENTITY",
        "columns": [
            {
                "type": "Integer",
                "name": "ENTITY_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ENTITY_GUID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ENTITY_NAME"
            },
            {
                "type": "Integer",
                "name": "ENTITY_TYPE_ID"
            }
        ]
    },
    "efp_app_statuses": {
        "name": "EFP_APP_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_SNAPSHOT_ID"
            }
        ]
    },
    "cms_portf_version": {
        "name": "CMS_PORTF_Version",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Status"
            },
            {
                "type": "TIMESTAMP",
                "name": "VersionDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PreviousVersion"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            }
        ]
    },
    "cms_cobol_anaoptions": {
        "name": "CMS_COBOL_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cobol_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JCL_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "IMS_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CICS_FileExtensions"
            },
            {
                "type": "Integer",
                "name": "IBM_Environment"
            },
            {
                "type": "Integer",
                "name": "Cobol_StartingColumn"
            },
            {
                "type": "Integer",
                "name": "Cobol_ReadTermFormat"
            },
            {
                "type": "Integer",
                "name": "Cobol_UseComponentName"
            },
            {
                "type": "Integer",
                "name": "Tab_Length"
            },
            {
                "type": "Integer",
                "name": "Cobol_CodeBeyondRightCol"
            },
            {
                "type": "Integer",
                "name": "IMS_IndcatorArea"
            }
        ]
    },
    "adg_work_object_list": {
        "name": "ADG_WORK_OBJECT_LIST",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "wk_dia_jeepath": {
        "name": "WK_DIA_JEEPATH",
        "columns": [
            {
                "type": "Integer",
                "name": "Id"
            },
            {
                "type": "Integer",
                "name": "JobId"
            },
            {
                "type": "Integer",
                "name": "MetricId"
            },
            {
                "type": "Integer",
                "name": "PathId"
            },
            {
                "type": "Integer",
                "name": "ObjectId"
            }
        ]
    },
    "dssapp_pkgfaninout": {
        "name": "DSSAPP_PKGFANINOUT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECTH_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECTB_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "FAN_IN"
            }
        ]
    },
    "cms_migr_local": {
        "name": "CMS_MIGR_Local",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LocalEntry"
            },
            {
                "type": "Integer",
                "name": "LocalDB_ID"
            }
        ]
    },
    "cms_am_qual_techcriteria": {
        "name": "CMS_AM_QUAL_TechCriteria",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "NameTranslationItem"
            },
            {
                "type": "Integer",
                "name": "DescriptionEntry"
            },
            {
                "type": "Integer",
                "name": "RationaleEntry"
            },
            {
                "type": "Integer",
                "name": "ShortNameEntry"
            },
            {
                "type": "Integer",
                "name": "ExternalID"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            }
        ]
    },
    "in_cat": {
        "name": "IN_CAT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CATNAM"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CATDSC"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "cms_amt_technologies": {
        "name": "CMS_AMT_Technologies",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "AMTObjectId"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Description"
            }
        ]
    },
    "fp_param_tableprefix": {
        "name": "FP_Param_TablePrefix",
        "columns": [
            {
                "type": "Integer",
                "name": "Appli_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Description"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Prefix"
            }
        ]
    },
    "cms_inf_sqlsrv_localdb": {
        "name": "CMS_INF_SQLSRV_LocalDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            },
            {
                "type": "Integer",
                "name": "Credential_ID"
            },
            {
                "type": "Integer",
                "name": "Server_ID"
            },
            {
                "type": "Integer",
                "name": "Service_Unique_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Portal_URL"
            },
            {
                "type": "Integer",
                "name": "ToMigrate"
            }
        ]
    },
    "cms_am_parm_txtlstparams": {
        "name": "CMS_AM_PARM_TxtLstParams",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "ParamIndex"
            },
            {
                "type": "Integer",
                "name": "Model_ID"
            },
            {
                "type": "Integer",
                "name": "DefValue"
            }
        ]
    },
    "cms_vb_anaoptions": {
        "name": "CMS_VB_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "ReferencesOnly"
            },
            {
                "type": "Integer",
                "name": "DefaultHandling"
            }
        ]
    },
    "cms_net_sqltargetdfm": {
        "name": "CMS_NET_SQLTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "cms_j2ee_pathmantgtdfm": {
        "name": "CMS_J2EE_PathManTgtDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "in_linkobject": {
        "name": "IN_LINKOBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECTTYPE_ID"
            },
            {
                "type": "Integer",
                "name": "ACCESSTYPELOW_ID"
            }
        ]
    },
    "imp": {
        "name": "Imp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdImp"
            },
            {
                "type": "String",
                "length": 30,
                "name": "ImpNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ImpLib"
            },
            {
                "type": "Integer",
                "name": "ImpOpt"
            },
            {
                "type": "Integer",
                "name": "IdCnx"
            }
        ]
    },
    "pbosyn": {
        "name": "PboSyn",
        "columns": [
            {
                "type": "Integer",
                "name": "IdSyn",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SynNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Mangling"
            },
            {
                "type": "Integer",
                "name": "SynClass"
            },
            {
                "type": "Integer",
                "name": "SynProp"
            }
        ]
    },
    "tmp_paridinterval": {
        "name": "TMP_PARIDINTERVAL",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID_MIN"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID_MAX"
            },
            {
                "type": "Integer",
                "name": "BLOCK"
            }
        ]
    },
    "apm_worktable_cur": {
        "name": "APM_WORKTABLE_CUR",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NODE"
            },
            {
                "type": "Numeric",
                "name": "RESULT"
            },
            {
                "type": "Numeric",
                "name": "RESULT_2"
            },
            {
                "type": "Numeric",
                "name": "RESULT_3"
            },
            {
                "type": "Numeric",
                "name": "RESULT_4"
            },
            {
                "type": "Numeric",
                "name": "RESULT_5"
            },
            {
                "type": "Numeric",
                "name": "RESULT_6"
            },
            {
                "type": "Numeric",
                "name": "RESULT_7"
            },
            {
                "type": "Numeric",
                "name": "RESULT_8"
            },
            {
                "type": "String",
                "length": 255,
                "name": "VAR_RESULT"
            }
        ]
    },
    "cms_cobol_prodoptions": {
        "name": "CMS_COBOL_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "PROD_SaveSectAndParagraph"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROD_DataStructure"
            },
            {
                "type": "Integer",
                "name": "PROD_SaveCopyBookData"
            },
            {
                "type": "Integer",
                "name": "UseInferenceEngine"
            },
            {
                "type": "Integer",
                "name": "LimitString"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget2"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget3"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget4"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget5"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget6"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget7"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget8"
            },
            {
                "type": "Integer",
                "name": "maxMem"
            }
        ]
    },
    "cms_sap_anaoptions": {
        "name": "CMS_SAP_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TablesPath"
            }
        ]
    },
    "accsymb": {
        "name": "AccSymb",
        "columns": [
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "IdClr"
            },
            {
                "type": "Integer",
                "name": "IdCle"
            },
            {
                "type": "Integer",
                "name": "AccTypLo"
            },
            {
                "type": "Integer",
                "name": "AccTypHi"
            },
            {
                "type": "Integer",
                "name": "AccTypLo2"
            },
            {
                "type": "Integer",
                "name": "AccTypHi2"
            },
            {
                "type": "Integer",
                "name": "AccKnd"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "adg_delta_snapshots": {
        "name": "ADG_DELTA_SNAPSHOTS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "LATEST"
            },
            {
                "type": "TIMESTAMP",
                "name": "FUNCTIONAL_DATE"
            },
            {
                "length": 30,
                "type": "String",
                "name": "TEXT_DATE"
            },
            {
                "type": "Integer",
                "name": "PREV_SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "FIRST_SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "LAST_SNAPSHOT_ID"
            },
            {
                "length": 30,
                "type": "String",
                "name": "PREV_TEXT_DATE"
            },
            {
                "length": 30,
                "type": "String",
                "name": "FIRST_TEXT_DATE"
            },
            {
                "length": 30,
                "type": "String",
                "name": "LAST_TEXT_DATE"
            }
        ]
    },
    "appmarq_applicationphasemodel": {
        "name": "AppMarq_ApplicationPhaseModel",
        "columns": [
            {
                "type": "Integer",
                "name": "ApplicationPhaseId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "ApplicationPhaseName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "ApplicationPhaseDescription"
            }
        ]
    },
    "dssext_metric_diags": {
        "name": "DSSEXT_METRIC_DIAGS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "TECH_ID"
            },
            {
                "type": "Integer",
                "name": "DIAG_ID"
            },
            {
                "type": "Integer",
                "name": "WEIGHT"
            }
        ]
    },
    "pak": {
        "name": "Pak",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPak"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 30,
                "name": "PakNam"
            },
            {
                "type": "Integer",
                "name": "PakNat"
            },
            {
                "type": "Integer",
                "name": "PakClass"
            },
            {
                "type": "Integer",
                "name": "PakProp"
            }
        ]
    },
    "dssapp_cob_worktable": {
        "name": "DSSAPP_COB_WORKTABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NODE"
            },
            {
                "type": "Integer",
                "name": "INH_LEVEL"
            }
        ]
    },
    "tmp_dia_cob_statm3": {
        "name": "TMP_DIA_COB_STATM3",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            }
        ]
    },
    "histo_typcat": {
        "name": "HISTO_TYPCAT",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDTYP"
            },
            {
                "type": "Integer",
                "name": "IDCATPARENT"
            },
            {
                "type": "Integer",
                "name": "ISCATPROP"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "wk_dia_singltcls": {
        "name": "WK_DIA_SINGLTCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_CLASS"
            },
            {
                "type": "Integer",
                "name": "ID_METHOD"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_vb_deftechno": {
        "name": "CMS_VB_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "ReferencesOnly"
            },
            {
                "type": "Integer",
                "name": "DefaultHandling"
            },
            {
                "type": "Integer",
                "name": "UseInferenceEngine"
            },
            {
                "type": "Integer",
                "name": "LimitString"
            },
            {
                "type": "Integer",
                "name": "MaxCodeSize"
            }
        ]
    },
    "in_char_properties_chk": {
        "name": "IN_CHAR_PROPERTIES_CHK",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "CHAR_BLOCK"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPERTY_CHAR"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DESCRIPTION"
            }
        ]
    },
    "objobj": {
        "name": "ObjObj",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj1"
            },
            {
                "type": "Integer",
                "name": "IdObj2"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "av_selection": {
        "name": "AV_SELECTION",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "ref_drop_table": {
        "name": "REF_DROP_TABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "POS"
            },
            {
                "type": "Integer",
                "name": "TYP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TABNAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "COLNAME"
            }
        ]
    },
    "cms_code_macro": {
        "name": "CMS_CODE_Macro",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Value"
            }
        ]
    },
    "fp_wk_subsets_info": {
        "name": "FP_WK_Subsets_Info",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "SUBSET_ID"
            },
            {
                "type": "Integer",
                "name": "SUBSET_GROUP"
            },
            {
                "type": "Integer",
                "name": "FP_Value"
            },
            {
                "type": "Integer",
                "name": "DET_Value"
            },
            {
                "type": "Integer",
                "name": "RET_Value"
            }
        ]
    },
    "wk_dia_springcls": {
        "name": "WK_DIA_SPRINGCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "BEAN_ID"
            }
        ]
    },
    "ci_no_properties": {
        "name": "CI_NO_PROPERTIES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "OBJECT_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "OBJECT_SHORTGUID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROP_NAME"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "amt_status": {
        "name": "AMT_STATUS",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "String",
                "length": 30,
                "name": "STATUS"
            }
        ]
    },
    "amt_clc": {
        "name": "AMT_CLC",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "STRING_BLOCK"
            },
            {
                "type": "Integer",
                "name": "INFTYPATT"
            },
            {
                "type": "Integer",
                "name": "INFSUBTYPATT"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPERTY_STRING"
            }
        ]
    },
    "dss_work_in_objects": {
        "name": "DSS_WORK_IN_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "OBJECT_NAME"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "OBJECT_DESCRIPTION"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "OBJECT_FULL_NAME"
            },
            {
                "type": "Integer",
                "name": "OBJECT_CHECKSUM"
            }
        ]
    },
    "dss_in_objects": {
        "name": "DSS_IN_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "OBJECT_NAME"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "OBJECT_DESCRIPTION"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "OBJECT_FULL_NAME"
            },
            {
                "type": "Integer",
                "name": "OBJECT_CHECKSUM"
            }
        ]
    },
    "dss_sourceidtranslation": {
        "name": "DSS_SourceIdTranslation",
        "columns": [
            {
                "type": "Integer",
                "name": "KB_SourceId"
            },
            {
                "type": "Integer",
                "name": "DSS_SourceId"
            }
        ]
    },
    "objects_similarities": {
        "name": "OBJECTS_SIMILARITIES",
        "columns": [
            {
                "type": "Integer",
                "name": "SIMILARITY_TYPE"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID_1"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID_2"
            },
            {
                "type": "Integer",
                "name": "OBJECTS_SIMILARITY"
            }
        ]
    },
    "cms_am_parm_fltoverrides": {
        "name": "CMS_AM_PARM_FltOverrides",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "ContextParam"
            },
            {
                "type": "Numeric",
                "name": "FloatValue"
            }
        ]
    },
    "dss_history": {
        "name": "DSS_HISTORY",
        "columns": [
            {
                "type": "String",
                "length": 500,
                "name": "DESCRIPTION"
            },
            {
                "type": "TIMESTAMP",
                "name": "ACTION_DATE"
            },
            {
                "type": "Integer",
                "name": "HISTORY_ID"
            }
        ]
    },
    "modkey": {
        "name": "ModKey",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            },
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "KeyNum"
            },
            {
                "type": "Integer",
                "name": "X"
            },
            {
                "type": "Integer",
                "name": "Y"
            },
            {
                "type": "Integer",
                "name": "Wdt"
            },
            {
                "type": "Integer",
                "name": "Hgt"
            },
            {
                "type": "Integer",
                "name": "IdLay"
            }
        ]
    },
    "histo_prop": {
        "name": "HISTO_PROP",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDPROP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPNAM"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPDSC"
            },
            {
                "type": "Integer",
                "name": "PROPTYP"
            },
            {
                "type": "String",
                "length": 3,
                "name": "PROPMRG"
            },
            {
                "type": "Integer",
                "name": "CARDMIN"
            },
            {
                "type": "Integer",
                "name": "CARDMAX"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "work_objects_hierarchy": {
        "name": "WORK_OBJECTS_HIERARCHY",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSIONID"
            },
            {
                "type": "Integer",
                "name": "RELATIONSHIPLEVEL"
            },
            {
                "type": "Integer",
                "name": "TOBESCANNED"
            },
            {
                "type": "Integer",
                "name": "IDPARENTKEY"
            },
            {
                "type": "Integer",
                "name": "IDKEY"
            },
            {
                "type": "Integer",
                "name": "KEYCLASS"
            },
            {
                "type": "Integer",
                "name": "KEYPROP"
            }
        ]
    },
    "viewer_cache_update": {
        "name": "VIEWER_CACHE_UPDATE",
        "columns": [
            {
                "type": "TIMESTAMP",
                "name": "UPDATE_DATE"
            },
            {
                "length": 255,
                "type": "String",
                "name": "CACHE_NAME"
            }
        ]
    },
    "wk_dia_prstcoll": {
        "name": "WK_DIA_PRSTCOLL",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TYPE_ID"
            }
        ]
    },
    "wk_dia_multiobject": {
        "name": "WK_DIA_MULTIOBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID_1"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID_2"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID_3"
            }
        ]
    },
    "cms_ua_prodoptions": {
        "name": "CMS_UA_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "diag_ctv_links_simple": {
        "name": "DIAG_CTV_LINKS_SIMPLE",
        "columns": [
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "cms_am_quantity_measures": {
        "name": "CMS_AM_QUANTITY_Measures",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "ActiveStatus"
            },
            {
                "type": "Integer",
                "name": "DeprecatedStatus"
            },
            {
                "type": "Integer",
                "name": "NameTranslationItem"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SizingMeasureType"
            },
            {
                "type": "Integer",
                "name": "DescriptionEntry"
            },
            {
                "type": "Integer",
                "name": "ShortNameEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "MeasureProcedure"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AggregationType"
            },
            {
                "type": "Integer",
                "name": "ExternalID"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            }
        ]
    },
    "cms_net_logfgtgtdfm": {
        "name": "CMS_NET_LogFgTgtDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "rgtprfjob": {
        "name": "RgtPrfJob",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRgtPrf"
            },
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "Rgt"
            }
        ]
    },
    "in_treecat": {
        "name": "IN_TREECAT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDFROM"
            },
            {
                "type": "Integer",
                "name": "IDTO"
            },
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "cms_j2ee_logfgtgtdfm": {
        "name": "CMS_J2EE_LogFgTgtDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "wk_dia_cfldataset": {
        "name": "WK_DIA_CFLDATASET",
        "columns": [
            {
                "type": "Integer",
                "name": "cfl"
            },
            {
                "type": "Integer",
                "name": "dataset"
            }
        ]
    },
    "cms_vb_analysis": {
        "name": "CMS_VB_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Project"
            },
            {
                "type": "Integer",
                "name": "ReferencesOnly"
            },
            {
                "type": "Integer",
                "name": "DefaultHandling"
            }
        ]
    },
    "wk_dia_singfactcls": {
        "name": "WK_DIA_SINGFACTCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "work_metric_distribution": {
        "name": "WORK_METRIC_DISTRIBUTION",
        "columns": [
            {
                "length": 255,
                "type": "String",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "NUM_VALUE"
            }
        ]
    },
    "anakeysel": {
        "name": "AnaKeySel",
        "columns": [
            {
                "type": "Integer",
                "name": "IdSel"
            },
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "SelVal"
            },
            {
                "type": "Integer",
                "name": "SelProp"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            },
            {
                "type": "Integer",
                "name": "SelTyp"
            },
            {
                "type": "Integer",
                "name": "IdCnx"
            }
        ]
    },
    "cms_forms_prodoptions": {
        "name": "CMS_FORMS_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "amt_lnklink": {
        "name": "AMT_LNKLINK",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "PROJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "SOURCE_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "TARGET_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "PROJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_PROJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROP"
            },
            {
                "type": "Integer",
                "name": "PROP_TYPE_LINK"
            },
            {
                "type": "String",
                "length": 1,
                "name": "LINK_KIND"
            }
        ]
    },
    "fp_result_excludedobjects": {
        "name": "FP_Result_ExcludedObjects",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            }
        ]
    },
    "viewer_filter_values": {
        "name": "VIEWER_FILTER_VALUES",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PARENT_SECTION_ID"
            },
            {
                "type": "Integer",
                "name": "CHILD_OFFSET"
            },
            {
                "length": 200,
                "type": "String",
                "name": "FILTER_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "FILTER_KEY"
            },
            {
                "length": 200,
                "type": "String",
                "name": "FRAME_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "SECTION_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "FILTEREDVALUE"
            },
            {
                "length": 2000,
                "type": "String",
                "name": "RETURNVALUE"
            }
        ]
    },
    "dss_snapshot_info": {
        "name": "DSS_SNAPSHOT_INFO",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "length": 50,
                "type": "String",
                "name": "OBJECT_VERSION"
            }
        ]
    },
    "dss_work_objects_flat_tree": {
        "name": "DSS_WORK_OBJECTS_FLAT_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "FLAT_LEVEL"
            }
        ]
    },
    "work_collect_filter": {
        "name": "WORK_COLLECT_FILTER",
        "columns": [
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            },
            {
                "type": "Integer",
                "name": "SEL_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_LEVEL"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "appmarq_techcriteria_bcriteria": {
        "name": "AppMarq_TechCriteria_BCriteria",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "type": "Integer",
                "name": "TechnicalCriterionId"
            },
            {
                "type": "Integer",
                "name": "BusinessCriterionId"
            },
            {
                "type": "Numeric",
                "name": "AggregationWeight"
            }
        ]
    },
    "cms_am_qual_sqlsettings": {
        "name": "CMS_AM_QUAL_SQLSettings",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Rule_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TotalProcedure"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DetailProcedure"
            }
        ]
    },
    "cms_portf_namefilter": {
        "name": "CMS_PORTF_NameFilter",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Pattern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternOpe"
            },
            {
                "type": "Integer",
                "name": "ParentFilter_ID"
            }
        ]
    },
    "cms_am_qual_ap_selection": {
        "name": "CMS_AM_QUAL_AP_Selection",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Exclusion"
            },
            {
                "type": "Integer",
                "name": "Selection"
            }
        ]
    },
    "difflistobj": {
        "name": "DiffListObj",
        "columns": [
            {
                "type": "Integer",
                "name": "Id"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjFulNam"
            },
            {
                "type": "Integer",
                "name": "ObjTyp"
            },
            {
                "type": "Integer",
                "name": "IdParent"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ParentFulNam"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ProNam"
            },
            {
                "type": "Integer",
                "name": "DiffTyp"
            }
        ]
    },
    "dssext_hit_counts": {
        "name": "DSSEXT_HIT_COUNTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "HIT_COUNT"
            }
        ]
    },
    "cms_cpp_project": {
        "name": "CMS_CPP_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cpp_Compilation"
            },
            {
                "type": "Integer",
                "name": "Managed_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "C_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cpp_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DevEnv_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Stl_Usage"
            },
            {
                "type": "Integer",
                "name": "MagicRgtShift"
            },
            {
                "type": "Integer",
                "name": "Trigraph"
            },
            {
                "type": "Integer",
                "name": "StdScope"
            },
            {
                "type": "Integer",
                "name": "IsoTypename"
            },
            {
                "type": "Integer",
                "name": "UnknownDirective"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PrecompiledHeader"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PchGenerator"
            },
            {
                "type": "Integer",
                "name": "DisableUseofPch"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ForceInclude"
            }
        ]
    },
    "dss_metric_value_types": {
        "name": "DSS_METRIC_VALUE_TYPES",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_VALUE_INDEX"
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_VALUE_NAME"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "METRIC_VALUE_DESCRIPTION"
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_VALUE_PROCEDURE_NAME"
            },
            {
                "type": "Integer",
                "name": "METRIC_AGGREGATE_OPERATOR"
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_VALUE_PROCEDURE_NAME_2"
            },
            {
                "type": "Integer",
                "name": "METRIC_AGGREGATE_OPERATOR_2"
            },
            {
                "type": "Integer",
                "name": "METRIC_VALUE_TYPE"
            }
        ]
    },
    "adg_work_grade": {
        "name": "ADG_WORK_GRADE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Numeric",
                "name": "COUNT_1"
            },
            {
                "type": "Numeric",
                "name": "COUNT_2"
            },
            {
                "type": "Numeric",
                "name": "COUNT_3"
            },
            {
                "type": "Numeric",
                "name": "COUNT_4"
            },
            {
                "type": "Numeric",
                "name": "COUNT_TOTAL"
            },
            {
                "type": "Numeric",
                "name": "GRADE_1"
            },
            {
                "type": "Numeric",
                "name": "GRADE_2"
            },
            {
                "type": "Numeric",
                "name": "GRADE_3"
            },
            {
                "type": "Numeric",
                "name": "GRADE_4"
            },
            {
                "type": "Numeric",
                "name": "GRADE"
            }
        ]
    },
    "kb_informations": {
        "name": "KB_INFORMATIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "INFO_KIND"
            },
            {
                "type": "Integer",
                "name": "INFO_INDEX1"
            },
            {
                "type": "Integer",
                "name": "INFO_INDEX2"
            },
            {
                "type": "Integer",
                "name": "INFO_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "INFO_CHAR_VALUE"
            },
            {
                "type": "TIMESTAMP",
                "name": "INFO_DATE_VALUE"
            }
        ]
    },
    "amt_prjlink": {
        "name": "AMT_PRJLINK",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "PROJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "SOURCE_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "TARGET_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "PROJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_PROJECT_ID"
            }
        ]
    },
    "cms_dynamicfields": {
        "name": "CMS_DynamicFields",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Entity_GUID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Field_GUID"
            },
            {
                "type": "String",
                "length": 3000,
                "name": "Field_Value"
            },
            {
                "type": "TIMESTAMP",
                "name": "Field_Date"
            }
        ]
    },
    "wk_dia_compare": {
        "name": "WK_DIA_COMPARE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Numeric",
                "name": "METRIC_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "METRIC_CHAR_VALUE"
            },
            {
                "type": "Integer",
                "name": "METRIC_OBJECT_ID"
            }
        ]
    },
    "cms_forms_anaoptions": {
        "name": "CMS_FORMS_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "CodeViewerFilesDir"
            }
        ]
    },
    "cms_sap_rfdefinition": {
        "name": "CMS_SAP_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "ci_objects_set": {
        "name": "CI_OBJECTS_SET",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "SET_NAME"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "OBJECT_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "OBJECT_SHORTGUID"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "jvoejb": {
        "name": "JvoEjb",
        "columns": [
            {
                "type": "Integer",
                "name": "IdEjb"
            },
            {
                "type": "String",
                "length": 255,
                "name": "EjbNam"
            },
            {
                "type": "Integer",
                "name": "ReEnt"
            },
            {
                "type": "Integer",
                "name": "PersTyp"
            },
            {
                "type": "Integer",
                "name": "SessTyp"
            },
            {
                "type": "Integer",
                "name": "TransTyp"
            },
            {
                "type": "Integer",
                "name": "AckMode"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FilPath"
            }
        ]
    },
    "cms_code_cont_file": {
        "name": "CMS_CODE_CONT_File",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            }
        ]
    },
    "cms_am_qual_qr_selection": {
        "name": "CMS_AM_QUAL_QR_Selection",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Selection"
            }
        ]
    },
    "accbooksymb": {
        "name": "AccBookSymb",
        "columns": [
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "BookMode"
            },
            {
                "type": "Integer",
                "name": "Info1"
            },
            {
                "type": "Integer",
                "name": "Info2"
            },
            {
                "type": "Integer",
                "name": "Info3"
            },
            {
                "type": "Integer",
                "name": "Info4"
            },
            {
                "type": "Integer",
                "name": "Prop"
            },
            {
                "type": "Integer",
                "name": "BlkNo"
            }
        ]
    },
    "cms_am_qual_healthfactors": {
        "name": "CMS_AM_QUAL_HealthFactors",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "NameTranslationItem"
            },
            {
                "type": "String",
                "length": 255,
                "name": "HFType"
            },
            {
                "type": "Integer",
                "name": "DescriptionEntry"
            },
            {
                "type": "Integer",
                "name": "RationaleEntry"
            },
            {
                "type": "Integer",
                "name": "ShortNameEntry"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            }
        ]
    },
    "cms_udb_rfdefinition": {
        "name": "CMS_UDB_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "pboapp": {
        "name": "PboApp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdApp",
                "primary": True
            },
            {
                "type": "String",
                "length": 255,
                "name": "AppNam"
            }
        ]
    },
    "cms_sap_apptechno": {
        "name": "CMS_SAP_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "wk_dia_eqprstsubcls": {
        "name": "WK_DIA_EQPRSTSUBCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "ENTITY_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "METHOD_ID"
            }
        ]
    },
    "cms_asp_analysis": {
        "name": "CMS_ASP_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Server_FileExtensions"
            },
            {
                "type": "Integer",
                "name": "Server_UseRoot"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Client_FileExtensions"
            },
            {
                "type": "Integer",
                "name": "Client_UseRoot"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefServerScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            }
        ]
    },
    "in_urf_host_files": {
        "name": "IN_URF_HOST_FILES",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSIONID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "PATH"
            }
        ]
    },
    "wk_dia_c_include": {
        "name": "WK_DIA_C_INCLUDE",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            }
        ]
    },
    "in_parents": {
        "name": "IN_PARENTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            }
        ]
    },
    "wk_scope_expensivepath": {
        "name": "WK_SCOPE_EXPENSIVEPATH",
        "columns": [
            {
                "type": "Integer",
                "name": "PathId"
            },
            {
                "type": "Integer",
                "name": "ScopeIndex"
            },
            {
                "type": "Integer",
                "name": "ContainerId"
            },
            {
                "type": "Integer",
                "name": "ProjectId"
            },
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "CalleeId"
            }
        ]
    },
    "cms_ua_analysis": {
        "name": "CMS_UA_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            }
        ]
    },
    "wk_dia_jeeesql001": {
        "name": "WK_DIA_JEEESQL001",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "modroot": {
        "name": "ModRoot",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            },
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "Typ"
            },
            {
                "type": "Integer",
                "name": "SubTyp"
            }
        ]
    },
    "monitor_time": {
        "name": "MONITOR_TIME",
        "columns": [
            {
                "type": "Integer",
                "name": "CNXID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROC_NAME"
            },
            {
                "type": "Integer",
                "name": "STEP_NUM"
            },
            {
                "type": "TIMESTAMP",
                "name": "DATE_INFO"
            }
        ]
    },
    "tmp_dia_cob_statmp": {
        "name": "TMP_DIA_COB_STATMP",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            }
        ]
    },
    "apm_ruleschecker": {
        "name": "APM_RULESCHECKER",
        "columns": [
            {
                "length": 255,
                "type": "String",
                "name": "PROCNAME"
            },
            {
                "length": 255,
                "type": "String",
                "name": "INFO"
            },
            {
                "length": 255,
                "type": "String",
                "name": "RESULT"
            },
            {
                "length": 255,
                "type": "String",
                "name": "RESULT2"
            },
            {
                "name": "MESSAGE_ID"
            }
        ]
    },
    "anapro": {
        "name": "AnaPro",
        "columns": [
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "IdJobParent"
            },
            {
                "type": "Integer",
                "name": "JobTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ProNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ProLib"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            }
        ]
    },
    "cms_tool_rfpattern": {
        "name": "CMS_TOOL_RfPattern",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "RefDef_ID"
            }
        ]
    },
    "csv_linktype": {
        "name": "CSV_LINKTYPE",
        "columns": [
            {
                "type": "Integer",
                "name": "AccTypLo"
            },
            {
                "type": "Integer",
                "name": "AccTypHi"
            },
            {
                "type": "String",
                "length": 255,
                "name": "StaticDesc"
            },
            {
                "type": "Integer",
                "name": "AccTypLo2"
            },
            {
                "type": "Integer",
                "name": "AccTypHi2"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DynamicDesc"
            }
        ]
    },
    "diff_cwmodel": {
        "name": "DIFF_CWMODEL",
        "columns": [
            {
                "type": "Integer",
                "name": "ID"
            },
            {
                "type": "String",
                "length": 6,
                "name": "TYP"
            }
        ]
    },
    "cms_udb_analysis": {
        "name": "CMS_UDB_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TableSize"
            }
        ]
    },
    "wk_dia_jsp_include": {
        "name": "WK_DIA_JSP_INCLUDE",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            }
        ]
    },
    "amt_object": {
        "name": "AMT_OBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "NAME_ID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "SHORT_NAME_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "STATUS"
            }
        ]
    },
    "wk_dia_persistget": {
        "name": "WK_DIA_PERSISTGET",
        "columns": [
            {
                "type": "Integer",
                "name": "PROPERTY_ID"
            },
            {
                "type": "Integer",
                "name": "METHOD_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "wk_dia_collection": {
        "name": "WK_DIA_COLLECTION",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Numeric",
                "name": "METRIC_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "METRIC_CHAR_VALUE"
            },
            {
                "type": "Integer",
                "name": "METRIC_OBJECT_ID"
            }
        ]
    },
    "opetrack": {
        "name": "OpeTrack",
        "columns": [
            {
                "type": "Integer",
                "name": "OpeTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OpeInfo"
            },
            {
                "type": "TIMESTAMP",
                "name": "DtInfo"
            },
            {
                "type": "String",
                "length": 3,
                "name": "IdUsr"
            }
        ]
    },
    "cms_sqlsrv_anaoptions": {
        "name": "CMS_SQLSRV_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "dssext_crit_path": {
        "name": "DSSEXT_CRIT_PATH",
        "columns": [
            {
                "length": 255,
                "type": "String",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "LEVEL_INDEX"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "accraw": {
        "name": "AccRaw",
        "columns": [
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "IdAccRaw"
            },
            {
                "type": "Integer",
                "name": "Dist"
            }
        ]
    },
    "cms_inf_css_analyticdb": {
        "name": "CMS_INF_CSS_AnalyticDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            },
            {
                "type": "Integer",
                "name": "Credential_ID"
            },
            {
                "type": "Integer",
                "name": "Server_ID"
            },
            {
                "type": "Integer",
                "name": "Service_Unique_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Status"
            }
        ]
    },
    "cms_bo_project": {
        "name": "CMS_BO_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            }
        ]
    },
    "appmarq_businesscriteria": {
        "name": "AppMarq_BusinessCriteria",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "type": "Integer",
                "name": "BusinessCriterionId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "BusinessCriterionName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "BusinessCriterionDescription"
            }
        ]
    },
    "amt_cda": {
        "name": "AMT_CDA",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "STRING_BLOCK"
            },
            {
                "type": "Integer",
                "name": "INFTYPATT"
            },
            {
                "type": "Integer",
                "name": "INFSUBTYPATT"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPERTY_STRING"
            }
        ]
    },
    "cms_ui_tool": {
        "name": "CMS_UI_Tool",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "VarContainer_ID"
            },
            {
                "type": "Integer",
                "name": "Mode_ID"
            }
        ]
    },
    "dss_metric_histo_params": {
        "name": "DSS_METRIC_HISTO_PARAMS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "PARAM_INDEX"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Numeric",
                "name": "PARAM_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "PARAM_CHAR_VALUE"
            }
        ]
    },
    "work_steps": {
        "name": "WORK_STEPS",
        "columns": [
            {
                "type": "Integer",
                "name": "STEP"
            },
            {
                "type": "Integer",
                "name": "NB"
            },
            {
                "type": "TIMESTAMP",
                "name": "STEP_DATE"
            }
        ]
    },
    "work_mafilref": {
        "name": "WORK_MAFILREF",
        "columns": [
            {
                "type": "Integer",
                "name": "KEY_ID"
            },
            {
                "type": "Integer",
                "name": "IDFILREF"
            },
            {
                "type": "Integer",
                "name": "KEYCLASS"
            },
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            }
        ]
    },
    "ctt_object_containers": {
        "name": "CTT_OBJECT_CONTAINERS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "CONTAINER_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "CONTAINER_TYPE"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_TYPE"
            }
        ]
    },
    "cms_sqlsrv_rfdefinition": {
        "name": "CMS_SQLSRV_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "cms_code_repo_formsextract": {
        "name": "CMS_CODE_REPO_FormsExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "appmarq_demographics": {
        "name": "AppMarq_Demographics",
        "columns": [
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "ApplicationName"
            },
            {
                "type": "Integer",
                "name": "TechnologyId"
            },
            {
                "type": "Integer",
                "name": "FunctionalDomainId"
            },
            {
                "type": "Integer",
                "name": "ApplicationTypeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "ApplicationTypeDescription"
            },
            {
                "type": "Integer",
                "name": "EndUsersRangeId"
            },
            {
                "type": "Integer",
                "name": "SourcingTypeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "VendorName"
            },
            {
                "length": 255,
                "type": "String",
                "name": "CountryName"
            },
            {
                "type": "Integer",
                "name": "DevMethodologyId"
            },
            {
                "type": "Integer",
                "name": "CMMILevelId"
            },
            {
                "type": "Integer",
                "name": "ReleasesPerYearId"
            },
            {
                "type": "Integer",
                "name": "ApplicationAgeId"
            },
            {
                "type": "Integer",
                "name": "QAPercentTimeId"
            },
            {
                "type": "Integer",
                "name": "FeaturePercentTimeId"
            },
            {
                "type": "Integer",
                "name": "DevelopersRangeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "DevelopersRange"
            },
            {
                "length": 255,
                "type": "String",
                "name": "CountryDevelopment"
            },
            {
                "type": "Integer",
                "name": "ShoringTypeId"
            },
            {
                "type": "Integer",
                "name": "ApplicationPhaseId"
            }
        ]
    },
    "pmc_archi_models": {
        "name": "PMC_ARCHI_MODELS",
        "columns": [
            {
                "type": "Integer",
                "name": "MODEL_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "MODEL_NAME"
            }
        ]
    },
    "tmp_dia_netobject": {
        "name": "TMP_DIA_NETOBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_net_file": {
        "name": "CMS_NET_FILE",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Parent_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            }
        ]
    },
    "wk_dia_javapackage": {
        "name": "WK_DIA_JAVAPACKAGE",
        "columns": [
            {
                "type": "Integer",
                "name": "GROUP_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "uax_sp_out": {
        "name": "UAX_SP_OUT",
        "columns": [
            {
                "type": "Integer",
                "name": "CALL_ID"
            },
            {
                "type": "Integer",
                "name": "RESULT"
            }
        ]
    },
    "objdsc": {
        "name": "ObjDsc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "InfTyp"
            },
            {
                "type": "Integer",
                "name": "InfSubTyp"
            },
            {
                "type": "Integer",
                "name": "BlkNo"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            },
            {
                "type": "Integer",
                "name": "Prop"
            },
            {
                "type": "String",
                "length": 255,
                "name": "InfVal"
            }
        ]
    },
    "dss_date_snapshot": {
        "name": "DSS_DATE_SNAPSHOT",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "FUNCTIONAL_DATE"
            },
            {
                "type": "String",
                "length": 30,
                "name": "TEXT_DATE"
            },
            {
                "type": "Integer",
                "name": "IS_COMPUTED"
            }
        ]
    },
    "wk_dia_setter": {
        "name": "WK_DIA_SETTER",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "SETTER_NAME"
            }
        ]
    },
    "wk_dia_dispactcls": {
        "name": "WK_DIA_DISPACTCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            }
        ]
    },
    "dss_links": {
        "name": "DSS_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "PREVIOUS_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NEXT_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            }
        ]
    },
    "cms_inf_sqlsrv_credential": {
        "name": "CMS_INF_SQLSRV_Credential",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UserName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Password"
            },
            {
                "type": "Integer",
                "name": "Trusted"
            }
        ]
    },
    "uax_import_instances": {
        "name": "UAX_IMPORT_INSTANCES",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "GROUPNAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "INSTANCE_ID"
            },
            {
                "type": "String",
                "length": 100,
                "name": "INSTANCE_TYPE"
            }
        ]
    },
    "cms_amt_objecttypes": {
        "name": "CMS_AMT_ObjectTypes",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "AMTObjectId"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Description"
            }
        ]
    },
    "dia_struts_validfld": {
        "name": "DIA_STRUTS_VALIDFLD",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "FIELD_ID"
            },
            {
                "type": "Integer",
                "name": "VALIDATE_FIELD_ID"
            },
            {
                "type": "Integer",
                "name": "VALIDATE_TYPE"
            }
        ]
    },
    "dss_metric_param_values": {
        "name": "DSS_METRIC_PARAM_VALUES",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "PARAM_INDEX"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Numeric",
                "name": "PARAM_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "PARAM_CHAR_VALUE"
            },
            {
                "type": "Integer",
                "name": "PARAM_ORDER"
            }
        ]
    },
    "cms_j2ee_sanitizationdfm": {
        "name": "CMS_J2EE_SanitizationDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            }
        ]
    },
    "dss_snapshots": {
        "name": "DSS_SNAPSHOTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "FUNCTIONAL_DATE"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_TYPE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SNAPSHOT_NAME"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "SNAPSHOT_DESCRIPTION"
            },
            {
                "type": "TIMESTAMP",
                "name": "SNAPSHOT_DATE"
            },
            {
                "type": "TIMESTAMP",
                "name": "COMPUTE_START_DATE"
            },
            {
                "type": "TIMESTAMP",
                "name": "COMPUTE_END_DATE"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_STATUS"
            },
            {
                "type": "Integer",
                "name": "EXTERNAL_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_CONSO_ID"
            }
        ]
    },
    "adg_work_status": {
        "name": "ADG_WORK_STATUS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Integer",
                "name": "RESULT_COUNT"
            }
        ]
    },
    "wk_dia_prstsubcls": {
        "name": "WK_DIA_PRSTSUBCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "ROOT_ENTITY"
            },
            {
                "type": "Integer",
                "name": "SUB_ENTITY"
            },
            {
                "type": "Integer",
                "name": "NBR_PRO"
            },
            {
                "type": "Integer",
                "name": "MAX_PRO"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_forms_apptechno": {
        "name": "CMS_FORMS_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "tmp_dia_jeeobject": {
        "name": "TMP_DIA_JEEOBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "sys_licenses": {
        "name": "SYS_LICENSES",
        "columns": [
            {
                "type": "Integer",
                "name": "LICENSE_ID"
            },
            {
                "type": "String",
                "length": 2000,
                "name": "LICENSE_CODE"
            }
        ]
    },
    "dss_work_folder_metrics": {
        "name": "DSS_WORK_FOLDER_METRICS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "TREE_LEVEL"
            }
        ]
    },
    "apm_module_list": {
        "name": "APM_MODULE_LIST",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "viewer_reports": {
        "name": "VIEWER_REPORTS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "type": "Integer",
                "name": "USER_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "type": "Integer",
                "name": "PDF_AUTOMATION"
            },
            {
                "type": "Integer",
                "name": "OUTDATED"
            }
        ]
    },
    "work_sel_objs_and_children": {
        "name": "WORK_SEL_OBJS_AND_CHILDREN",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSIONID"
            },
            {
                "type": "Integer",
                "name": "RELATIONSHIPLEVEL"
            },
            {
                "type": "Integer",
                "name": "IDPARENTKEY"
            },
            {
                "type": "Integer",
                "name": "IDKEY"
            }
        ]
    },
    "viewer_user_pages": {
        "name": "VIEWER_USER_PAGES",
        "columns": [
            {
                "type": "Integer",
                "name": "USER_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PAGE_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PAGE_NAME"
            },
            {
                "type": "Integer",
                "name": "PAGE_INDEX"
            }
        ]
    },
    "appmarq_applications": {
        "name": "AppMarq_Applications",
        "columns": [
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "FunctionalDomainId"
            },
            {
                "type": "Integer",
                "name": "TechnologyId"
            }
        ]
    },
    "cms_migr_target": {
        "name": "CMS_MIGR_Target",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            }
        ]
    },
    "work_selectionl_tree": {
        "name": "WORK_SELECTIONL_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            },
            {
                "type": "Integer",
                "name": "RESULT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_LEVEL"
            },
            {
                "type": "Integer",
                "name": "FIRSTOBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECTTYPE_ID"
            },
            {
                "type": "Integer",
                "name": "ACCESSTYPELOW_ID"
            }
        ]
    },
    "cms_am_qual_propsettings": {
        "name": "CMS_AM_QUAL_PropSettings",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Rule_ID"
            },
            {
                "type": "Integer",
                "name": "TotalScope"
            },
            {
                "type": "Integer",
                "name": "DetailProperty"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SpecificTotalProcedure"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SpecificDetailProcedure"
            }
        ]
    },
    "cms_net_sanitizationdfm": {
        "name": "CMS_NET_SanitizationDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            }
        ]
    },
    "cms_bo_prodoptions": {
        "name": "CMS_BO_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "trash": {
        "name": "Trash",
        "columns": [
            {
                "type": "Integer",
                "name": "Spid"
            },
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "OpeTyp"
            }
        ]
    },
    "col": {
        "name": "Col",
        "columns": [
            {
                "type": "Integer",
                "name": "IdCol",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 128,
                "name": "ColNam"
            },
            {
                "type": "Integer",
                "name": "ColNum"
            },
            {
                "type": "Integer",
                "name": "ColKeyNum"
            },
            {
                "type": "Integer",
                "name": "SprOutCol"
            },
            {
                "type": "Integer",
                "name": "IdDtp"
            },
            {
                "type": "Integer",
                "name": "ColLen"
            },
            {
                "type": "Integer",
                "name": "ColPrc"
            },
            {
                "type": "Integer",
                "name": "ColNul"
            },
            {
                "type": "Integer",
                "name": "ColScl"
            },
            {
                "type": "Integer",
                "name": "ColIdt"
            },
            {
                "type": "Integer",
                "name": "ColLck"
            }
        ]
    },
    "csv": {
        "name": "CSV",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "BITAND16"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE"
            }
        ]
    },
    "dss_tree_violations": {
        "name": "DSS_TREE_VIOLATIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "DIAG_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TREE_LEVEL"
            },
            {
                "type": "Integer",
                "name": "TREE_LEFT_POSITION"
            },
            {
                "type": "Integer",
                "name": "TREE_RIGHT_POSITION"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "cms_syb_anaoptions": {
        "name": "CMS_SYB_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "cw_dbg_param_instr": {
        "name": "CW_DBG_PARAM_INSTR",
        "columns": [
            {
                "type": "TIMESTAMP",
                "name": "datestamp"
            },
            {
                "type": "Integer",
                "name": "numexec"
            },
            {
                "type": "String",
                "length": 128,
                "name": "dbename"
            },
            {
                "type": "String",
                "length": 128,
                "name": "ownername"
            },
            {
                "type": "String",
                "length": 128,
                "name": "sprname"
            },
            {
                "type": "String",
                "length": 128,
                "name": "param"
            },
            {
                "type": "String",
                "length": 7356,
                "name": "strvalue"
            },
            {
                "name": "ordnum"
            },
            {
                "name": "prop"
            }
        ]
    },
    "dss_sites": {
        "name": "DSS_SITES",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "SITE_TYPE"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SITE_NAME"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "SITE_DESCRIPTION"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SITE_SYSTEM"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SITE_SERVER"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SITE_USER"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SITE_PASSWORD"
            },
            {
                "type": "Integer",
                "name": "ENCRYPTION_TYPE"
            },
            {
                "type": "Integer",
                "name": "SERVER_TYPE"
            },
            {
                "type": "TIMESTAMP",
                "name": "LAST_UPDATE"
            },
            {
                "length": 255,
                "type": "String",
                "name": "LOCAL_DSS_NAME"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_STATUS"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SITE_SRVADDRESS_TYPE"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "SITE_SRVADDRESS"
            }
        ]
    },
    "enmodenmod": {
        "name": "ENModENMod",
        "columns": [
            {
                "type": "Integer",
                "name": "IdENMod"
            },
            {
                "type": "Integer",
                "name": "IdMod"
            }
        ]
    },
    "cms_zos_deftechno": {
        "name": "CMS_ZOS_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "UseZOSSystemCatalog"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "wk_dia_javaallinherit": {
        "name": "WK_DIA_JAVAALLINHERIT",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "dss_snapshot_types": {
        "name": "DSS_SNAPSHOT_TYPES",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_TYPE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SNAPSHOT_TYPE_NAME"
            }
        ]
    },
    "cms_code_sourcefilenet": {
        "name": "CMS_CODE_SourceFileNet",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Usage"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            },
            {
                "type": "String",
                "length": 255,
                "name": "buildAction"
            }
        ]
    },
    "cms_am_desc_remediationsample": {
        "name": "CMS_AM_DESC_RemediationSample",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            }
        ]
    },
    "cms_dep_standard": {
        "name": "CMS_DEP_Standard",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Source"
            },
            {
                "type": "Integer",
                "name": "Target"
            },
            {
                "type": "Integer",
                "name": "ReferenceFinder"
            }
        ]
    },
    "wk_dia_setflushmod": {
        "name": "WK_DIA_SETFLUSHMOD",
        "columns": [
            {
                "type": "Integer",
                "name": "METHOD_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "cms_j2ee_userinputdfm": {
        "name": "CMS_J2EE_UserInputDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            }
        ]
    },
    "seq": {
        "name": "Seq",
        "columns": [
            {
                "type": "Integer",
                "name": "IdSeq"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 30,
                "name": "SeqNam"
            },
            {
                "type": "String",
                "length": 50,
                "name": "MinVal"
            },
            {
                "type": "String",
                "length": 50,
                "name": "MaxVal"
            },
            {
                "type": "String",
                "length": 50,
                "name": "Inc"
            },
            {
                "type": "String",
                "length": 50,
                "name": "Cache"
            },
            {
                "type": "Integer",
                "name": "SeqCycle"
            },
            {
                "type": "Integer",
                "name": "SeqOrder"
            }
        ]
    },
    "wk_dia_abap_include": {
        "name": "WK_DIA_ABAP_INCLUDE",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            }
        ]
    },
    "viewer_profile_function_access": {
        "name": "VIEWER_PROFILE_FUNCTION_ACCESS",
        "columns": [
            {
                "type": "Integer",
                "name": "PROFILE_ID"
            },
            {
                "type": "Integer",
                "name": "FUNCTION_ID"
            }
        ]
    },
    "wk_search_results": {
        "name": "WK_SEARCH_RESULTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_CATEGORY"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SESSION_ID"
            }
        ]
    },
    "in_urf_analyzed_projects": {
        "name": "IN_URF_ANALYZED_PROJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSIONID"
            },
            {
                "type": "Integer",
                "name": "IDPRO"
            }
        ]
    },
    "uax_sp_in": {
        "name": "UAX_SP_IN",
        "columns": [
            {
                "type": "Integer",
                "name": "CALL_ID"
            },
            {
                "type": "Integer",
                "name": "PARAM_ORDER"
            },
            {
                "type": "String",
                "length": 100,
                "name": "VALUE"
            },
            {
                "type": "String",
                "length": 100,
                "name": "PROCEDURE_NAME"
            }
        ]
    },
    "work_imported_jobs": {
        "name": "WORK_IMPORTED_JOBS",
        "columns": [
            {
                "type": "Integer",
                "name": "IMPORT_ID"
            },
            {
                "type": "Integer",
                "name": "JOB_ID"
            }
        ]
    },
    "cms_cobol_apptechno": {
        "name": "CMS_COBOL_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "wk_dia_ejbclass": {
        "name": "WK_DIA_EJBCLASS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            }
        ]
    },
    "ref_info_kind": {
        "name": "REF_INFO_KIND",
        "columns": [
            {
                "type": "Integer",
                "name": "INFO_KIND"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DESCRIPTION"
            },
            {
                "type": "Integer",
                "name": "PROPERTY"
            }
        ]
    },
    "cms_portf_module": {
        "name": "CMS_PORTF_Module",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 2000,
                "name": "Description"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefinitionType"
            },
            {
                "type": "Integer",
                "name": "ExplicitFilter_ID"
            }
        ]
    },
    "histo_treecat": {
        "name": "HISTO_TREECAT",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDFROM"
            },
            {
                "type": "Integer",
                "name": "IDTO"
            },
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "cms_net_oscmdtargetdfm": {
        "name": "CMS_NET_OSCmdTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "wk_dia_validatemet": {
        "name": "WK_DIA_VALIDATEMET",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "METHOD_ID"
            }
        ]
    },
    "cms_inf_sqlsrv_accessinst": {
        "name": "CMS_INF_SQLSRV_AccessInst",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Instance"
            }
        ]
    },
    "srvcnx": {
        "name": "SrvCnx",
        "columns": [
            {
                "type": "Integer",
                "name": "IdCnx"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CnxNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "System"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Server"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Usr"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Password"
            },
            {
                "type": "Integer",
                "name": "PwdLen"
            },
            {
                "type": "Integer",
                "name": "Crypting"
            },
            {
                "type": "Integer",
                "name": "IdSrv"
            }
        ]
    },
    "wk_dia_jeeobject": {
        "name": "WK_DIA_JEEOBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_code_repo_dbudb": {
        "name": "CMS_CODE_REPO_DBUDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "viewer_action_plan_config": {
        "name": "VIEWER_ACTION_PLAN_CONFIG",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "PURGE"
            }
        ]
    },
    "ana_c_systemfunctions": {
        "name": "ANA_C_SystemFunctions",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "FunctionName"
            }
        ]
    },
    "usrpwd": {
        "name": "UsrPwd",
        "columns": [
            {
                "type": "String",
                "length": 50,
                "name": "UsrNam"
            },
            {
                "name": "UsrPwd"
            },
            {
                "type": "Integer",
                "name": "PwdLen"
            },
            {
                "type": "Integer",
                "name": "Crypting"
            }
        ]
    },
    "tmp_dia_cob_statm5": {
        "name": "TMP_DIA_COB_STATM5",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            }
        ]
    },
    "dbg_savingdataresults": {
        "name": "DBG_SavingDataResults",
        "columns": [
            {
                "type": "Integer",
                "name": "UnitId"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TreatmentName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SourceTableName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TargetTableName"
            },
            {
                "type": "Integer",
                "name": "ResultCount"
            },
            {
                "type": "TIMESTAMP",
                "name": "SavingDate"
            }
        ]
    },
    "cost_config": {
        "name": "COST_CONFIG",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "PROFILE_NAME"
            },
            {
                "type": "Integer",
                "name": "TECHNO_ID"
            },
            {
                "type": "Integer",
                "name": "COST_VALUE_INDEX"
            },
            {
                "type": "Numeric",
                "name": "COST_NUM_VALUE"
            }
        ]
    },
    "cms_am_desc_stranslations": {
        "name": "CMS_AM_DESC_STranslations",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Text"
            }
        ]
    },
    "wk_dia_cobparacfl": {
        "name": "WK_DIA_COBPARACFL",
        "columns": [
            {
                "type": "Integer",
                "name": "para"
            },
            {
                "type": "Integer",
                "name": "cfl"
            },
            {
                "type": "Integer",
                "name": "type_hi"
            }
        ]
    },
    "dss_metric_histo_thresholds": {
        "name": "DSS_METRIC_HISTO_THRESHOLDS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Numeric",
                "name": "THRESHOLD_1"
            },
            {
                "type": "Numeric",
                "name": "THRESHOLD_2"
            },
            {
                "type": "Numeric",
                "name": "THRESHOLD_3"
            },
            {
                "type": "Numeric",
                "name": "THRESHOLD_4"
            }
        ]
    },
    "amt_link": {
        "name": "AMT_LINK",
        "columns": [
            {
                "type": "Integer",
                "name": "EXTERNAL_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "STATUS"
            },
            {
                "type": "Integer",
                "name": "PROP"
            },
            {
                "type": "Integer",
                "name": "MODIF"
            },
            {
                "type": "String",
                "length": 1,
                "name": "LINK_KIND"
            }
        ]
    },
    "vew": {
        "name": "Vew",
        "columns": [
            {
                "type": "Integer",
                "name": "IdVew",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 128,
                "name": "VewNam"
            },
            {
                "type": "Integer",
                "name": "VewClass"
            },
            {
                "type": "Integer",
                "name": "VewProp"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "amt_project": {
        "name": "AMT_PROJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDPRO"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Integer",
                "name": "TYPE"
            }
        ]
    },
    "viewer_languages": {
        "name": "VIEWER_LANGUAGES",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "LOCALREF"
            }
        ]
    },
    "cms_am_parm_fltlstoverrides": {
        "name": "CMS_AM_PARM_FltLstOverrides",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            },
            {
                "type": "Integer",
                "name": "ContextParam"
            }
        ]
    },
    "viewer_sites": {
        "name": "VIEWER_SITES",
        "columns": [
            {
                "type": "Integer",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "USR"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PWD"
            },
            {
                "length": 200,
                "type": "String",
                "name": "DB"
            },
            {
                "length": 200,
                "type": "String",
                "name": "DRIVER"
            },
            {
                "length": 200,
                "type": "String",
                "name": "SUBPROTOCOL"
            },
            {
                "length": 200,
                "type": "String",
                "name": "DBDATABASE"
            },
            {
                "type": "Integer",
                "name": "ENCRYPTION_TYPE"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "DESCRIPTION"
            },
            {
                "length": 30,
                "type": "String",
                "name": "VERSION"
            },
            {
                "length": 30,
                "type": "String",
                "name": "BUILDNUM"
            }
        ]
    },
    "cms_cpp_prodoptions": {
        "name": "CMS_CPP_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "MaxCodeSize"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "genobj": {
        "name": "GenObj",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 240,
                "name": "ObjNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjLib"
            },
            {
                "type": "Integer",
                "name": "IdTyp"
            },
            {
                "type": "Integer",
                "name": "IdApp"
            },
            {
                "type": "Integer",
                "name": "GenObjTyp"
            },
            {
                "type": "Integer",
                "name": "IdParent"
            },
            {
                "type": "String",
                "length": 250,
                "name": "Path"
            }
        ]
    },
    "jobres": {
        "name": "JobRes",
        "columns": [
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "ImpLevel"
            },
            {
                "type": "Integer",
                "name": "Ord"
            },
            {
                "type": "Integer",
                "name": "RefLin"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Layer_Name"
            }
        ]
    },
    "cms_ui_toolmoddb": {
        "name": "CMS_UI_ToolModDb",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "GroupName"
            },
            {
                "type": "Integer",
                "name": "DropData"
            }
        ]
    },
    "csv_param": {
        "name": "CSV_PARAM",
        "columns": [
            {
                "length": 10,
                "type": "String",
                "name": "PARAM_TYPE"
            },
            {
                "type": "Integer",
                "name": "ID"
            },
            {
                "length": 250,
                "type": "String",
                "name": "LIB"
            }
        ]
    },
    "cms_tool_csv": {
        "name": "CMS_TOOL_CSV",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            }
        ]
    },
    "amt_bor": {
        "name": "AMT_BOR",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_INT"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            }
        ]
    },
    "dss_metric_results": {
        "name": "DSS_METRIC_RESULTS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_VALUE_INDEX"
            },
            {
                "type": "Numeric",
                "name": "METRIC_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "METRIC_CHAR_VALUE"
            },
            {
                "type": "Integer",
                "name": "METRIC_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "POSITION_ID"
            }
        ]
    },
    "monitor_count": {
        "name": "MONITOR_COUNT",
        "columns": [
            {
                "type": "Integer",
                "name": "CNXID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROC_NAME"
            },
            {
                "type": "Integer",
                "name": "STEP_NUM"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TAB_NAME"
            },
            {
                "type": "Integer",
                "name": "NBLINE"
            }
        ]
    },
    "cms_inf_ora_localdb": {
        "name": "CMS_INF_ORA_LocalDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            },
            {
                "type": "Integer",
                "name": "Credential_ID"
            },
            {
                "type": "Integer",
                "name": "Server_ID"
            },
            {
                "type": "Integer",
                "name": "Service_Unique_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Portal_URL"
            },
            {
                "type": "Integer",
                "name": "ToMigrate"
            }
        ]
    },
    "viewer_user_roles": {
        "name": "VIEWER_USER_ROLES",
        "columns": [
            {
                "type": "Integer",
                "name": "USER_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "ROLE_ID"
            }
        ]
    },
    "dss_work_obj_typ": {
        "name": "DSS_WORK_OBJ_TYP",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            }
        ]
    },
    "in_parameters": {
        "name": "IN_PARAMETERS",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "PARAMETER_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "PARAMETER_ORDER"
            },
            {
                "type": "Integer",
                "name": "PARAMETER_KIND"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PARAMETER_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PARAMETER_TYPE"
            },
            {
                "type": "Integer",
                "name": "PROPERTY"
            }
        ]
    },
    "efp_obj_cpt_statuses": {
        "name": "EFP_OBJ_CPT_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Integer",
                "name": "IS_ART"
            },
            {
                "type": "Numeric",
                "name": "RESULT_COUNT"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_SNAPSHOT_ID"
            }
        ]
    },
    "wk_dia_objcallers": {
        "name": "WK_DIA_OBJCALLERS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "wk_dia_cobpsbpgm": {
        "name": "WK_DIA_COBPSBPGM",
        "columns": [
            {
                "type": "Integer",
                "name": "APPIDPGM"
            },
            {
                "type": "Integer",
                "name": "PSB"
            },
            {
                "type": "Integer",
                "name": "PGM"
            }
        ]
    },
    "wk_dia_cob_static": {
        "name": "WK_DIA_COB_STATIC",
        "columns": [
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "pmc_archi_allow_links": {
        "name": "PMC_ARCHI_ALLOW_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            }
        ]
    },
    "modcom": {
        "name": "ModCom",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            },
            {
                "type": "Integer",
                "name": "Typ"
            },
            {
                "type": "Integer",
                "name": "SubTyp"
            },
            {
                "type": "Integer",
                "name": "Grid"
            },
            {
                "type": "Integer",
                "name": "Grp"
            }
        ]
    },
    "colrefobj": {
        "name": "ColRefObj",
        "columns": [
            {
                "type": "Integer",
                "name": "IdCol"
            },
            {
                "type": "String",
                "length": 250,
                "name": "TypNam"
            },
            {
                "type": "Integer",
                "name": "TypTyp"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 6,
                "name": "ObjTyp"
            },
            {
                "type": "Integer",
                "name": "ItmTyp"
            }
        ]
    },
    "viewer_worktable2": {
        "name": "VIEWER_WORKTABLE2",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "OBJECT_NAME"
            }
        ]
    },
    "cms_inf_css_centraldb": {
        "name": "CMS_INF_CSS_CentralDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            },
            {
                "type": "Integer",
                "name": "Credential_ID"
            },
            {
                "type": "Integer",
                "name": "Server_ID"
            },
            {
                "type": "Integer",
                "name": "Service_Unique_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Portal_URL"
            },
            {
                "type": "Integer",
                "name": "ToMigrate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CorporateName"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProductivityFilePath"
            }
        ]
    },
    "in_links_chk": {
        "name": "IN_LINKS_CHK",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "PROJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "SOURCE_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "TARGET_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "PROJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DESCRIPTION"
            }
        ]
    },
    "fnc": {
        "name": "Fnc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFnc",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 128,
                "name": "FncNam"
            },
            {
                "type": "Integer",
                "name": "RetDtp"
            },
            {
                "type": "Integer",
                "name": "RetLen"
            },
            {
                "type": "Integer",
                "name": "RetPrc"
            },
            {
                "type": "Integer",
                "name": "RetScl"
            },
            {
                "type": "Integer",
                "name": "FncClass"
            },
            {
                "type": "Integer",
                "name": "FncProp"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "dssapp_olia_tmp_forms": {
        "name": "DSSAPP_OLIA_TMP_FORMS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "adg_metric_svssu": {
        "name": "ADG_METRIC_SVSSU",
        "columns": [
            {
                "type": "Integer",
                "name": "CONTEXT_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Numeric",
                "name": "OBJ_THRESHOLD"
            },
            {
                "type": "Integer",
                "name": "OBJ_COUNT"
            },
            {
                "type": "Numeric",
                "name": "PER"
            },
            {
                "type": "Integer",
                "name": "ADDED"
            },
            {
                "type": "Integer",
                "name": "DELETED"
            },
            {
                "type": "Integer",
                "name": "UPDATED"
            },
            {
                "type": "Integer",
                "name": "TOTAL"
            }
        ]
    },
    "consistency_log": {
        "name": "CONSISTENCY_LOG",
        "columns": [
            {
                "type": "String",
                "length": 1000,
                "name": "DESCRIPTION"
            },
            {
                "type": "Integer",
                "name": "CHK"
            },
            {
                "type": "TIMESTAMP",
                "name": "DATETEST"
            }
        ]
    },
    "dss_metric_type_trees_upgrade": {
        "name": "DSS_METRIC_TYPE_TREES_UPGRADE",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_INDEX"
            },
            {
                "type": "Numeric",
                "name": "AGGREGATE_WEIGHT"
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_SCOPE_PROCEDURE_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_SCOPE_PROCEDURE_NAME_2"
            }
        ]
    },
    "server_ids": {
        "name": "SERVER_IDS",
        "columns": [
            {
                "type": "Integer",
                "name": "NEXT_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "ID_CATEGORY"
            }
        ]
    },
    "cms_ua_apptechno": {
        "name": "CMS_UA_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "cms_code_repo_uiextract": {
        "name": "CMS_CODE_REPO_UIExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "cms_sqlsrv_apptechno": {
        "name": "CMS_SQLSRV_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "objpar": {
        "name": "ObjPar",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ParNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ParTyp"
            },
            {
                "type": "Integer",
                "name": "ParKnd"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "efp_tran_info": {
        "name": "EFP_Tran_Info",
        "columns": [
            {
                "type": "Integer",
                "name": "Snapshot_ID"
            },
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "Object_Checksum"
            }
        ]
    },
    "in_ref_properties_chk": {
        "name": "IN_REF_PROPERTIES_CHK",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "REFERENCE_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "REFERENCE_KIND"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DESCRIPTION"
            }
        ]
    },
    "cms_am_parm_intoverrides": {
        "name": "CMS_AM_PARM_IntOverrides",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "ContextParam"
            },
            {
                "type": "Integer",
                "name": "IntValue"
            }
        ]
    },
    "appmarq_applicationtypemodel": {
        "name": "AppMarq_ApplicationTypeModel",
        "columns": [
            {
                "type": "Integer",
                "name": "ApplicationTypeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "ApplicationTypeName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "ApplicationTypeDescription"
            }
        ]
    },
    "wk_dia_entlink": {
        "name": "WK_DIA_ENTLINK",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            },
            {
                "type": "String",
                "length": 500,
                "name": "ASSOC_TYP"
            }
        ]
    },
    "cms_inf_snapshot": {
        "name": "CMS_INF_Snapshot",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "TIMESTAMP",
                "name": "FunctionalDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "VersionLabel"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Central_ID"
            }
        ]
    },
    "dss_metric_execution_list": {
        "name": "DSS_METRIC_EXECUTION_LIST",
        "columns": [
            {
                "type": "Integer",
                "name": "OPERATION_STATUS"
            },
            {
                "type": "Integer",
                "name": "OPERATION_TYPE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OPERATION_PROCNAME"
            },
            {
                "type": "Integer",
                "name": "METRIC_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_CHILD_OR_VALUE"
            }
        ]
    },
    "appmarq_technotechidx": {
        "name": "AppMarq_TechnoTechIdx",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "SnapshotId"
            },
            {
                "type": "Integer",
                "name": "TechnologyId"
            },
            {
                "type": "Integer",
                "name": "TechnicalCriterionId"
            },
            {
                "type": "Numeric",
                "name": "TechnicalCriterionGrade"
            }
        ]
    },
    "cms_inf_ora_credential": {
        "name": "CMS_INF_ORA_Credential",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UserName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Password"
            }
        ]
    },
    "prop": {
        "name": "Prop",
        "columns": [
            {
                "type": "Integer",
                "name": "IdProp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PropNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PropDsc"
            },
            {
                "type": "Integer",
                "name": "PropTyp"
            },
            {
                "type": "String",
                "length": 3,
                "name": "PropMrg"
            },
            {
                "type": "Integer",
                "name": "CardMin"
            },
            {
                "type": "Integer",
                "name": "CardMax"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "frmapp": {
        "name": "FrmApp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdApp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AppNam"
            },
            {
                "type": "Integer",
                "name": "AppClass"
            },
            {
                "type": "Integer",
                "name": "AppProp"
            }
        ]
    },
    "accgrpraw": {
        "name": "AccGrpRaw",
        "columns": [
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "IdAccGrp"
            }
        ]
    },
    "in_propcat": {
        "name": "IN_PROPCAT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDPROP"
            },
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "wk_dia_classmember": {
        "name": "WK_DIA_CLASSMEMBER",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_CLASS"
            },
            {
                "type": "Integer",
                "name": "ID_MEMBER"
            },
            {
                "type": "Integer",
                "name": "MEMBER_TYPE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "MEMBER_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "MEMBER_FULLNAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE_EXT"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "pmc_subset_objects": {
        "name": "PMC_SUBSET_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SUBSET_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "tmp_fileproject": {
        "name": "TMP_FILEPROJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDPRO"
            },
            {
                "type": "Integer",
                "name": "FILETYPE"
            },
            {
                "type": "Integer",
                "name": "IDFILE"
            },
            {
                "type": "String",
                "length": 600,
                "name": "FILEPATH"
            },
            {
                "type": "Integer",
                "name": "FILECRC"
            }
        ]
    },
    "csv_status": {
        "name": "CSV_STATUS",
        "columns": [
            {
                "type": "Integer",
                "name": "CSV_VER"
            },
            {
                "type": "Integer",
                "name": "CSV_TYP"
            },
            {
                "type": "String",
                "length": 3,
                "name": "USRLCK"
            },
            {
                "type": "TIMESTAMP",
                "name": "LASTUPDDATE"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            }
        ]
    },
    "work_imported_selection": {
        "name": "WORK_IMPORTED_SELECTION",
        "columns": [
            {
                "type": "Integer",
                "name": "IMPORT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "KEY_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_LEVEL"
            }
        ]
    },
    "dss_transactionroots": {
        "name": "DSS_TransactionRoots",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "Root_ID"
            },
            {
                "type": "Integer",
                "name": "MergeFlags"
            }
        ]
    },
    "sys_site_options": {
        "name": "SYS_SITE_OPTIONS",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "OPTION_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OPTION_VALUE"
            }
        ]
    },
    "cms_cpp_path": {
        "name": "CMS_CPP_Path",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ClassPath"
            },
            {
                "type": "Integer",
                "name": "Recursive"
            }
        ]
    },
    "dss_in_metric_results": {
        "name": "DSS_IN_METRIC_RESULTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_VALUE_INDEX"
            },
            {
                "type": "Numeric",
                "name": "METRIC_NUM_VALUE"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "METRIC_CHAR_VALUE"
            },
            {
                "type": "Integer",
                "name": "METRIC_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "POSITION_ID"
            }
        ]
    },
    "sys_site_data": {
        "name": "SYS_SITE_DATA",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "DATA_NAME"
            },
            {
                "name": "DATA_VALUE"
            },
            {
                "type": "Integer",
                "name": "DATA_BLOCK"
            },
            {
                "type": "Integer",
                "name": "DATA_SIZE"
            }
        ]
    },
    "work_action_plan_set": {
        "name": "WORK_ACTION_PLAN_SET",
        "columns": [
            {
                "length": 255,
                "type": "String",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "cms_asp_prodoptions": {
        "name": "CMS_ASP_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "CallLightImport"
            },
            {
                "type": "Integer",
                "name": "IncludeLightImport"
            },
            {
                "type": "Integer",
                "name": "MaxComplixity"
            },
            {
                "type": "Integer",
                "name": "MaxCodeSize"
            }
        ]
    },
    "cms_sap_analysis": {
        "name": "CMS_SAP_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TablesPath"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TableSize"
            }
        ]
    },
    "genapptxt": {
        "name": "GenAppTxt",
        "columns": [
            {
                "type": "Integer",
                "name": "IdApp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "RegExp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Txt"
            },
            {
                "type": "Integer",
                "name": "RegExpTyp"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            }
        ]
    },
    "wk_dia_strutsmtd": {
        "name": "WK_DIA_STRUTSMTD",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID_JSP"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID_JAVA"
            },
            {
                "type": "Integer",
                "name": "BEAN_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "VALIDATOR_ID"
            },
            {
                "type": "Integer",
                "name": "METHOD_ID"
            },
            {
                "type": "Integer",
                "name": "KO_ID"
            }
        ]
    },
    "cms_ua_project": {
        "name": "CMS_UA_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "LanguagesStr"
            }
        ]
    },
    "wk_dia_asp_include": {
        "name": "WK_DIA_ASP_INCLUDE",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            }
        ]
    },
    "cms_forms_project": {
        "name": "CMS_FORMS_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            }
        ]
    },
    "cms_code_cont_extract": {
        "name": "CMS_CODE_CONT_Extract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            }
        ]
    },
    "amt_objfname": {
        "name": "AMT_OBJFNAME",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "STRING_BLOCK"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPERTY_STRING"
            }
        ]
    },
    "appmarq_releasesperyearmodel": {
        "name": "AppMarq_ReleasesPerYearModel",
        "columns": [
            {
                "type": "Integer",
                "name": "ReleasesPerYearId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "ReleasesPerYearName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "ReleasesPerYearDescription"
            }
        ]
    },
    "apm_work_metric_list": {
        "name": "APM_WORK_METRIC_LIST",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            }
        ]
    },
    "cms_dep_linkunit": {
        "name": "CMS_DEP_LinkUnit",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Content_Mode"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type_Mode"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name_Mode"
            },
            {
                "type": "Integer",
                "name": "App_ID"
            }
        ]
    },
    "tmp_dia_link": {
        "name": "TMP_DIA_LINK",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            }
        ]
    },
    "amt_parameters": {
        "name": "AMT_PARAMETERS",
        "columns": [
            {
                "type": "Integer",
                "name": "PARAMETER_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "PARAMETER_ORDER"
            },
            {
                "type": "Integer",
                "name": "PARAMETER_KIND"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PARAMETER_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PARAMETER_TYPE"
            },
            {
                "type": "Integer",
                "name": "PROPERTY"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            }
        ]
    },
    "cms_am_parm_strings": {
        "name": "CMS_AM_PARM_Strings",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "StringValue"
            }
        ]
    },
    "appmarq_technohf": {
        "name": "AppMarq_TechnoHF",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "SnapshotId"
            },
            {
                "type": "Integer",
                "name": "TechnologyId"
            },
            {
                "type": "Integer",
                "name": "BusinessCriterionId"
            },
            {
                "type": "Numeric",
                "name": "BusinessCriterionGrade"
            }
        ]
    },
    "pmc_subsets": {
        "name": "PMC_SUBSETS",
        "columns": [
            {
                "type": "Integer",
                "name": "SUBSET_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SUBSET_NAME"
            }
        ]
    },
    "esc_accdonotignore": {
        "name": "ESC_AccDoNotIgnore",
        "columns": [
            {
                "type": "Integer",
                "name": "IdAcc"
            }
        ]
    },
    "wk_dia_netutlcls": {
        "name": "WK_DIA_NETUTLCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_CLASS"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "MEMBER_TYPE"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            }
        ]
    },
    "dssapp_ifpug_det_children": {
        "name": "DSSAPP_IFPUG_DET_CHILDREN",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_MAIN_OBJECT"
            },
            {
                "type": "Integer",
                "name": "ID_CHILD_OBJECT"
            }
        ]
    },
    "dss_keysextradeleted": {
        "name": "DSS_KeysExtraDeleted",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "Key_ID"
            },
            {
                "type": "Integer",
                "name": "Appli_ID"
            }
        ]
    },
    "appmarq_functionaldomainmodel": {
        "name": "AppMarq_FunctionalDomainModel",
        "columns": [
            {
                "type": "Integer",
                "name": "FunctionalDomainId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "FunctionalDomainName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "FunctionalDomainDescription"
            }
        ]
    },
    "apm_mi_worktable": {
        "name": "APM_MI_WORKTABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NODE"
            },
            {
                "type": "Numeric",
                "name": "RESULT"
            },
            {
                "type": "Numeric",
                "name": "RESULT_2"
            },
            {
                "type": "Numeric",
                "name": "RESULT_3"
            },
            {
                "type": "Numeric",
                "name": "RESULT_4"
            },
            {
                "type": "Numeric",
                "name": "RESULT_5"
            },
            {
                "type": "Numeric",
                "name": "RESULT_6"
            }
        ]
    },
    "dss_objects": {
        "name": "DSS_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_NAME"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "OBJECT_DESCRIPTION"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "OBJECT_FULL_NAME"
            },
            {
                "type": "Integer",
                "name": "OBJECT_CHECKSUM"
            }
        ]
    },
    "cms_udb_project": {
        "name": "CMS_UDB_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            }
        ]
    },
    "classobjtyp": {
        "name": "ClassObjTyp",
        "columns": [
            {
                "type": "Integer",
                "name": "Class"
            },
            {
                "type": "Integer",
                "name": "ObjTyp"
            }
        ]
    },
    "dss_datafunction": {
        "name": "DSS_DataFunction",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "MainTable_ID"
            },
            {
                "type": "Integer",
                "name": "DET"
            },
            {
                "type": "Integer",
                "name": "RET"
            },
            {
                "type": "Integer",
                "name": "ILF"
            },
            {
                "type": "Integer",
                "name": "ILF_Ex"
            },
            {
                "type": "Integer",
                "name": "IsInternal"
            },
            {
                "type": "Integer",
                "name": "Appli_ID"
            },
            {
                "type": "Integer",
                "name": "User_FP_Value"
            },
            {
                "type": "Integer",
                "name": "User_IsInternal"
            },
            {
                "type": "Integer",
                "name": "Cal_Flags"
            },
            {
                "type": "Integer",
                "name": "Cal_MergeRoot_ID"
            }
        ]
    },
    "cms_tool_progafter": {
        "name": "CMS_TOOL_ProgAfter",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "VarContainer_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProgName"
            },
            {
                "type": "Integer",
                "name": "ProgWait"
            }
        ]
    },
    "cms_asp_apptechno": {
        "name": "CMS_ASP_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "anainf": {
        "name": "AnaInf",
        "columns": [
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "InfTyp"
            },
            {
                "type": "Integer",
                "name": "InfSubTyp"
            },
            {
                "type": "Integer",
                "name": "BlkNo"
            },
            {
                "type": "Integer",
                "name": "InfVal"
            }
        ]
    },
    "cms_cpp_anaoptions": {
        "name": "CMS_CPP_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cpp_Compilation"
            },
            {
                "type": "Integer",
                "name": "Managed_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "C_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cpp_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DevEnv_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Stl_Usage"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ForceInclude"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PrecompiledHeader"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PchGenerator"
            },
            {
                "type": "Integer",
                "name": "DisableUseofPch"
            },
            {
                "type": "Integer",
                "name": "MagicRgtShift"
            },
            {
                "type": "Integer",
                "name": "Trigraph"
            },
            {
                "type": "Integer",
                "name": "StdScope"
            },
            {
                "type": "Integer",
                "name": "IsoTypename"
            },
            {
                "type": "Integer",
                "name": "UnknownDirective"
            }
        ]
    },
    "cms_sap_deftechno": {
        "name": "CMS_SAP_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "dss_metric_work_except": {
        "name": "DSS_METRIC_WORK_EXCEPT",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "enaction": {
        "name": "ENAction",
        "columns": [
            {
                "type": "Integer",
                "name": "IdENMod"
            },
            {
                "type": "Integer",
                "name": "ActionType"
            },
            {
                "type": "Integer",
                "name": "ActionTypeIndex"
            }
        ]
    },
    "cms_ua_rfdefinition": {
        "name": "CMS_UA_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "dss_metric_values": {
        "name": "DSS_METRIC_VALUES",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "METRIC_NAME"
            },
            {
                "type": "Numeric",
                "name": "METRIC_GRADE"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SNAPSHOT_NAME"
            },
            {
                "type": "Integer",
                "name": "CONTEXT_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "CONTEXT_NAME"
            },
            {
                "type": "TIMESTAMP",
                "name": "FUNCTIONAL_DATE"
            }
        ]
    },
    "wk_dia_prstcls": {
        "name": "WK_DIA_PRSTCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "ENTITY_ID"
            }
        ]
    },
    "accsyn": {
        "name": "AccSyn",
        "columns": [
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "IdSyn"
            }
        ]
    },
    "dss_work_objlnk_type": {
        "name": "DSS_WORK_OBJLNK_TYPE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            }
        ]
    },
    "objpro": {
        "name": "ObjPro",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "in_catcat": {
        "name": "IN_CATCAT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "Integer",
                "name": "IDCATPARENT"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "cms_forms_rfdefinition": {
        "name": "CMS_FORMS_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "cal_setassociation": {
        "name": "CAL_SetAssociation",
        "columns": [
            {
                "type": "Integer",
                "name": "Set_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AttributeName"
            },
            {
                "type": "Numeric",
                "name": "AttributeNumValue"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AttributeCharValue"
            }
        ]
    },
    "cms_am_qual_hf_selection": {
        "name": "CMS_AM_QUAL_HF_Selection",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Selection"
            }
        ]
    },
    "viewer_data_renderers": {
        "name": "VIEWER_DATA_RENDERERS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PARENT_COMPONENT_ID"
            },
            {
                "type": "Integer",
                "name": "CHILD_OFFSET"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "CLASS_PATH"
            }
        ]
    },
    "modlnk": {
        "name": "ModLnk",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            },
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "AccNum"
            },
            {
                "type": "Integer",
                "name": "LnkArw"
            },
            {
                "name": "Lnk"
            },
            {
                "type": "Integer",
                "name": "FirstNum"
            },
            {
                "type": "Integer",
                "name": "SecondNum"
            },
            {
                "type": "Integer",
                "name": "IdLay"
            },
            {
                "type": "Integer",
                "name": "LnkVis"
            },
            {
                "type": "Integer",
                "name": "AccTypLo"
            },
            {
                "type": "Integer",
                "name": "AccTypHi"
            },
            {
                "type": "Integer",
                "name": "Dist"
            }
        ]
    },
    "cms_inf_store_sqlserver": {
        "name": "CMS_INF_STORE_SqlServer",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Discover_Flag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UserName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Password"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Host"
            },
            {
                "type": "Integer",
                "name": "Access_ID"
            },
            {
                "type": "Integer",
                "name": "Trusted"
            }
        ]
    },
    "ci_parents": {
        "name": "CI_PARENTS",
        "columns": [
            {
                "type": "String",
                "length": 590,
                "name": "OBJECT_GUID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "PARENT_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "PARENT_SHORTGUID"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "cms_net_folder": {
        "name": "CMS_NET_FOLDER",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Parent_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            }
        ]
    },
    "cltfnc": {
        "name": "CltFnc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFnc"
            },
            {
                "type": "String",
                "length": 240,
                "name": "FncNam"
            },
            {
                "type": "Integer",
                "name": "FncClass"
            },
            {
                "type": "Integer",
                "name": "FncProp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Mangling"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            }
        ]
    },
    "cms_net_webproject": {
        "name": "CMS_NET_WebProject",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "jscriptUsage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "frameworkVersion"
            },
            {
                "type": "String",
                "length": 255,
                "name": "compilationConstants"
            },
            {
                "type": "String",
                "length": 255,
                "name": "assemblyName"
            }
        ]
    },
    "ctt_link_decode_type": {
        "name": "CTT_LINK_DECODE_TYPE",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_TYPE_LO"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_HI"
            },
            {
                "type": "Integer",
                "name": "LINK_CATEGORY"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LINK_TYPE_STR"
            }
        ]
    },
    "gentyp": {
        "name": "GenTyp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdTyp"
            },
            {
                "type": "String",
                "length": 30,
                "name": "TypNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TypLib"
            },
            {
                "type": "Integer",
                "name": "IdIco"
            },
            {
                "type": "Integer",
                "name": "TypTyp"
            }
        ]
    },
    "cms_am_moduleconsomode": {
        "name": "CMS_AM_ModuleConsoMode",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            },
            {
                "type": "Integer",
                "name": "noneConsolidationMode"
            }
        ]
    },
    "apm_rulescheck_tmp": {
        "name": "APM_RULESCHECK_TMP",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "OBJECT_NAME"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OVERPARENT_ID"
            },
            {
                "type": "Integer",
                "name": "FLAT_LEVEL"
            },
            {
                "type": "Integer",
                "name": "OBJECT_GROUP"
            }
        ]
    },
    "work_selection_tree": {
        "name": "WORK_SELECTION_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_LEVEL"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "PROJECT_ID"
            },
            {
                "type": "Integer",
                "name": "IS_PARENT"
            }
        ]
    },
    "fp_cms_application": {
        "name": "FP_CMS_Application",
        "columns": [
            {
                "type": "Integer",
                "name": "Appli_ID"
            },
            {
                "type": "Integer",
                "name": "Module_ID"
            }
        ]
    },
    "tab": {
        "name": "Tab",
        "columns": [
            {
                "type": "Integer",
                "name": "IdTab",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 128,
                "name": "TabNam"
            },
            {
                "type": "Integer",
                "name": "TabClass"
            },
            {
                "type": "Integer",
                "name": "TabProp"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "cms_ua_deftechno": {
        "name": "CMS_UA_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "cms_net_project": {
        "name": "CMS_NET_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "jscriptUsage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "frameworkVersion"
            },
            {
                "type": "String",
                "length": 255,
                "name": "compilationConstants"
            },
            {
                "type": "String",
                "length": 255,
                "name": "assemblyName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "defaultNamespace"
            },
            {
                "type": "Integer",
                "name": "allowUnsafeBlocks"
            }
        ]
    },
    "dssapp_all_artifacts": {
        "name": "DSSAPP_ALL_ARTIFACTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            }
        ]
    },
    "cms_portf_application": {
        "name": "CMS_PORTF_Application",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "DeployPath"
            },
            {
                "type": "Integer",
                "name": "Version_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "PrepSnapExecDate"
            },
            {
                "type": "Integer",
                "name": "LocalDB_ID"
            },
            {
                "type": "String",
                "length": 1050,
                "name": "Mail"
            }
        ]
    },
    "appmarq_rules": {
        "name": "AppMarq_Rules",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "type": "Integer",
                "name": "RuleId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "RuleName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "RuleDescription"
            },
            {
                "type": "Numeric",
                "name": "RuleThreshold1"
            },
            {
                "type": "Numeric",
                "name": "RuleThreshold2"
            },
            {
                "type": "Numeric",
                "name": "RuleThreshold3"
            },
            {
                "type": "Numeric",
                "name": "RuleThreshold4"
            }
        ]
    },
    "fp_dataendpoints": {
        "name": "FP_DataEndPoints",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "GenericType"
            },
            {
                "type": "Integer",
                "name": "Appli_ID"
            },
            {
                "type": "Integer",
                "name": "FP_Value"
            },
            {
                "type": "Integer",
                "name": "DET_Value"
            },
            {
                "type": "Integer",
                "name": "RET_Value"
            }
        ]
    },
    "dss_code_bookmarks": {
        "name": "DSS_CODE_BOOKMARKS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "POSITION_ID"
            },
            {
                "type": "Integer",
                "name": "RANK"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LOCAL_SITE_ID"
            },
            {
                "type": "Integer",
                "name": "LOCAL_SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "START_LINE"
            },
            {
                "type": "Integer",
                "name": "START_COLUMN"
            },
            {
                "type": "Integer",
                "name": "END_LINE"
            },
            {
                "type": "Integer",
                "name": "END_COLUMN"
            },
            {
                "type": "Integer",
                "name": "LOCAL_POSITION_ID"
            }
        ]
    },
    "in_libobjmaj": {
        "name": "IN_LIBOBJMAJ",
        "columns": [
            {
                "type": "Integer",
                "name": "IDPARENT"
            },
            {
                "type": "Integer",
                "name": "IDLIB"
            },
            {
                "type": "Integer",
                "name": "TYPE"
            },
            {
                "type": "Integer",
                "name": "SESSION_ID"
            }
        ]
    },
    "cms_j2ee_uncontfstargetdfm": {
        "name": "CMS_J2EE_UncontFSTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "wk_dia_singltctor": {
        "name": "WK_DIA_SINGLTCTOR",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_CLASS"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_inf_store_oracle": {
        "name": "CMS_INF_STORE_Oracle",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Discover_Flag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UserName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Password"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Host"
            },
            {
                "type": "Integer",
                "name": "Port"
            },
            {
                "type": "Integer",
                "name": "Access_ID"
            }
        ]
    },
    "cms_am_desc_reference": {
        "name": "CMS_AM_DESC_Reference",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            }
        ]
    },
    "cms_am_qual_tgradesettings": {
        "name": "CMS_AM_QUAL_TGradeSettings",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Weight"
            },
            {
                "type": "Integer",
                "name": "Critical"
            },
            {
                "type": "Integer",
                "name": "TechnicalCriterion"
            },
            {
                "type": "Integer",
                "name": "QualityRuleDistributionMeasure"
            }
        ]
    },
    "appset": {
        "name": "APPSET",
        "columns": [
            {
                "type": "Integer",
                "name": "IDSET"
            },
            {
                "type": "String",
                "length": 600,
                "name": "IDSETNAM"
            },
            {
                "type": "Integer",
                "name": "IDJOB"
            }
        ]
    },
    "cms_rf_embedregexp": {
        "name": "CMS_RF_EmbedRegExp",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "RF_ID"
            }
        ]
    },
    "cms_inf_store_css": {
        "name": "CMS_INF_STORE_CSS",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Discover_Flag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UserName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Password"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Host"
            },
            {
                "type": "Integer",
                "name": "Port"
            }
        ]
    },
    "cms_next_id": {
        "name": "CMS_NEXT_ID",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "Lib"
            },
            {
                "type": "Integer",
                "name": "IntVal"
            }
        ]
    },
    "appmarq_endusersrangemodel": {
        "name": "AppMarq_EndUsersRangeModel",
        "columns": [
            {
                "type": "Integer",
                "name": "EndUsersRangeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "EndUsersRangeName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "EndUsersRangeDescription"
            }
        ]
    },
    "diag_object_parents": {
        "name": "DIAG_OBJECT_PARENTS",
        "columns": [
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_TYPE"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            }
        ]
    },
    "cms_code_sourcefile": {
        "name": "CMS_CODE_SourceFile",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Usage"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            }
        ]
    },
    "dssapp_package": {
        "name": "DSSAPP_PACKAGE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "CE"
            },
            {
                "type": "Integer",
                "name": "CA"
            }
        ]
    },
    "dss_metric_descriptions": {
        "name": "DSS_METRIC_DESCRIPTIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "DESCRIPTION_TYPE_ID"
            },
            {
                "type": "String",
                "length": 200,
                "name": "LANGUAGE"
            },
            {
                "type": "String",
                "length": 3000,
                "name": "METRIC_DESCRIPTION"
            }
        ]
    },
    "usrpro": {
        "name": "UsrPro",
        "columns": [
            {
                "type": "Integer",
                "name": "IdUsrPro"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UsrProNam"
            },
            {
                "type": "Integer",
                "name": "ORDNUM"
            }
        ]
    },
    "appmarq_rules_techcriteria": {
        "name": "AppMarq_Rules_TechCriteria",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "type": "Integer",
                "name": "RuleId"
            },
            {
                "type": "Integer",
                "name": "TechnicalCriterionId"
            },
            {
                "type": "Numeric",
                "name": "AggregationWeight"
            }
        ]
    },
    "cal_objsetdef": {
        "name": "CAL_ObjSetDef",
        "columns": [
            {
                "type": "Integer",
                "name": "Set_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SetName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SetType"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SetTable"
            },
            {
                "type": "Text",
                "name": "SetDefinition"
            }
        ]
    },
    "rul": {
        "name": "Rul",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRul"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 128,
                "name": "RulNam"
            }
        ]
    },
    "cms_am_desc_rationale": {
        "name": "CMS_AM_DESC_Rationale",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            }
        ]
    },
    "work_selection": {
        "name": "WORK_SELECTION",
        "columns": [
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            },
            {
                "type": "Integer",
                "name": "KEY_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "PROJECT_ID"
            },
            {
                "type": "Integer",
                "name": "IS_SELECTED"
            },
            {
                "type": "Integer",
                "name": "KEY_LEVEL"
            }
        ]
    },
    "cms_net_vbproject": {
        "name": "CMS_NET_VBProject",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "jscriptUsage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "frameworkVersion"
            },
            {
                "type": "String",
                "length": 255,
                "name": "compilationConstants"
            },
            {
                "type": "String",
                "length": 255,
                "name": "assemblyName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "rootNamespace"
            },
            {
                "type": "Integer",
                "name": "optionExplicit"
            },
            {
                "type": "Integer",
                "name": "optionStrict"
            },
            {
                "type": "Integer",
                "name": "optionInfer"
            }
        ]
    },
    "qr_subset_objects": {
        "name": "QR_Subset_Objects",
        "columns": [
            {
                "type": "Integer",
                "name": "SUBSET_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "cms_net_xsstargetdfm": {
        "name": "CMS_NET_XSSTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "dss_log_metric_scopes": {
        "name": "DSS_LOG_METRIC_SCOPES",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Numeric",
                "name": "METRIC_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "METRIC_CHAR_VALUE"
            },
            {
                "type": "Integer",
                "name": "METRIC_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "COMPUTE_VALUE"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "fp_largestscc": {
        "name": "FP_LargestSCC",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            }
        ]
    },
    "cms_cobol_config": {
        "name": "CMS_COBOL_Config",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            }
        ]
    },
    "tmp_dia_method": {
        "name": "TMP_DIA_METHOD",
        "columns": [
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "METHOD_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "keydfc": {
        "name": "KeyDfc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "IdDfc"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "histo_cat": {
        "name": "HISTO_CAT",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CATNAM"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CATDSC"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "amt_objname": {
        "name": "AMT_OBJNAME",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPERTY_STRING"
            }
        ]
    },
    "dssapp_all_methods_simple": {
        "name": "DSSAPP_ALL_METHODS_SIMPLE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            }
        ]
    },
    "dss_in_object_ranking": {
        "name": "DSS_IN_OBJECT_RANKING",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "HIT_COUNT"
            },
            {
                "type": "Integer",
                "name": "FAN_IN"
            },
            {
                "type": "Integer",
                "name": "TRAN_PROPER"
            },
            {
                "type": "Integer",
                "name": "TRAN_CUMUL"
            },
            {
                "type": "Integer",
                "name": "CHAN_PROPER"
            },
            {
                "type": "Integer",
                "name": "CHAN_CUMUL"
            },
            {
                "type": "Integer",
                "name": "ROBU_PROPER"
            },
            {
                "type": "Integer",
                "name": "ROBU_CUMUL"
            },
            {
                "type": "Integer",
                "name": "PERF_PROPER"
            },
            {
                "type": "Integer",
                "name": "PERF_CUMUL"
            },
            {
                "type": "Integer",
                "name": "SECU_PROPER"
            },
            {
                "type": "Integer",
                "name": "SECU_CUMUL"
            }
        ]
    },
    "setroot": {
        "name": "SETROOT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDSET"
            },
            {
                "type": "Integer",
                "name": "IDROOT"
            }
        ]
    },
    "cms_archi_model": {
        "name": "CMS_ARCHI_Model",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectFile"
            },
            {
                "type": "Integer",
                "name": "AggregateWeight"
            },
            {
                "type": "Integer",
                "name": "CriticalContribution"
            },
            {
                "type": "Integer",
                "name": "ExternalID"
            }
        ]
    },
    "envision_effort_child_stats": {
        "name": "ENVISION_EFFORT_CHILD_STATS",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdKeyMod"
            },
            {
                "type": "Integer",
                "name": "IdKeyChild"
            }
        ]
    },
    "out_linkobject": {
        "name": "OUT_LINKOBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            },
            {
                "type": "Integer",
                "name": "RESULT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_LEVEL"
            },
            {
                "type": "Integer",
                "name": "OBJECTTYPE_ID"
            },
            {
                "type": "Integer",
                "name": "ACCESSTYPELOW_ID"
            }
        ]
    },
    "tmp_dia_clsmember": {
        "name": "TMP_DIA_CLSMEMBER",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_CLASS"
            },
            {
                "type": "Integer",
                "name": "ID_MEMBER"
            },
            {
                "type": "Integer",
                "name": "MEMBER_TYPE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "MEMBER_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "MEMBER_FULLNAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE_EXT"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "dsprul": {
        "name": "DspRul",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRul"
            },
            {
                "type": "String",
                "length": 255,
                "name": "RulNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "RulLib"
            },
            {
                "type": "Integer",
                "name": "DftRul"
            }
        ]
    },
    "in_setlinkerunit": {
        "name": "IN_SetLinkerUnit",
        "columns": [
            {
                "type": "Integer",
                "name": "UserProjectId"
            },
            {
                "type": "Integer",
                "name": "SourceSetId"
            },
            {
                "type": "Integer",
                "name": "TargetSetId"
            }
        ]
    },
    "viewer_services": {
        "name": "VIEWER_SERVICES",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "VERSION"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "CLASS_PATH"
            }
        ]
    },
    "jvojdo": {
        "name": "JvoJdo",
        "columns": [
            {
                "type": "Integer",
                "name": "IdJdo"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JdoNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JdoFulNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JdoIdTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JdoIdCls"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JdoSupCls"
            },
            {
                "type": "Integer",
                "name": "ReqExt"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FilPath"
            }
        ]
    },
    "cms_inf_sqlsrv_centraldb": {
        "name": "CMS_INF_SQLSRV_CentralDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            },
            {
                "type": "Integer",
                "name": "Credential_ID"
            },
            {
                "type": "Integer",
                "name": "Server_ID"
            },
            {
                "type": "Integer",
                "name": "Service_Unique_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Portal_URL"
            },
            {
                "type": "Integer",
                "name": "ToMigrate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CorporateName"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProductivityFilePath"
            }
        ]
    },
    "cms_am_qual_hgradesettings": {
        "name": "CMS_AM_QUAL_HGradeSettings",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Weight"
            },
            {
                "type": "Integer",
                "name": "Critical"
            },
            {
                "type": "Integer",
                "name": "HealthFactor"
            },
            {
                "type": "Integer",
                "name": "TechnicalCriterion"
            }
        ]
    },
    "dss_module_links": {
        "name": "DSS_MODULE_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "dtp": {
        "name": "Dtp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdDtp",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 128,
                "name": "DtpNam"
            },
            {
                "type": "Integer",
                "name": "DtpSysId"
            },
            {
                "type": "Integer",
                "name": "DtpLen"
            },
            {
                "type": "Integer",
                "name": "DtpPrc"
            },
            {
                "type": "Integer",
                "name": "DtpNul"
            },
            {
                "type": "Integer",
                "name": "DtpScl"
            },
            {
                "type": "Integer",
                "name": "DtpRul"
            },
            {
                "type": "Integer",
                "name": "IdParent"
            },
            {
                "type": "Integer",
                "name": "IdItmParent"
            },
            {
                "type": "Integer",
                "name": "DtpTyp"
            },
            {
                "type": "Integer",
                "name": "DtpClass"
            },
            {
                "type": "Integer",
                "name": "DtpProp"
            },
            {
                "type": "String",
                "length": 2000,
                "name": "DtpMng"
            },
            {
                "type": "Integer",
                "name": "NumLin"
            },
            {
                "type": "Integer",
                "name": "NumCol"
            },
            {
                "type": "String",
                "length": 6,
                "name": "ParentTyp"
            },
            {
                "type": "Integer",
                "name": "DtpNat"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "appmarq_rulelongdescriptions": {
        "name": "AppMarq_RuleLongDescriptions",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "type": "Integer",
                "name": "RuleId"
            },
            {
                "type": "Integer",
                "name": "RuleLongDescriptionType"
            },
            {
                "length": 3000,
                "type": "String",
                "name": "RuleLongDescription"
            }
        ]
    },
    "wk_dia_prstrootcls": {
        "name": "WK_DIA_PRSTROOTCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            }
        ]
    },
    "pmc_archi_result_links": {
        "name": "PMC_ARCHI_RESULT_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "CALLER_SUBSET_ID"
            },
            {
                "type": "Integer",
                "name": "CALLEE_SUBSET_ID"
            }
        ]
    },
    "wk_dia_dynlink": {
        "name": "WK_DIA_DYNLINK",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            }
        ]
    },
    "cms_inf_css_localdb": {
        "name": "CMS_INF_CSS_LocalDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            },
            {
                "type": "Integer",
                "name": "Credential_ID"
            },
            {
                "type": "Integer",
                "name": "Server_ID"
            },
            {
                "type": "Integer",
                "name": "Service_Unique_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Portal_URL"
            },
            {
                "type": "Integer",
                "name": "ToMigrate"
            }
        ]
    },
    "wk_dia_prototypapp": {
        "name": "WK_DIA_PROTOTYPAPP",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            }
        ]
    },
    "cms_code_dbexecunit": {
        "name": "CMS_CODE_DbExecUnit",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "cms_oracle_project": {
        "name": "CMS_Oracle_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            }
        ]
    },
    "syndsc": {
        "name": "SynDsc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdAccSyn"
            },
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "AccTypLo"
            },
            {
                "type": "Integer",
                "name": "AccTypHi"
            }
        ]
    },
    "cms_sap_prodoptions": {
        "name": "CMS_SAP_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "wk_dia_javautlcls": {
        "name": "WK_DIA_JAVAUTLCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_CLASS"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "MEMBER_TYPE"
            }
        ]
    },
    "in_int_properties_chk": {
        "name": "IN_INT_PROPERTIES_CHK",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_INT"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DESCRIPTION"
            }
        ]
    },
    "dss_metric_status_thresholds": {
        "name": "DSS_METRIC_STATUS_THRESHOLDS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Numeric",
                "name": "THRESHOLD_1"
            },
            {
                "type": "Numeric",
                "name": "THRESHOLD_2"
            },
            {
                "type": "Numeric",
                "name": "THRESHOLD_3"
            },
            {
                "type": "Numeric",
                "name": "THRESHOLD_4"
            }
        ]
    },
    "cms_sqlsrv_project": {
        "name": "CMS_SQLSRV_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            }
        ]
    },
    "tmp_dia_coblink_status": {
        "name": "TMP_DIA_COBLINK_STATUS",
        "columns": [
            {
                "type": "Integer",
                "name": "IDCLR"
            },
            {
                "type": "Integer",
                "name": "IDCLE"
            },
            {
                "type": "Integer",
                "name": "HI"
            }
        ]
    },
    "cms_zos_analysis": {
        "name": "CMS_ZOS_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TableSize"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExtractionFileMigrated"
            }
        ]
    },
    "amt_del_prodep": {
        "name": "AMT_DEL_PRODEP",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            }
        ]
    },
    "cms_inf_versioninformation": {
        "name": "CMS_INF_VersionInformation",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Snapshot_ID"
            },
            {
                "type": "Integer",
                "name": "Module_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "VersionLabel"
            }
        ]
    },
    "uax_import_properties": {
        "name": "UAX_IMPORT_PROPERTIES",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "GROUPNAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "INSTANCE_ID"
            },
            {
                "type": "String",
                "length": 100,
                "name": "CATEGORY"
            },
            {
                "type": "String",
                "length": 100,
                "name": "PROPERTY_NAME"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "VALUE"
            }
        ]
    },
    "viewer_worktable": {
        "name": "VIEWER_WORKTABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "trg": {
        "name": "Trg",
        "columns": [
            {
                "type": "Integer",
                "name": "IdTrg",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "Integer",
                "name": "IdTab"
            },
            {
                "type": "String",
                "length": 128,
                "name": "TrgNam"
            },
            {
                "type": "Integer",
                "name": "TrgAct"
            },
            {
                "type": "Integer",
                "name": "TrgMod"
            },
            {
                "type": "Integer",
                "name": "TrgClass"
            },
            {
                "type": "Integer",
                "name": "TrgProp"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "dss_processing": {
        "name": "DSS_PROCESSING",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "PROCESS_TYPE"
            },
            {
                "type": "Integer",
                "name": "PROCESS_CURRENT_VALUE"
            },
            {
                "type": "Integer",
                "name": "PROCESS_MAX_VALUE"
            },
            {
                "type": "TIMESTAMP",
                "name": "PROCESS_START_TIME"
            },
            {
                "type": "TIMESTAMP",
                "name": "PROCESS_CURRENT_TIME"
            }
        ]
    },
    "wkt_omc_t": {
        "name": "WKT_OMC_T",
        "columns": [
            {
                "type": "Integer",
                "name": "Lvl"
            },
            {
                "type": "Integer",
                "name": "IdParent"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "IdCtx"
            }
        ]
    },
    "dia_jee_linkcall": {
        "name": "DIA_JEE_LINKCALL",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_TYPE_LO"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_HI"
            }
        ]
    },
    "dss_object_info": {
        "name": "DSS_OBJECT_INFO",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_CHECKSUM"
            }
        ]
    },
    "proroot": {
        "name": "ProRoot",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "Integer",
                "name": "IdRoot"
            }
        ]
    },
    "cms_tool_sqlafter": {
        "name": "CMS_TOOL_SqlAfter",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "VarContainer_ID"
            }
        ]
    },
    "setdep": {
        "name": "SETDEP",
        "columns": [
            {
                "type": "Integer",
                "name": "IDSET"
            },
            {
                "type": "Integer",
                "name": "IDPRO"
            }
        ]
    },
    "envision_effort_stats": {
        "name": "ENVISION_EFFORT_STATS",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdKeyMod"
            },
            {
                "type": "Integer",
                "name": "HasCsv"
            },
            {
                "type": "Integer",
                "name": "HasCost"
            },
            {
                "type": "Integer",
                "name": "HasChildCost"
            },
            {
                "type": "Integer",
                "name": "HasSupport"
            }
        ]
    },
    "cms_zos_rfdefinition": {
        "name": "CMS_ZOS_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "cms_j2ee_project": {
        "name": "CMS_J2EE_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "AppPath"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Java_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "XML_FileExtensions"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "WEB_Descriptor"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JSP_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Client_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Java_Version"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JSP_Servlet_StdVer"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JUnit_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CommonLogging_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Dom4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Hibernate_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Struts_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Spring_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Jsf_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Log4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Mx4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Ejb_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cics_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "WBS_Usage"
            }
        ]
    },
    "viewer_benchmark": {
        "name": "VIEWER_BENCHMARK",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SESSION_ID"
            }
        ]
    },
    "amt_objpro": {
        "name": "AMT_OBJPRO",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "PROP"
            },
            {
                "type": "String",
                "length": 1,
                "name": "STATUS"
            }
        ]
    },
    "cms_ora_analysis": {
        "name": "CMS_ORA_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TableSize"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExtractionFileMigrated"
            }
        ]
    },
    "amt_ignore": {
        "name": "AMT_IGNORE",
        "columns": [
            {
                "type": "Integer",
                "name": "PROJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            }
        ]
    },
    "wk_dia_netnamespace": {
        "name": "WK_DIA_NETNAMESPACE",
        "columns": [
            {
                "type": "Integer",
                "name": "GROUP_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            }
        ]
    },
    "dssapp_jeemodules": {
        "name": "DSSAPP_JEEMODULES",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "PERSIST_TYPE"
            }
        ]
    },
    "dss_metric_types": {
        "name": "DSS_METRIC_TYPES",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID",
                "primary": True
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_NAME"
            },
            {
                "type": "String",
                "length": 1500,
                "name": "METRIC_DESCRIPTION"
            },
            {
                "type": "Integer",
                "name": "METRIC_TYPE"
            },
            {
                "type": "Integer",
                "name": "METRIC_GROUP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_DEPENDS_ON"
            },
            {
                "type": "Integer",
                "name": "METRIC_OPTIONS"
            },
            {
                "type": "Integer",
                "name": "SCOPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_ID"
            }
        ]
    },
    "cms_net_apptechno": {
        "name": "CMS_NET_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "cms_j2ee_path": {
        "name": "CMS_J2EE_Path",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ClassPath"
            }
        ]
    },
    "frmtrg": {
        "name": "FrmTrg",
        "columns": [
            {
                "type": "Integer",
                "name": "IdTrg"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TrgNam"
            },
            {
                "type": "Integer",
                "name": "TrgClass"
            },
            {
                "type": "Integer",
                "name": "TrgProp"
            }
        ]
    },
    "appmarq_rules_technologies": {
        "name": "AppMarq_Rules_Technologies",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "type": "Integer",
                "name": "RuleId"
            },
            {
                "type": "Integer",
                "name": "TechnologyId"
            }
        ]
    },
    "dsprulobj": {
        "name": "DspRulObj",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRul"
            },
            {
                "type": "Integer",
                "name": "ObjTyp"
            },
            {
                "type": "Integer",
                "name": "SubTyp"
            },
            {
                "type": "Integer",
                "name": "Clr"
            }
        ]
    },
    "amt_prodep": {
        "name": "AMT_PRODEP",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "PROP"
            },
            {
                "type": "String",
                "length": 1,
                "name": "STATUS"
            }
        ]
    },
    "work_filter": {
        "name": "WORK_FILTER",
        "columns": [
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            }
        ]
    },
    "dss_metric_exceptions": {
        "name": "DSS_METRIC_EXCEPTIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_TYPE_ID"
            }
        ]
    },
    "wk_dia_statefulbean": {
        "name": "WK_DIA_STATEFULBEAN",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "INTERFACE_ID"
            }
        ]
    },
    "dss_snapshot_ranking": {
        "name": "DSS_SNAPSHOT_RANKING",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "BUSINESS_CRITERION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "VIOLATED_RULES_NB"
            },
            {
                "type": "Integer",
                "name": "VIOLATIONS_NB"
            },
            {
                "type": "Numeric",
                "name": "RISK_PROPAGATION_FACTOR"
            },
            {
                "type": "Numeric",
                "name": "VIOLATION_INDEX"
            },
            {
                "type": "Numeric",
                "name": "PROPAGATED_RISK_INDEX"
            }
        ]
    },
    "ctt_object_applications": {
        "name": "CTT_OBJECT_APPLICATIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_TYPE"
            },
            {
                "type": "Integer",
                "name": "PROPERTIES"
            }
        ]
    },
    "pmc_archi_appli_links": {
        "name": "PMC_ARCHI_APPLI_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "Integer",
                "name": "CALLEE_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_LOW"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_HIGH"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "CALLER_SUBSET_ID"
            },
            {
                "type": "Integer",
                "name": "CALLEE_SUBSET_ID"
            }
        ]
    },
    "cms_migr_rf": {
        "name": "CMS_MIGR_RF",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "String",
                "length": 1050,
                "name": "Mail"
            },
            {
                "type": "Integer",
                "name": "LocalDB_Unique_ID"
            },
            {
                "type": "Integer",
                "name": "JobType"
            },
            {
                "type": "Integer",
                "name": "SearchStrings"
            }
        ]
    },
    "wk_dia_actioncls": {
        "name": "WK_DIA_ACTIONCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            }
        ]
    },
    "cms_am_parm_intparams": {
        "name": "CMS_AM_PARM_IntParams",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "ParamIndex"
            },
            {
                "type": "Integer",
                "name": "Model_ID"
            },
            {
                "type": "Integer",
                "name": "DefValue"
            },
            {
                "type": "Integer",
                "name": "DefaultIntegerValue"
            }
        ]
    },
    "cms_code_sourcefoldercpp": {
        "name": "CMS_CODE_SourceFolderCPP",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Usage"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            }
        ]
    },
    "amt_del_link": {
        "name": "AMT_DEL_LINK",
        "columns": [
            {
                "type": "Integer",
                "name": "EXTERNAL_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_ID"
            }
        ]
    },
    "cal_next_id": {
        "name": "CAL_NEXT_ID",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "Lib"
            },
            {
                "type": "Integer",
                "name": "IntVal"
            }
        ]
    },
    "wk_dia_factorycls": {
        "name": "WK_DIA_FACTORYCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_CLASS"
            },
            {
                "type": "Integer",
                "name": "ID_METHOD"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_tool_sqlmodule": {
        "name": "CMS_TOOL_SqlModule",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "VarContainer_ID"
            }
        ]
    },
    "appmarq_snapshots": {
        "name": "AppMarq_Snapshots",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "SnapshotId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SnapshotName"
            },
            {
                "type": "TIMESTAMP",
                "name": "SnapshotDate"
            }
        ]
    },
    "wk_dia_parenthood": {
        "name": "WK_DIA_PARENTHOOD",
        "columns": [
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_TYP"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYP"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "vboapp": {
        "name": "VboApp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdApp",
                "primary": True
            },
            {
                "type": "String",
                "length": 40,
                "name": "AppNam"
            },
            {
                "type": "Integer",
                "name": "AppClass"
            },
            {
                "type": "Integer",
                "name": "AppProp"
            },
            {
                "type": "Integer",
                "name": "AnaProp"
            }
        ]
    },
    "dbg_savingunit": {
        "name": "DBG_SavingUnit",
        "columns": [
            {
                "type": "Integer",
                "name": "UnitId"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TreatmentName"
            },
            {
                "type": "TIMESTAMP",
                "name": "StartDate"
            },
            {
                "type": "TIMESTAMP",
                "name": "EndDate"
            },
            {
                "type": "Integer",
                "name": "JobId"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JobName"
            },
            {
                "type": "Integer",
                "name": "JobType"
            },
            {
                "type": "Integer",
                "name": "UsrProId"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UsrProName"
            }
        ]
    },
    "dss_object_diag_details": {
        "name": "DSS_OBJECT_DIAG_DETAILS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "BUSINESS_CRITERION_ID"
            },
            {
                "type": "Integer",
                "name": "DIAG_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "cms_net_analysis": {
        "name": "CMS_NET_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "Integer",
                "name": "sourceSelection"
            },
            {
                "type": "String",
                "length": 255,
                "name": "assemblyName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "frameworkVersion"
            },
            {
                "type": "String",
                "length": 255,
                "name": "compilationConstants"
            },
            {
                "type": "String",
                "length": 255,
                "name": "defaultNamespace"
            },
            {
                "type": "Integer",
                "name": "allowUnsafeBlocks"
            },
            {
                "type": "String",
                "length": 255,
                "name": "rootNamespace"
            },
            {
                "type": "Integer",
                "name": "optionExplicit"
            },
            {
                "type": "Integer",
                "name": "optionStrict"
            },
            {
                "type": "Integer",
                "name": "optionInfer"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            }
        ]
    },
    "amt_allil": {
        "name": "AMT_ALLIL",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "INFTYPATT"
            },
            {
                "type": "Integer",
                "name": "INFSUBTYPATT"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_INT"
            }
        ]
    },
    "cms_tool_csvbefore": {
        "name": "CMS_TOOL_CSVBefore",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            }
        ]
    },
    "csv_parent": {
        "name": "CSV_PARENT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_FULLNAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_MANGLING"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE_EXT"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "CONTAINER_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "ANALYSIS_ID"
            },
            {
                "type": "String",
                "length": 30,
                "name": "LANGUAGE_NAME"
            },
            {
                "type": "Integer",
                "name": "LVL"
            }
        ]
    },
    "cms_am_desc_remediation": {
        "name": "CMS_AM_DESC_Remediation",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            }
        ]
    },
    "dss_quality_tree": {
        "name": "DSS_QUALITY_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "B_CRITERION_ID"
            },
            {
                "type": "Integer",
                "name": "T_CRITERION_ID"
            },
            {
                "type": "Numeric",
                "name": "T_WEIGHT"
            },
            {
                "type": "Integer",
                "name": "T_CRIT"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Numeric",
                "name": "M_WEIGHT"
            },
            {
                "type": "Integer",
                "name": "M_CRIT"
            }
        ]
    },
    "tmp_dia_null": {
        "name": "TMP_DIA_NULL",
        "columns": [
            {
                "type": "Integer",
                "name": "NULL_ID"
            }
        ]
    },
    "dssapp_forms": {
        "name": "DSSAPP_FORMS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "CODE_LINES"
            },
            {
                "type": "Integer",
                "name": "FORM_WEIGHT"
            },
            {
                "type": "Integer",
                "name": "DATA_LAYER"
            },
            {
                "type": "Integer",
                "name": "FAN_OUT"
            },
            {
                "type": "Integer",
                "name": "COMPLEXITY"
            }
        ]
    },
    "in_ref_properties": {
        "name": "IN_REF_PROPERTIES",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "REFERENCE_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "REFERENCE_KIND"
            }
        ]
    },
    "in_urf_selected_objects": {
        "name": "IN_URF_SELECTED_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSIONID"
            },
            {
                "type": "Integer",
                "name": "IDOBJECT"
            }
        ]
    },
    "usr": {
        "name": "Usr",
        "columns": [
            {
                "type": "String",
                "length": 3,
                "name": "IdUsr"
            },
            {
                "type": "String",
                "length": 50,
                "name": "UsrLogin"
            },
            {
                "type": "String",
                "length": 50,
                "name": "UsrNam"
            },
            {
                "name": "UsrPwd"
            },
            {
                "type": "Integer",
                "name": "PwdLen"
            },
            {
                "type": "Integer",
                "name": "Crypting"
            },
            {
                "type": "Integer",
                "name": "IdRgtPrf"
            }
        ]
    },
    "cwlng": {
        "name": "CWLng",
        "columns": [
            {
                "type": "Integer",
                "name": "IdLng"
            },
            {
                "type": "Integer",
                "name": "LngTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LngNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LngDesc"
            },
            {
                "type": "Integer",
                "name": "LngProp"
            },
            {
                "type": "Integer",
                "name": "LngSeg"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LngXmlFile"
            }
        ]
    },
    "cms_cobol_workingfolder": {
        "name": "CMS_COBOL_WorkingFolder",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Working_Folder"
            },
            {
                "type": "Integer",
                "name": "Recursive"
            }
        ]
    },
    "sys_site": {
        "name": "SYS_SITE",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SITE_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SITE_DESCRIPTION"
            },
            {
                "type": "Integer",
                "name": "SITE_TYPE"
            },
            {
                "type": "TIMESTAMP",
                "name": "TREE_REF_DATE"
            },
            {
                "type": "Integer",
                "name": "SITE_EXTERNAL_REF"
            }
        ]
    },
    "dss_source_positions": {
        "name": "DSS_SOURCE_POSITIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "LINE_START"
            },
            {
                "type": "Integer",
                "name": "LINE_END"
            },
            {
                "type": "Integer",
                "name": "COL_START"
            },
            {
                "type": "Integer",
                "name": "COL_END"
            },
            {
                "type": "Integer",
                "name": "PANEL"
            }
        ]
    },
    "srv": {
        "name": "Srv",
        "columns": [
            {
                "type": "Integer",
                "name": "IdSrv"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SrvNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SrvHostNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SrvLib"
            },
            {
                "type": "Integer",
                "name": "SrvVer"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ApiVer"
            },
            {
                "type": "Integer",
                "name": "SrvCrc"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "cms_sap_path": {
        "name": "CMS_SAP_Path",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ClassPath"
            },
            {
                "type": "Integer",
                "name": "Recursive"
            }
        ]
    },
    "cms_inf_ora_centraldb": {
        "name": "CMS_INF_ORA_CentralDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            },
            {
                "type": "Integer",
                "name": "Credential_ID"
            },
            {
                "type": "Integer",
                "name": "Server_ID"
            },
            {
                "type": "Integer",
                "name": "Service_Unique_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Portal_URL"
            },
            {
                "type": "Integer",
                "name": "ToMigrate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CorporateName"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProductivityFilePath"
            }
        ]
    },
    "viewer_users": {
        "name": "VIEWER_USERS",
        "columns": [
            {
                "type": "Integer",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PASSWORD"
            },
            {
                "length": 200,
                "type": "String",
                "name": "LANGUAGE"
            },
            {
                "type": "Integer",
                "name": "ADMINISTRATOR"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "HOMEPAGE"
            },
            {
                "length": 200,
                "type": "String",
                "name": "EXTERNAL_ID"
            }
        ]
    },
    "vbofil": {
        "name": "VboFil",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFil"
            },
            {
                "type": "Integer",
                "name": "IdApp"
            },
            {
                "type": "String",
                "length": 600,
                "name": "FilPath"
            },
            {
                "type": "Integer",
                "name": "FilTyp"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            },
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "IdParent"
            },
            {
                "type": "Integer",
                "name": "IdFilBase"
            }
        ]
    },
    "cms_am_parm_objecttypefilters": {
        "name": "CMS_AM_PARM_ObjectTypeFilters",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "OverrideValue"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CategoryDesc"
            },
            {
                "type": "Integer",
                "name": "AmtCategory"
            }
        ]
    },
    "cms_migr_targetname": {
        "name": "CMS_MIGR_TargetName",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            }
        ]
    },
    "amt_refproperties": {
        "name": "AMT_REFPROPERTIES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "REFERENCE_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "REFERENCE_KIND"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_REFERENCE_ID"
            }
        ]
    },
    "wk_dia_object": {
        "name": "WK_DIA_OBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "histo_propattr": {
        "name": "HISTO_PROPATTR",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDPROP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ATTRNAM"
            },
            {
                "type": "Integer",
                "name": "ATTRTYP"
            },
            {
                "type": "Integer",
                "name": "INTVAL"
            },
            {
                "type": "String",
                "length": 255,
                "name": "STRVAL"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "ci_objects": {
        "name": "CI_OBJECTS",
        "columns": [
            {
                "type": "String",
                "length": 590,
                "name": "OBJECT_GUID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_FULLNAME"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "appmarq_technologyviolations": {
        "name": "AppMarq_TechnologyViolations",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "SnapshotId"
            },
            {
                "type": "Integer",
                "name": "TechnologyId"
            },
            {
                "type": "Integer",
                "name": "RuleId"
            },
            {
                "type": "Integer",
                "name": "TotalNumber"
            },
            {
                "type": "Integer",
                "name": "ViolationNumber"
            },
            {
                "type": "Numeric",
                "name": "RuleGrade"
            }
        ]
    },
    "viewer_user_views": {
        "name": "VIEWER_USER_VIEWS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "SOURCE_TABLE"
            },
            {
                "length": 200,
                "type": "String",
                "name": "MAP"
            },
            {
                "length": 2000,
                "type": "String",
                "name": "CODE"
            }
        ]
    },
    "histo_catcat": {
        "name": "HISTO_CATCAT",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "Integer",
                "name": "IDCATPARENT"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "wk_dia_jeeub002": {
        "name": "WK_DIA_JEEUB002",
        "columns": [
            {
                "type": "Integer",
                "name": "ENTITY_ID"
            },
            {
                "type": "Integer",
                "name": "PERSISTENT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "ci_no_objects": {
        "name": "CI_NO_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "OBJECT_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "OBJECT_SHORTGUID"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "cfg_appview": {
        "name": "Cfg_AppView",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "ParmNam"
            },
            {
                "type": "Integer",
                "name": "DefaultVal"
            },
            {
                "type": "Integer",
                "name": "ConfigVal"
            }
        ]
    },
    "cms_j2ee_anaoptions": {
        "name": "CMS_J2EE_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Java_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "XML_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JSP_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Client_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Java_Version"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JSP_Servlet_StdVer"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Hibernate_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Struts_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Spring_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Jsf_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CommonLogging_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Dom4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JUnit_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Log4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Mx4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cics_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "WBS_Usage"
            },
            {
                "type": "Integer",
                "name": "EnvProfWBS"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Ejb_Usage"
            },
            {
                "type": "Integer",
                "name": "EnvProfEJB"
            }
        ]
    },
    "work_object_distribution": {
        "name": "WORK_OBJECT_DISTRIBUTION",
        "columns": [
            {
                "length": 255,
                "type": "String",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NUM_VALUE"
            }
        ]
    },
    "appmarq_devmethodologymodel": {
        "name": "AppMarq_DevMethodologyModel",
        "columns": [
            {
                "type": "Integer",
                "name": "DevMethodologyId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "DevMethodologyName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "DevMethodologyDescription"
            }
        ]
    },
    "dynlink_treated": {
        "name": "DYNLINK_TREATED",
        "columns": [
            {
                "type": "Integer",
                "name": "IDACC"
            },
            {
                "type": "Integer",
                "name": "IDPRO"
            }
        ]
    },
    "tmp_dia_hbjvcollect": {
        "name": "TMP_DIA_HBJVCOLLECT",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "J_COLLECTION"
            },
            {
                "type": "String",
                "length": 255,
                "name": "H_COLLECTION"
            }
        ]
    },
    "cms_j2ee_oscmdtargetdfm": {
        "name": "CMS_J2EE_OSCmdTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "dssapp_worktable": {
        "name": "DSSAPP_WORKTABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NODE"
            },
            {
                "type": "Numeric",
                "name": "RESULT"
            },
            {
                "type": "Numeric",
                "name": "RESULT_2"
            },
            {
                "type": "Numeric",
                "name": "RESULT_3"
            },
            {
                "type": "Numeric",
                "name": "RESULT_4"
            },
            {
                "type": "Numeric",
                "name": "RESULT_5"
            },
            {
                "type": "Numeric",
                "name": "RESULT_6"
            },
            {
                "type": "Numeric",
                "name": "RESULT_7"
            },
            {
                "type": "Numeric",
                "name": "RESULT_8"
            },
            {
                "type": "String",
                "length": 255,
                "name": "VAR_RESULT"
            }
        ]
    },
    "cms_zos_prodoptions": {
        "name": "CMS_ZOS_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "UseZOSSystemCatalog"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "anajob": {
        "name": "AnaJob",
        "columns": [
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JobNam"
            },
            {
                "type": "Integer",
                "name": "JobTyp"
            },
            {
                "type": "Integer",
                "name": "JobVer"
            },
            {
                "type": "Integer",
                "name": "IdCnx"
            },
            {
                "type": "TIMESTAMP",
                "name": "JOBBEGINDATE"
            },
            {
                "type": "TIMESTAMP",
                "name": "JOBENDDATE"
            }
        ]
    },
    "amt_objectstatus": {
        "name": "AMT_OBJECTSTATUS",
        "columns": [
            {
                "type": "Integer",
                "name": "EXTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "STATUS"
            },
            {
                "type": "Integer",
                "name": "CHK"
            }
        ]
    },
    "appmarq_apphf": {
        "name": "AppMarq_AppHF",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "SnapshotId"
            },
            {
                "type": "Integer",
                "name": "BusinessCriterionId"
            },
            {
                "type": "Numeric",
                "name": "BusinessCriterionGrade"
            }
        ]
    },
    "appmarq_technicalcriteria": {
        "name": "AppMarq_TechnicalCriteria",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "type": "Integer",
                "name": "TechnicalCriterionId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "TechnicalCriterionName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "TechnicalCriterionDescription"
            }
        ]
    },
    "in_typcat": {
        "name": "IN_TYPCAT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDTYP"
            },
            {
                "type": "Integer",
                "name": "IDCATPARENT"
            },
            {
                "type": "Integer",
                "name": "ISCATPROP"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "cms_migr_targettype": {
        "name": "CMS_MIGR_TargetType",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Object_Type"
            }
        ]
    },
    "wk_dia_link": {
        "name": "WK_DIA_LINK",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            }
        ]
    },
    "dssapp_artifacts": {
        "name": "DSSAPP_ARTIFACTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "CODE_LINES"
            },
            {
                "type": "Integer",
                "name": "COMMENT_LINES"
            },
            {
                "type": "Integer",
                "name": "COUPLING"
            },
            {
                "type": "Integer",
                "name": "FAN_IN"
            },
            {
                "type": "Integer",
                "name": "FAN_OUT"
            },
            {
                "type": "Integer",
                "name": "CYCLOMATIC"
            },
            {
                "type": "Integer",
                "name": "PARAMETERS"
            },
            {
                "type": "Integer",
                "name": "NB_RECURSIVE"
            },
            {
                "type": "Numeric",
                "name": "CM_RATIO"
            },
            {
                "type": "Numeric",
                "name": "H_PGM_LENGTH"
            },
            {
                "type": "Numeric",
                "name": "H_PGM_VOCABULARY"
            },
            {
                "type": "Numeric",
                "name": "H_VOLUME"
            },
            {
                "type": "Integer",
                "name": "INTEGRATION"
            },
            {
                "type": "Integer",
                "name": "ESSENTIAL"
            },
            {
                "type": "Integer",
                "name": "LONG_LINES"
            },
            {
                "type": "Integer",
                "name": "CODE_DEPTH"
            },
            {
                "type": "Integer",
                "name": "COMMENTED_OUT_CL"
            }
        ]
    },
    "amt_parlink": {
        "name": "AMT_PARLINK",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "PROJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "SOURCE_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "TARGET_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "PROJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_PROJECT_ID"
            }
        ]
    },
    "dss_metric_scopes": {
        "name": "DSS_METRIC_SCOPES",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Numeric",
                "name": "METRIC_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "METRIC_CHAR_VALUE"
            },
            {
                "type": "Integer",
                "name": "METRIC_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "COMPUTE_VALUE"
            },
            {
                "type": "Integer",
                "name": "POSITION_ID"
            }
        ]
    },
    "cltpro": {
        "name": "CltPro",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "String",
                "length": 240,
                "name": "ProNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ProSrcPath"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ProPath"
            },
            {
                "type": "Integer",
                "name": "ProVerMaj"
            },
            {
                "type": "Integer",
                "name": "ProVerMin"
            },
            {
                "type": "String",
                "length": 38,
                "name": "ProGUID"
            },
            {
                "type": "Integer",
                "name": "ProClass"
            },
            {
                "type": "Integer",
                "name": "ProProp"
            }
        ]
    },
    "set_contents": {
        "name": "SET_Contents",
        "columns": [
            {
                "type": "Integer",
                "name": "SetId"
            },
            {
                "type": "Integer",
                "name": "ObjectId"
            }
        ]
    },
    "viewer_sections": {
        "name": "VIEWER_SECTIONS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PARENT_SECTION_ID"
            },
            {
                "type": "Integer",
                "name": "CHILD_OFFSET"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PARENT_FRAME_ID"
            }
        ]
    },
    "cms_pb_apptechno": {
        "name": "CMS_PB_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "csv_ana_appli": {
        "name": "CSV_ANA_APPLI",
        "columns": [
            {
                "type": "Integer",
                "name": "ANALYSIS_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ANALYSIS_NAME"
            }
        ]
    },
    "cms_am_externalconsomode": {
        "name": "CMS_AM_ExternalConsoMode",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            },
            {
                "type": "Integer",
                "name": "ExternalDataEntry"
            }
        ]
    },
    "dss_work_func_module_tree": {
        "name": "DSS_WORK_FUNC_MODULE_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "FLAT_LEVEL"
            }
        ]
    },
    "cms_cpp_rfdefinition": {
        "name": "CMS_CPP_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "cms_am_sizingconsomode": {
        "name": "CMS_AM_SizingConsoMode",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            },
            {
                "type": "Integer",
                "name": "SizingMeasure"
            }
        ]
    },
    "cms_portf_explicitfilter": {
        "name": "CMS_PORTF_ExplicitFilter",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            }
        ]
    },
    "dss_metric_folders": {
        "name": "DSS_METRIC_FOLDERS",
        "columns": [
            {
                "type": "Integer",
                "name": "FOLDER_ID"
            }
        ]
    },
    "dssapp_all_artifacts_simple": {
        "name": "DSSAPP_ALL_ARTIFACTS_SIMPLE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "enmodkey": {
        "name": "ENModKey",
        "columns": [
            {
                "type": "Integer",
                "name": "IdENMod"
            },
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "ArrangeOrder"
            }
        ]
    },
    "tmp_dia_javaallinherit": {
        "name": "TMP_DIA_JAVAALLINHERIT",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            }
        ]
    },
    "refpath": {
        "name": "RefPath",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFilRef"
            },
            {
                "type": "String",
                "length": 600,
                "name": "Path"
            }
        ]
    },
    "cms_j2ee_dataflow": {
        "name": "CMS_J2EE_Dataflow",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            }
        ]
    },
    "cms_bo_deftechno": {
        "name": "CMS_BO_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            }
        ]
    },
    "in_int_properties": {
        "name": "IN_INT_PROPERTIES",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_INT"
            }
        ]
    },
    "ci_int_properties": {
        "name": "CI_INT_PROPERTIES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "OBJECT_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "OBJECT_SHORTGUID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROP_NAME"
            },
            {
                "type": "Integer",
                "name": "VALUE"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "temp_ctt_object_applications": {
        "name": "TEMP_CTT_OBJECT_APPLICATIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_TYPE"
            },
            {
                "type": "Integer",
                "name": "PROPERTIES"
            }
        ]
    },
    "tmp_dia_objnam": {
        "name": "TMP_DIA_OBJNAM",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_NAME"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_syb_analysis": {
        "name": "CMS_SYB_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TableSize"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExtractionFileMigrated"
            }
        ]
    },
    "jobresdsc": {
        "name": "JobResDsc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdResDsc"
            },
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "BookMode"
            },
            {
                "type": "Integer",
                "name": "Info1"
            },
            {
                "type": "Integer",
                "name": "Info2"
            },
            {
                "type": "Integer",
                "name": "Info3"
            },
            {
                "type": "Integer",
                "name": "Info4"
            },
            {
                "type": "Integer",
                "name": "HdrRes"
            }
        ]
    },
    "dss_metric_exception_statuses": {
        "name": "DSS_METRIC_EXCEPTION_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "wk_dia_eventsgraph": {
        "name": "WK_DIA_EVENTSGRAPH",
        "columns": [
            {
                "type": "Integer",
                "name": "ORIGIN_EVENT_ID"
            },
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            },
            {
                "type": "Integer",
                "name": "CALL_LEVEL"
            },
            {
                "type": "String",
                "length": 1,
                "name": "IS_CALLEE_EVENT"
            }
        ]
    },
    "cms_code_repo_sybaseextract": {
        "name": "CMS_CODE_REPO_SybaseExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "work_object_children": {
        "name": "WORK_OBJECT_CHILDREN",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSIONID"
            },
            {
                "type": "Integer",
                "name": "RELATIONSHIPLEVEL"
            },
            {
                "type": "Integer",
                "name": "IDPARENTKEY"
            },
            {
                "type": "Integer",
                "name": "IDKEY"
            }
        ]
    },
    "cms_inf_sqlsrv_analyticdb": {
        "name": "CMS_INF_SQLSRV_AnalyticDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            },
            {
                "type": "Integer",
                "name": "Credential_ID"
            },
            {
                "type": "Integer",
                "name": "Server_ID"
            },
            {
                "type": "Integer",
                "name": "Service_Unique_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Status"
            }
        ]
    },
    "cms_am_qual_exclusion": {
        "name": "CMS_AM_QUAL_Exclusion",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Context"
            },
            {
                "type": "Integer",
                "name": "Portfolio"
            },
            {
                "type": "Integer",
                "name": "Metric"
            }
        ]
    },
    "cms_forms_analysis": {
        "name": "CMS_FORMS_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TableSize"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExtractionFileMigrated"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "CodeViewerFilesDir"
            }
        ]
    },
    "difftempotab": {
        "name": "DiffTempoTab",
        "columns": [
            {
                "type": "Integer",
                "name": "CnxId"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjFulNam"
            },
            {
                "type": "Integer",
                "name": "ObjTyp"
            },
            {
                "type": "Integer",
                "name": "IdParent"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ParentFulNam"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ProNam"
            },
            {
                "type": "Integer",
                "name": "Crc"
            }
        ]
    },
    "wk_dia_pbinherit": {
        "name": "WK_DIA_PBINHERIT",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_am_models": {
        "name": "CMS_AM_Models",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "ConsolidationMode"
            }
        ]
    },
    "dss_metric_histo_delta": {
        "name": "DSS_METRIC_HISTO_DELTA",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "IS_TREE_CHANGED"
            },
            {
                "type": "Integer",
                "name": "IS_PARAM_CHANGED"
            },
            {
                "type": "Integer",
                "name": "IS_THRESHOLD_CHANGED"
            }
        ]
    },
    "pboext": {
        "name": "PboExt",
        "columns": [
            {
                "type": "Integer",
                "name": "IdExt",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExtNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Mangling"
            },
            {
                "type": "Integer",
                "name": "ExtClass"
            },
            {
                "type": "Integer",
                "name": "ExtProp"
            }
        ]
    },
    "cms_am_parm_integers": {
        "name": "CMS_AM_PARM_Integers",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "IntergerValue"
            }
        ]
    },
    "wk_defana": {
        "name": "WK_DEFANA",
        "columns": [
            {
                "type": "Integer",
                "name": "ID"
            },
            {
                "type": "Integer",
                "name": "ENTITY_ID"
            },
            {
                "type": "Integer",
                "name": "DEPTH"
            }
        ]
    },
    "dia_struts_actionfield": {
        "name": "DIA_STRUTS_ACTIONFIELD",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "IS_INHERITED"
            },
            {
                "type": "Integer",
                "name": "FIELD_ID"
            }
        ]
    },
    "cms_am_parm_txtoverrides": {
        "name": "CMS_AM_PARM_TxtOverrides",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "ContextParam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TextValue"
            }
        ]
    },
    "cms_pb_rfdefinition": {
        "name": "CMS_PB_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "cms_am_desc_translations": {
        "name": "CMS_AM_DESC_Translations",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 3000,
                "name": "Text"
            }
        ]
    },
    "cms_am_qual_distcategories": {
        "name": "CMS_AM_QUAL_DistCategories",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Position"
            },
            {
                "type": "Integer",
                "name": "TranslationItem"
            },
            {
                "type": "Integer",
                "name": "PatternDescItem"
            },
            {
                "type": "Numeric",
                "name": "Threshold4"
            },
            {
                "type": "Numeric",
                "name": "Threshold3"
            },
            {
                "type": "Numeric",
                "name": "Threshold2"
            },
            {
                "type": "Numeric",
                "name": "Threshold1"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SQLProcedure"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "Distribution"
            }
        ]
    },
    "dssapp_tran_calls": {
        "name": "DSSAPP_TRAN_CALLS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "CALL_LEVEL"
            }
        ]
    },
    "ci_errors": {
        "name": "CI_ERRORS",
        "columns": [
            {
                "type": "Integer",
                "name": "ERROR_ID"
            },
            {
                "type": "Integer",
                "name": "CATEGORY"
            },
            {
                "type": "String",
                "length": 500,
                "name": "MESSAGE"
            }
        ]
    },
    "cms_migr_analysis": {
        "name": "CMS_MIGR_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "String",
                "length": 1050,
                "name": "Mail"
            },
            {
                "type": "Integer",
                "name": "LocalDB_Unique_ID"
            },
            {
                "type": "Integer",
                "name": "JobType"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectDesc"
            }
        ]
    },
    "dss_code_groups": {
        "name": "DSS_CODE_GROUPS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "GROUP_ID"
            },
            {
                "type": "Integer",
                "name": "LOCAL_SITE_ID"
            },
            {
                "type": "Integer",
                "name": "SECONDARY_OBJECT_ID"
            }
        ]
    },
    "ctt_object_parents": {
        "name": "CTT_OBJECT_PARENTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "PARENT_TYPE"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_TYPE"
            }
        ]
    },
    "apm_thresholds": {
        "name": "APM_THRESHOLDS",
        "columns": [
            {
                "type": "Integer",
                "name": "THRESHOLD_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "MIN_VALUE"
            },
            {
                "type": "Integer",
                "name": "MAX_VALUE"
            }
        ]
    },
    "histo_typprop": {
        "name": "HISTO_TYPPROP",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDTYP"
            },
            {
                "type": "Integer",
                "name": "IDPROP"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "dssapp_method_m_links": {
        "name": "DSSAPP_METHOD_M_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "IdParentClr"
            },
            {
                "type": "Integer",
                "name": "IdParentCle"
            },
            {
                "type": "Integer",
                "name": "IdClr"
            },
            {
                "type": "Integer",
                "name": "IdCle"
            }
        ]
    },
    "apm_inh_worktable": {
        "name": "APM_INH_WORKTABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NODE"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "INH_LEVEL"
            }
        ]
    },
    "cms_dep_discover": {
        "name": "CMS_DEP_Discover",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Source"
            },
            {
                "type": "Integer",
                "name": "Target"
            }
        ]
    },
    "dss_positions": {
        "name": "DSS_Positions",
        "columns": [
            {
                "type": "Integer",
                "name": "MetricPositionId"
            },
            {
                "type": "Integer",
                "name": "ObjectId"
            },
            {
                "type": "Integer",
                "name": "PropertyId"
            },
            {
                "type": "Integer",
                "name": "SourceId"
            },
            {
                "type": "Integer",
                "name": "PositionId"
            },
            {
                "type": "Integer",
                "name": "PositionIndex"
            },
            {
                "type": "Integer",
                "name": "LineStart"
            },
            {
                "type": "Integer",
                "name": "ColStart"
            },
            {
                "type": "Integer",
                "name": "LineEnd"
            },
            {
                "type": "Integer",
                "name": "ColEnd"
            }
        ]
    },
    "amt_del_object": {
        "name": "AMT_DEL_OBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "INTERNAL_ID"
            }
        ]
    },
    "amt_sum": {
        "name": "AMT_SUM",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_INT"
            },
            {
                "type": "Integer",
                "name": "INFTYPATT"
            },
            {
                "type": "Integer",
                "name": "INFSUBTYPATT"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            }
        ]
    },
    "fp_wk_lkp_tab": {
        "name": "FP_WK_Lkp_Tab",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "Num_Reserved_Col"
            },
            {
                "type": "Integer",
                "name": "Num_Char_Col"
            },
            {
                "type": "Integer",
                "name": "Num_Int_Col"
            },
            {
                "type": "Integer",
                "name": "Num_Other_Col"
            },
            {
                "type": "Integer",
                "name": "Tab_Type"
            }
        ]
    },
    "dssext_art_cost_statuses": {
        "name": "DSSEXT_ART_COST_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Numeric",
                "name": "RESULT_COST"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_SNAPSHOT_ID"
            }
        ]
    },
    "appmarq_metrics": {
        "name": "AppMarq_Metrics",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "type": "Integer",
                "name": "MetricId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "MetricName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "MetricDescription"
            }
        ]
    },
    "appmarq_apptechidx": {
        "name": "AppMarq_AppTechIdx",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "SnapshotId"
            },
            {
                "type": "Integer",
                "name": "TechnicalCriterionId"
            },
            {
                "type": "Numeric",
                "name": "TechnicalCriterionGrade"
            }
        ]
    },
    "cms_ui_project": {
        "name": "CMS_UI_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            }
        ]
    },
    "cms_j2ee_ldaptargetdfm": {
        "name": "CMS_J2EE_LDAPTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "viewer_precalc": {
        "name": "VIEWER_PRECALC",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PRECALC_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Numeric",
                "name": "KPI"
            },
            {
                "type": "Numeric",
                "name": "KPI_1"
            },
            {
                "type": "Numeric",
                "name": "KPI_2"
            },
            {
                "type": "Numeric",
                "name": "KPI_3"
            },
            {
                "type": "Numeric",
                "name": "KPI_4"
            },
            {
                "type": "Numeric",
                "name": "KPI_5"
            }
        ]
    },
    "cms_j2ee_rfdefinition": {
        "name": "CMS_J2EE_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "cms_j2ee_prodoptions": {
        "name": "CMS_J2EE_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "CallLightImport"
            },
            {
                "type": "Integer",
                "name": "IncludeLightImport"
            },
            {
                "type": "Integer",
                "name": "MaxComplixity"
            },
            {
                "type": "Integer",
                "name": "ExtractXMLFromJar"
            },
            {
                "type": "Integer",
                "name": "UseInferenceEngine"
            },
            {
                "type": "Integer",
                "name": "LimitString"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget"
            },
            {
                "type": "Integer",
                "name": "LimitLocalSubTarget"
            },
            {
                "type": "Integer",
                "name": "LimitSubTargetDF"
            },
            {
                "type": "Integer",
                "name": "MaxCodeSize"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "cms_udb_prodoptions": {
        "name": "CMS_UDB_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "objset": {
        "name": "OBJSET",
        "columns": [
            {
                "type": "Integer",
                "name": "IDSET"
            },
            {
                "type": "Integer",
                "name": "IDOBJ"
            }
        ]
    },
    "cms_common_apptechno": {
        "name": "CMS_Common_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "sys_migration_history": {
        "name": "SYS_MIGRATION_HISTORY",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "FINAL_VERSION"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "INFO_MESSAGE"
            }
        ]
    },
    "dssapp_ifpug_det": {
        "name": "DSSAPP_IFPUG_DET",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_MAIN_OBJECT"
            },
            {
                "type": "Integer",
                "name": "DET_VALUE"
            },
            {
                "type": "Integer",
                "name": "RET_VALUE"
            },
            {
                "type": "Integer",
                "name": "ILF_VALUE"
            }
        ]
    },
    "dssapp_sources": {
        "name": "DSSAPP_SOURCES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "CODE_LINES"
            },
            {
                "type": "Integer",
                "name": "COMMENT_LINES"
            },
            {
                "type": "Numeric",
                "name": "BFP_RATIO"
            }
        ]
    },
    "in_positions": {
        "name": "IN_POSITIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_SOURCE_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_SOURCE_KIND"
            },
            {
                "type": "Integer",
                "name": "SEQ_NUM"
            },
            {
                "type": "Integer",
                "name": "POSITION_MODE"
            },
            {
                "type": "Integer",
                "name": "POSITION1"
            },
            {
                "type": "Integer",
                "name": "POSITION2"
            },
            {
                "type": "Integer",
                "name": "POSITION3"
            },
            {
                "type": "Integer",
                "name": "POSITION4"
            },
            {
                "type": "Integer",
                "name": "GROUP_NUM"
            }
        ]
    },
    "impjob": {
        "name": "ImpJob",
        "columns": [
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "IdImp"
            },
            {
                "type": "String",
                "length": 30,
                "name": "JobNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JobLib"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "ImpTyp"
            }
        ]
    },
    "cat": {
        "name": "Cat",
        "columns": [
            {
                "type": "Integer",
                "name": "IdCat"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CatNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CatDsc"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "in_prop": {
        "name": "IN_PROP",
        "columns": [
            {
                "type": "Integer",
                "name": "IDPROP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPNAM"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPDSC"
            },
            {
                "type": "Integer",
                "name": "PROPTYP"
            },
            {
                "type": "String",
                "length": 3,
                "name": "PROPMRG"
            },
            {
                "type": "Integer",
                "name": "CARDMIN"
            },
            {
                "type": "Integer",
                "name": "CARDMAX"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "wk_dia_singltfld": {
        "name": "WK_DIA_SINGLTFLD",
        "columns": [
            {
                "type": "Integer",
                "name": "ID_CLASS"
            },
            {
                "type": "Integer",
                "name": "ID_FIELD"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_sqlsrv_analysis": {
        "name": "CMS_SQLSRV_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TableSize"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExtractionFileMigrated"
            }
        ]
    },
    "objdat": {
        "name": "OBJDAT",
        "columns": [
            {
                "type": "Integer",
                "name": "IDOBJ"
            },
            {
                "type": "Integer",
                "name": "IDPROP"
            },
            {
                "type": "TIMESTAMP",
                "name": "DTINFO"
            }
        ]
    },
    "keypar": {
        "name": "KeyPar",
        "columns": [
            {
                "type": "Integer",
                "name": "IdKeyPar",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "IdParent"
            },
            {
                "type": "Integer",
                "name": "ParTyp"
            }
        ]
    },
    "wk_dia_servletfld": {
        "name": "WK_DIA_SERVLETFLD",
        "columns": [
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "FIELD_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "dbl": {
        "name": "Dbl",
        "columns": [
            {
                "type": "Integer",
                "name": "IdDbl"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 128,
                "name": "DblNam"
            },
            {
                "type": "Integer",
                "name": "DblClass"
            },
            {
                "type": "Integer",
                "name": "DblProp"
            },
            {
                "type": "String",
                "length": 30,
                "name": "DblUser"
            },
            {
                "type": "String",
                "length": 2000,
                "name": "DblHost"
            },
            {
                "type": "Integer",
                "name": "IdSrv"
            }
        ]
    },
    "cms_cpp_analysis": {
        "name": "CMS_CPP_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cpp_Compilation"
            },
            {
                "type": "Integer",
                "name": "Managed_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "C_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cpp_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DevEnv_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Stl_Usage"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ForceInclude"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PrecompiledHeader"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PchGenerator"
            },
            {
                "type": "Integer",
                "name": "DisableUseofPch"
            },
            {
                "type": "Integer",
                "name": "MagicRgtShift"
            },
            {
                "type": "Integer",
                "name": "Trigraph"
            },
            {
                "type": "Integer",
                "name": "StdScope"
            },
            {
                "type": "Integer",
                "name": "IsoTypename"
            },
            {
                "type": "Integer",
                "name": "UnknownDirective"
            }
        ]
    },
    "cms_objectlinks": {
        "name": "CMS_ObjectLinks",
        "columns": [
            {
                "type": "Integer",
                "name": "Caller_ID"
            },
            {
                "type": "Integer",
                "name": "Callee_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Symbol"
            },
            {
                "type": "Integer",
                "name": "Position"
            }
        ]
    },
    "cms_j2ee_sqltargetdfm": {
        "name": "CMS_J2EE_SQLTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "dss_in_links": {
        "name": "DSS_IN_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NEXT_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            }
        ]
    },
    "wk_dia_privfld": {
        "name": "WK_DIA_PRIVFLD",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_NAME"
            },
            {
                "type": "Integer",
                "name": "IS_BOOLEAN"
            },
            {
                "type": "Integer",
                "name": "NB_GET_ACCESSOR"
            },
            {
                "type": "Integer",
                "name": "NB_SET_ACCESSOR"
            }
        ]
    },
    "modimg": {
        "name": "ModImg",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            },
            {
                "type": "Integer",
                "name": "NumPos"
            },
            {
                "name": "ModImg"
            },
            {
                "type": "Integer",
                "name": "ImgNumOrd"
            },
            {
                "type": "Integer",
                "name": "ImgSiz"
            }
        ]
    },
    "cms_asp_anaoptions": {
        "name": "CMS_ASP_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Server_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Client_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefServerScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            }
        ]
    },
    "adg_tech_module_parents": {
        "name": "ADG_TECH_MODULE_PARENTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "diag_object_parents_simple": {
        "name": "DIAG_OBJECT_PARENTS_SIMPLE",
        "columns": [
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "wk_dia_serialfld": {
        "name": "WK_DIA_SERIALFLD",
        "columns": [
            {
                "type": "Integer",
                "name": "FIELD_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "FIELD_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            }
        ]
    },
    "cms_zos_project": {
        "name": "CMS_ZOS_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            }
        ]
    },
    "in_escalatedlink": {
        "name": "IN_EscalatedLink",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "Integer",
                "name": "BaseLinkId"
            },
            {
                "type": "Integer",
                "name": "CallerId"
            },
            {
                "type": "Integer",
                "name": "CalleeId"
            },
            {
                "type": "Integer",
                "name": "Distance"
            }
        ]
    },
    "amt_refcrcobject": {
        "name": "AMT_REFCRCOBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "EXTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "EXTERNAL_REF_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_REF_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "STATUS"
            }
        ]
    },
    "tmp_dia_cob_statm2": {
        "name": "TMP_DIA_COB_STATM2",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            }
        ]
    },
    "wk_dia_cppinherit": {
        "name": "WK_DIA_CPPINHERIT",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "dssext_obj_cpt_statuses": {
        "name": "DSSEXT_OBJ_CPT_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Integer",
                "name": "IS_ART"
            },
            {
                "type": "Numeric",
                "name": "RESULT_COUNT"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_SNAPSHOT_ID"
            }
        ]
    },
    "cms_rf_simpleregexp": {
        "name": "CMS_RF_SimpleRegExp",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "RF_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Expression"
            }
        ]
    },
    "viewer_functions": {
        "name": "VIEWER_FUNCTIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "ID",
                "primary": True
            },
            {
                "length": 255,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 255,
                "type": "String",
                "name": "DESCRIPTION"
            }
        ]
    },
    "in_analysislinkerunit": {
        "name": "IN_AnalysisLinkerUnit",
        "columns": [
            {
                "type": "Integer",
                "name": "UserProjectId"
            },
            {
                "type": "Integer",
                "name": "SourceAnalysisId"
            },
            {
                "type": "Integer",
                "name": "TargetAnalysisId"
            }
        ]
    },
    "fusacc": {
        "name": "FusAcc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFus"
            },
            {
                "type": "Integer",
                "name": "IdAcc"
            }
        ]
    },
    "dss_translation_table": {
        "name": "DSS_TRANSLATION_TABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "SITE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "dbg_savingdataconfig": {
        "name": "DBG_SavingDataConfig",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "TreatmentName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SourceTableName"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Activation"
            },
            {
                "type": "Integer",
                "name": "LastExecutionNumber"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ProcName"
            }
        ]
    },
    "cms_am_parm_technofilters": {
        "name": "CMS_AM_PARM_TechnoFilters",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "OverrideValue"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CategoryDesc"
            },
            {
                "type": "Integer",
                "name": "AmtCategory"
            }
        ]
    },
    "wk_dia_prstsetter": {
        "name": "WK_DIA_PRSTSETTER",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "appmarq_sourcingtypemodel": {
        "name": "AppMarq_SourcingTypeModel",
        "columns": [
            {
                "type": "Integer",
                "name": "SourcingTypeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "SourcingTypeName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "SourcingTypeDescription"
            }
        ]
    },
    "amt_del_linksymb": {
        "name": "AMT_DEL_LINKSYMB",
        "columns": [
            {
                "type": "Integer",
                "name": "EXTERNAL_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_ID"
            }
        ]
    },
    "cms_bo_analysis": {
        "name": "CMS_BO_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TableSize"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExtractionFileMigrated"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            }
        ]
    },
    "cms_bo_rfdefinition": {
        "name": "CMS_BO_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "dss_selection": {
        "name": "DSS_SELECTION",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "COMPUTE_NOW"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_bo_anaoptions": {
        "name": "CMS_BO_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "dssext_defect_counts": {
        "name": "DSSEXT_DEFECT_COUNTS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "DEF_COUNT"
            }
        ]
    },
    "objects": {
        "name": "Objects",
        "columns": [
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "IdNam"
            },
            {
                "type": "String",
                "length": 600,
                "name": "IdShortNam"
            },
            {
                "type": "Integer",
                "name": "ObjTyp"
            }
        ]
    },
    "in_objects_chk": {
        "name": "IN_OBJECTS_CHK",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "NAME_ID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "SHORT_NAME_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DESCRIPTION"
            }
        ]
    },
    "pbowsp": {
        "name": "PboWsp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdWsp",
                "primary": True
            },
            {
                "type": "String",
                "length": 255,
                "name": "WspNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "WspPath"
            },
            {
                "type": "Integer",
                "name": "WspClass"
            },
            {
                "type": "Integer",
                "name": "WspProp"
            }
        ]
    },
    "viewer_action_plans_log": {
        "name": "VIEWER_ACTION_PLANS_LOG",
        "columns": [
            {
                "type": "TIMESTAMP",
                "name": "LAST_DATE"
            }
        ]
    },
    "cms_am_extern_data": {
        "name": "CMS_AM_EXTERN_Data",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "NameTranslationItem"
            },
            {
                "type": "Integer",
                "name": "DescriptionEntry"
            },
            {
                "type": "Integer",
                "name": "ExternalID"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            }
        ]
    },
    "cms_asp_rfdefinition": {
        "name": "CMS_ASP_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "cms_sqlsrv_deftechno": {
        "name": "CMS_SQLSRV_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "dssapp_cls_worktable": {
        "name": "DSSAPP_CLS_WORKTABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "PARENT_TYPE"
            }
        ]
    },
    "adg_system_tree": {
        "name": "ADG_SYSTEM_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_GROUP"
            },
            {
                "type": "Integer",
                "name": "TREE_LEVEL"
            },
            {
                "type": "Integer",
                "name": "IS_FUNC_MODULE"
            },
            {
                "type": "Numeric",
                "name": "AGGREGATE_WEIGHT"
            }
        ]
    },
    "appmarq_applicationagemodel": {
        "name": "AppMarq_ApplicationAgeModel",
        "columns": [
            {
                "type": "Integer",
                "name": "ApplicationAgeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "ApplicationAgeName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "ApplicationAgeDescription"
            }
        ]
    },
    "tmp_objidinterval": {
        "name": "TMP_OBJIDINTERVAL",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID_MIN"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID_MAX"
            },
            {
                "type": "Integer",
                "name": "BLOCK"
            }
        ]
    },
    "efp_art_cost_statuses_app": {
        "name": "EFP_ART_COST_STATUSES_APP",
        "columns": [
            {
                "length": 30,
                "type": "String",
                "name": "DATE_END"
            },
            {
                "length": 30,
                "type": "String",
                "name": "DATE_START"
            },
            {
                "type": "Integer",
                "name": "APP_ID"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Numeric",
                "name": "RESULT_EFFORT"
            },
            {
                "type": "Numeric",
                "name": "RESULT_COST"
            }
        ]
    },
    "cms_portf_system": {
        "name": "CMS_PORTF_System",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Central_ID"
            }
        ]
    },
    "tmp_dia_object01": {
        "name": "TMP_DIA_OBJECT01",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "appmarq_cmmilevelmodel": {
        "name": "AppMarq_CMMILevelModel",
        "columns": [
            {
                "type": "Integer",
                "name": "CMMILevelId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "CMMILevelName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "CMMILevelDescription"
            }
        ]
    },
    "dss_link_info3": {
        "name": "DSS_LINK_INFO3",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NEXT_OBJECT_ID"
            }
        ]
    },
    "dss_code_sources": {
        "name": "DSS_CODE_SOURCES",
        "columns": [
            {
                "type": "String",
                "length": 600,
                "name": "SOURCE_PATH"
            },
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SOURCE_ERROR"
            },
            {
                "type": "Text",
                "name": "SOURCE_CODE"
            },
            {
                "type": "Integer",
                "name": "SOURCE_CRC"
            }
        ]
    },
    "cms_udb_apptechno": {
        "name": "CMS_UDB_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "cms_tool_sqlbefore": {
        "name": "CMS_TOOL_SqlBefore",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "VarContainer_ID"
            }
        ]
    },
    "cms_j2ee_archivefile": {
        "name": "CMS_J2EE_ArchiveFile",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ClassPath"
            }
        ]
    },
    "cms_systemcollections": {
        "name": "CMS_SystemCollections",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Field_GUID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Field_Value"
            },
            {
                "type": "Integer",
                "name": "Position"
            }
        ]
    },
    "fp_wk_subset_objects": {
        "name": "FP_WK_Subset_Objects",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "SUBSET_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "mod": {
        "name": "Mod",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod",
                "primary": True
            },
            {
                "type": "String",
                "length": 255,
                "name": "ModNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ModLib"
            },
            {
                "type": "Integer",
                "name": "ModTyp"
            },
            {
                "type": "Integer",
                "name": "IdFld"
            },
            {
                "type": "String",
                "length": 600,
                "name": "Path"
            },
            {
                "type": "String",
                "length": 3,
                "name": "IdUsr"
            }
        ]
    },
    "dssapp_worktable_cur": {
        "name": "DSSAPP_WORKTABLE_CUR",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NODE"
            },
            {
                "type": "Numeric",
                "name": "RESULT"
            },
            {
                "type": "Numeric",
                "name": "RESULT_2"
            },
            {
                "type": "Numeric",
                "name": "RESULT_3"
            },
            {
                "type": "Numeric",
                "name": "RESULT_4"
            },
            {
                "type": "Numeric",
                "name": "RESULT_5"
            },
            {
                "type": "Numeric",
                "name": "RESULT_6"
            },
            {
                "type": "Numeric",
                "name": "RESULT_7"
            },
            {
                "type": "Numeric",
                "name": "RESULT_8"
            },
            {
                "type": "String",
                "length": 255,
                "name": "VAR_RESULT"
            }
        ]
    },
    "cwref": {
        "name": "CWRef",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRef",
                "primary": True
            },
            {
                "type": "String",
                "length": 128,
                "name": "RefNam"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "Integer",
                "name": "RefTyp"
            },
            {
                "type": "Integer",
                "name": "RefMod"
            },
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "tmp_dia_inc_curr1": {
        "name": "TMP_DIA_INC_CURR1",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            }
        ]
    },
    "adg_diag_severity": {
        "name": "ADG_DIAG_SEVERITY",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "SEVERITY"
            }
        ]
    },
    "cms_net_dataflow": {
        "name": "CMS_NET_Dataflow",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            }
        ]
    },
    "pmc_archi_model_modules": {
        "name": "PMC_ARCHI_MODEL_MODULES",
        "columns": [
            {
                "type": "Integer",
                "name": "MODEL_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "cms_syb_apptechno": {
        "name": "CMS_SYB_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "cms_text_replacement": {
        "name": "CMS_Text_Replacement",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Expression"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Replacement"
            }
        ]
    },
    "pmc_archi_forbid_links": {
        "name": "PMC_ARCHI_FORBID_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            }
        ]
    },
    "dss_object_ranking": {
        "name": "DSS_OBJECT_RANKING",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "HIT_COUNT"
            },
            {
                "type": "Integer",
                "name": "FAN_IN"
            },
            {
                "type": "Integer",
                "name": "TRAN_PROPER"
            },
            {
                "type": "Integer",
                "name": "TRAN_CUMUL"
            },
            {
                "type": "Integer",
                "name": "CHAN_PROPER"
            },
            {
                "type": "Integer",
                "name": "CHAN_CUMUL"
            },
            {
                "type": "Integer",
                "name": "ROBU_PROPER"
            },
            {
                "type": "Integer",
                "name": "ROBU_CUMUL"
            },
            {
                "type": "Integer",
                "name": "PERF_PROPER"
            },
            {
                "type": "Integer",
                "name": "PERF_CUMUL"
            },
            {
                "type": "Integer",
                "name": "SECU_PROPER"
            },
            {
                "type": "Integer",
                "name": "SECU_CUMUL"
            }
        ]
    },
    "cms_inf_ora_accesssid": {
        "name": "CMS_INF_ORA_AccessSid",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Service"
            }
        ]
    },
    "viewer_session_id": {
        "name": "VIEWER_SESSION_ID",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID",
                "primary": True
            },
            {
                "length": 255,
                "type": "String",
                "name": "NAME_ID"
            }
        ]
    },
    "cms_net_prodoptions": {
        "name": "CMS_NET_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "DynamicAnalysisOptions"
            },
            {
                "type": "Integer",
                "name": "AllowExtensions"
            },
            {
                "type": "Integer",
                "name": "CallLightImport"
            },
            {
                "type": "Integer",
                "name": "IncludeLightImport"
            },
            {
                "type": "Integer",
                "name": "MaxComplexity"
            }
        ]
    },
    "cms_net_xpathtargetdfm": {
        "name": "CMS_NET_XPathTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "anaattr": {
        "name": "ANAATTR",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ATTRNAM"
            },
            {
                "type": "Integer",
                "name": "INTVAL"
            }
        ]
    },
    "wk_dia_prstartifact": {
        "name": "WK_DIA_PRSTARTIFACT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "propattr": {
        "name": "PropAttr",
        "columns": [
            {
                "type": "Integer",
                "name": "IdProp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AttrNam"
            },
            {
                "type": "Integer",
                "name": "AttrTyp"
            },
            {
                "type": "Integer",
                "name": "IntVal"
            },
            {
                "type": "String",
                "length": 255,
                "name": "StrVal"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "adgv_cost_statuses": {
        "name": "ADGV_COST_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TECHNO_ID"
            },
            {
                "type": "Integer",
                "name": "CPLX_TYPE"
            },
            {
                "type": "Integer",
                "name": "CHANGE_TYPE"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "wk_dia_chainsynonym": {
        "name": "WK_DIA_CHAINSYNONYM",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DESCRIPTION"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "defana_entityattr": {
        "name": "DEFANA_ENTITYATTR",
        "columns": [
            {
                "type": "Integer",
                "name": "ENTITY_ID"
            },
            {
                "type": "Integer",
                "name": "ATTR_OWNER_ID"
            },
            {
                "type": "Integer",
                "name": "ATTR_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "ATTR_VALUE_INDEX"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "ATTR_VALUE_STRING"
            },
            {
                "type": "Integer",
                "name": "ATTR_VALUE_REF"
            }
        ]
    },
    "in_typattr": {
        "name": "IN_TYPATTR",
        "columns": [
            {
                "type": "Integer",
                "name": "IDTYP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ATTRNAM"
            },
            {
                "type": "Integer",
                "name": "ATTRTYP"
            },
            {
                "type": "Integer",
                "name": "INTVAL"
            },
            {
                "type": "String",
                "length": 255,
                "name": "STRVAL"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "dss_tree_ranking2": {
        "name": "DSS_TREE_RANKING2",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "BUSINESS_CRITERION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TREE_LEVEL"
            },
            {
                "type": "Integer",
                "name": "TREE_LEFT_POSITION"
            },
            {
                "type": "Integer",
                "name": "TREE_RIGHT_POSITION"
            },
            {
                "type": "Integer",
                "name": "ALL_VIOLATED_RULES_NB"
            },
            {
                "type": "Integer",
                "name": "ALL_VIOLATING_OBJECTS_NB"
            },
            {
                "type": "Integer",
                "name": "ALL_VIOLATIONS_NB"
            }
        ]
    },
    "set_definitions": {
        "name": "SET_Definitions",
        "columns": [
            {
                "type": "Integer",
                "name": "SetId"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SetName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SetType"
            },
            {
                "type": "String",
                "length": 30,
                "name": "SetProcedure"
            }
        ]
    },
    "viewer_report_sections": {
        "name": "VIEWER_REPORT_SECTIONS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REPORT_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "SECTION_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "SECTION_NAME"
            },
            {
                "type": "Integer",
                "name": "SECTION_OFFSET"
            },
            {
                "type": "Integer",
                "name": "PAGE_BREAK"
            }
        ]
    },
    "cms_ui_toolmodfil": {
        "name": "CMS_UI_ToolModFil",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            }
        ]
    },
    "dssapp_inh_worktable": {
        "name": "DSSAPP_INH_WORKTABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NODE"
            },
            {
                "type": "Integer",
                "name": "INH_LEVEL"
            }
        ]
    },
    "cms_gen_envprof": {
        "name": "CMS_GEN_EnvProf",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Guid"
            }
        ]
    },
    "cms_am_qual_tc_selection": {
        "name": "CMS_AM_QUAL_TC_Selection",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Selection"
            }
        ]
    },
    "frmgenobj": {
        "name": "FrmGenObj",
        "columns": [
            {
                "type": "Integer",
                "name": "IDGENOBJ"
            },
            {
                "type": "String",
                "length": 255,
                "name": "GENOBJNAM"
            },
            {
                "type": "Integer",
                "name": "GENOBJCLASS"
            },
            {
                "type": "Integer",
                "name": "GENOBJPROP"
            },
            {
                "type": "Integer",
                "name": "IDPARENT"
            }
        ]
    },
    "appmarq_technicalversions": {
        "name": "AppMarq_TechnicalVersions",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "length": 30,
                "type": "String",
                "name": "TechnicalVersion"
            }
        ]
    },
    "prt": {
        "name": "Prt",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPrt"
            },
            {
                "type": "Integer",
                "name": "IdClt"
            },
            {
                "type": "Integer",
                "name": "IdApp"
            },
            {
                "type": "Integer",
                "name": "IdCod"
            },
            {
                "type": "Integer",
                "name": "IdDat"
            },
            {
                "name": "PrtVal"
            },
            {
                "type": "Integer",
                "name": "IdChk"
            }
        ]
    },
    "dss_business_criteria": {
        "name": "DSS_BUSINESS_CRITERIA",
        "columns": [
            {
                "type": "Integer",
                "name": "DIAG_ID"
            },
            {
                "type": "Integer",
                "name": "BUSINESS_CRITERION_ID"
            }
        ]
    },
    "cms_inf_bodb": {
        "name": "CMS_INF_BODB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UserName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Password"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Host"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Authentication"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            }
        ]
    },
    "dss_log_links": {
        "name": "DSS_LOG_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NEXT_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "rep": {
        "name": "Rep",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRep"
            },
            {
                "type": "String",
                "length": 255,
                "name": "RepNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Path"
            },
            {
                "type": "Integer",
                "name": "RepClass"
            },
            {
                "type": "Integer",
                "name": "RepProp"
            }
        ]
    },
    "dbe": {
        "name": "Dbe",
        "columns": [
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 128,
                "name": "DbeNam"
            },
            {
                "type": "Integer",
                "name": "IdSrv"
            },
            {
                "type": "Integer",
                "name": "IdDbeAlias"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "keys": {
        "name": "Keys",
        "columns": [
            {
                "type": "Integer",
                "name": "IdKey",
                "primary": True
            },
            {
                "type": "String",
                "length": 255,
                "name": "KeyNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "KeyLib"
            },
            {
                "type": "String",
                "length": 6,
                "name": "KeyTyp"
            },
            {
                "type": "Integer",
                "name": "KeySubTyp"
            },
            {
                "type": "Integer",
                "name": "KeyClass"
            },
            {
                "type": "Integer",
                "name": "KeyProp"
            },
            {
                "type": "Integer",
                "name": "ObjTyp"
            },
            {
                "type": "String",
                "length": 3,
                "name": "IdUsrDevPro"
            },
            {
                "type": "TIMESTAMP",
                "name": "KeyDevDat"
            },
            {
                "type": "TIMESTAMP",
                "name": "KeyDevVldDat"
            },
            {
                "type": "Integer",
                "name": "Status"
            },
            {
                "type": "String",
                "length": 128,
                "name": "SqlOwner"
            }
        ]
    },
    "cms_am_parm_fltparams": {
        "name": "CMS_AM_PARM_FltParams",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "ParamIndex"
            },
            {
                "type": "Integer",
                "name": "Model_ID"
            },
            {
                "type": "Integer",
                "name": "DefValue"
            },
            {
                "type": "Numeric",
                "name": "DefaultFloatValue"
            }
        ]
    },
    "cms_tool_progbefore": {
        "name": "CMS_TOOL_ProgBefore",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "VarContainer_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProgName"
            },
            {
                "type": "Integer",
                "name": "ProgWait"
            }
        ]
    },
    "cms_code_cont_dbextract": {
        "name": "CMS_CODE_CONT_DBExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            }
        ]
    },
    "prodep": {
        "name": "ProDep",
        "columns": [
            {
                "type": "Integer",
                "name": "IdProMain"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "dssapp_sql_artifacts": {
        "name": "DSSAPP_SQL_ARTIFACTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "IS_SQL_OBJECT"
            },
            {
                "type": "Integer",
                "name": "IS_ARTIFACT"
            },
            {
                "type": "Integer",
                "name": "LARGE_JOINS"
            },
            {
                "type": "Integer",
                "name": "SUBQUERIES"
            },
            {
                "type": "Integer",
                "name": "GROUP_BY"
            },
            {
                "type": "Integer",
                "name": "UPDATES"
            },
            {
                "type": "Integer",
                "name": "RAW_COMPLEXITY"
            },
            {
                "type": "Integer",
                "name": "COMPLEX_SELECT"
            },
            {
                "type": "Integer",
                "name": "SELECT_ALL_COL"
            },
            {
                "type": "Integer",
                "name": "SQL_COMPLEXITY"
            }
        ]
    },
    "impjobcol": {
        "name": "ImpJobCol",
        "columns": [
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "IdCol"
            },
            {
                "type": "String",
                "length": 128,
                "name": "AddColNam"
            },
            {
                "type": "String",
                "length": 128,
                "name": "AddColTyp"
            },
            {
                "type": "Integer",
                "name": "AddColPty"
            }
        ]
    },
    "cms_syb_technology": {
        "name": "CMS_SYB_Technology",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "cms_am_qual_distributions": {
        "name": "CMS_AM_QUAL_Distributions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "TranslationItem"
            },
            {
                "type": "Integer",
                "name": "PatternDescItem"
            },
            {
                "type": "Integer",
                "name": "RationaleDescItem"
            },
            {
                "type": "Integer",
                "name": "OutputDescItem"
            },
            {
                "type": "Integer",
                "name": "ShortNameItem"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ScopeInitProcedure"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            }
        ]
    },
    "cms_j2ee_deftechno": {
        "name": "CMS_J2EE_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Java_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JSP_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Client_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "XML_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Java_Version"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JSP_Servlet_StdVer"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Hibernate_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Struts_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Spring_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Jsf_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CommonLogging_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Dom4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JUnit_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Log4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Mx4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cics_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Wbs_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Ejb_Usage"
            },
            {
                "type": "Integer",
                "name": "CallLightImport"
            },
            {
                "type": "Integer",
                "name": "IncludeLightImport"
            },
            {
                "type": "Integer",
                "name": "MaxComplexity"
            },
            {
                "type": "Integer",
                "name": "ExtractXMLFromJars"
            },
            {
                "type": "Integer",
                "name": "UseInferenceEngine"
            },
            {
                "type": "Integer",
                "name": "LimitString"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget"
            },
            {
                "type": "Integer",
                "name": "LimitLocalSubTarget"
            },
            {
                "type": "Integer",
                "name": "LimitSubTargetDF"
            },
            {
                "type": "Integer",
                "name": "MaxCodeSize"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "CastScriptPath"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CastTagsPath"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "DeployPath"
            }
        ]
    },
    "spr": {
        "name": "Spr",
        "columns": [
            {
                "type": "Integer",
                "name": "IdSpr",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 128,
                "name": "SprNam"
            },
            {
                "type": "Integer",
                "name": "SprClass"
            },
            {
                "type": "Integer",
                "name": "SprProp"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "moddsprul": {
        "name": "ModDspRul",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRul"
            },
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            }
        ]
    },
    "dss_central_selection": {
        "name": "DSS_CENTRAL_SELECTION",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "COMPUTE_NOW"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "adg_work_grade_avg": {
        "name": "ADG_WORK_GRADE_AVG",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Numeric",
                "name": "GRADE_AVG"
            }
        ]
    },
    "cms_vb_rfdefinition": {
        "name": "CMS_VB_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "fil": {
        "name": "Fil",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFil",
                "primary": True
            },
            {
                "type": "String",
                "length": 255,
                "name": "FilNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Path"
            },
            {
                "type": "Integer",
                "name": "FilClass"
            },
            {
                "type": "Integer",
                "name": "FilProp"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            }
        ]
    },
    "viewer_report_parameters": {
        "name": "VIEWER_REPORT_PARAMETERS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REPORT_SECTION_ID"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "VALUE"
            }
        ]
    },
    "cms_gen_string": {
        "name": "CMS_GEN_String",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            }
        ]
    },
    "cms_am_qual_rules": {
        "name": "CMS_AM_QUAL_Rules",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "TranslationItem"
            },
            {
                "type": "Integer",
                "name": "PatternDescItem"
            },
            {
                "type": "Integer",
                "name": "RationaleDescItem"
            },
            {
                "type": "Integer",
                "name": "ReferenceDescItem"
            },
            {
                "type": "Integer",
                "name": "RemediationDescItem"
            },
            {
                "type": "Integer",
                "name": "RemediationSampleDescItem"
            },
            {
                "type": "Integer",
                "name": "SampleDescItem"
            },
            {
                "type": "Integer",
                "name": "ScopeDescItem"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ValueType"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ValueMultiplicity"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AssociatedValueName"
            },
            {
                "type": "Integer",
                "name": "OutputDescItem"
            },
            {
                "type": "Integer",
                "name": "ShortNameItem"
            },
            {
                "type": "Numeric",
                "name": "Threshold4"
            },
            {
                "type": "Numeric",
                "name": "Threshold3"
            },
            {
                "type": "Numeric",
                "name": "Threshold2"
            },
            {
                "type": "Numeric",
                "name": "Threshold1"
            },
            {
                "type": "Integer",
                "name": "computingConfiguration"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Rationalized"
            },
            {
                "type": "String",
                "length": 255,
                "name": "XXL"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            }
        ]
    },
    "work_selectionkp_tree": {
        "name": "WORK_SELECTIONKP_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "SELECTION_ID"
            },
            {
                "type": "Integer",
                "name": "KEY_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_LEVEL"
            },
            {
                "type": "Integer",
                "name": "PROJECT_ID"
            },
            {
                "type": "Integer",
                "name": "IS_PARENT"
            }
        ]
    },
    "cms_tool_kbupdate": {
        "name": "CMS_TOOL_KbUpdate",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "VarContainer_ID"
            },
            {
                "type": "Integer",
                "name": "Mode_ID"
            }
        ]
    },
    "wk_dbelist_del": {
        "name": "WK_DBELIST_DEL",
        "columns": [
            {
                "type": "Integer",
                "name": "IDSESSION"
            },
            {
                "type": "Integer",
                "name": "IDUSRPRO"
            },
            {
                "type": "Integer",
                "name": "IDDBE"
            },
            {
                "type": "Integer",
                "name": "IDPRODYN"
            }
        ]
    },
    "dss_metric_side_process": {
        "name": "DSS_METRIC_SIDE_PROCESS",
        "columns": [
            {
                "type": "Integer",
                "name": "PROCESS_SIDE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROCESS_NAME"
            },
            {
                "type": "Integer",
                "name": "OPERATION_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OPERATION_PROCNAME"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "OPERATION_DESCRIPTION"
            }
        ]
    },
    "idxcol": {
        "name": "IdxCol",
        "columns": [
            {
                "type": "Integer",
                "name": "IdIdxCol"
            },
            {
                "type": "Integer",
                "name": "IdIdx"
            },
            {
                "type": "Integer",
                "name": "IdCol"
            },
            {
                "type": "Integer",
                "name": "ColNum"
            }
        ]
    },
    "cms_cobol_deftechno": {
        "name": "CMS_COBOL_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cobol_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JCL_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "IMS_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CICS_FileExtensions"
            },
            {
                "type": "Integer",
                "name": "IBM_Environment"
            },
            {
                "type": "Integer",
                "name": "Cobol_StartingColumn"
            },
            {
                "type": "Integer",
                "name": "Cobol_ReadTermFormat"
            },
            {
                "type": "Integer",
                "name": "Cobol_UseComponentName"
            },
            {
                "type": "Integer",
                "name": "Tab_Length"
            },
            {
                "type": "Integer",
                "name": "cobol_CodeBeyondRightCol"
            },
            {
                "type": "Integer",
                "name": "IMS_IndcatorArea"
            },
            {
                "type": "Integer",
                "name": "PROD_SaveSectAndParagraph"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROD_DataStructure"
            },
            {
                "type": "Integer",
                "name": "PROD_SaveCopyBookData"
            },
            {
                "type": "Integer",
                "name": "UseInferenceEngine"
            },
            {
                "type": "Integer",
                "name": "LimitString"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget2"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget3"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget4"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget5"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget6"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget7"
            },
            {
                "type": "Integer",
                "name": "LimitSubTarget8"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            },
            {
                "type": "Integer",
                "name": "JCL_WithCustomConfig"
            }
        ]
    },
    "wk_dia_openconnectmethod": {
        "name": "WK_DIA_OPENCONNECTMETHOD",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "efp_tran_exclusion": {
        "name": "EFP_Tran_Exclusion",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            }
        ]
    },
    "pbofnc": {
        "name": "PboFnc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFnc",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FncNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Mangling"
            },
            {
                "type": "Integer",
                "name": "FncClass"
            },
            {
                "type": "Integer",
                "name": "FncProp"
            }
        ]
    },
    "anaproset": {
        "name": "ANAPROSET",
        "columns": [
            {
                "type": "Integer",
                "name": "IDJOB"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JOBNAM"
            },
            {
                "type": "Integer",
                "name": "IDPRO"
            },
            {
                "type": "Integer",
                "name": "IDTYP"
            },
            {
                "type": "String",
                "length": 600,
                "name": "IDSETNAM"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PRONAM"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LNGNAM"
            }
        ]
    },
    "in_propattr": {
        "name": "IN_PROPATTR",
        "columns": [
            {
                "type": "Integer",
                "name": "IDPROP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ATTRNAM"
            },
            {
                "type": "Integer",
                "name": "ATTRTYP"
            },
            {
                "type": "Integer",
                "name": "INTVAL"
            },
            {
                "type": "String",
                "length": 255,
                "name": "STRVAL"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "in_date_properties_chk": {
        "name": "IN_DATE_PROPERTIES_CHK",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "TIMESTAMP",
                "name": "PROPERTY_DATE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DESCRIPTION"
            }
        ]
    },
    "histo_catattr": {
        "name": "HISTO_CATATTR",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ATTRNAM"
            },
            {
                "type": "Integer",
                "name": "ATTRTYP"
            },
            {
                "type": "Integer",
                "name": "INTVAL"
            },
            {
                "type": "String",
                "length": 255,
                "name": "STRVAL"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "dss_objects_statuses": {
        "name": "DSS_OBJECTS_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_STATUS"
            },
            {
                "type": "Integer",
                "name": "IS_ART"
            },
            {
                "type": "Numeric",
                "name": "COST_COMPLEXITY"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE_ID"
            }
        ]
    },
    "tmp_allidinterval": {
        "name": "TMP_ALLIDINTERVAL",
        "columns": [
            {
                "type": "Integer",
                "name": "ALL_ID_MIN"
            },
            {
                "type": "Integer",
                "name": "ALL_ID_MAX"
            },
            {
                "type": "Integer",
                "name": "BLOCK"
            }
        ]
    },
    "appmarq_applicationmeasures": {
        "name": "AppMarq_ApplicationMeasures",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "SnapshotId"
            },
            {
                "type": "Integer",
                "name": "MetricId"
            },
            {
                "type": "Numeric",
                "name": "MetricValue"
            }
        ]
    },
    "cms_ora_rfdefinition": {
        "name": "CMS_ORA_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "dssext_fan_ins": {
        "name": "DSSEXT_FAN_INS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "FAN_IN"
            }
        ]
    },
    "cms_asp_deftechno": {
        "name": "CMS_ASP_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Server_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Client_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefServerScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            },
            {
                "type": "Integer",
                "name": "CallLightImport"
            },
            {
                "type": "Integer",
                "name": "IncludeLightImport"
            },
            {
                "type": "Integer",
                "name": "MaxComplixity"
            },
            {
                "type": "Integer",
                "name": "MaxCodeSize"
            }
        ]
    },
    "anafncrulparm": {
        "name": "AnaFncRulParm",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFncRul"
            },
            {
                "type": "Integer",
                "name": "IdxParm"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ParmExp"
            },
            {
                "type": "Integer",
                "name": "IdxParent"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ParentExp"
            },
            {
                "type": "Integer",
                "name": "ObjTyp"
            },
            {
                "type": "Integer",
                "name": "AccTypLo"
            },
            {
                "type": "Integer",
                "name": "AccTypHi"
            },
            {
                "type": "Integer",
                "name": "AccTypLo2"
            },
            {
                "type": "Integer",
                "name": "AccTypHi2"
            },
            {
                "type": "Integer",
                "name": "IsReturnValue"
            }
        ]
    },
    "in_prop_positions": {
        "name": "IN_PROP_POSITIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_SOURCE_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_SOURCE_KIND"
            },
            {
                "type": "Integer",
                "name": "POSITION_ID"
            },
            {
                "type": "Integer",
                "name": "POSITION_INDEX"
            },
            {
                "type": "Integer",
                "name": "LINE_START"
            },
            {
                "type": "Integer",
                "name": "COL_START"
            },
            {
                "type": "Integer",
                "name": "LINE_END"
            },
            {
                "type": "Integer",
                "name": "COL_END"
            }
        ]
    },
    "adg_func_mod_and_techno_list": {
        "name": "ADG_FUNC_MOD_AND_TECHNO_LIST",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "linktyp": {
        "name": "LinkTyp",
        "columns": [
            {
                "type": "Integer",
                "name": "LinkTyp"
            },
            {
                "type": "Integer",
                "name": "AccTypLo"
            },
            {
                "type": "Integer",
                "name": "AccTypHi"
            },
            {
                "type": "Integer",
                "name": "AccTypLo2"
            },
            {
                "type": "Integer",
                "name": "AccTypHi2"
            }
        ]
    },
    "dssapp_method_f_links": {
        "name": "DSSAPP_METHOD_F_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "IdParentClr"
            },
            {
                "type": "Integer",
                "name": "IdParentCle"
            },
            {
                "type": "Integer",
                "name": "IdClr"
            },
            {
                "type": "Integer",
                "name": "IdCle"
            }
        ]
    },
    "dss_object_types": {
        "name": "DSS_OBJECT_TYPES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE_NAME"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "OBJECT_TYPE_DESCRIPTION"
            },
            {
                "type": "Integer",
                "name": "OBJECT_GROUP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE_NAME_EX"
            }
        ]
    },
    "dssapp_all_tran_calls": {
        "name": "DSSAPP_ALL_TRAN_CALLS",
        "columns": [
            {
                "type": "Integer",
                "name": "MAIN_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "CALL_LEVEL"
            }
        ]
    },
    "tmp_dia_par": {
        "name": "TMP_DIA_PAR",
        "columns": [
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "PARAM_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PARAM_CHAR_VALUE"
            },
            {
                "type": "Integer",
                "name": "PARAM_INDEX"
            }
        ]
    },
    "lckcon": {
        "name": "LCKCON",
        "columns": [
            {
                "type": "Integer",
                "name": "SID"
            },
            {
                "type": "Integer",
                "name": "AUDSID"
            }
        ]
    },
    "modvew": {
        "name": "ModVew",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            },
            {
                "type": "Integer",
                "name": "Num"
            },
            {
                "type": "Integer",
                "name": "StartCol"
            },
            {
                "type": "Integer",
                "name": "StartRow"
            },
            {
                "type": "Integer",
                "name": "Width"
            },
            {
                "type": "Integer",
                "name": "Height"
            },
            {
                "type": "Integer",
                "name": "ZoomFactor"
            }
        ]
    },
    "dss_metric_histo_tree": {
        "name": "DSS_METRIC_HISTO_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_INDEX"
            },
            {
                "type": "Integer",
                "name": "METRIC_TYPE"
            },
            {
                "type": "Numeric",
                "name": "AGGREGATE_WEIGHT"
            },
            {
                "type": "Integer",
                "name": "METRIC_CRITICAL"
            }
        ]
    },
    "wk_dia_prstfld": {
        "name": "WK_DIA_PRSTFLD",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "FIELD_ID"
            },
            {
                "type": "Integer",
                "name": "PROP_ID"
            }
        ]
    },
    "cms_am_parm_txtparams": {
        "name": "CMS_AM_PARM_TxtParams",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "ParamIndex"
            },
            {
                "type": "Integer",
                "name": "Model_ID"
            },
            {
                "type": "Integer",
                "name": "DefValue"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefaultTextValue"
            }
        ]
    },
    "backup_idpmc": {
        "name": "backup_IdPMC",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "String",
                "length": 3000,
                "name": "Field_Value"
            }
        ]
    },
    "amt_del_parent": {
        "name": "AMT_DEL_PARENT",
        "columns": [
            {
                "type": "Integer",
                "name": "EXTERNAL_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_ID"
            }
        ]
    },
    "dssapp_modules": {
        "name": "DSSAPP_MODULES",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LANGUAGE_NAME"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "NB_CLASSES"
            },
            {
                "type": "Integer",
                "name": "NB_INTERFACES"
            },
            {
                "type": "Integer",
                "name": "NB_ARTIFACTS"
            },
            {
                "type": "Numeric",
                "name": "AVG_H_VOLUME"
            },
            {
                "type": "Numeric",
                "name": "AVG_CYCLOMATIC"
            },
            {
                "type": "Numeric",
                "name": "AVG_CODELINES"
            },
            {
                "type": "Numeric",
                "name": "AVG_CM_RATIO"
            }
        ]
    },
    "user_datafunction": {
        "name": "USER_DataFunction",
        "columns": [
            {
                "type": "Integer",
                "name": "MainTable_ID"
            },
            {
                "type": "Integer",
                "name": "ILF"
            },
            {
                "type": "Integer",
                "name": "ILF_Ex"
            },
            {
                "type": "Integer",
                "name": "IsInternal"
            }
        ]
    },
    "dssapp_classes_simple": {
        "name": "DSSAPP_CLASSES_SIMPLE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "amt_prjprop": {
        "name": "AMT_PRJPROP",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_INT"
            }
        ]
    },
    "cms_pb_deftechno": {
        "name": "CMS_PB_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "EnableDashes"
            },
            {
                "type": "Integer",
                "name": "UseInferenceEngine"
            }
        ]
    },
    "acc": {
        "name": "Acc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdAcc",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdClr"
            },
            {
                "type": "Integer",
                "name": "IdCle"
            },
            {
                "type": "Integer",
                "name": "AccTypLo"
            },
            {
                "type": "Integer",
                "name": "AccTypHi"
            },
            {
                "type": "Integer",
                "name": "AccTypLo2"
            },
            {
                "type": "Integer",
                "name": "AccTypHi2"
            },
            {
                "type": "Integer",
                "name": "AccKnd"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "cms_code_fileexecunit": {
        "name": "CMS_CODE_FileExecUnit",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "filobj": {
        "name": "FilObj",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj",
                "primary": True
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Mangling"
            },
            {
                "type": "Integer",
                "name": "ObjClass"
            },
            {
                "type": "Integer",
                "name": "ObjProp"
            },
            {
                "type": "Integer",
                "name": "Pos"
            }
        ]
    },
    "cms_pb_project": {
        "name": "CMS_PB_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TargetFilePath"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Pb_Version"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Pbroc_dll"
            },
            {
                "type": "Integer",
                "name": "EnableDashes"
            }
        ]
    },
    "parms": {
        "name": "Parms",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "Lib"
            },
            {
                "type": "Integer",
                "name": "IntVal"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CarVal"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Trash1"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Trash2"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Trash3"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Trash4"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Trash5"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Trash6"
            }
        ]
    },
    "tmp_named_object": {
        "name": "TMP_NAMED_OBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_NAME"
            }
        ]
    },
    "difflist": {
        "name": "DiffList",
        "columns": [
            {
                "type": "Integer",
                "name": "Id"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "TIMESTAMP",
                "name": "AnaDat"
            },
            {
                "type": "String",
                "length": 3,
                "name": "IdUsr"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "guid_objects": {
        "name": "GUID_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "OBJECT_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "OBJECT_SHORTGUID"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "cms_code_sourcefoldernet": {
        "name": "CMS_CODE_SourceFolderNet",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Usage"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            },
            {
                "type": "String",
                "length": 255,
                "name": "buildAction"
            }
        ]
    },
    "dss_codepath": {
        "name": "DSS_CodePath",
        "columns": [
            {
                "type": "Integer",
                "name": "PathId"
            },
            {
                "type": "Integer",
                "name": "StepIndex"
            },
            {
                "type": "Integer",
                "name": "StepDepth"
            },
            {
                "type": "Integer",
                "name": "SourceId"
            },
            {
                "type": "Integer",
                "name": "StartLine"
            },
            {
                "type": "Integer",
                "name": "FinishLine"
            },
            {
                "type": "Integer",
                "name": "ContainerId"
            }
        ]
    },
    "cms_portf_objectfilter": {
        "name": "CMS_PORTF_ObjectFilter",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Content_Mode"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type_Mode"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name_Mode"
            },
            {
                "type": "Integer",
                "name": "Module_ID"
            }
        ]
    },
    "moddfc": {
        "name": "ModDfc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            },
            {
                "type": "Integer",
                "name": "IdDfc"
            }
        ]
    },
    "dss_code_paths": {
        "name": "DSS_CODE_PATHS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LOCAL_SITE_ID"
            },
            {
                "type": "Integer",
                "name": "LOCAL_SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "PATH_ID"
            },
            {
                "type": "Integer",
                "name": "RANK"
            },
            {
                "type": "Integer",
                "name": "STEP_LEVEL"
            },
            {
                "type": "Integer",
                "name": "START_LINE"
            },
            {
                "type": "Integer",
                "name": "END_LINE"
            }
        ]
    },
    "pmc_archi_model_subsets": {
        "name": "PMC_ARCHI_MODEL_SUBSETS",
        "columns": [
            {
                "type": "Integer",
                "name": "MODEL_ID"
            },
            {
                "type": "Integer",
                "name": "SUBSET_ID"
            }
        ]
    },
    "clppro": {
        "name": "ClpPro",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Entry"
            },
            {
                "type": "Integer",
                "name": "ClpPos"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "wk_dia_net_object_parents": {
        "name": "WK_DIA_NET_OBJECT_PARENTS",
        "columns": [
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "viewer_action_plan_criteria": {
        "name": "VIEWER_ACTION_PLAN_CRITERIA",
        "columns": [
            {
                "type": "Integer",
                "name": "ID",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "METRIC_KIND"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_CRITICAL"
            },
            {
                "type": "Integer",
                "name": "ADDED"
            },
            {
                "type": "Integer",
                "name": "PRIORITY"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "CRIT_COMMENT"
            },
            {
                "type": "Integer",
                "name": "ACTIVE"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "LIST_POSITION"
            }
        ]
    },
    "pmc_archi_rules": {
        "name": "PMC_ARCHI_RULES",
        "columns": [
            {
                "type": "Integer",
                "name": "MODEL_ID"
            },
            {
                "type": "Integer",
                "name": "RULE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "RULE_NAME"
            }
        ]
    },
    "sqlownrul": {
        "name": "SqlOwnRul",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRul"
            },
            {
                "type": "Integer",
                "name": "RulPos"
            },
            {
                "type": "String",
                "length": 128,
                "name": "SrvNam"
            },
            {
                "type": "Integer",
                "name": "IdSrv"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Rul"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            }
        ]
    },
    "propcat": {
        "name": "PropCat",
        "columns": [
            {
                "type": "Integer",
                "name": "IdProp"
            },
            {
                "type": "Integer",
                "name": "IdCat"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "cms_ua_anaoptions": {
        "name": "CMS_UA_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "dia_struts_actioncaller": {
        "name": "DIA_STRUTS_ACTIONCALLER",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "CALLER_CLASS"
            },
            {
                "type": "Integer",
                "name": "CALLER_OBJECT"
            },
            {
                "type": "Integer",
                "name": "CALLER_TYPE"
            }
        ]
    },
    "dss_datafunctiondetails": {
        "name": "DSS_DataFunctionDetails",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "Table_ID"
            },
            {
                "type": "Integer",
                "name": "MergeFlags"
            }
        ]
    },
    "dssapp_metric_param_values": {
        "name": "DSSAPP_METRIC_PARAM_VALUES",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "PARAM_INDEX"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Numeric",
                "name": "PARAM_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "PARAM_CHAR_VALUE"
            }
        ]
    },
    "adg_work_object_results": {
        "name": "ADG_WORK_OBJECT_RESULTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "cms_gen_stringro": {
        "name": "CMS_GEN_StringRO",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            }
        ]
    },
    "efp_art_cost_statuses": {
        "name": "EFP_ART_COST_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "STATUS"
            },
            {
                "type": "Numeric",
                "name": "RESULT_EFFORT"
            },
            {
                "type": "Numeric",
                "name": "RESULT_COST"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_SNAPSHOT_ID"
            }
        ]
    },
    "wk_dia_eqprstcls": {
        "name": "WK_DIA_EQPRSTCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "ENTITY_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "METHOD_ID"
            }
        ]
    },
    "viewer_user_access": {
        "name": "VIEWER_USER_ACCESS",
        "columns": [
            {
                "type": "Integer",
                "name": "USER_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_CATEGORY"
            },
            {
                "type": "Integer",
                "name": "ACCESS_MODE"
            },
            {
                "type": "Integer",
                "name": "ACCESS_EXCEPT"
            },
            {
                "type": "Integer",
                "name": "ACCESS_ACTION"
            },
            {
                "type": "Integer",
                "name": "ACCESS_LIST"
            }
        ]
    },
    "cms_code_sourcefilecpp": {
        "name": "CMS_CODE_SourceFileCPP",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Usage"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            }
        ]
    },
    "cms_dynamicfields_text": {
        "name": "CMS_DynamicFields_TEXT",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Entity_GUID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Field_GUID"
            },
            {
                "type": "Text",
                "name": "Field_Value"
            }
        ]
    },
    "adg_techno_links": {
        "name": "ADG_TECHNO_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NEXT_OBJECT_ID"
            }
        ]
    },
    "cms_code_repo_oracleextract": {
        "name": "CMS_CODE_REPO_OracleExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "objinf": {
        "name": "ObjInf",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "InfTyp"
            },
            {
                "type": "Integer",
                "name": "InfSubTyp"
            },
            {
                "type": "Integer",
                "name": "BlkNo"
            },
            {
                "type": "Integer",
                "name": "InfVal"
            }
        ]
    },
    "dss_transactiondetails": {
        "name": "DSS_TransactionDetails",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "Child_ID"
            },
            {
                "type": "Integer",
                "name": "ChildType"
            },
            {
                "type": "Integer",
                "name": "Contribute"
            }
        ]
    },
    "catattr": {
        "name": "CatAttr",
        "columns": [
            {
                "type": "Integer",
                "name": "IdCat"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AttrNam"
            },
            {
                "type": "Integer",
                "name": "AttrTyp"
            },
            {
                "type": "Integer",
                "name": "IntVal"
            },
            {
                "type": "String",
                "length": 255,
                "name": "StrVal"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "wk_dia_cobparapcb": {
        "name": "WK_DIA_COBPARAPCB",
        "columns": [
            {
                "type": "Integer",
                "name": "APPIDPARA"
            },
            {
                "type": "Integer",
                "name": "PARA"
            },
            {
                "type": "Integer",
                "name": "PCB"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "LVL"
            }
        ]
    },
    "cms_cpp_deftechno": {
        "name": "CMS_CPP_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cpp_Compilation"
            },
            {
                "type": "Integer",
                "name": "Managed_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "C_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cpp_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DevEnv_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Stl_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PrecompiledHeader"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PchGenerator"
            },
            {
                "type": "Integer",
                "name": "DisableUseofPch"
            },
            {
                "type": "Integer",
                "name": "MagicRgtShift"
            },
            {
                "type": "Integer",
                "name": "Trigraph"
            },
            {
                "type": "Integer",
                "name": "StdScope"
            },
            {
                "type": "Integer",
                "name": "IsoTypename"
            },
            {
                "type": "Integer",
                "name": "UnknownDirective"
            },
            {
                "type": "Integer",
                "name": "MaxCodeSize"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "anasel": {
        "name": "AnaSel",
        "columns": [
            {
                "type": "Integer",
                "name": "IdSel"
            },
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "SelTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "SelVal"
            },
            {
                "type": "Integer",
                "name": "SelProp"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            },
            {
                "type": "Integer",
                "name": "StrBlk"
            },
            {
                "type": "Integer",
                "name": "IdCnx"
            }
        ]
    },
    "dss_metric_work_tables": {
        "name": "DSS_METRIC_WORK_TABLES",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "WORK_CATEGORY"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TABLE_NAME"
            }
        ]
    },
    "viewer_data_retrievers": {
        "name": "VIEWER_DATA_RETRIEVERS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PARENT_COMPONENT_ID"
            },
            {
                "type": "Integer",
                "name": "CHILD_OFFSET"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "CLASS_PATH"
            },
            {
                "length": 200,
                "type": "String",
                "name": "ROW_DATA_TYPE_IDS"
            }
        ]
    },
    "cms_ora_apptechno": {
        "name": "CMS_ORA_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "wk_dia_cobppm": {
        "name": "WK_DIA_COBPPM",
        "columns": [
            {
                "type": "Integer",
                "name": "para"
            },
            {
                "type": "Integer",
                "name": "pgm"
            }
        ]
    },
    "cms_inf_ora_accesssrv": {
        "name": "CMS_INF_ORA_AccessSrv",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Service"
            }
        ]
    },
    "keygrp": {
        "name": "KeyGrp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "IdGrp"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "appmarq_developersrangemodel": {
        "name": "AppMarq_DevelopersRangeModel",
        "columns": [
            {
                "type": "Integer",
                "name": "DevelopersRangeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "DevelopersRangeName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "DevelopersRangeDescription"
            }
        ]
    },
    "cms_pb_analysis": {
        "name": "CMS_PB_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Project"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Pb_Version"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Pbroc_dll"
            },
            {
                "type": "Integer",
                "name": "EnableDashes"
            }
        ]
    },
    "cms_ui_analysis": {
        "name": "CMS_UI_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            }
        ]
    },
    "cms_j2ee_xsstargetdfm": {
        "name": "CMS_J2EE_XSSTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "viewer_profiles": {
        "name": "VIEWER_PROFILES",
        "columns": [
            {
                "type": "Integer",
                "name": "ID",
                "primary": True
            },
            {
                "length": 255,
                "type": "String",
                "name": "NAME"
            }
        ]
    },
    "pboobj": {
        "name": "PboObj",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdPbl"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjNam"
            },
            {
                "type": "Integer",
                "name": "ObjClass"
            },
            {
                "type": "Integer",
                "name": "ObjProp"
            }
        ]
    },
    "amt_ili": {
        "name": "AMT_ILI",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "INFTYPATT"
            },
            {
                "type": "Integer",
                "name": "INFSUBTYPATT"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_INT"
            }
        ]
    },
    "cms_pref_sources": {
        "name": "CMS_PREF_Sources",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ServerPath"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "DeployPath"
            }
        ]
    },
    "objdscref": {
        "name": "ObjDscRef",
        "columns": [
            {
                "type": "Integer",
                "name": "InfTyp"
            },
            {
                "type": "Integer",
                "name": "InfSubTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Dsc"
            },
            {
                "type": "Integer",
                "name": "DscAccess"
            }
        ]
    },
    "jobanalysisproperties": {
        "name": "JobAnalysisProperties",
        "columns": [
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "GuidLevel"
            }
        ]
    },
    "tmp_lnkidinterval": {
        "name": "TMP_LNKIDINTERVAL",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID_MIN"
            },
            {
                "type": "Integer",
                "name": "LINK_ID_MAX"
            },
            {
                "type": "Integer",
                "name": "BLOCK"
            }
        ]
    },
    "frmobj": {
        "name": "FrmObj",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjNam"
            },
            {
                "type": "Integer",
                "name": "ObjClass"
            },
            {
                "type": "Integer",
                "name": "ObjProp"
            }
        ]
    },
    "dia_codepath": {
        "name": "DIA_CODEPATH",
        "columns": [
            {
                "type": "Integer",
                "name": "Id"
            },
            {
                "type": "Integer",
                "name": "JobId"
            },
            {
                "type": "Integer",
                "name": "MetricId"
            },
            {
                "type": "Integer",
                "name": "PathId"
            },
            {
                "type": "Integer",
                "name": "ObjectId"
            }
        ]
    },
    "histo_typ": {
        "name": "HISTO_TYP",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDTYP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TYPNAM"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TYPDSC"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "srvali": {
        "name": "SrvAli",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "SrvNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AliNam"
            },
            {
                "type": "Integer",
                "name": "IdSrv"
            }
        ]
    },
    "objprodat": {
        "name": "ObjProDat",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "Integer",
                "name": "Prop"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            },
            {
                "type": "TIMESTAMP",
                "name": "DtInfo"
            },
            {
                "type": "Integer",
                "name": "CRC"
            }
        ]
    },
    "dsprullnk": {
        "name": "DspRulLnk",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRul"
            },
            {
                "type": "Integer",
                "name": "AccTypLo"
            },
            {
                "type": "Integer",
                "name": "AccTypHi"
            },
            {
                "type": "Integer",
                "name": "AccTypLo2"
            },
            {
                "type": "Integer",
                "name": "AccTypHi2"
            }
        ]
    },
    "cms_am_bvconsomode": {
        "name": "CMS_AM_BVConsoMode",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "AssessmentModel"
            },
            {
                "type": "Integer",
                "name": "BusinessValue"
            }
        ]
    },
    "appmarq_technologies": {
        "name": "AppMarq_Technologies",
        "columns": [
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "type": "Integer",
                "name": "TechnologyId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "TechnologyName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "TechnologyDescription"
            }
        ]
    },
    "cltelt": {
        "name": "CltElt",
        "columns": [
            {
                "type": "Integer",
                "name": "IdElt"
            },
            {
                "type": "String",
                "length": 128,
                "name": "EltNam"
            },
            {
                "type": "Integer",
                "name": "EltClass"
            },
            {
                "type": "Integer",
                "name": "EltProp"
            },
            {
                "type": "String",
                "length": 38,
                "name": "EltGUID"
            }
        ]
    },
    "pmc_tmp_subset_tree": {
        "name": "PMC_TMP_SUBSET_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_LEVEL"
            }
        ]
    },
    "wk_fgiaimpactlist": {
        "name": "WK_FGIAIMPACTLIST",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSIONID"
            },
            {
                "type": "Integer",
                "name": "IDKEYSTART"
            },
            {
                "type": "String",
                "length": 255,
                "name": "KEYNAMESTART"
            },
            {
                "type": "String",
                "length": 128,
                "name": "OWNERIMPACT"
            },
            {
                "type": "Integer",
                "name": "IDKEYIMPACT"
            },
            {
                "type": "String",
                "length": 255,
                "name": "KEYNAMEIMPACT"
            },
            {
                "type": "Integer",
                "name": "KEYCLASSIMPACT"
            }
        ]
    },
    "cms_syb_rfdefinition": {
        "name": "CMS_SYB_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "cms_pg_credential": {
        "name": "CMS_PG_Credential",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UserName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Password"
            }
        ]
    },
    "cms_syb_prodoptions": {
        "name": "CMS_SYB_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "inkb_dataflowresults": {
        "name": "INKB_DataflowResults",
        "columns": [
            {
                "type": "Integer",
                "name": "MetricId"
            },
            {
                "type": "String",
                "length": 600,
                "name": "SourcePath"
            },
            {
                "type": "Integer",
                "name": "StartLine"
            },
            {
                "type": "Integer",
                "name": "FinishLine"
            },
            {
                "type": "Integer",
                "name": "ContainerId"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "ContainerGuid"
            },
            {
                "type": "String",
                "length": 600,
                "name": "ContainerShortGuid"
            },
            {
                "type": "Integer",
                "name": "PathId"
            },
            {
                "type": "Integer",
                "name": "StepIndex"
            },
            {
                "type": "Integer",
                "name": "StepDepth"
            },
            {
                "type": "Integer",
                "name": "JobId"
            }
        ]
    },
    "cms_rf_embeddedrule": {
        "name": "CMS_RF_EmbeddedRule",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "EmbRuleBegin"
            },
            {
                "type": "String",
                "length": 255,
                "name": "EmbRuleExpression"
            },
            {
                "type": "String",
                "length": 255,
                "name": "EmbRuleEnd"
            }
        ]
    },
    "wk_tcc_reorder_trace": {
        "name": "WK_TCC_REORDER_TRACE",
        "columns": [
            {
                "type": "Integer",
                "name": "Target_Datafunction"
            },
            {
                "type": "Integer",
                "name": "Source_Datafunction"
            },
            {
                "type": "Integer",
                "name": "Source_MainTable_ID"
            },
            {
                "type": "Integer",
                "name": "Source_Table_ID"
            },
            {
                "type": "String",
                "length": 50,
                "name": "ACTION_TYPE"
            },
            {
                "type": "TIMESTAMP",
                "name": "ACTION_DATE"
            },
            {
                "type": "String",
                "length": 500,
                "name": "ACTION_DESCRIPTION"
            }
        ]
    },
    "cms_net_assembly_folder": {
        "name": "CMS_NET_ASSEMBLY_FOLDER",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "AssemblyPath"
            },
            {
                "type": "Integer",
                "name": "Recursive"
            }
        ]
    },
    "user_transaction": {
        "name": "USER_Transaction",
        "columns": [
            {
                "type": "Integer",
                "name": "Form_ID"
            },
            {
                "type": "Integer",
                "name": "TF"
            },
            {
                "type": "Integer",
                "name": "TF_Ex"
            },
            {
                "type": "Integer",
                "name": "IsInput"
            }
        ]
    },
    "apm_worktable": {
        "name": "APM_WORKTABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NODE"
            },
            {
                "type": "Numeric",
                "name": "RESULT"
            },
            {
                "type": "Numeric",
                "name": "RESULT_2"
            },
            {
                "type": "Numeric",
                "name": "RESULT_3"
            },
            {
                "type": "Numeric",
                "name": "RESULT_4"
            },
            {
                "type": "Numeric",
                "name": "RESULT_5"
            },
            {
                "type": "Numeric",
                "name": "RESULT_6"
            },
            {
                "type": "Numeric",
                "name": "RESULT_7"
            },
            {
                "type": "Numeric",
                "name": "RESULT_8"
            },
            {
                "type": "String",
                "length": 255,
                "name": "VAR_RESULT"
            }
        ]
    },
    "cms_net_assembly_file": {
        "name": "CMS_NET_ASSEMBLY_FILE",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "AssemblyPath"
            }
        ]
    },
    "cms_udb_deftechno": {
        "name": "CMS_UDB_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            }
        ]
    },
    "cms_ora_prodoptions": {
        "name": "CMS_ORA_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            },
            {
                "type": "Integer",
                "name": "LinksToPkgSubObjects"
            }
        ]
    },
    "cal_ignoredtable": {
        "name": "CAL_IgnoredTable",
        "columns": [
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Description"
            },
            {
                "type": "String",
                "length": 255,
                "name": "RegExp"
            }
        ]
    },
    "cms_code_cont_sapextract": {
        "name": "CMS_CODE_CONT_SAPExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TablesFolder"
            }
        ]
    },
    "cms_net_userinputdfm": {
        "name": "CMS_NET_UserInputDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            }
        ]
    },
    "in_char_properties": {
        "name": "IN_CHAR_PROPERTIES",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "Integer",
                "name": "CHAR_BLOCK"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROPERTY_CHAR"
            }
        ]
    },
    "dss_transaction": {
        "name": "DSS_Transaction",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "Form_ID"
            },
            {
                "type": "Integer",
                "name": "DET"
            },
            {
                "type": "Integer",
                "name": "FTR"
            },
            {
                "type": "Integer",
                "name": "TF"
            },
            {
                "type": "Integer",
                "name": "TF_Ex"
            },
            {
                "type": "Integer",
                "name": "IsInput"
            },
            {
                "type": "Integer",
                "name": "Appli_ID"
            },
            {
                "type": "Integer",
                "name": "User_FP_Value"
            },
            {
                "type": "Integer",
                "name": "User_IsInput"
            },
            {
                "type": "Integer",
                "name": "Cal_Flags"
            },
            {
                "type": "Integer",
                "name": "Cal_MergeRoot_ID"
            }
        ]
    },
    "cms_cobol_rfdefinition": {
        "name": "CMS_COBOL_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "dss_metric_param_types": {
        "name": "DSS_METRIC_PARAM_TYPES",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "PARAM_INDEX"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PARAM_TYPE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PARAM_NAME"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "PARAM_DESCRIPTION"
            }
        ]
    },
    "dss_metric_type_trees": {
        "name": "DSS_METRIC_TYPE_TREES",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_INDEX"
            },
            {
                "type": "Numeric",
                "name": "AGGREGATE_WEIGHT"
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_SCOPE_PROCEDURE_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "METRIC_SCOPE_PROCEDURE_NAME_2"
            },
            {
                "type": "Integer",
                "name": "METRIC_CRITICAL"
            }
        ]
    },
    "cms_pb_anaoptions": {
        "name": "CMS_PB_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "EnableDashes"
            }
        ]
    },
    "pboctl": {
        "name": "PboCtl",
        "columns": [
            {
                "type": "Integer",
                "name": "IdCtl",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CtlNam"
            },
            {
                "type": "Integer",
                "name": "CtlClass"
            },
            {
                "type": "Integer",
                "name": "CtlProp"
            }
        ]
    },
    "cms_inf_ora_analyticdb": {
        "name": "CMS_INF_ORA_AnalyticDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Version"
            },
            {
                "type": "Integer",
                "name": "Credential_ID"
            },
            {
                "type": "Integer",
                "name": "Server_ID"
            },
            {
                "type": "Integer",
                "name": "Service_Unique_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Status"
            }
        ]
    },
    "keydat": {
        "name": "KeyDat",
        "columns": [
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "TIMESTAMP",
                "name": "CrDat"
            },
            {
                "type": "TIMESTAMP",
                "name": "AnaDat"
            },
            {
                "type": "TIMESTAMP",
                "name": "DocDat"
            },
            {
                "type": "TIMESTAMP",
                "name": "FlagDate"
            }
        ]
    },
    "viewer_olia": {
        "name": "VIEWER_OLIA",
        "columns": [
            {
                "type": "String",
                "length": 255,
                "name": "SPID"
            },
            {
                "type": "Integer",
                "name": "IMPLEVEL"
            },
            {
                "type": "Integer",
                "name": "CHILDLEVEL"
            },
            {
                "type": "Integer",
                "name": "IDOBJ"
            },
            {
                "type": "Integer",
                "name": "IDPARENT"
            },
            {
                "type": "Integer",
                "name": "IDCLRCLE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FULLQUALIFIEDNAME"
            },
            {
                "type": "String",
                "length": 20,
                "name": "IMPACTTYPE"
            },
            {
                "type": "Integer",
                "name": "ACCTYPLO"
            },
            {
                "type": "Integer",
                "name": "ACCTYPHI"
            }
        ]
    },
    "fld": {
        "name": "Fld",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFld"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FldNam"
            },
            {
                "type": "Integer",
                "name": "FldParent"
            },
            {
                "type": "String",
                "length": 600,
                "name": "FldPath"
            }
        ]
    },
    "dss_link_types": {
        "name": "DSS_LINK_TYPES",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LINK_TYPE_NAME"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "LINK_TYPE_DESCRIPTION"
            },
            {
                "type": "Integer",
                "name": "LINK_GROUP"
            }
        ]
    },
    "usrprojob_del": {
        "name": "UsrProJob_Del",
        "columns": [
            {
                "type": "Integer",
                "name": "IdUsrPro"
            },
            {
                "type": "Integer",
                "name": "IdJob"
            }
        ]
    },
    "objfilref": {
        "name": "ObjFilRef",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "IdFilRef"
            },
            {
                "type": "Integer",
                "name": "IdFil"
            }
        ]
    },
    "dss_link_info": {
        "name": "DSS_LINK_INFO",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "NEXT_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            }
        ]
    },
    "dss_tree_ranking": {
        "name": "DSS_TREE_RANKING",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "BUSINESS_CRITERION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TREE_LEVEL"
            },
            {
                "type": "Integer",
                "name": "TREE_LEFT_POSITION"
            },
            {
                "type": "Integer",
                "name": "TREE_RIGHT_POSITION"
            },
            {
                "type": "Integer",
                "name": "ALL_VIOLATED_RULES_NB"
            },
            {
                "type": "Integer",
                "name": "ALL_VIOLATING_OBJECTS_NB"
            },
            {
                "type": "Integer",
                "name": "ALL_VIOLATIONS_NB"
            }
        ]
    },
    "amt_parent": {
        "name": "AMT_PARENT",
        "columns": [
            {
                "type": "Integer",
                "name": "EXTERNAL_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "STATUS"
            }
        ]
    },
    "cms_common_deftechno": {
        "name": "CMS_Common_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "EscalateLinks"
            },
            {
                "type": "Integer",
                "name": "Store"
            },
            {
                "type": "Integer",
                "name": "Vars_ID"
            }
        ]
    },
    "dia_method_loop": {
        "name": "DIA_METHOD_LOOP",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "POS"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "in_typ": {
        "name": "IN_TYP",
        "columns": [
            {
                "type": "Integer",
                "name": "IDTYP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TYPNAM"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TYPDSC"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "amt_oflink": {
        "name": "AMT_OFLINK",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "PROJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "SOURCE_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "TARGET_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "PROJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_PROJECT_ID"
            }
        ]
    },
    "ci_links": {
        "name": "CI_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "CALLER_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "CALLER_SHORTGUID"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "CALLED_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "CALLED_SHORTGUID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LINK_TYPE"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "apm_module_parents": {
        "name": "APM_MODULE_PARENTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "TREE_LEVEL"
            }
        ]
    },
    "esc_projects": {
        "name": "ESC_Projects",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPro"
            }
        ]
    },
    "all_prop_positions": {
        "name": "ALL_PROP_POSITIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_SOURCE_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_SOURCE_KIND"
            },
            {
                "type": "Integer",
                "name": "POSITION_ID"
            },
            {
                "type": "Integer",
                "name": "POSITION_INDEX"
            },
            {
                "type": "Integer",
                "name": "LINE_START"
            },
            {
                "type": "Integer",
                "name": "COL_START"
            },
            {
                "type": "Integer",
                "name": "LINE_END"
            },
            {
                "type": "Integer",
                "name": "COL_END"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_SOURCE_ID"
            }
        ]
    },
    "dss_keysextra": {
        "name": "DSS_KeysExtra",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Object_Type"
            },
            {
                "type": "Integer",
                "name": "Object_Checksum"
            }
        ]
    },
    "wk_dia_alleqprscls": {
        "name": "WK_DIA_ALLEQPRSCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "METHOD_ID"
            }
        ]
    },
    "wk_dia_netinherit": {
        "name": "WK_DIA_NETINHERIT",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "cms_migr_analysismanytoone": {
        "name": "CMS_MIGR_AnalysisManyToOne",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "String",
                "length": 1050,
                "name": "Mail"
            },
            {
                "type": "Integer",
                "name": "LocalDB_Unique_ID"
            },
            {
                "type": "Integer",
                "name": "JobType"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectDesc"
            }
        ]
    },
    "keysana": {
        "name": "KeysAna",
        "columns": [
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "String",
                "length": 255,
                "name": "KeyNamAna"
            },
            {
                "type": "Integer",
                "name": "KeyClass"
            },
            {
                "type": "Integer",
                "name": "KeyProp"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            }
        ]
    },
    "refcol": {
        "name": "RefCol",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRef"
            },
            {
                "type": "Integer",
                "name": "IdMotherCol"
            },
            {
                "type": "Integer",
                "name": "IdDaughterCol"
            }
        ]
    },
    "cms_net_rfdefinition": {
        "name": "CMS_NET_RFDefinition",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "SearchInCode"
            },
            {
                "type": "Integer",
                "name": "SearchInComment"
            },
            {
                "type": "Integer",
                "name": "SearchInString"
            },
            {
                "type": "Integer",
                "name": "SearchInEmbedSql"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LanguageFilterMode"
            },
            {
                "type": "Integer",
                "name": "RegExp"
            },
            {
                "type": "Integer",
                "name": "RegexpMatchCase"
            },
            {
                "type": "Integer",
                "name": "MatchWordOnly"
            },
            {
                "type": "Integer",
                "name": "UseFlag"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ReplacementString"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PatternType"
            },
            {
                "type": "Integer",
                "name": "MatchCase"
            },
            {
                "type": "String",
                "length": 255,
                "name": "NameMatching"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LinkType"
            },
            {
                "type": "Integer",
                "name": "ExcludeXFileLinks"
            }
        ]
    },
    "ctt_object_decode_type": {
        "name": "CTT_OBJECT_DECODE_TYPE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE_STR"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_LANGUAGE"
            }
        ]
    },
    "cms_code_repo_file": {
        "name": "CMS_CODE_REPO_File",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "typattr": {
        "name": "TypAttr",
        "columns": [
            {
                "type": "Integer",
                "name": "IdTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AttrNam"
            },
            {
                "type": "Integer",
                "name": "AttrTyp"
            },
            {
                "type": "Integer",
                "name": "IntVal"
            },
            {
                "type": "String",
                "length": 255,
                "name": "StrVal"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "cms_vb_apptechno": {
        "name": "CMS_VB_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "appmarq_qapercenttimemodel": {
        "name": "AppMarq_QAPercentTimeModel",
        "columns": [
            {
                "type": "Integer",
                "name": "QAPercentTimeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "QAPercentTimeName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "QAPercentTimeDescription"
            }
        ]
    },
    "cms_am_desc_scope": {
        "name": "CMS_AM_DESC_Scope",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            }
        ]
    },
    "amt_objfilref": {
        "name": "AMT_OBJFILREF",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "String",
                "length": 600,
                "name": "PROPERTY_STRING"
            }
        ]
    },
    "cms_am_qual_mod_selection": {
        "name": "CMS_AM_QUAL_MOD_Selection",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Exclusion"
            },
            {
                "type": "Integer",
                "name": "Selection"
            }
        ]
    },
    "cms_code_repo_dbzosextract": {
        "name": "CMS_CODE_REPO_DBZOSExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "apm_work_mod_results": {
        "name": "APM_WORK_MOD_RESULTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "VALUE_INDEX"
            },
            {
                "type": "Numeric",
                "name": "RESULT"
            }
        ]
    },
    "cms_zos_apptechno": {
        "name": "CMS_ZOS_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "typ": {
        "name": "Typ",
        "columns": [
            {
                "type": "Integer",
                "name": "IdTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TypNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TypDsc"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "sys_package_version": {
        "name": "SYS_PACKAGE_VERSION",
        "columns": [
            {
                "type": "String",
                "length": 100,
                "name": "PACKAGE_NAME"
            },
            {
                "type": "String",
                "length": 30,
                "name": "VERSION"
            }
        ]
    },
    "backup_idanalysisunit": {
        "name": "backup_IdAnalysisUnit",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Entity_GUID"
            },
            {
                "type": "String",
                "length": 3000,
                "name": "Field_Value"
            }
        ]
    },
    "dss_technologies": {
        "name": "DSS_TECHNOLOGIES",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE_ID"
            }
        ]
    },
    "appmarq_centrals": {
        "name": "AppMarq_Centrals",
        "columns": [
            {
                "type": "Integer",
                "name": "CustomerId"
            },
            {
                "type": "Integer",
                "name": "CentralId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "CentralGUID"
            }
        ]
    },
    "wk_dia_statement": {
        "name": "WK_DIA_STATEMENT",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            }
        ]
    },
    "wk_dia_prstprp": {
        "name": "WK_DIA_PRSTPRP",
        "columns": [
            {
                "type": "Integer",
                "name": "PROPERTY_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PRO_COLLECTION"
            },
            {
                "type": "Integer",
                "name": "METHOD_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "ctt_link_decode_category": {
        "name": "CTT_LINK_DECODE_CATEGORY",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_CATEGORY"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LINK_CATEGORY_STR"
            }
        ]
    },
    "cdt_objects": {
        "name": "CDT_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_NAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_FULLNAME"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE_STR"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_MANGLING"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_TYPE_EXT"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_LANGUAGE_NAME"
            }
        ]
    },
    "apm_temp": {
        "name": "APM_TEMP",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "in_links": {
        "name": "IN_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_ID"
            },
            {
                "type": "Integer",
                "name": "PROJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "SOURCE_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "TARGET_KIND"
            },
            {
                "type": "String",
                "length": 1,
                "name": "PROJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            }
        ]
    },
    "viewer_action_plans": {
        "name": "VIEWER_ACTION_PLANS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "FIRST_SNAPSHOT_DATE"
            },
            {
                "type": "TIMESTAMP",
                "name": "LAST_SNAPSHOT_DATE"
            },
            {
                "length": 255,
                "type": "String",
                "name": "USER_NAME"
            },
            {
                "type": "TIMESTAMP",
                "name": "SEL_DATE"
            },
            {
                "type": "Integer",
                "name": "PRIORITY"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "ACTION_DEF"
            }
        ]
    },
    "dssapp_classes": {
        "name": "DSSAPP_CLASSES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "IS_INTERFACE"
            },
            {
                "type": "Integer",
                "name": "CODE_LINES"
            },
            {
                "type": "Integer",
                "name": "COMMENT_LINES"
            },
            {
                "type": "Integer",
                "name": "SUMAK"
            },
            {
                "type": "Integer",
                "name": "NUM_METHODS"
            },
            {
                "type": "Integer",
                "name": "NUM_METHODS2"
            },
            {
                "type": "Integer",
                "name": "NUM_REMOTE_METHODS"
            },
            {
                "type": "Integer",
                "name": "NUM_FIELDS"
            },
            {
                "type": "Integer",
                "name": "NUM_PUB_FIELDS"
            },
            {
                "type": "Integer",
                "name": "INH_LEVEL"
            },
            {
                "type": "Numeric",
                "name": "LCOM"
            },
            {
                "type": "Numeric",
                "name": "LCOM2"
            },
            {
                "type": "Numeric",
                "name": "ABSTRACT_RATIO"
            },
            {
                "type": "Integer",
                "name": "WEIGHTED_METHODS"
            },
            {
                "type": "Integer",
                "name": "NUM_PARENTS"
            },
            {
                "type": "Integer",
                "name": "NUM_CHILDREN"
            },
            {
                "type": "Integer",
                "name": "CFAN_IN"
            },
            {
                "type": "Integer",
                "name": "CFAN_OUT"
            },
            {
                "type": "Integer",
                "name": "RESPONSE"
            },
            {
                "type": "Integer",
                "name": "OO_COMPLEXITY"
            }
        ]
    },
    "dfc": {
        "name": "Dfc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdDfc"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DfcNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DfcLib"
            },
            {
                "type": "Integer",
                "name": "DfcParent"
            },
            {
                "type": "Integer",
                "name": "Color"
            }
        ]
    },
    "itm": {
        "name": "Itm",
        "columns": [
            {
                "type": "Integer",
                "name": "IdItm"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "Integer",
                "name": "IdParent"
            },
            {
                "type": "Integer",
                "name": "IdItmParent"
            },
            {
                "type": "String",
                "length": 30,
                "name": "ItmNam"
            },
            {
                "type": "String",
                "length": 2000,
                "name": "ItmMng"
            },
            {
                "type": "Integer",
                "name": "ItmTyp"
            },
            {
                "type": "Integer",
                "name": "ItmClass"
            },
            {
                "type": "Integer",
                "name": "ItmProp"
            },
            {
                "type": "Integer",
                "name": "NumLin"
            },
            {
                "type": "Integer",
                "name": "NumCol"
            },
            {
                "type": "Integer",
                "name": "RetDtp"
            },
            {
                "type": "Integer",
                "name": "RetLen"
            },
            {
                "type": "Integer",
                "name": "RetPrc"
            },
            {
                "type": "Integer",
                "name": "RetScl"
            },
            {
                "type": "Integer",
                "name": "ItmNat"
            }
        ]
    },
    "tmp_dia_qryinloop": {
        "name": "TMP_DIA_QRYINLOOP",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "cms_ua_language": {
        "name": "CMS_UA_Language",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "InternalName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Extensions"
            }
        ]
    },
    "sys_package_history": {
        "name": "SYS_PACKAGE_HISTORY",
        "columns": [
            {
                "type": "String",
                "length": 100,
                "name": "PACKAGE_NAME"
            },
            {
                "type": "String",
                "length": 30,
                "name": "REVISION"
            },
            {
                "type": "Integer",
                "name": "REVISION_TYPE"
            },
            {
                "type": "TIMESTAMP",
                "name": "REVISION_DATE"
            },
            {
                "type": "String",
                "length": 100,
                "name": "INSTALLER"
            }
        ]
    },
    "cms_zos_anaoptions": {
        "name": "CMS_ZOS_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "fp_wk_group_objects": {
        "name": "FP_WK_Group_Objects",
        "columns": [
            {
                "type": "Integer",
                "name": "Appli_ID"
            },
            {
                "type": "Integer",
                "name": "Subset_Group"
            },
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "FP_Value"
            },
            {
                "type": "Integer",
                "name": "DET_Value"
            },
            {
                "type": "Integer",
                "name": "RET_Value"
            }
        ]
    },
    "dss_work_module_flat_tree": {
        "name": "DSS_WORK_MODULE_FLAT_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "FLAT_LEVEL"
            }
        ]
    },
    "appmarq_technologymeasures": {
        "name": "AppMarq_TechnologyMeasures",
        "columns": [
            {
                "type": "Integer",
                "name": "TechnicalVersionId"
            },
            {
                "type": "Integer",
                "name": "ApplicationId"
            },
            {
                "type": "Integer",
                "name": "SnapshotId"
            },
            {
                "type": "Integer",
                "name": "TechnologyId"
            },
            {
                "type": "Integer",
                "name": "MetricId"
            },
            {
                "type": "Numeric",
                "name": "MetricValue"
            }
        ]
    },
    "cms_cobol_analysis": {
        "name": "CMS_COBOL_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cobol_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JCL_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "IMS_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CICS_FileExtensions"
            },
            {
                "type": "Integer",
                "name": "IBM_Environment"
            },
            {
                "type": "Integer",
                "name": "Cobol_StartingColumn"
            },
            {
                "type": "Integer",
                "name": "Cobol_ReadTermFormat"
            },
            {
                "type": "Integer",
                "name": "Cobol_UseComponentName"
            },
            {
                "type": "Integer",
                "name": "Tab_Length"
            },
            {
                "type": "Integer",
                "name": "cobol_CodeBeyondRightCol"
            },
            {
                "type": "Integer",
                "name": "IMS_IndcatorArea"
            }
        ]
    },
    "cms_sap_project": {
        "name": "CMS_SAP_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "TablesPath"
            }
        ]
    },
    "cms_tool_variable": {
        "name": "CMS_TOOL_Variable",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Var_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Var_Value"
            },
            {
                "type": "String",
                "length": 2000,
                "name": "Var_Desc"
            }
        ]
    },
    "viewer_filters": {
        "name": "VIEWER_FILTERS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PARENT_SECTION_ID"
            },
            {
                "type": "Integer",
                "name": "CHILD_OFFSET"
            },
            {
                "length": 200,
                "type": "String",
                "name": "FILTERED_FIELDS"
            }
        ]
    },
    "cms_common_prodoptions": {
        "name": "CMS_Common_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "EscalateLinks"
            }
        ]
    },
    "viewer_data_persisters": {
        "name": "VIEWER_DATA_PERSISTERS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PARENT_COMPONENT_ID"
            },
            {
                "type": "Integer",
                "name": "CHILD_OFFSET"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "CLASS_PATH"
            },
            {
                "length": 200,
                "type": "String",
                "name": "ROW_DATA_TYPE_IDS"
            }
        ]
    },
    "apm_temp_volumes": {
        "name": "APM_TEMP_VOLUMES",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "COPY_VOLUME"
            },
            {
                "type": "Integer",
                "name": "CODE_LINES"
            }
        ]
    },
    "dss_config_export": {
        "name": "DSS_CONFIG_EXPORT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_INDEX"
            }
        ]
    },
    "dssapp_cls_type_couples": {
        "name": "DSSAPP_CLS_TYPE_COUPLES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_TYPE"
            },
            {
                "type": "Integer",
                "name": "PARENT_TYPE"
            }
        ]
    },
    "wk_dia_calllink": {
        "name": "WK_DIA_CALLLINK",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPro"
            },
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "IdClr"
            },
            {
                "type": "Integer",
                "name": "IdCle"
            },
            {
                "type": "Integer",
                "name": "Info1"
            }
        ]
    },
    "accbook": {
        "name": "AccBook",
        "columns": [
            {
                "type": "Integer",
                "name": "IdAcc"
            },
            {
                "type": "Integer",
                "name": "BookMode"
            },
            {
                "type": "Integer",
                "name": "Info1"
            },
            {
                "type": "Integer",
                "name": "Info2"
            },
            {
                "type": "Integer",
                "name": "Info3"
            },
            {
                "type": "Integer",
                "name": "Info4"
            },
            {
                "type": "Integer",
                "name": "Prop"
            },
            {
                "type": "Integer",
                "name": "BlkNo"
            }
        ]
    },
    "fp_result_objectlist": {
        "name": "FP_Result_ObjectList",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "Integer",
                "name": "FP_Value"
            },
            {
                "type": "Integer",
                "name": "DET_Value"
            },
            {
                "type": "Integer",
                "name": "RET_Value"
            }
        ]
    },
    "inkb_dataflowscopes": {
        "name": "INKB_DataflowScopes",
        "columns": [
            {
                "type": "Integer",
                "name": "MetricId"
            },
            {
                "type": "Integer",
                "name": "ObjectId"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "ObjectGuid"
            },
            {
                "type": "String",
                "length": 600,
                "name": "ObjectShortGuid"
            },
            {
                "type": "Integer",
                "name": "JobId"
            }
        ]
    },
    "objdfc": {
        "name": "ObjDfc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "IdCon"
            }
        ]
    },
    "adg_func_module_list": {
        "name": "ADG_FUNC_MODULE_LIST",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "cms_code_sourcefolder": {
        "name": "CMS_CODE_SourceFolder",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Usage"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            }
        ]
    },
    "modlay": {
        "name": "ModLay",
        "columns": [
            {
                "type": "Integer",
                "name": "IdLay"
            },
            {
                "type": "String",
                "length": 30,
                "name": "LayNam"
            },
            {
                "type": "Integer",
                "name": "LayVis"
            },
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            }
        ]
    },
    "cms_bo_apptechno": {
        "name": "CMS_BO_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "cms_asp_project": {
        "name": "CMS_ASP_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "AppPath"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Server_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Client_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefServerScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            }
        ]
    },
    "cnxusr": {
        "name": "CnxUsr",
        "columns": [
            {
                "type": "Integer",
                "name": "spid"
            },
            {
                "type": "String",
                "length": 8,
                "name": "hostprocess"
            },
            {
                "type": "Integer",
                "name": "AppSpid"
            },
            {
                "type": "String",
                "length": 3,
                "name": "IdUsr"
            },
            {
                "type": "Integer",
                "name": "Rgt"
            },
            {
                "type": "Integer",
                "name": "IdRgtPrf"
            }
        ]
    },
    "wk_dia_component": {
        "name": "WK_DIA_COMPONENT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "adg_techno_module_links": {
        "name": "ADG_TECHNO_MODULE_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            }
        ]
    },
    "histo_typattr": {
        "name": "HISTO_TYPATTR",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDTYP"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ATTRNAM"
            },
            {
                "type": "Integer",
                "name": "ATTRTYP"
            },
            {
                "type": "Integer",
                "name": "INTVAL"
            },
            {
                "type": "String",
                "length": 255,
                "name": "STRVAL"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "dia_struts_action": {
        "name": "DIA_STRUTS_ACTION",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "CLASS_ID"
            },
            {
                "type": "Integer",
                "name": "VERSION"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE"
            },
            {
                "type": "Integer",
                "name": "IS_INHERITED"
            }
        ]
    },
    "dss_object_exceptions": {
        "name": "DSS_OBJECT_EXCEPTIONS",
        "columns": [
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "dss_log_objects": {
        "name": "DSS_LOG_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_NAME"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "OBJECT_DESCRIPTION"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "OBJECT_FULL_NAME"
            },
            {
                "type": "Integer",
                "name": "OBJECT_CHECKSUM"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "treecat": {
        "name": "TreeCat",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFrom"
            },
            {
                "type": "Integer",
                "name": "IdTo"
            },
            {
                "type": "Integer",
                "name": "IdCat"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "tmp_excluded_object": {
        "name": "TMP_EXCLUDED_OBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "cms_inf_sqlsrv_accessport": {
        "name": "CMS_INF_SQLSRV_AccessPort",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Port"
            }
        ]
    },
    "cms_syb_project": {
        "name": "CMS_SYB_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            }
        ]
    },
    "dss_violation_statuses": {
        "name": "DSS_VIOLATION_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "DIAG_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "VIOLATION_STATUS"
            }
        ]
    },
    "dssapp_artifact_links": {
        "name": "DSSAPP_ARTIFACT_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "IdClr"
            },
            {
                "type": "Integer",
                "name": "IdCle"
            }
        ]
    },
    "cms_net_ldaptargetdfm": {
        "name": "CMS_NET_LDAPTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "cltudt": {
        "name": "CltUdt",
        "columns": [
            {
                "type": "Integer",
                "name": "IdUdt"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UdtNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UdtPath"
            },
            {
                "type": "String",
                "length": 38,
                "name": "UdtGUID"
            },
            {
                "type": "Integer",
                "name": "UdtClass"
            },
            {
                "type": "Integer",
                "name": "UdtProp"
            }
        ]
    },
    "in_objects": {
        "name": "IN_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "NAME_ID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "SHORT_NAME_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            }
        ]
    },
    "wk_dia_inclink": {
        "name": "WK_DIA_INCLINK",
        "columns": [
            {
                "type": "Integer",
                "name": "LINK_ID"
            },
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            }
        ]
    },
    "stat_table": {
        "name": "STAT_TABLE",
        "columns": [
            {
                "type": "Integer",
                "name": "ID"
            },
            {
                "type": "Integer",
                "name": "ROWCNT"
            },
            {
                "type": "TIMESTAMP",
                "name": "STAT_DATE"
            },
            {
                "type": "String",
                "length": 255,
                "name": "TABLE_NAME"
            }
        ]
    },
    "dia_codegroup": {
        "name": "DIA_CODEGROUP",
        "columns": [
            {
                "type": "Integer",
                "name": "Id"
            },
            {
                "type": "Integer",
                "name": "IdAbs"
            },
            {
                "type": "Integer",
                "name": "IdUsrPro"
            },
            {
                "type": "Integer",
                "name": "MetricId"
            },
            {
                "type": "Integer",
                "name": "ObjectId"
            }
        ]
    },
    "objtypstr": {
        "name": "ObjTypStr",
        "columns": [
            {
                "type": "Integer",
                "name": "ObjTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ObjTypStr"
            },
            {
                "type": "Integer",
                "name": "BrwProp"
            },
            {
                "type": "Integer",
                "name": "LngTyp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "LngStr"
            }
        ]
    },
    "dia_sc_jvobjects": {
        "name": "DIA_SC_JVOBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "IS_JAVALL"
            },
            {
                "type": "Integer",
                "name": "IS_JAVART"
            }
        ]
    },
    "tmp_dia_cppobject": {
        "name": "TMP_DIA_CPPOBJECT",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "adg_func_module_parents": {
        "name": "ADG_FUNC_MODULE_PARENTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "TREE_LEVEL"
            }
        ]
    },
    "dssapp_cls_inh_links": {
        "name": "DSSAPP_CLS_INH_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "IdClr"
            },
            {
                "type": "Integer",
                "name": "IdCle"
            }
        ]
    },
    "cms_migr_userproject": {
        "name": "CMS_MIGR_UserProject",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "String",
                "length": 1050,
                "name": "Mail"
            },
            {
                "type": "Integer",
                "name": "LocalDB_Unique_ID"
            },
            {
                "type": "Integer",
                "name": "JobType"
            }
        ]
    },
    "wk_dia_inhprstcls": {
        "name": "WK_DIA_INHPRSTCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "HIBERNATE_ID"
            },
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "idx": {
        "name": "Idx",
        "columns": [
            {
                "type": "Integer",
                "name": "IdIdx",
                "primary": True
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            },
            {
                "type": "String",
                "length": 128,
                "name": "IdxNam"
            },
            {
                "type": "Integer",
                "name": "IdTab"
            },
            {
                "type": "Integer",
                "name": "IdxNat"
            },
            {
                "type": "Integer",
                "name": "SrvTyp"
            }
        ]
    },
    "cms_am_desc_output": {
        "name": "CMS_AM_DESC_Output",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Language"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Type"
            }
        ]
    },
    "dss_portf_tree": {
        "name": "DSS_PORTF_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "SYST_ID"
            },
            {
                "type": "Integer",
                "name": "APP_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "objsrc": {
        "name": "OBJSRC",
        "columns": [
            {
                "type": "Integer",
                "name": "IDOBJ"
            },
            {
                "type": "Integer",
                "name": "IDPRO"
            },
            {
                "type": "Integer",
                "name": "IDSRC"
            }
        ]
    },
    "cms_j2ee_apptechno": {
        "name": "CMS_J2EE_AppTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "DefaultTechno_ID"
            },
            {
                "type": "Integer",
                "name": "AnaOptions_ID"
            },
            {
                "type": "Integer",
                "name": "ProdOptions_ID"
            }
        ]
    },
    "wk_dia_serialcls": {
        "name": "WK_DIA_SERIALCLS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "OBJECT_FULLNAME"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "wk_dia_mtdexcept": {
        "name": "WK_DIA_MTDEXCEPT",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTIES"
            },
            {
                "type": "Integer",
                "name": "METHOD_ID"
            },
            {
                "type": "Integer",
                "name": "METHOD_TYPE"
            },
            {
                "type": "Integer",
                "name": "EXCEPTION_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            }
        ]
    },
    "appmarq_shoringtypemodel": {
        "name": "AppMarq_ShoringTypeModel",
        "columns": [
            {
                "type": "Integer",
                "name": "ShoringTypeId"
            },
            {
                "length": 255,
                "type": "String",
                "name": "ShoringTypeName"
            },
            {
                "length": 1500,
                "type": "String",
                "name": "ShoringTypeDescription"
            }
        ]
    },
    "chgtrack": {
        "name": "ChgTrack",
        "columns": [
            {
                "type": "Integer",
                "name": "IdUsr"
            },
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Info"
            },
            {
                "type": "TIMESTAMP",
                "name": "DtInfo"
            }
        ]
    },
    "modgrp": {
        "name": "ModGrp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdMod"
            },
            {
                "type": "Integer",
                "name": "IdxModCom"
            },
            {
                "type": "Integer",
                "name": "IdGrp"
            }
        ]
    },
    "cms_udb_anaoptions": {
        "name": "CMS_UDB_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            }
        ]
    },
    "wk_dia_javainherit": {
        "name": "WK_DIA_JAVAINHERIT",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "anafncrul": {
        "name": "AnaFncRul",
        "columns": [
            {
                "type": "Integer",
                "name": "IdFncRul"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Rul"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            },
            {
                "type": "Integer",
                "name": "IdGrp"
            }
        ]
    },
    "viewer_macros": {
        "name": "VIEWER_MACROS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "CLASS_PATH"
            }
        ]
    },
    "cms_tool_varcont": {
        "name": "CMS_TOOL_VarCont",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            }
        ]
    },
    "cal_tableprefix": {
        "name": "CAL_TablePrefix",
        "columns": [
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Prefix"
            }
        ]
    },
    "wk_action_plan_preview": {
        "name": "WK_ACTION_PLAN_PREVIEW",
        "columns": [
            {
                "length": 255,
                "type": "String",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "FIRST_SNAPSHOT_DATE"
            },
            {
                "type": "TIMESTAMP",
                "name": "LAST_SNAPSHOT_DATE"
            },
            {
                "length": 255,
                "type": "String",
                "name": "USER_NAME"
            },
            {
                "type": "TIMESTAMP",
                "name": "SEL_DATE"
            },
            {
                "type": "Integer",
                "name": "PRIORITY"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "ACTION_DEF"
            }
        ]
    },
    "wk_dia_netallinherit": {
        "name": "WK_DIA_NETALLINHERIT",
        "columns": [
            {
                "type": "Integer",
                "name": "SOURCE_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "TARGET_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LEV"
            },
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            }
        ]
    },
    "wk_prop_positions_id": {
        "name": "WK_PROP_POSITIONS_ID",
        "columns": [
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "ID"
            }
        ]
    },
    "dss_app_statuses": {
        "name": "DSS_APP_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "APPLICATION_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_SNAPSHOT_ID"
            }
        ]
    },
    "cms_forms_deftechno": {
        "name": "CMS_FORMS_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "CodeViewerFilesDir"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            }
        ]
    },
    "cms_code_extractexecunit": {
        "name": "CMS_CODE_ExtractExecUnit",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "SelectFile"
            }
        ]
    },
    "cms_net_anaoptions": {
        "name": "CMS_NET_AnaOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            }
        ]
    },
    "lck": {
        "name": "Lck",
        "columns": [
            {
                "type": "Integer",
                "name": "Spid"
            },
            {
                "type": "Integer",
                "name": "IdKey"
            },
            {
                "type": "Integer",
                "name": "LckTyp"
            },
            {
                "type": "TIMESTAMP",
                "name": "LckDat"
            },
            {
                "type": "Integer",
                "name": "LckCnt"
            },
            {
                "type": "String",
                "length": 3,
                "name": "IdUsr"
            },
            {
                "type": "Integer",
                "name": "IdDbe"
            }
        ]
    },
    "anadsc": {
        "name": "AnaDsc",
        "columns": [
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "InfTyp"
            },
            {
                "type": "Integer",
                "name": "InfSubTyp"
            },
            {
                "type": "Integer",
                "name": "BlkNo"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            },
            {
                "type": "Integer",
                "name": "Prop"
            },
            {
                "type": "String",
                "length": 255,
                "name": "InfVal"
            }
        ]
    },
    "in_catattr": {
        "name": "IN_CATATTR",
        "columns": [
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ATTRNAM"
            },
            {
                "type": "Integer",
                "name": "ATTRTYP"
            },
            {
                "type": "Integer",
                "name": "INTVAL"
            },
            {
                "type": "String",
                "length": 255,
                "name": "STRVAL"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "usrprojob": {
        "name": "UsrProJob",
        "columns": [
            {
                "type": "Integer",
                "name": "IdUsrPro"
            },
            {
                "type": "Integer",
                "name": "IdJob"
            },
            {
                "type": "Integer",
                "name": "OrdNum"
            },
            {
                "type": "Integer",
                "name": "Prop"
            }
        ]
    },
    "cms_code_repo_sapextract": {
        "name": "CMS_CODE_REPO_SAPExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "cms_inf_partp_dbudb": {
        "name": "CMS_INF_PARTP_DBUDB",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 255,
                "name": "UserName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Password"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Host"
            },
            {
                "type": "Integer",
                "name": "Port"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DbName"
            }
        ]
    },
    "histo_propcat": {
        "name": "HISTO_PROPCAT",
        "columns": [
            {
                "type": "String",
                "length": 30,
                "name": "HISTO_VERSION"
            },
            {
                "type": "Integer",
                "name": "IDPROP"
            },
            {
                "type": "Integer",
                "name": "IDCAT"
            },
            {
                "type": "String",
                "length": 10,
                "name": "STATUS"
            }
        ]
    },
    "ci_no_links": {
        "name": "CI_NO_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "CALLER_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "CALLER_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "CALLER_SHORTGUID"
            },
            {
                "type": "Integer",
                "name": "CALLED_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "CALLED_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "CALLED_SHORTGUID"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "viewer_role_access": {
        "name": "VIEWER_ROLE_ACCESS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ROLE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_CATEGORY"
            },
            {
                "type": "Integer",
                "name": "ACCESS_MODE"
            }
        ]
    },
    "dss_log_metric_results": {
        "name": "DSS_LOG_METRIC_RESULTS",
        "columns": [
            {
                "type": "Integer",
                "name": "SITE_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "METRIC_VALUE_INDEX"
            },
            {
                "type": "Numeric",
                "name": "METRIC_NUM_VALUE"
            },
            {
                "type": "String",
                "length": 1000,
                "name": "METRIC_CHAR_VALUE"
            },
            {
                "type": "Integer",
                "name": "METRIC_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "cms_code_repo_sqlserverextract": {
        "name": "CMS_CODE_REPO_SqlServerExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "typcat": {
        "name": "TypCat",
        "columns": [
            {
                "type": "Integer",
                "name": "IdTyp"
            },
            {
                "type": "Integer",
                "name": "IdCatParent"
            },
            {
                "type": "Integer",
                "name": "IsCatProp"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "dssapp_tmp_objects": {
        "name": "DSSAPP_TMP_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            }
        ]
    },
    "dss_diagdetails": {
        "name": "DSS_DIAGDETAILS",
        "columns": [
            {
                "type": "Integer",
                "name": "DIAG_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Numeric",
                "name": "DIAG_VALUE"
            },
            {
                "type": "Integer",
                "name": "DIAG_OBJ"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "DIAG_TEXT"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "CONTEXT_ID"
            }
        ]
    },
    "amt_prjrel": {
        "name": "AMT_PRJREL",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "OBJECT_KIND"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_INT"
            }
        ]
    },
    "cms_forms_include": {
        "name": "CMS_FORMS_Include",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Path"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "Name"
            }
        ]
    },
    "cms_am_parm_fltlstparams": {
        "name": "CMS_AM_PARM_FltLstParams",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "ParamIndex"
            },
            {
                "type": "Integer",
                "name": "Model_ID"
            },
            {
                "type": "Integer",
                "name": "DefValue"
            }
        ]
    },
    "viewer_data_field_types": {
        "name": "VIEWER_DATA_FIELD_TYPES",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "PARENT_DATA_TYPE_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "FIELD_TYPE_ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "SQL_MAPPING_NAME"
            },
            {
                "length": 200,
                "type": "String",
                "name": "XML_MAPPING_NAME"
            },
            {
                "type": "Integer",
                "name": "IS_KEY"
            },
            {
                "type": "Integer",
                "name": "IS_CLASS_PATH"
            },
            {
                "type": "Integer",
                "name": "JOIN_INDEX"
            },
            {
                "type": "Integer",
                "name": "JOIN_OFFSET"
            },
            {
                "length": 200,
                "type": "String",
                "name": "JOIN_DATA_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "FIELD_LENGTH"
            },
            {
                "type": "Integer",
                "name": "FIELD_PRECISION"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "DEFAULT_VALUE"
            },
            {
                "type": "Integer",
                "name": "C_OFFSET"
            }
        ]
    },
    "in_date_properties": {
        "name": "IN_DATE_PROPERTIES",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "PROPERTY_OFFSET"
            },
            {
                "type": "TIMESTAMP",
                "name": "PROPERTY_DATE"
            }
        ]
    },
    "rgtprf": {
        "name": "RgtPrf",
        "columns": [
            {
                "type": "Integer",
                "name": "IdRgtPrf"
            },
            {
                "type": "String",
                "length": 255,
                "name": "RgtPrfNam"
            },
            {
                "type": "Integer",
                "name": "Rgt"
            }
        ]
    },
    "cms_vb_project": {
        "name": "CMS_VB_Project",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "Integer",
                "name": "ReferencesOnly"
            },
            {
                "type": "Integer",
                "name": "DefaultHandling"
            }
        ]
    },
    "efp_objects_statuses": {
        "name": "EFP_OBJECTS_STATUSES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "PREVIOUS_SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_STATUS"
            },
            {
                "type": "Integer",
                "name": "IS_ART"
            },
            {
                "type": "Numeric",
                "name": "COST_COMPLEXITY"
            },
            {
                "type": "Integer",
                "name": "TECHNO_TYPE_ID"
            }
        ]
    },
    "cms_code_repo_mfextract": {
        "name": "CMS_CODE_REPO_MFExtract",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "genico": {
        "name": "GenIco",
        "columns": [
            {
                "type": "Integer",
                "name": "IdIco"
            },
            {
                "type": "Integer",
                "name": "NumLin"
            },
            {
                "name": "IcoDat"
            }
        ]
    },
    "cms_j2ee_analysis": {
        "name": "CMS_J2EE_Analysis",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "Resource_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProjectEntry"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerProjectName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "analyzerLegacyProjectName"
            },
            {
                "type": "Integer",
                "name": "Active"
            },
            {
                "type": "Integer",
                "name": "Project_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecTag"
            },
            {
                "type": "Integer",
                "name": "CodeSize"
            },
            {
                "type": "Integer",
                "name": "IsPivot"
            },
            {
                "type": "Integer",
                "name": "IsExtern"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecStatus"
            },
            {
                "type": "TIMESTAMP",
                "name": "ExecDate"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecCfgChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecDepChk"
            },
            {
                "type": "String",
                "length": 255,
                "name": "ExecVersion"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ExecLog"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Java_FileExtensions"
            },
            {
                "type": "String",
                "length": 255,
                "name": "XML_FileExtensions"
            },
            {
                "type": "Integer",
                "name": "XML_AsJava"
            },
            {
                "type": "Integer",
                "name": "PROP_AsJava"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "WEB_Descriptor"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JSP_FileExtensions"
            },
            {
                "type": "Integer",
                "name": "JSP_AsJava"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Client_FileExtensions"
            },
            {
                "type": "Integer",
                "name": "Client_AsJava"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Java_Version"
            },
            {
                "type": "String",
                "length": 255,
                "name": "DefClientScriptingLng"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JSP_Servlet_StdVer"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Hibernate_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Struts_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Spring_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Jsf_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CommonLogging_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Dom4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "JUnit_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Log4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Mx4J_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Cics_Usage"
            },
            {
                "type": "String",
                "length": 255,
                "name": "WBS_Usage"
            },
            {
                "type": "Integer",
                "name": "EnvProfWBS"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Ejb_Usage"
            },
            {
                "type": "Integer",
                "name": "EnvProfEJB"
            }
        ]
    },
    "in_code_sources": {
        "name": "IN_CODE_SOURCES",
        "columns": [
            {
                "type": "Integer",
                "name": "SESSION_ID"
            },
            {
                "type": "Integer",
                "name": "SOURCE_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "SOURCE_KIND"
            },
            {
                "type": "Integer",
                "name": "SOURCE_CRC"
            },
            {
                "type": "Text",
                "name": "SOURCE_CODE"
            }
        ]
    },
    "pbopbl": {
        "name": "PboPbl",
        "columns": [
            {
                "type": "Integer",
                "name": "IdPbl",
                "primary": True
            },
            {
                "type": "String",
                "length": 255,
                "name": "PblNam"
            },
            {
                "type": "Integer",
                "name": "PblClass"
            },
            {
                "type": "Integer",
                "name": "PblProp"
            }
        ]
    },
    "dss_func_module_links": {
        "name": "DSS_FUNC_MODULE_LINKS",
        "columns": [
            {
                "type": "Integer",
                "name": "MODULE_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            }
        ]
    },
    "cms_tool_kbupdate_externalmode": {
        "name": "CMS_TOOL_KbUpdate_ExternalMode",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ProgName"
            },
            {
                "type": "Integer",
                "name": "ProgWait"
            }
        ]
    },
    "cms_tool_kbupdate_sqlmode": {
        "name": "CMS_TOOL_KbUpdate_SQLMode",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            }
        ]
    },
    "ci_str_properties": {
        "name": "CI_STR_PROPERTIES",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "String",
                "length": 1015,
                "name": "OBJECT_GUID"
            },
            {
                "type": "String",
                "length": 600,
                "name": "OBJECT_SHORTGUID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "PROP_NAME"
            },
            {
                "type": "Integer",
                "name": "ORDER_NUMBER"
            },
            {
                "type": "String",
                "length": 255,
                "name": "VALUE"
            },
            {
                "type": "Integer",
                "name": "ERROR_ID"
            }
        ]
    },
    "cms_ora_deftechno": {
        "name": "CMS_ORA_DefTechno",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "MaxMem"
            },
            {
                "type": "Integer",
                "name": "LinksToPkgSubObjects"
            }
        ]
    },
    "genapp": {
        "name": "GenApp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdApp"
            },
            {
                "type": "String",
                "length": 240,
                "name": "AppNam"
            },
            {
                "type": "String",
                "length": 255,
                "name": "AppLib"
            },
            {
                "type": "String",
                "length": 250,
                "name": "Path"
            },
            {
                "type": "Integer",
                "name": "AppTyp"
            }
        ]
    },
    "cms_j2ee_xpathtargetdfm": {
        "name": "CMS_J2EE_XPathTargetDFM",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Dataflow_ID"
            },
            {
                "type": "String",
                "length": 255,
                "name": "FullName"
            },
            {
                "type": "String",
                "length": 255,
                "name": "CreationContext"
            }
        ]
    },
    "dss_work_objects": {
        "name": "DSS_WORK_OBJECTS",
        "columns": [
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_TYPE_ID"
            },
            {
                "length": 255,
                "type": "String",
                "name": "OBJECT_NAME"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "OBJECT_DESCRIPTION"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "OBJECT_FULL_NAME"
            },
            {
                "type": "Integer",
                "name": "OBJECT_CHECKSUM"
            }
        ]
    },
    "cms_j2ee_archivefolder": {
        "name": "CMS_J2EE_ArchiveFolder",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "ClassPath"
            },
            {
                "type": "Integer",
                "name": "Recursive"
            }
        ]
    },
    "amt_refcrc": {
        "name": "AMT_REFCRC",
        "columns": [
            {
                "type": "Integer",
                "name": "EXTERNAL_ID"
            },
            {
                "type": "Integer",
                "name": "INTERNAL_ID"
            },
            {
                "type": "String",
                "length": 1,
                "name": "STATUS"
            },
            {
                "type": "Integer",
                "name": "CRC"
            }
        ]
    },
    "dss_tree_info": {
        "name": "DSS_TREE_INFO",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "LINK_TYPE_ID"
            },
            {
                "type": "Integer",
                "name": "TREE_LEVEL"
            },
            {
                "type": "Integer",
                "name": "TREE_LEFT_POSITION"
            },
            {
                "type": "Integer",
                "name": "TREE_RIGHT_POSITION"
            }
        ]
    },
    "cms_code_repo_bo": {
        "name": "CMS_CODE_REPO_BO",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "String",
                "length": 255,
                "name": "Object_Name"
            },
            {
                "type": "Integer",
                "name": "Application_ID"
            },
            {
                "type": "Integer",
                "name": "Container_ID"
            },
            {
                "type": "String",
                "length": 1024,
                "name": "RootPath"
            },
            {
                "type": "Integer",
                "name": "Deploy"
            },
            {
                "type": "Integer",
                "name": "IsMigrated"
            }
        ]
    },
    "viewer_actions": {
        "name": "VIEWER_ACTIONS",
        "columns": [
            {
                "length": 200,
                "type": "String",
                "name": "ID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "REFID"
            },
            {
                "length": 200,
                "type": "String",
                "name": "NAME"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "ICON_URL"
            },
            {
                "length": 1000,
                "type": "String",
                "name": "CLASS_PATH"
            }
        ]
    },
    "objpos": {
        "name": "ObjPos",
        "columns": [
            {
                "type": "Integer",
                "name": "IdObj"
            },
            {
                "type": "Integer",
                "name": "IdObjRef"
            },
            {
                "type": "Integer",
                "name": "PosMode"
            },
            {
                "type": "Integer",
                "name": "Info1"
            },
            {
                "type": "Integer",
                "name": "Info2"
            },
            {
                "type": "Integer",
                "name": "Info3"
            },
            {
                "type": "Integer",
                "name": "Info4"
            },
            {
                "type": "Integer",
                "name": "Prop"
            },
            {
                "type": "Integer",
                "name": "BlkNo"
            }
        ]
    },
    "cms_vb_prodoptions": {
        "name": "CMS_VB_ProdOptions",
        "columns": [
            {
                "type": "Integer",
                "name": "Object_ID"
            },
            {
                "type": "TIMESTAMP",
                "name": "Internal_Timestamp"
            },
            {
                "type": "Integer",
                "name": "Techno_ID"
            },
            {
                "type": "Integer",
                "name": "UseInferenceEngine"
            },
            {
                "type": "Integer",
                "name": "LimitString"
            }
        ]
    },
    "typprop": {
        "name": "TypProp",
        "columns": [
            {
                "type": "Integer",
                "name": "IdTyp"
            },
            {
                "type": "Integer",
                "name": "IdProp"
            },
            {
                "type": "String",
                "length": 10,
                "name": "Status"
            }
        ]
    },
    "apm_system_tree": {
        "name": "APM_SYSTEM_TREE",
        "columns": [
            {
                "type": "Integer",
                "name": "SNAPSHOT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_PARENT_ID"
            },
            {
                "type": "Integer",
                "name": "OBJECT_ID"
            },
            {
                "type": "Integer",
                "name": "PARENT_GROUP"
            },
            {
                "type": "Integer",
                "name": "OBJECT_GROUP"
            },
            {
                "type": "Integer",
                "name": "TREE_LEVEL"
            }
        ]
    }
}