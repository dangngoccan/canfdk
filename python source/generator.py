#! python3

class r_gen:
    import json
    import os.path
    from string import Template

    path_input = "user_setting.xml"
    path_template = "template.c"
    path_output_dir = "out"
    path_output_type = ".c"

    path_current = os.path.dirname(__file__)
    #path_output = os.path.join(path_current,"/out")

    def gen(self):
        # Load user setting
        import os
        import os.path
        # from pathlib import Path
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.path_input)
        root = tree.getroot()

        path_output = os.path.join(self.path_current, "out")

        for configure in root.findall('configure'):
            configureName = configure.find('configureName').text
            configureName.replace(" ", "_")
            # Create output file
            dirout = os.path.abspath(path_output)

            if not os.path.exists(dirout):
                os.makedirs(dirout)

            pathout = os.path.abspath(os.path.join(path_output, configureName + self.path_output_type))
            file_output = open(pathout, 'w')
            # Load template
            file_template = open(self.path_template, 'r')
            for line in file_template:
                # ONE line update
                strb = line
                for items in configure.findall('configuredvalue'):
                    #print(items.tag)
                    updater = items.text
                    repl = updater.split('=')
                    maker = '<' + repl[0] + '>'
                    value = repl[1]
                    print(maker)
                    print(value)
                    strb = strb.replace(maker, value)
                file_output.write(strb)
            file_output.close()
            file_template.close()

