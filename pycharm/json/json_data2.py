
import json

check = json.dumps('한글')
print(check)

check = json.dumps('한글',ensure_ascii=False)
print(check)
