import requests
from datetime import datetime
from pprint import pprint as pp
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


domain = "https://api.vk.com/method"
access_token = '0050006975860ca3ef99dbc9a6e734c9018dfead63e24866b3a450c0b01d47f5848f7ea732f2182b838ee'
# user_id = 21631774

# query_params = {
#     'domain' : domain,
#     'access_token': access_token,
#     'user_id': user_id,
#     'fields': 'bdate'
# }

# query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**query_params)
# response = requests.get(query)


def age_predict(user_id):
    assert isinstance(user_id, int), "user_id must be positive integer"
    query_params = {
    'domain' : domain,
    'access_token': access_token,
    'user_id': user_id,
    'fields': 'bdate'
    }

    query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**query_params)
    response = requests.get(query)

    today = datetime.now().year # Текущий год для вычисления возраста
    age_list = [] # Список для хранения дат рождений

    for person in response.json()['response']['items']:
        try:
            # age_list = [person['bdate'][-4:] for person in response.json()['response']['items'] if len(person['bdate']) > 5]
            if len(person['bdate']) > 5:
                age_list.append(int(person['bdate'][-4:]))
                # print("{} {} bday: {}".format(person['first_name'], person['last_name'], person['bdate'][-4:]))
            # print(person['bday'])
        except KeyError:
            # print('No bday in {}'.format(person['id']))
            pass

    avg = lambda x: sum(x) / len(x)
    return today - avg(age_list)

def build_graphic(user_id, offset=0, count=20):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    query_params = {
        'domain' : domain,
        'access_token': access_token,
        'user_id': user_id,
        'offset': offset,
        'count': count
        }
    query = "{domain}/messages.getHistory?access_token={access_token}&user_id={user_id}&offset={offset}&count={count}&v=5.53".format(**query_params)
    response = requests.get(query)

    messages = response.json()['response']['items']

    def count_dates_from_messages(messages):
        freq = {}
        for message in messages:
            date = datetime.fromtimestamp(message['date']).strftime("%Y-%m-%d")
            if date in freq:
                freq[date] += 1
            else:
                freq[date] = 1

        return freq

    dates_dict = count_dates_from_messages(messages)

    data = [go.Scatter(x=sorted(dates_dict.keys()), y=[dates_dict[key] for key in sorted(dates_dict.keys())])]
    py.iplot(data)


# print(build_graphic(79150488, 0, 200))
print(age_predict(21631774))









