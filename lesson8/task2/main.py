from file_utils import load_json, save_json, load_csv, save_csv, load_pickle, save_pickle

json_data = load_json('data.json')
csv_data = load_csv('data.csv')
pickle_data = load_pickle('data.pickle')

save_json(json_data, 'new_data.json')
save_csv(csv_data, 'new_data.csv')
save_pickle(pickle_data, 'new_data.pickle')
