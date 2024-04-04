from src.psychlua import PsychLuaObjectGenerator as ObjectGenerator # Simplify
import os

def export(filepath:str, watermark:bool = True):
    # idk
    parse = ObjectGenerator(filepath)
    parse.generate(watermark)

    # If there is an error here it will show it
    try:
        os.mkdir("./output")
    except OSError as e:
        pass

    # create files with the code
    for i, v in enumerate(parse.codes):
        stageid = list(parse.content.keys())
        outputfile = open(f'output/{stageid[i]}.lua', "w")
        outputfile.write(v)