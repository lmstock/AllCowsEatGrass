bestiary = {
    'meatzuxa': {'_id': "ObjectId('64090b9ff4745ace84b0dea3')", 'species_type': 'meatzuxa', 'head': 'oval', 'size': 'large', 'body_type': 'soft tissued', 'species_img': '15', 'rest': [320, 320], 'sleep_duration': 550.0, 'rest_gain': 0.58, 'base_fatigue': -0.71, 'satiety': [100, -1, 100], 'hostility': [100, 100], 'health': [100, 100], 'energy': [100, 100], 'speed': 77, 'fov': 1000},
    'oweh': {'_id': "ObjectId('64090b9ff4745ace84b0dea4')", 'species_type': 'oweh', 'head': 'oval', 'size': 'small', 'body_type': 'soft tissued', 'species_img': '37', 'rest': [170, 170], 'sleep_duration': 460.0, 'rest_gain': 0.37, 'base_fatigue': -0.31, 'satiety': [100, -1, 100], 'hostility': [100, 100], 'health': [100, 100], 'energy': [100, 100], 'speed': 68, 'fov': 1000},
    'ze': {'_id': "ObjectId('64090b9ff4745ace84b0dea5')", 'species_type': 'ze', 'head': 'bald', 'size': 'large', 'body_type': 'soft tissued', 'species_img': '39', 'rest': [190, 190], 'sleep_duration': 250.0, 'rest_gain': 0.76, 'base_fatigue': -0.25, 'satiety': [100, -1, 100], 'hostility': [100, 100], 'health': [100, 100], 'energy': [100, 100], 'speed': 75, 'fov': 1000},
    'utlo': {'_id': "ObjectId('64090b9ff4745ace84b0dea6')", 'species_type': 'utlo', 'head': 'segmented', 'size': 'large', 'body_type': 'segmented with a head, thorax, and abdomen', 'species_img': '9', 'rest': [320, 320], 'sleep_duration': 440.0, 'rest_gain': 0.73, 'base_fatigue': -0.57, 'satiety': [100, -1, 100], 'hostility': [100, 100], 'health': [100, 100], 'energy': [100, 100], 'speed': 70, 'fov': 1000}
    }

def get_headers():
    headers = []
    sample = []
    for k in bestiary.keys():
        sample = []
        sample.append(k)
    for l in bestiary[sample[0]].keys():
        headers.append(l)
    return headers

def get_rows():
    rows = []
    for v in bestiary.values():
        row = []
        for i in v.values():
            row.append(i)
        rows.append(row)
    return rows


headers = get_headers()
print (headers)

# rows = get_rows()
# print(rows)
    