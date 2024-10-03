msg = "good morning"
print(msg)

first_name="\tMasao"
last_name="Ono"
full_name=f"!{first_name}{last_name}!"
print(full_name)
print(f"morning, {full_name}")
greeting = f"morning, {full_name.upper()}"
print(greeting)

print("Programming Languages: \nPython \nJava")

# strip(), rstrip(), lstrip()
favorite_lan = '    python  '
scd_favorite_lag = '    Java    '
print(favorite_lan.rstrip(),scd_favorite_lag.lstrip())
print(favorite_lan.strip(),scd_favorite_lag.strip())

# .removeprefix('str') .removesuffix('str')
bbc_link = "https://www.bbc.com/news/business-68017347"
simple_bbc_link1 = bbc_link.removeprefix("https://")
simple_bbc_link2 = bbc_link.removesuffix("/business-68017347")
print(f"original link is : {bbc_link}")
print(simple_bbc_link1)
print(simple_bbc_link2)

