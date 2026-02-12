class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}

        # looping over the list of strings and split the string by spaces 
        for string in paths:
            parts = string.split()
            folder = parts[0] # the root path is the first element

            # we loop on the rest of the parts list so to separate the file name and the content inside it
            for i in range(1, len(parts)):
                file_name, content = parts[i].split("(")
                content = content[:-1]


                # then aim to create a hashmap to store the content as a key and the full path as a value in a list 
                full_path = folder + "/" + file_name

                if content not in d:
                    d[content] = []
                d[content].append(full_path)

        # return d

        return [v for k,v in d.items() if len(v) > 1]



        