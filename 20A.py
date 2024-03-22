s = input()
parts = [part for part in s.split('/') if part]
cs = '/' + '/'.join(parts) if parts else '/'
print(cs)


