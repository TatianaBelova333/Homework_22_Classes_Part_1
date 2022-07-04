csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(data):
    lines = data.split('\n')
    return [{"name": line.split(";")[0], "age": int(line.split(";")[1])} for line in lines]


def _sort(data):
    sorted_data = sorted(data, key=lambda x: x["age"])
    return sorted_data


def _filter(data):
    filtered_data = list(filter(lambda x: x["age"] >= 10, data))
    return filtered_data


def get_users_list(data=csv):
    data = _read(data)
    data = _sort(data)
    return _filter(data)


if __name__ == "__main__":
    print(get_users_list())