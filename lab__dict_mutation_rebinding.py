def add_entry(d):
    d["city"]="Delhi"

def reassign_dict(d):
    d={"status":"reassigned","count":100}    


test_dict_1={"name":"John","age":30}
print("Initial Dictionary: ",test_dict_1)
add_entry(test_dict_1)
print("After adding entry: ",test_dict_1)

test_dict_2={"name":"John","age":30}
print("Initial Dictionary: ",test_dict_2)
reassign_dict(test_dict_2)
print("After reassigning dictionary: ",test_dict_2)