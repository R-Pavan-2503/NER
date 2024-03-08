import re

a="F:\PYTHON\INTERN\ml_files\\NVSD_A_1595675_J.xml"
f= open(a, 'r')
text = f.read()
text = text.replace("\n","")
text = text.replace('\t',"")

xml_value=[]
pattern = r'<ref-list>(.*?)</ref-list>'
matches = re.findall(pattern, text,re.DOTALL)
for match in matches:
    xml_value.append(match)

for val in xml_value:
    pattern2 = r'<title>(.*?)</title>'
    pattern3 = r'<label>(.*?)</label>'
    pattern4 = r'<mixed-citation publication-type="book">'
    pattern5 = r'<\/mixed-citation>'
    pre_val = re.sub(pattern2,"",val,flags=re.DOTALL)
    pre_val = re.sub(pattern3,"",pre_val,flags=re.DOTALL)
    pre_val = re.sub(pattern4,"",pre_val)
    pre_val = re.sub(pattern5,"",pre_val)
   # print(pre_val)

article_name_list,article_name=[],[]
article_name_matches= re.findall(r'<article-title>(.*?)</article-title>',pre_val,re.DOTALL)
for name in article_name_matches:
    article_name_list.append(name)

for j in article_name_list:
    starting_index=pre_val.index(j)
    ending_index = starting_index + len(j) - 1
    article_name.append((j,starting_index,ending_index,"article_name"))

for name in article_name:
    print(name)