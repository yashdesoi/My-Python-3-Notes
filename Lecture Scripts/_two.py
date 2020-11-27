import _one

print('Top of module _two')

_one.some_func()

if __name__ == '__main__':
	print('python _two.py in cmd prompt')

else:
	print('module _two is imported')