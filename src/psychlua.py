import yaml

class PsychLuaObjectGenerator:
    fileext:str = ".yaml"
    codes:list = []
    content:dict = {}

    def __init__(self, filepath:str) -> None:
        with open(filepath + self.fileext) as file:
            self.content = yaml.safe_load(file)

    def generate(self, watermark:bool = True):
        for e in list(self.content.keys()):
            this_code:str = ""
            if watermark:
                this_code += f'-- generated with YAML to Psych Object' + '\n'
                this_code += f'-- ID: {e}' + '\n\n'
                
            for i in self.content[e]:
                yate:dict = i

                if yate["anims"] != []:
                    this_code += f'makeAnimatedLuaSprite("{yate["tag"]}","{yate["img"]}",{yate["pos"][0]},{yate["pos"][1]})' + '\n'
                    for anim in yate["anims"]:
                        if anim["indices"] != []:
                            indices:str = ""
                            for order, indice in enumerate(anim["indices"]):
                                indices += str(indice) + ('' if order == len(anim["indices"]) - 1 else ',')
                            this_code += f'addAnimationByIndices("{yate["tag"]}","{anim["name"]}","{anim["prefix"]}","{indices}",{anim["framerate"]},{str(anim["loop"]).lower()})' + '\n'
                        else:
                            this_code += f'addAnimationByPrefix("{yate["tag"]}","{anim["name"]}","{anim["prefix"]}",{anim["framerate"]},{str(anim["loop"]).lower()})' + '\n'
                else:
                    this_code += f'makeLuaSprite("{yate["tag"]}","{yate["img"]}",{yate["pos"][0]},{yate["pos"][1]})' + '\n'
                this_code += f'addLuaSprite("{yate["tag"]}")' + '\n\n'
            this_code = this_code.strip()    

            self.codes.append(this_code)
