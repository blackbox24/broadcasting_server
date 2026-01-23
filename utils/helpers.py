import json

def read_file(file):
    data = {}
    with open(file, "r+") as f:
        try:
            data = json.load(f)
            print(data)
        except json.decoder.JSONDecodeError as e:
            json.dump({},f)

    return data

def write_file(file, users):
    with open(file, "w") as f:
        # try:
        #     data = read_file(file)
        #     data['users'].append(user)
            
        # except KeyError:
        data = {"users": users}
        json.dump(
            data,
            f,
            indent=2
        )