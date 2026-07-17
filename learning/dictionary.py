a={'ausd':'appleusd','busd':'baallusd'}
a.update({'yo':90})

print(a['ausd'])
dic={
    'a':'1'
}
converted_dict = {k: float(v) for k, v in dic.items()}
print(converted_dict.items())