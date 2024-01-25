import pprint

json_data = {
    'project': {
        'name': 'mermaid',
        'datetime': '2024-02-01',
        'shot': {
            'EP0001': {
                'EP0001_0010': {
                    'fps': 24,
                    'frange': [1001, 1100],
                    'author': ['anon', 'aa'],
                    'filepath': {
                        'hipfile': '/home/rapa/down',
                        'nkfile': '/home/rapa/nk',
                    }
                }
            },
            'EP0002': {
                'EP002_0010': {
                    'fps': 24,
                    'frange': [1001, 1050],
                    'author': 'anon',
                }
            },
        }
    }
}
def json_modify_easy(j_data, path: list, c_data) -> None:
    if isinstance(j_data, dict):
        for k1, v1 in j_data.items():
            if k1 == path[0]: #
                if len(path) == 1: # 최종 키값 도달하면 데이터 바꾸기
                    j_data[k1]= c_data
                    return
                json_modify_easy(v1, path[1:], c_data) # 0번 키값 찾으면 그거 빼고 return

    return j_data
path = []
chg_data = [1001,1,200]
a = json_modify_easy(json_data, ['project','shot','EP0002','EP002_0010','author'], chg_data)
print('1차 >> ')
pprint.pprint(a)