class Solution:
    def interpret(self, command: str) -> str:
        return_string = ""
        tmp=""
        for each in command:
            if each=="G":
                return_string+="G"
                tmp =""
            else:
                tmp+=each
                if tmp =="()":
                    return_string+="o"
                    tmp=""
                if tmp =="(al)":
                    return_string+="al"
                    tmp=""
        return return_string
        # command=command.replace("()","o")
        # command=command.replace("(al)","al")
        # return command