from MegaUpBypass.deobfuscate import deobuscate
from OUOBypass.ouo_bypass import ouo_bypass

from re import search

from pythonmonkey import eval
from requests import get

if __name__ == "__main__":
    output = ouo_bypass(url=input("Enter ouo.io or ouo.press url: "))
    print(f"Original: {output[0]}")
    print(f"Bypassed: {output[1]}")

    response = get(url=output[1]).text
    rgx = search(r"DeObfuscate_String_and_Create_Form_With_Mhoa_URL(.*);", response)
    if rgx:
        cleaned_one = rgx.group(0).replace("DeObfuscate_String_and_Create_Form_With_Mhoa_URL(", "")
        cleaned_two = cleaned_one.replace(");", "")

        items = cleaned_two.split(", ")
        new_items = [item.replace("'", "") for item in items]
        
        eval(deobuscate)
        js_de = eval("deobfuscate")

        returned = js_de(new_items[0], new_items[1], new_items[2], new_items[3])
        id_url = returned["0"].replace("undefined", "").replace("+", "%2B").replace("=", "%3D")
        id_filename = returned["1"].replace(" ", "+")
        id_filesize = returned["2"].replace(" ", "+")

        print(f"https://download.megaup.net/?idurl={id_url}&idfilename={id_filename}&idfilesize={id_filesize}")
    else:
        print("nope")
