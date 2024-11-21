from typing import Dict, Union

DeepNestedDict = Dict[str, Union[str, 'DeepNestedDict']]

# https://www.tryexponent.com/practice/prepare/flatten-a-dictionary
def flatten_dictionary_recursive(dictionary: DeepNestedDict) -> Dict[str, str]:
    result = {}
    def flatten(obj: Union[DeepNestedDict, str], parentKey: str = ""):
        if (isinstance(obj, str)):
            result[parentKey] = obj
            return

        for key, value in obj.items():
            if not parentKey:
                nextKey = key
            elif not key:
                nextKey = parentKey
            else:
                nextKey = f"{parentKey}.{key}"
            flatten(value, nextKey)

    flatten(dictionary)
    return result

def flatten_dictionary(dictionary: DeepNestedDict) -> Dict[str, str]:
    result = {}
    processing = [("", dictionary)]

    while processing:
        nextProcessing = []
        for parentKey, obj in processing:
            if isinstance(obj, str):
                result[parentKey] = obj
                continue

            for key, val in obj.items():
                if not parentKey:
                    nextKey = key
                elif not key:
                    nextKey = parentKey
                else:
                    nextKey = f"{parentKey}.{key}"
                nextProcessing.append((nextKey, val))

        processing = nextProcessing

    return result

# debug your code below
dict_input = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

print(flatten_dictionary(dict_input))
