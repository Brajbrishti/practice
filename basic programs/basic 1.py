import json
odics='{"k1":"val1","k2":"val2","k3":"val3"}'
result=json.loads(odics)
print(result['k2'])

