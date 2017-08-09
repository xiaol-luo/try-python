import configparser

STRING_EMPTY = ""

class Excel2CsvDescript(object):
    def __init__(self, owner, **kwargs):
        self._owner = owner
        self.file_path = STRING_EMPTY
        self.sheet_name = STRING_EMPTY
        self.out_csv_file_path = STRING_EMPTY
        self.class_name = STRING_EMPTY
        self.out_cs_file_path = STRING_EMPTY
        self.out_cpp_file_path = STRING_EMPTY
        self.out_lua_file_path = STRING_EMPTY
        return super().__init__(**kwargs)
    
    def Init(self, cfg_praser):
        file_path = env_section["file_path"]
        sheet_name = env_section["sheet_name"]
        out_csv_file_path = env_section["out_csv_file_path"]
        class_name = env_section["class_name"]
        out_cs_file_path = env_section["out_cs_file_path"]
        out_cpp_file_path = env_section["out_cpp_file_path"]
        out_lua_file_path = env_section["out_lua_file_path"]
        return True

class ConfigListDescript(object):
    ENV_SECTION = "env"
    EXCEL2CSV_REGEX_PATTERN = r'^excel2csv-.*'

    def __init__(self, **kwargs):
        self.excel_dir = STRING_EMPTY
        self.out_config_dir = STRING_EMPTY
        self.out_code_dir = STRING_EMPTY
        self.excel2csv_descs = []
        return super().__init__(**kwargs)

    def Init(self, cfg_praser):
        for section in cfg_praser.sections():
            print("{0}".format(section))
        if not cfg_praser.has_section(ConfigListDescript.ENV_SECTION):
            return False
        env_section = cfg_praser[ConfigListDescript.ENV_SECTION]
        excel_dir = env_section["excel_dir"]
        out_config_dir = env_section["out_config_dir"]
        out_code_dir = env_section["out_code_dir"]
        self.excel2csv_descs = []
        for section_name in cfg_praser.sections:
            if not re.match(ConfigListDescript.EXCEL2CSV_REGEX_PATTERN, section_name):
                continue
            excel2csv_desc = Excel2CsvDescript()
            if not excel2csv_desc.Init(cfg_praser[section_name]):
                log.error("cfg_path - {0} {1} error {2}".format(cfg_path, section_name, cfg_praser.sections[section_name]))
            else:
                self.excel2csv_descs.append(excel2csv_desc)
        return True