def make_element(name, value, **kwargs):
	keyvals = ['%s = %s' % item for item in kwargs.items()]
	attr_str = ' '.join(keyvals)
	element = '<{name} {attrs}>{value}</{name}>'.format(name = name, value = value, attrs = attr_str)
	return element
