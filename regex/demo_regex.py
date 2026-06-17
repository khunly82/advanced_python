import re

pattern = r's.+?e\b'
s2 = 'se text soe speciale'

m = re.match(pattern, s2)
print(m)

m2 = re.search(pattern, s2)
print(m2)

m3 = re.findall(pattern, s2)
print(m3)

m4 = re.finditer(pattern, s2)
print(list(m4))
for m in m4:
    print(m)

s3 = "Java is good"
print(re.sub('Ja.a', 'Python', s3))


print(re.match(r'a{6,9}\b', 'aaaaaaaaaa'))


s4 = 'This 3 houses cost between $100000 and $200000'
print(re.findall(r'(?<=\$)\b\d+', s4))