	import string
	from time import gmtime, strftime

	class cdk_struct:
		app_name =""
		structname =""
		structsize = 2
		myelement = []
		mytype =[]
		mysize =[]

		storage = "EEPROM"
		startAddress = 0

		output = "output.c"
		FILE_OUT = open(output,'w')

		def __init__(self):
			self.app_name =""
			self.structname =""
			self.structsize = 2
			self.myelement = []
			self.mytype =[]
			self.mysize =[]
			self.storage = "EEPROM"
			self.startAddress = 0
			self.output = "output.c"
			self.FILE_OUT = open(self.output,'a')

		def out_newcreate(self):
			current = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			self.FILE_OUT = open(self.output,'w')
			self.FILE_OUT.write("//Create date: " + current +"\n")
			self.FILE_OUT.close();
			self.FILE_OUT = open(self.output,'a')

		def out_close(self):
			self.FILE_OUT.close()

		def out_print(self,message):
			self.FILE_OUT.write(message)

		def createapp(self,name):
			self.app_name = name

		def createname(self, name):
			self.structname = name
		
		def setaddress(self,address):
			self.startAddress = address

		def getSize(self):
			struct_size = 0
			for i in range(len(self.myelement)):
				struct_size += self.mysize[i]

			if (self.structsize > 1):
				struct_size = struct_size * self.structsize

			return struct_size

		def addelement(self, pelement, ptype, psize):
			self.myelement.append(pelement)
			self.mytype.append(ptype)
			self.mysize.append(psize)

		def get_struct_name(self):
			template = "r_dlms_storage_<app>_<name>_t"
			STRUCT_NAME = template
			STRUCT_NAME = STRUCT_NAME.replace("<app>", self.app_name)
			STRUCT_NAME = STRUCT_NAME.replace("<name>", self.structname)
			return STRUCT_NAME

		def printstruct(self):
			template = """
	typedef struct tag_<struct>
	{<element>
	} <struct>;
	"""
			MyStr = template.replace("<app_name>", self.app_name)
			MyStr = MyStr.replace("<struct>", self.get_struct_name())
			
			MyStrElement = ""
			for i in range(len(self.myelement)):
				MyStrArray = ""
				if self.mysize[i] != 1:
					MyStrArray = "[" + str(self.mysize[i]) + "]"

				MyStrElement += "\n    " + self.mytype[i] + " " + self.myelement[i] + MyStrArray + ","

			MyStr = MyStr.replace("<element>", MyStrElement) + "\n"
			self.out_print(MyStr)

		def print_format(self):
			template_base_address = """STORAGE_<storage>_DLMS_<app>_<name>_ADDR"""
			template_base_size = """STORAGE_<storage>_DLMS_<app>_<name>_SIZE"""

			template = """#define STORAGE_<storage>_DLMS_<app>_<name>_ADDR	(<address>)
	#define STORAGE_<storage>_DLMS_<app>_<name>_SIZE	(<size>)
	"""
			template_ID_address = """#define STORAGE_<storage>_DLMS_<app>_<name>_ADDR_ID(index) ( (<structsize> * index) + STORAGE_<storage>_DLMS_<app>_<name>_ADDR)\n\n"""


			MEMORY_MAP = ""

			template = template.replace("<storage>",self.storage.upper())
			template = template.replace("<app>", self.app_name.upper())

			template_ID_address = template_ID_address.replace("<storage>",self.storage.upper())
			template_ID_address = template_ID_address.replace("<app>", self.app_name.upper())

			#struct name
			STRUCT_NAME = self.get_struct_name()

			STRUCT_ADDRESS = template_base_address
			STRUCT_ADDRESS = STRUCT_ADDRESS.replace("<storage>",self.storage.upper())
			STRUCT_ADDRESS = STRUCT_ADDRESS.replace("<app>", self.app_name.upper())
			STRUCT_ADDRESS = STRUCT_ADDRESS.replace("<name>", self.structname.upper())
			
			STRUCT_SIZE = template_base_size
			STRUCT_SIZE = STRUCT_SIZE.replace("<storage>",self.storage.upper())
			STRUCT_SIZE = STRUCT_SIZE.replace("<app>", self.app_name.upper())
			STRUCT_SIZE = STRUCT_SIZE.replace("<name>", self.structname.upper())

			# print struct
			str_comment = """/**********************************************/\n/* Group Name: <groupname> */\n"""
			str_comment = str_comment.replace("<groupname>", self.structname)
			str_struct = str_comment + template

			if (self.structsize > 1):
				str_struct += template_ID_address

			str_struct = str_struct.replace("<name>", self.structname.upper())
			str_struct = str_struct.replace("<address>", str(self.startAddress).upper())
			str_struct = str_struct.replace("<structsize>", STRUCT_SIZE)

			struct_size = 0
			for i in range(len(self.myelement)):
				struct_size += self.mysize[i]
			str_struct = str_struct.replace("<size>", "sizeof(" + self.get_struct_name() + ")")
			
			#print element
			str_element = ""
			for i in range(len(self.myelement)):
				str_comment = "/* <comment_name> */\n"

				temp_str = str_comment + template

				if (self.structsize > 1):
					temp_str += template_ID_address

				temp_str = temp_str.replace("<structName>", STRUCT_NAME)
				temp_str = temp_str.replace("<structsize>", STRUCT_SIZE)

				temp_str = temp_str.replace("<name>", self.structname.upper() + "_" + self.myelement[i].upper())
				temp_str = temp_str.replace("<size>", str(self.mysize[i]).upper())
				str_offset = "<baseaddress> + offsetof(<structName>, <element>)"
				str_offset = str_offset.replace("<baseaddress>", STRUCT_ADDRESS)
				str_offset = str_offset.replace("<structName>", STRUCT_NAME)

				str_offset = str_offset.replace("<element>", self.myelement[i])

				temp_str = temp_str.replace("<address>", str_offset)
				temp_str = temp_str.replace("<comment_name>", self.myelement[i])

				str_element += temp_str

			MEMORY_MAP += str_struct
			MEMORY_MAP += str_element

			self.out_print(MEMORY_MAP)

		def gen(self):
			self.printstruct()
			self.print_format()





