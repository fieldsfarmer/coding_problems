#example of decorator

def get_text(name):
	return "blah blah {0}".format(name)

print get_text('nima')

def p_decotrate(func):
	def func_wrapper(name):
		return "<p>{0}</p>".format(func(name))
	return func_wrapper

my_get_text = p_decotrate(get_text)
print my_get_text("Chicago!")

get_text = p_decotrate(get_text)
print get_text("Now, decorator!")

#python special sytax for decorator
@p_decotrate
def get_text1(name):
	return "hello, {0}".format(name)

print  get_text1("Li Yang")
