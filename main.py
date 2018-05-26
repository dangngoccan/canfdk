import ccore

start_address = 0

gen_struct = ccore.cdk_struct()
gen_struct.out_newcreate()

gen_struct = ccore.cdk_struct()
gen_struct.createapp("name")
gen_struct.setaddress(start_address)
gen_struct.createname("plate")
gen_struct.addelement("id", "uint8_t", 16)
gen_struct.addelement("MFY", "uint8_t", 4)
gen_struct.gen()
start_address += gen_struct.getSize()
gen_struct.out_close()

gen_struct = ccore.cdk_struct()
gen_struct.createapp("tod")
gen_struct.setaddress(start_address)
gen_struct.createname("season")
gen_struct.addelement("name", "uint8_t", 16)
gen_struct.addelement("rtc", "uint8_t", 12)
gen_struct.addelement("week_name", "uint8_t", 16)
gen_struct.gen()
start_address += gen_struct.getSize()
gen_struct.out_close()

gen_struct = ccore.cdk_struct()
gen_struct.createapp("tod")
gen_struct.setaddress(start_address)
gen_struct.createname("season_passive")
gen_struct.addelement("name", "uint8_t", 16)
gen_struct.addelement("rtc", "uint8_t", 12)
gen_struct.addelement("week_name", "uint8_t", 16)
gen_struct.gen()
start_address += gen_struct.getSize()
gen_struct.out_close()
