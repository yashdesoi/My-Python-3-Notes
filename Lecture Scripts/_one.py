def some_func():
	print('Hello World')

print('Top of module _one')

if __name__ == '__main__':
	print('python _one.py in cmd prompt')
	some_func()

else:
	print('module _one is imported')