import functools

### a decorator to count how many times a function is called
def counter(func):
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		wrapper.count += 1
		print('%s is called %d times' %(func.__name__, wrapper.count))
		return func(*args, **kwargs)
	wrapper.count = 0
	return wrapper

# @counter
def foo():
	print('123')
# or use the following to decorate
foo = counter(foo)
foo()
foo()
foo()
print ('The function %s is called %d times totally' %(foo.__name__, foo.count))


def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('start calling %s' %func.__name__)
		func(*args, **kw)
		print('end calling %s' %func.__name__)
	return wrapper

foo = log(foo)
foo()
# print(foo.__name__)


# import time
 
# def timeit(func):
#     @functools.wraps(func)
#     def wrapper():
#         start = time.clock()
#         func()
#         end =time.clock()
#         print 'used:', end - start
#     return wrapper
 
# @timeit
# def bar():
#     print 'in bar()'
 
# bar()
# print bar.__name__


